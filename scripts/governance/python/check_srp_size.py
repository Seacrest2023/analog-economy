#!/usr/bin/env python3
"""
SRP Size Guardrails: Single Responsibility Principle Enforcer

Enforces file and function size limits to maintain Single Responsibility.

Thresholds:
  - Implementation files: warn >300 LOC, fail >600 LOC
  - Test files: warn >200 LOC, fail >300 LOC
  - Functions/methods: fail >75 LOC

Philosophy:
  Large files = multiple responsibilities = harder to test and maintain.

Usage:
    python scripts/governance/check_srp_size.py

Exit Codes:
    0 - All files pass SRP checks
    1 - One or more files exceed size limits
"""
import ast
import subprocess
import sys
from pathlib import Path

# Configuration
IMPL_WARN_LOC = 300
IMPL_FAIL_LOC = 600
TEST_WARN_LOC = 200
TEST_FAIL_LOC = 300
FUNC_FAIL_LOC = 75

EXEMPT_MARKER = "SRP_EXEMPT"


def count_lines(file_path: Path) -> int:
    """Count non-empty, non-comment lines."""
    try:
        content = file_path.read_text(encoding="utf-8")
    except Exception:
        return 0

    lines = content.split("\n")
    count = 0

    for line in lines:
        stripped = line.strip()
        if stripped and not stripped.startswith("#"):
            count += 1

    return count


def get_function_sizes(file_path: Path) -> list[tuple[str, int, int]]:
    """Get function/method names and their line counts."""
    try:
        content = file_path.read_text(encoding="utf-8")
        tree = ast.parse(content)
    except Exception:
        return []

    functions = []

    for node in ast.walk(tree):
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            if node.end_lineno and node.lineno:
                lines = node.end_lineno - node.lineno + 1
                functions.append((node.name, lines, node.lineno))

    return functions


def is_test_file(file_path: Path) -> bool:
    """Check if file is a test file."""
    return "test" in file_path.name.lower() or str(file_path).startswith("core-governance/tests")


def is_exempt(file_path: Path) -> bool:
    """Check if file has exemption marker."""
    try:
        content = file_path.read_text(encoding="utf-8")
        return EXEMPT_MARKER in content
    except Exception:
        return False


def get_staged_files() -> list[str]:
    """Get list of staged Python files in core-governance."""
    try:
        result = subprocess.run(
            ["git", "diff", "--cached", "--name-only", "--diff-filter=ACMR"],
            capture_output=True,
            text=True,
            check=True,
        )
        files = [
            f for f in result.stdout.strip().split("\n")
            if f.endswith(".py") and f.startswith("core-governance/gaian/")
        ]
        return [f for f in files if f]
    except Exception:
        return []


def main():
    print("=" * 60)
    print("SRP SIZE GUARDRAILS")
    print("=" * 60)

    # Get staged files
    staged_files = get_staged_files()
    if not staged_files:
        print("No staged Python files in core-governance/gaian/")
        print("=" * 60)
        sys.exit(0)

    print(f"Checking {len(staged_files)} file(s)...")

    warnings = []
    errors = []

    for file in staged_files:
        file_path = Path(file)
        if not file_path.exists():
            continue

        if is_exempt(file_path):
            print(f"  [EXEMPT] {file}")
            continue

        loc = count_lines(file_path)
        is_test = is_test_file(file_path)

        # File size checks
        warn_threshold = TEST_WARN_LOC if is_test else IMPL_WARN_LOC
        fail_threshold = TEST_FAIL_LOC if is_test else IMPL_FAIL_LOC

        if loc > fail_threshold:
            errors.append({
                "file": file,
                "type": "file_size",
                "lines": loc,
                "threshold": fail_threshold,
            })
            print(f"  [FAIL] {file} - {loc} LOC (max: {fail_threshold})")
        elif loc > warn_threshold:
            warnings.append({
                "file": file,
                "type": "file_size",
                "lines": loc,
                "threshold": warn_threshold,
            })
            print(f"  [WARN] {file} - {loc} LOC (recommended: <{warn_threshold})")
        else:
            print(f"  [OK] {file} - {loc} LOC")

        # Function size checks (only for non-test files)
        if not is_test:
            functions = get_function_sizes(file_path)
            for func_name, func_lines, line_no in functions:
                if func_lines > FUNC_FAIL_LOC:
                    errors.append({
                        "file": file,
                        "type": "function_size",
                        "function": func_name,
                        "lines": func_lines,
                        "line_no": line_no,
                        "threshold": FUNC_FAIL_LOC,
                    })
                    print(f"       [FAIL] {func_name}() at line {line_no} - {func_lines} LOC")

    if warnings:
        print()
        print("-" * 60)
        print("WARNINGS:")
        for w in warnings:
            print(f"  {w['file']}: {w['lines']} LOC (consider splitting)")
        print("-" * 60)

    if errors:
        print()
        print("=" * 60)
        print("SRP GUARDRAILS: Size Violations")
        print("=" * 60)
        print()

        file_errors = [e for e in errors if e["type"] == "file_size"]
        func_errors = [e for e in errors if e["type"] == "function_size"]

        if file_errors:
            print("FILE SIZE VIOLATIONS:")
            for e in file_errors:
                print(f"  {e['file']}: {e['lines']} LOC (max: {e['threshold']})")
            print()

        if func_errors:
            print("FUNCTION SIZE VIOLATIONS:")
            for e in func_errors:
                print(f"  {e['file']}:{e['line_no']} {e['function']}(): {e['lines']} LOC")
            print()

        print("-" * 60)
        print("BLOCKED: Files or functions exceed SRP size limits!")
        print()
        print("FIX OPTIONS:")
        print("  1. Split large files into smaller, focused modules")
        print("  2. Extract functions into separate helper modules")
        print("  3. If legitimate, add `# SRP_EXEMPT: reason` at file top")
        print()
        print("Large files indicate multiple responsibilities.")
        print("-" * 60)
        sys.exit(1)

    print()
    print("SRP size check passed")
    print("=" * 60)
    sys.exit(0)


if __name__ == "__main__":
    main()
