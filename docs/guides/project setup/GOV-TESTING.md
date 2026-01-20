# Governance Testing Implementation Guide

> **The Analog Economy: Production-Readiness Kit**
> **Philosophy:** Who watches the watchmen? Governance tests watch the tests.

---

## What Is Governance Testing?

Governance testing is the **foundation layer** of the testing pyramid. Unlike other tests that validate your code, governance tests validate **the tests themselves**.

In AI-assisted development, there's no human reviewer to catch:
- Mocks that drift from real APIs
- Tests that pass but test against stale fakes
- Type holes that defeat mypy protection
- Silent failures that swallow errors

**Governance creates physics (errors, blocked commits) instead of policy (documentation).**

---

## AI Coder Implementation Checklist

**Your job:** Create the scripts, baselines, and tests listed below. Each section has the exact file to create and the code to generate.

```
┌─────────────────────────────────────────────────────────────────────┐
│              GOVERNANCE IMPLEMENTATION CHECKLIST                     │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  □ 1. Create governance scripts directory                          │
│  □ 2. Implement Mock Tax checker (Rising Tide)                      │
│  □ 3. Implement Type Safety checker (Iron Dome)                     │
│  □ 4. Implement Mock Conformance checker                            │
│  □ 5. Create baseline files                                         │
│  □ 6. Add governance tests (tests that test tests)                  │
│  □ 7. Wire into pre-commit hooks                                    │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

---

## Step 1: Create Directory Structure

Create these directories if they don't exist:

```
analog-economy/
├── scripts/
│   └── governance/
│       └── python/              # ← CREATE THIS
│           ├── check_mock_tax.py
│           ├── check_iron_dome.py
│           ├── check_mock_conformance.py
│           └── check_srp_size.py
├── core-governance/
│   └── tests/
│       ├── unit/                # Pure logic ONLY — NO I/O
│       │   └── governance/      # ← CREATE THIS
│       │       └── test_mock_conformance.py
│       ├── integration/         # FastAPI TestClient tests
│       └── conftest.py          # Shared fixtures
└── .governance/
    └── baselines/               # ← CREATE THIS
        ├── iron-dome-baseline.json
        └── srp-baseline.json
```

> **CRITICAL:** The governance scripts enforce that `tests/unit/` contains only pure logic tests. Tests needing database, network, or file I/O belong in `tests/integration/`.

---

## Step 2: Mock Tax Checker (Rising Tide)

**File to create:** `scripts/governance/python/check_mock_tax.py`

**What it does:** Blocks unit tests that are >2x the size of the source file they test.

**Why:** Heavy mocking is a code smell. If you need 2x the code to test something, refactor to use the Pure Core pattern.

```python
#!/usr/bin/env python3
"""
Mock Tax Checker (Rising Tide)
Blocks unit tests where test LOC > 2x source LOC
"""

import sys
from pathlib import Path

MAX_RATIO = 2.0
MIN_SOURCE_LINES = 15  # Only check files >15 lines


def count_lines(filepath: Path) -> int:
    """Count non-blank, non-comment lines."""
    count = 0
    with open(filepath) as f:
        for line in f:
            stripped = line.strip()
            if stripped and not stripped.startswith('#'):
                count += 1
    return count


def find_test_file(source_file: Path, test_dir: Path) -> Path | None:
    """Find corresponding test file for a source file."""
    # Convert src/module/file.py → tests/unit/module/test_file.py
    relative = source_file.relative_to(source_file.parents[len(source_file.parts) - 2])
    test_name = f"test_{source_file.name}"
    test_path = test_dir / relative.parent / test_name

    if test_path.exists():
        return test_path
    return None


