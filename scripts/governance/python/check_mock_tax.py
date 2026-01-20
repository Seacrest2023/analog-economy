#!/usr/bin/env python3
"""
Rising Tide: Mock Tax Enforcer

Blocks commits where test files exceed 2x the source file size.
Heavy mocking indicates tight coupling - write integration tests instead.

The 2x Rule:
  - Test < 2x source = Healthy
  - Test > 2x source with mocks = REJECTED

Philosophy:
  "A rising tide lifts all boats."
  As integration test coverage increases, bloated unit tests naturally sink.

Usage:
    python scripts/governance/check_mock_tax.py [test_files...]

Exit Codes:
    0 - All tests pass the mock tax check
    1 - One or more tests exceed the 2x ratio
"""
import json
import re
import subprocess
import sys
from pathlib import Path

# Configuration
MAX_RATIO = 2.0
MIN_SOURCE_LINES = 15  # Only check tests for files with meaningful size
BASELINE_PATH = Path(".governance/mock-tax-baseline.json")
EXEMPT_MARKER = "MOCK_TAX_EXEMPT"

# Mock detection patterns (Python)
MOCK_PATTERNS = [
    r"@patch",
    r"@mock\.patch",
    r"Mock\(",
    r"MagicMock\(",
    r"create_autospec\(",
    r"mocker\.",  # pytest-mock
]


def count_lines(file_path: Path) -> int:
    """Count non-empty, non-comment lines."""
    try:
        content = file_path.read_text(encoding="utf-8")
    except Exception:
        return 0

    lines = content.split("\n")
    count = 0
    in_docstring = False

    for line in lines:
        stripped = line.strip()

        # Skip empty lines
        if not stripped:
            continue

        # Track docstrings
        if '"""' in stripped or "'''" in stripped:
            quotes = '"""' if '"""' in stripped else "'''"
            # Check if it's a one-liner docstring
            if stripped.count(quotes) >= 2:
                continue  # Skip one-liner docstrings
            in_docstring = not in_docstring
            continue

        if in_docstring:
            continue

        # Skip comments
        if stripped.startswith("#"):
            continue

        count += 1

    return count


def has_mocks(file_path: Path) -> bool:
    """Check if a test file contains mock patterns."""
    try:
        content = file_path.read_text(encoding="utf-8")
    except Exception:
        return False

    for pattern in MOCK_PATTERNS:
        if re.search(pattern, content):
            return True
    return False


def is_exempt(file_path: Path) -> bool:
    """Check if file has exemption marker."""
    try:
        content = file_path.read_text(encoding="utf-8")
        return EXEMPT_MARKER in content
    except Exception:
        return False


def map_test_to_source(test_path: Path) -> Path | None:
    """
    Map test file to its source file.

    Examples:
        core-governance/tests/test_main.py -> core-governance/gaian/main.py
        core-governance/tests/unit/test_config.py -> core-governance/gaian/config.py
        core-governance/tests/routes/test_action.py -> core-governance/gaian/routes/action.py
    """
    test_str = str(test_path)

    # Extract the test name
    test_name = test_path.stem  # e.g., "test_main" or "test_action"
    if test_name.startswith("test_"):
        source_name = test_name[5:]  # Remove "test_" prefix
    else:
        source_name = test_name

    # Try common mappings
    possible_sources = [
        # Direct mapping: tests/test_X.py -> gaian/X.py
        Path(f"core-governance/gaian/{source_name}.py"),
        # Nested: tests/unit/test_X.py -> gaian/X.py
        Path(f"core-governance/gaian/{source_name}.py"),
        # Route tests: tests/routes/test_action.py -> gaian/routes/action.py
        Path(f"core-governance/gaian/routes/{source_name}.py"),
        # Model tests: tests/models/test_action.py -> gaian/models/action.py
        Path(f"core-governance/gaian/models/{source_name}.py"),
        # Core tests: tests/core/test_X.py -> gaian/core/X.py
        Path(f"core-governance/gaian/core/{source_name}.py"),
    ]

    # Try to find matching source based on test path structure
    if "routes" in test_str:
        possible_sources.insert(0, Path(f"core-governance/gaian/routes/{source_name}.py"))
    elif "models" in test_str:
        possible_sources.insert(0, Path(f"core-governance/gaian/models/{source_name}.py"))
    elif "core" in test_str:
        possible_sources.insert(0, Path(f"core-governance/gaian/core/{source_name}.py"))

    for source in possible_sources:
        if source.exists():
            return source

    return None


