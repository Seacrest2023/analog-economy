#!/usr/bin/env python3
"""
Iron Dome: Type Safety Enforcer

Counts type-safety holes and blocks commits that increase the count.
The ratchet only goes DOWN - quality can only improve over time.

Type Safety Holes (Python):
  - `type: ignore` comments
  - `Any` type annotations
  - `cast()` calls
  - `# noqa` comments
  - `# pylint: disable` comments

Usage:
    python scripts/governance/check_iron_dome.py
    python scripts/governance/check_iron_dome.py --generate-baseline

Exit Codes:
    0 - All files pass (no increase in type-safety holes)
    1 - Violations detected (holes increased)
"""
import json
import re
import subprocess
import sys
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path

# Configuration
BASELINE_PATH = Path(".governance/type-safety-baseline.json")
EXEMPT_MARKER = "IRON_DOME_EXEMPT"

# Patterns to detect (Python)
PATTERNS = [
    {"name": "type: ignore", "pattern": r"#\s*type:\s*ignore", "weight": 1.0},
    {"name": "Any import", "pattern": r"from typing import.*\bAny\b", "weight": 0.5},
    {"name": "Any annotation", "pattern": r":\s*Any\b", "weight": 1.0},
    {"name": "-> Any", "pattern": r"->\s*Any\b", "weight": 1.0},
    {"name": "cast()", "pattern": r"\bcast\s*\(", "weight": 1.0},
    {"name": "noqa", "pattern": r"#\s*noqa", "weight": 0.5},
    {"name": "pylint: disable", "pattern": r"#\s*pylint:\s*disable", "weight": 0.5},
]


@dataclass
class FileResult:
    path: str
    total: float
    breakdown: dict


def count_holes(file_path: Path) -> FileResult:
    """Count type-safety holes in a file."""
    try:
        content = file_path.read_text(encoding="utf-8")
    except Exception:
        return FileResult(str(file_path), 0, {})

    # Skip lines with IRON_DOME_EXEMPT
    lines = [line for line in content.split("\n") if EXEMPT_MARKER not in line]
    content = "\n".join(lines)

    total = 0.0
    breakdown = {}

    for pattern_def in PATTERNS:
        matches = re.findall(pattern_def["pattern"], content)
        count = len(matches)
        if count > 0:
            breakdown[pattern_def["name"]] = count
            total += count * pattern_def["weight"]

    return FileResult(str(file_path), total, breakdown)


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
            if f.endswith(".py") and f.startswith("core-governance/")
        ]
        return [f for f in files if f]  # Filter empty strings
    except Exception:
        return []


def get_all_python_files() -> list[Path]:
    """Get all Python files in core-governance."""
    root = Path("core-governance")
    if not root.exists():
        return []
    return list(root.glob("**/*.py"))


def load_baseline() -> dict:
    """Load baseline from file."""
    if not BASELINE_PATH.exists():
        return {"totalHoles": 0, "byFile": {}, "generated": None}
    try:
        return json.loads(BASELINE_PATH.read_text())
    except Exception:
        return {"totalHoles": 0, "byFile": {}, "generated": None}


def save_baseline(data: dict) -> None:
    """Save baseline to file."""
    BASELINE_PATH.parent.mkdir(parents=True, exist_ok=True)
    data["generated"] = datetime.now().isoformat()
    BASELINE_PATH.write_text(json.dumps(data, indent=2))


def generate_baseline():
    """Generate baseline for entire codebase."""
    print("=" * 60)
    print("IRON DOME: Generating Baseline")
    print("=" * 60)

    files = get_all_python_files()
    print(f"Scanning {len(files)} files...")

    total_holes = 0.0
    by_file = {}

    for file_path in files:
        result = count_holes(file_path)
        if result.total > 0:
            total_holes += result.total
            by_file[str(file_path)] = {
                "total": result.total,
                "breakdown": result.breakdown,
            }

    baseline = {
        "totalHoles": total_holes,
        "byFile": by_file,
    }
    save_baseline(baseline)

    print(f"\nFound {total_holes:.1f} type-safety holes")
    print(f"Baseline saved to {BASELINE_PATH}")
    print("=" * 60)


def main():
    if "--generate-baseline" in sys.argv:
        generate_baseline()
        sys.exit(0)

    print("=" * 60)
    print("IRON DOME: Type Safety Check")
    print("=" * 60)

    # Get staged files or all files
    staged_files = get_staged_files()
    if not staged_files:
        print("No staged Python files in core-governance/")
        print("=" * 60)
        sys.exit(0)

    print(f"Checking {len(staged_files)} staged file(s)...")

    baseline = load_baseline()
    violations = []
    current_total = 0.0

    for file in staged_files:
        file_path = Path(file)
        if not file_path.exists():
            continue

        result = count_holes(file_path)
        current_total += result.total

        baseline_for_file = baseline.get("byFile", {}).get(file, {}).get("total", 0)

        if result.total > baseline_for_file:
            violations.append({
                "file": file,
                "current": result.total,
                "baseline": baseline_for_file,
                "breakdown": result.breakdown,
            })

    if violations:
        print()
        print("=" * 60)
        print("IRON DOME: Type Safety Violations")
        print("=" * 60)
        print()

        for v in violations:
            print(f"TYPE-SAFETY: {v['file']}")
            print(f"  Current: {v['current']:.1f} holes, Baseline: {v['baseline']:.1f} holes")
            print(f"  Breakdown: {v['breakdown']}")
            print()

        print("-" * 60)
        print("BLOCKED: Type-safety holes increased!")
        print()
        print("FIX OPTIONS:")
        print("  1. Replace `Any` with proper type annotations")
        print("  2. Remove `# type: ignore` and fix the type error")
        print("  3. If legitimate, add `# IRON_DOME_EXEMPT: reason` comment")
        print()
        print("See: docs/guides/project setup/IRON-DOME.md")
        print("-" * 60)
        sys.exit(1)

    # Success - optionally update baseline if improved
    print()
    if current_total < baseline.get("totalHoles", 0):
        print(f"Improved! {baseline['totalHoles']:.1f} -> {current_total:.1f} holes")

    print("Type safety check passed")
    print("=" * 60)
    sys.exit(0)


if __name__ == "__main__":
    main()