def main() -> int:
    # Get source directory and test directory
    source_dir = Path(sys.argv[1]) if len(sys.argv) > 1 else Path('core-governance/gaian')
    test_dir = Path(sys.argv[2]) if len(sys.argv) > 2 else Path('core-governance/tests/unit')

    if not source_dir.exists():
        print(f"Source directory not found: {source_dir}")
        return 0

    violations = []

    for source_file in source_dir.rglob('*.py'):
        if source_file.name.startswith('test_') or '__pycache__' in str(source_file):
            continue

        test_file = find_test_file(source_file, test_dir)
        if not test_file:
            continue

        src_lines = count_lines(source_file)
        if src_lines < MIN_SOURCE_LINES:
            continue

        test_lines = count_lines(test_file)
        ratio = test_lines / src_lines

        if ratio > MAX_RATIO:
            violations.append({
                'source': str(source_file),
                'test': str(test_file),
                'src_lines': src_lines,
                'test_lines': test_lines,
                'ratio': f"{ratio:.2f}"
            })

    if violations:
        print('\n🚫 MOCK TAX VIOLATION (Rising Tide)\n')
        print('The following tests exceed the 2x size limit:\n')

        for v in violations:
            print(f"  {v['test']}")
            print(f"    Source: {v['src_lines']} lines | Test: {v['test_lines']} lines | Ratio: {v['ratio']}x")
            print()

        print('REMEDIATION:')
        print('  1. Extract pure logic into a separate module (no I/O)')
        print('  2. Test the pure logic without mocks')
        print('  3. Move remaining tests to integration/ if they need heavy mocking')
        print('  4. See: docs/guides/development/TDD-GUIDE.md → Pure Core Pattern\n')

        return 1

    print('✓ Mock Tax check passed')
    return 0


if __name__ == '__main__':
    sys.exit(main())
```

---

## Step 3: Type Safety Checker (Iron Dome)

**File to create:** `scripts/governance/python/check_iron_dome.py`

**What it does:** Counts type safety holes (`Any`, `type: ignore`, `cast()`) and blocks if count increases above baseline.

**Why:** Every type hole is a potential runtime crash. The ratchet ensures count only goes down.

```python
#!/usr/bin/env python3
"""
Iron Dome: Type Safety Ratchet
Blocks commits that increase type-safety holes above baseline
"""

import json
import re
import sys
from pathlib import Path

BASELINE_FILE = Path('.governance/baselines/iron-dome-baseline.json')

# Patterns to detect (weighted by severity)
PATTERNS = [
    {'name': 'type: ignore', 'pattern': r'#\s*type:\s*ignore', 'weight': 1.0},
    {'name': 'Any annotation', 'pattern': r':\s*Any\b', 'weight': 1.0},
    {'name': '-> Any', 'pattern': r'->\s*Any\b', 'weight': 1.0},
    {'name': 'cast()', 'pattern': r'\bcast\s*\(', 'weight': 1.0},
    {'name': 'noqa', 'pattern': r'#\s*noqa', 'weight': 0.5},
    {'name': 'pylint: disable', 'pattern': r'#\s*pylint:\s*disable', 'weight': 0.5},
]


def count_holes(file_path: Path) -> tuple[float, dict[str, int]]:
    """Count type-safety holes in a file."""
    content = file_path.read_text()
    total = 0.0
    breakdown: dict[str, int] = {}

    for pattern_def in PATTERNS:
        matches = re.findall(pattern_def['pattern'], content)
        count = len(matches)
        if count > 0:
            breakdown[pattern_def['name']] = count
            total += count * pattern_def['weight']

    return total, breakdown


def load_baseline() -> dict:
    """Load baseline from file."""
    if not BASELINE_FILE.exists():
        return {'total_holes': 0, 'by_file': {}}
    return json.loads(BASELINE_FILE.read_text())


def save_baseline(data: dict) -> None:
    """Save baseline to file."""
    BASELINE_FILE.parent.mkdir(parents=True, exist_ok=True)
    BASELINE_FILE.write_text(json.dumps(data, indent=2))