def get_staged_test_files() -> list[str]:
    """Get list of staged test files."""
    try:
        result = subprocess.run(
            ["git", "diff", "--cached", "--name-only", "--diff-filter=ACMR"],
            capture_output=True,
            text=True,
            check=True,
        )
        files = [
            f for f in result.stdout.strip().split("\n")
            if f.endswith(".py")
            and f.startswith("core-governance/tests/")
            and "test_" in f
        ]
        return [f for f in files if f]
    except Exception:
        return []


def load_baseline() -> dict:
    """Load baseline exemptions."""
    if not BASELINE_PATH.exists():
        return {"violations": [], "exemptions": []}
    try:
        return json.loads(BASELINE_PATH.read_text())
    except Exception:
        return {"violations": [], "exemptions": []}


def main():
    print("=" * 60)
    print("RISING TIDE: Mock Tax Check")
    print("=" * 60)

    # Get test files from args or staged files
    if len(sys.argv) > 1:
        test_files = [f for f in sys.argv[1:] if f.endswith(".py")]
    else:
        test_files = get_staged_test_files()

    if not test_files:
        print("No test files to check")
        print("=" * 60)
        sys.exit(0)

    print(f"Checking {len(test_files)} test file(s)...")

    baseline = load_baseline()
    exempted_files = {e.get("file") for e in baseline.get("exemptions", [])}
    violations = []

    for test_file in test_files:
        test_path = Path(test_file)

        if not test_path.exists():
            continue

        # Check exemptions
        if str(test_path) in exempted_files or is_exempt(test_path):
            print(f"  [EXEMPT] {test_file}")
            continue

        source_path = map_test_to_source(test_path)
        if not source_path:
            print(f"  [SKIP] {test_file} - No matching source found")
            continue

        test_lines = count_lines(test_path)
        source_lines = count_lines(source_path)

        if source_lines < MIN_SOURCE_LINES:
            print(f"  [SKIP] {test_file} - Source too small ({source_lines} lines)")
            continue

        # Only check if test has mocks
        if not has_mocks(test_path):
            print(f"  [OK] {test_file} - No mocks")
            continue

        ratio = test_lines / source_lines

        if ratio > MAX_RATIO:
            violations.append({
                "test_file": str(test_path),
                "source_file": str(source_path),
                "test_lines": test_lines,
                "source_lines": source_lines,
                "ratio": ratio,
            })
            print(f"  [FAIL] {test_file} - {ratio:.1f}x ratio")
        else:
            print(f"  [OK] {test_file} - {ratio:.1f}x ratio")

    if violations:
        print()
        print("=" * 60)
        print("RISING TIDE: Mock Tax Violations")
        print("=" * 60)
        print()

        for v in violations:
            print(f"MOCK-TAX: {v['test_file']}")
            print(f"  Test: {v['test_lines']} lines, Source: {v['source_lines']} lines")
            print(f"  Ratio: {v['ratio']:.1f}x (max: {MAX_RATIO}x)")
            print(f"  Source: {v['source_file']}")
            print()

        print("-" * 60)
        print("BLOCKED: Test file(s) exceed the 2x ratio!")
        print()
        print("FIX OPTIONS:")
        print("  1. DELETE the unit test and write an integration test instead")
        print("  2. Reduce mocking by using real dependencies")
        print("  3. If legitimate, add `# MOCK_TAX_EXEMPT: reason` at file top")
        print()
        print("Philosophy: Heavy mocking indicates tight coupling.")
        print("Integration tests catch real bugs that mocks hide.")
        print()
        print("See: docs/guides/project setup/RISING-TIDE.md")
        print("-" * 60)
        sys.exit(1)

    print()
    print("Mock tax check passed")
    print("=" * 60)
    sys.exit(0)


if __name__ == "__main__":
    main()
