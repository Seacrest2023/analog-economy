#!/usr/bin/env python3
"""
Mock Conformance Check: create_autospec Enforcement

Ensures test fixtures use create_autospec() instead of bare Mock().
Bare mocks accept any method call, masking interface drift.

Problem:
  Mock() accepts ANY attribute access, even typos.
  If the real interface changes, tests still pass but production breaks.

Solution:
  create_autospec(ServiceClass, instance=True) validates method names.

Usage:
    python scripts/governance/check_mock_conformance.py

Exit Codes:
    0 - All conftest.py files pass mock conformance
    1 - Bare Mock() detected in fixtures
"""
import re
import subprocess
import sys
from pathlib import Path

# Patterns
BARE_MOCK_PATTERNS = [
    r"=\s*Mock\(\s*\)",  # x = Mock()
    r"=\s*MagicMock\(\s*\)",  # x = MagicMock()
    r"Mock\(\s*return_value",  # Mock(return_value=...)
    r"MagicMock\(\s*return_value",  # MagicMock(return_value=...)
]

# Safe patterns (allowed)
SAFE_PATTERNS = [
    r"create_autospec",
    r"spec=",
    r"spec_set=",
    r"autospec=",
]

EXEMPT_MARKER = "MOCK_CONFORMANCE_EXEMPT"


def check_mock_conformance(file_path: Path) -> list[dict]:
    """Check a file for bare Mock() usage."""
    try:
        content = file_path.read_text(encoding="utf-8")
    except Exception:
        return []

    violations = []
    lines = content.split("\n")

    for line_no, line in enumerate(lines, 1):
        # Skip exempted lines
        if EXEMPT_MARKER in line:
            continue

        # Check for bare mock patterns
        for pattern in BARE_MOCK_PATTERNS:
            if re.search(pattern, line):
                # Check if it's actually safe (has spec)
                is_safe = any(re.search(safe, line) for safe in SAFE_PATTERNS)
                if not is_safe:
                    violations.append({
                        "line_no": line_no,
                        "line": line.strip(),
                        "file": str(file_path),
                    })
                    break  # Only report once per line

    return violations


def get_staged_conftest_files() -> list[str]:
    """Get list of staged conftest.py files."""
    try:
        result = subprocess.run(
            ["git", "diff", "--cached", "--name-only", "--diff-filter=ACMR"],
            capture_output=True,
            text=True,
            check=True,
        )
        files = [
            f for f in result.stdout.strip().split("\n")
            if f.endswith("conftest.py") and f.startswith("core-governance/")
        ]
        return [f for f in files if f]
    except Exception:
        return []


def main():
    print("=" * 60)
    print("MOCK CONFORMANCE CHECK")
    print("=" * 60)

    # Get staged conftest files
    conftest_files = get_staged_conftest_files()

    # Also check if we're running manually
    if not conftest_files:
        # Check all conftest files in core-governance
        conftest_path = Path("core-governance/tests/conftest.py")
        if conftest_path.exists():
            conftest_files = [str(conftest_path)]

    if not conftest_files:
        print("No conftest.py files to check")
        print("=" * 60)
        sys.exit(0)

    print(f"Checking {len(conftest_files)} conftest file(s)...")

    all_violations = []

    for file in conftest_files:
        file_path = Path(file)
        if not file_path.exists():
            continue

        violations = check_mock_conformance(file_path)
        if violations:
            all_violations.extend(violations)
            print(f"  [FAIL] {file} - {len(violations)} bare Mock() found")
        else:
            print(f"  [OK] {file}")

    if all_violations:
        print()
        print("=" * 60)
        print("MOCK CONFORMANCE: Violations")
        print("=" * 60)
        print()

        for v in all_violations:
            print(f"BARE-MOCK: {v['file']}:{v['line_no']}")
            print(f"  Line: {v['line']}")
            print()

        print("-" * 60)
        print("BLOCKED: Bare Mock() detected in test fixtures!")
        print()
        print("WHY THIS MATTERS:")
        print("  Mock() accepts ANY method call, even typos.")
        print("  If the real interface changes, tests pass but production breaks.")
        print()
        print("FIX: Replace with create_autospec():")
        print()
        print("  # BEFORE (dangerous):")
        print('  mock_service = Mock()')
        print()
        print("  # AFTER (safe):")
        print("  from unittest.mock import create_autospec")
        print("  mock_service = create_autospec(RealService, instance=True)")
        print()
        print("  # Or with spec=:")
        print("  mock_service = Mock(spec=RealService)")
        print()
        print("If intentional, add `# MOCK_CONFORMANCE_EXEMPT: reason`")
        print("-" * 60)
        sys.exit(1)

    print()
    print("Mock conformance check passed")
    print("=" * 60)
    sys.exit(0)


if __name__ == "__main__":
    main()