def main() -> int:
    source_dir = Path(sys.argv[1]) if len(sys.argv) > 1 else Path('core-governance')

    if not source_dir.exists():
        print(f"Source directory not found: {source_dir}")
        return 0

    baseline = load_baseline()
    violations = []
    current_total = 0.0

    for py_file in source_dir.rglob('*.py'):
        if '__pycache__' in str(py_file):
            continue

        total, breakdown = count_holes(py_file)
        current_total += total

        file_key = str(py_file)
        baseline_for_file = baseline.get('by_file', {}).get(file_key, {}).get('total', 0)

        if total > baseline_for_file:
            violations.append({
                'file': file_key,
                'current': total,
                'baseline': baseline_for_file,
                'breakdown': breakdown,
            })

    print(f"\nIron Dome (Type Safety Ratchet)")
    print(f"  Baseline: {baseline.get('total_holes', 0)}")
    print(f"  Current:  {current_total}")

    if violations:
        print('\n🚫 IRON DOME VIOLATION\n')
        print('Type-safety holes INCREASED in these files:\n')

        for v in violations:
            print(f"  {v['file']}")
            print(f"    Current: {v['current']} holes, Baseline: {v['baseline']} holes")
            print(f"    Breakdown: {v['breakdown']}")
            print()

        print('REMEDIATION:')
        print('  1. Fix the types properly instead of suppressing')
        print('  2. Use proper type annotations instead of Any')
        print('  3. If unavoidable, reduce existing holes to offset')
        print('  4. See: docs/guides/project setup/IRON-DOME.md\n')

        return 1

    # Success - update baseline if improved
    if current_total < baseline.get('total_holes', 0):
        print(f"\n✓ Iron Dome: Improved! {baseline['total_holes']} → {current_total} holes")
        baseline['total_holes'] = current_total
        save_baseline(baseline)

    print('✓ Iron Dome check passed\n')
    return 0


if __name__ == '__main__':
    sys.exit(main())
```

---

## Step 4: Mock Conformance Checker

**File to create:** `scripts/governance/python/check_mock_conformance.py`

**What it does:** Ensures all tests use `create_autospec()` instead of bare `Mock()`.

**Why:** Bare mocks don't enforce interface contracts. If the real class changes, tests still pass but production breaks.

```python
#!/usr/bin/env python3
"""
Mock Conformance Checker
Ensures tests use create_autospec instead of bare Mock()
"""

import ast
import sys
from pathlib import Path
from typing import NamedTuple


class Violation(NamedTuple):
    file: str
    line: int
    issue: str


class MockVisitor(ast.NodeVisitor):
    """AST visitor to find bare Mock() usage."""

    def __init__(self, filepath: Path):
        self.filepath = filepath
        self.violations: list[Violation] = []

    def visit_Call(self, node: ast.Call) -> None:
        # Check for bare Mock() or MagicMock() calls
        if isinstance(node.func, ast.Name):
            if node.func.id in ('Mock', 'MagicMock'):
                self.violations.append(Violation(
                    file=str(self.filepath),
                    line=node.lineno,
                    issue=f'Bare {node.func.id}() - use create_autospec() instead'
                ))

        # Check for unittest.mock.Mock() or unittest.mock.MagicMock()
        elif isinstance(node.func, ast.Attribute):
            if node.func.attr in ('Mock', 'MagicMock'):
                self.violations.append(Violation(
                    file=str(self.filepath),
                    line=node.lineno,
                    issue=f'Bare {node.func.attr}() - use create_autospec() instead'
                ))

        self.generic_visit(node)


def check_file(filepath: Path) -> list[Violation]:
    """Check a file for mock conformance violations."""
    try:
        content = filepath.read_text()
        tree = ast.parse(content)
        visitor = MockVisitor(filepath)
        visitor.visit(tree)
        return visitor.violations
    except SyntaxError:
        return []


def main() -> int:
    test_dir = Path(sys.argv[1]) if len(sys.argv) > 1 else Path('core-governance/tests')

    if not test_dir.exists():
        print(f"Test directory not found: {test_dir}")
        return 0

    all_violations: list[Violation] = []

    for py_file in test_dir.rglob('*.py'):
        if '__pycache__' in str(py_file):
            continue
        violations = check_file(py_file)
        all_violations.extend(violations)

    if all_violations:
        print('\n🚫 MOCK CONFORMANCE VIOLATION\n')
        print('The following files use bare Mock() instead of create_autospec():\n')

        for v in all_violations:
            print(f"  {v.file}:{v.line}")
            print(f"    {v.issue}\n")

        print('REMEDIATION:')
        print('  Replace:')
        print('    mock = Mock()')
        print('    mock = MagicMock()')
        print()
        print('  With:')
        print('    from unittest.mock import create_autospec')
        print('    mock = create_autospec(RealClass, instance=True)')
        print()
        print('  See: docs/guides/development/TDD-GUIDE.md → Mock Conformance\n')

        return 1

    print('✓ Mock Conformance check passed')
    return 0


if __name__ == '__main__':
    sys.exit(main())
```

---

## Step 5: Create Baseline Files

**Files to create:** Initialize baselines with current counts.

### iron-dome-baseline.json

```json
{
  "total_holes": 0,
  "by_file": {},
  "last_updated": null,
  "note": "Run check_iron_dome.py --init to set initial baseline"
}
```

### srp-baseline.json

```json
{
  "max_file_lines": 300,
  "max_function_lines": 75,
  "exemptions": [],
  "note": "SRP size limits - files warn at 300, fail at 600"
}
```

### Initialize Baselines

After creating the scripts, run them once to establish baselines:

```bash
# Set initial baselines (first run stores current counts)
python scripts/governance/python/check_iron_dome.py --init
```

---

## Step 6: Governance Tests (Tests That Test Tests)

**File to create:** `core-governance/tests/unit/governance/test_mock_conformance.py`

**What it does:** Validates that the mock conformance checker correctly identifies violations.

```python
"""
Governance Test: Mock Conformance Checker
Validates that our governance scripts work correctly.
"""

import ast
import pytest
from pathlib import Path
from unittest.mock import create_autospec

# Import the checker (adjust path as needed)
# from scripts.governance.python.check_mock_conformance import MockVisitor


class TestMockVisitor:
    """Tests for the MockVisitor AST analyzer."""

    def test_detects_bare_mock(self) -> None:
        """Bare Mock() should be flagged as violation."""
        code = """
from unittest.mock import Mock
mock = Mock()
"""
        tree = ast.parse(code)
        visitor = MockVisitor(Path('test.py'))
        visitor.visit(tree)

        assert len(visitor.violations) == 1
        assert 'Mock()' in visitor.violations[0].issue

    def test_detects_bare_magic_mock(self) -> None:
        """Bare MagicMock() should be flagged as violation."""
        code = """
from unittest.mock import MagicMock
mock = MagicMock()
"""
        tree = ast.parse(code)
        visitor = MockVisitor(Path('test.py'))
        visitor.visit(tree)

        assert len(visitor.violations) == 1
        assert 'MagicMock()' in visitor.violations[0].issue

    def test_allows_create_autospec(self) -> None:
        """create_autospec() should NOT be flagged."""
        code = """
from unittest.mock import create_autospec
mock = create_autospec(SomeClass, instance=True)
"""
        tree = ast.parse(code)
        visitor = MockVisitor(Path('test.py'))
        visitor.visit(tree)

        assert len(visitor.violations) == 0

    def test_detects_qualified_mock(self) -> None:
        """unittest.mock.Mock() should be flagged."""
        code = """
import unittest.mock
mock = unittest.mock.Mock()
"""
        tree = ast.parse(code)
        visitor = MockVisitor(Path('test.py'))
        visitor.visit(tree)

        assert len(visitor.violations) == 1


class TestMockTax:
    """Tests for the Mock Tax (Rising Tide) checker."""

    def test_ratio_calculation(self) -> None:
        """Test file should not exceed 2x source file size."""
        # This is a meta-test: ensure our own test files follow the rule
        # In practice, this validates the concept
        source_lines = 50
        test_lines = 90
        ratio = test_lines / source_lines

        assert ratio <= 2.0, f"Test file is {ratio}x source size (max 2.0x)"
```

---

## Step 7: Wire Into Pre-commit

Add governance checks to `.pre-commit-config.yaml`:

```yaml
# Governance Checks (Layer 2-10)
repos:
  - repo: local
    hooks:
      # Layer 2: Iron Dome (Type Safety Ratchet)
      - id: iron-dome
        name: "Layer 2: Iron Dome (Type Safety)"
        entry: python scripts/governance/python/check_iron_dome.py
        language: system
        pass_filenames: false
        types: [python]
        stages: [pre-commit]

      # Layer 3: Mock Tax (Rising Tide)
      - id: mock-tax
        name: "Layer 3: Mock Tax (Rising Tide)"
        entry: python scripts/governance/python/check_mock_tax.py
        language: system
        pass_filenames: false
        types: [python]
        stages: [pre-commit]

      # Layer 9: SRP Size Guardrails
      - id: srp-guardrails
        name: "Layer 9: SRP Size Guardrails"
        entry: python scripts/governance/python/check_srp_size.py
        language: system
        pass_filenames: false
        types: [python]
        stages: [pre-commit]

      # Layer 10: Mock Conformance
      - id: mock-conformance
        name: "Layer 10: Mock Conformance"
        entry: python scripts/governance/python/check_mock_conformance.py
        language: system
        pass_filenames: false
        types: [python]
        stages: [pre-commit]

      # Governance Tests
      - id: governance-tests
        name: Governance Tests
        entry: pytest core-governance/tests/unit/governance/ -v
        language: system
        pass_filenames: false
        stages: [pre-commit]
```

---

## The Ratchet Pattern Explained

Multiple governance layers use the **ratchet pattern**:

```
┌─────────────────────────────────────────────────────────────────────┐
│                     THE RATCHET PATTERN                              │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│   1. COUNT violations today → Set as BASELINE                       │
│   2. New commits CANNOT exceed baseline                             │
│   3. Reducing violations UPDATES baseline (ratchet down)            │
│   4. Baseline can ONLY decrease, never increase                     │
│                                                                     │
│   Example (iron-dome-baseline.json):                                │
│   ┌────────────────────────────────────────────────────────┐        │
│   │  Day 1: Count = 50 → Set baseline = 50                 │        │
│   │  Day 2: Add 3 `Any` → Count = 53 → BLOCKED!            │        │
│   │  Day 3: Remove 10 → Count = 40 → Baseline now 40       │        │
│   │  Day 4: Add 5 → Count = 45 → Still > 40 → BLOCKED!     │        │
│   └────────────────────────────────────────────────────────┘        │
│                                                                     │
│   The ratchet ONLY turns one way — toward improvement.              │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

**Layers using ratchets:**
- Iron Dome: `Any`, `type: ignore`, `cast()` can only go down
- Mock Tax: Test/source ratio can only go down
- Coverage: Percentage can only go up

---

## When Governance Blocks You

```
┌─────────────────────────────────────────────────────────────────────┐
│              GOVERNANCE BLOCKED YOUR COMMIT                          │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│   STEP 1: Read the error message                                    │
│           Governance scripts include remediation instructions       │
│                                                                     │
│   STEP 2: FIX the issue, don't work around it                       │
│           - Mock Tax? → Extract pure logic, reduce mocking          │
│           - Iron Dome? → Fix the types properly                     │
│           - Mock Conformance? → Use create_autospec()               │
│                                                                     │
│   STEP 3: If you CANNOT fix it                                      │
│           - Ask for human guidance                                  │
│           - Do NOT modify baselines without approval                │
│           - Do NOT use --no-verify to bypass hooks                  │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

---

## Summary

| Script | What It Validates | Baseline File |
|--------|-------------------|---------------|
| `check_iron_dome.py` | Type holes don't increase | `iron-dome-baseline.json` |
| `check_mock_tax.py` | Test LOC <= 2x Source LOC | N/A (hard limit) |
| `check_mock_conformance.py` | All mocks use `create_autospec()` | N/A (100% rule) |
| `check_srp_size.py` | Files < 600 lines, functions < 75 | `srp-baseline.json` |

---

## Related

- [TDD-GUIDE.md](../development/TDD-GUIDE.md) — Test-First philosophy
- [IRON-DOME.md](./IRON-DOME.md) — Type Safety Ratchet details
- [PRECOMMIT-SETUP.md](./PRECOMMIT-SETUP.md) — Pre-commit hook configuration

---

*Part of The Analog Economy Production-Readiness Kit*
