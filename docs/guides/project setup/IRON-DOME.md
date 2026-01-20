# IRON-DOME.md — Type Safety Philosophy

> **The Iron Dome Strategy:** Every `Any`, `type: ignore`, or `cast()` is a hole in your defense. Track them. Ratchet them down. Never let them increase.

---

## The Problem: Death by a Thousand Cuts

```
┌─────────────────────────────────────────────────────────────────────┐
│                    THE TYPE SAFETY DECAY SPIRAL                      │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│   Day 1: Clean codebase, strict mypy                                │
│        ↓                                                            │
│   Day 10: Deadline pressure → "just add `Any` for now"              │
│        ↓                                                            │
│   Day 30: 5 `Any` types scattered in code                           │
│        ↓                                                            │
│   Day 90: Team sees `Any` is "acceptable" → 50 more added           │
│        ↓                                                            │
│   Day 180: Type system provides false confidence                    │
│        ↓                                                            │
│   RUNTIME ERRORS IN PRODUCTION                                      │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

**The Iron Dome Principle:** Intercept type-safety violations before they land in master.

---

## Type Safety Holes in Python

| Hole | Risk | Example |
|------|------|---------|
| `Any` | Complete type erasure | `def func(x: Any) -> Any:` |
| `type: ignore` | Suppresses type error | `result = bad_call()  # type: ignore` |
| `cast()` | Lies to type checker | `user = cast(User, data)` |
| No annotations | Implicit Any | `def func(x):` (without hints) |
| `# noqa` | Suppresses all lints | `import *  # noqa` |
| `pylint: disable` | Suppresses pylint | `# pylint: disable=no-member` |

### Comparison: TypeScript vs Python

| Concept | TypeScript | Python |
|---------|------------|--------|
| Any type | `: any` | `: Any` |
| Suppress error | `@ts-ignore` | `# type: ignore` |
| Type assertion | `as User` | `cast(User, data)` |
| Strict mode | `tsconfig.json` | `mypy --strict` |
| Lint disable | `eslint-disable` | `# noqa` |

---

## The Iron Dome Defense

```
┌─────────────────────────────────────────────────────────────────────┐
│                         IRON DOME LAYERS                             │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  Layer 0: CONFIG FILE VALIDATION                                    │
│    • Validate pyproject.toml, mypy.ini parse correctly              │
│    • If config is corrupted, all downstream layers fail-open        │
│    • Fastest check — run first, fail fast                           │
│                                                                     │
│  Layer 1: TYPE CHECKER STRICTNESS                                   │
│    • Enable mypy --strict mode                                      │
│    • Catches ~80% of issues automatically                           │
│                                                                     │
│  Layer 2: LINT RULES                                                │
│    • Ruff rules for type safety                                     │
│    • Catches patterns type checker allows                           │
│                                                                     │
│  Layer 3: PRE-COMMIT GATE (Iron Dome)                               │
│    • Counts type-safety holes in staged files                       │
│    • Blocks commits that increase count                             │
│    • Ratchet: only goes down, never up                              │
│                                                                     │
│  Layer 4: CI/CD VERIFICATION                                        │
│    • Full codebase scan on PR                                       │
│    • Reports total holes vs baseline                                │
│                                                                     │
│  Layer 5: SUPPLY CHAIN SECURITY                                     │
│    • Detect AI-hallucinated packages BEFORE pip install             │
│    • Block packages that don't exist on PyPI                        │
│    • Block packages < 30 days old (suspicious)                      │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

---

## Layer 0: Config File Validation

> **The Config Fragility Problem:** If `pyproject.toml` or `mypy.ini` is corrupted, all downstream governance layers fail-open. Mypy won't enforce strict mode on invalid config.

### Why Layer 0 Matters

```
┌─────────────────────────────────────────────────────────────────────┐
│                     CONFIG FRAGILITY RISK                            │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│   Scenario: AI accidentally corrupts pyproject.toml                 │
│        ↓                                                            │
│   Mypy: "Config invalid, using defaults"                            │
│        ↓                                                            │
│   Defaults = no strict mode = Any allowed everywhere                │
│        ↓                                                            │
│   All Layer 1-5 checks pass (nothing to enforce!)                   │
│        ↓                                                            │
│   GOVERNANCE SILENTLY DISABLED                                      │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

### Implementation Script

```python
#!/usr/bin/env python3
"""
Layer 0: Config File Validation
Run BEFORE any other governance checks
"""

import sys
import tomllib
from pathlib import Path


def validate_pyproject() -> bool:
    """Validate pyproject.toml is valid TOML."""
    pyproject = Path('pyproject.toml')
    if not pyproject.exists():
        print("⚠ pyproject.toml not found")
        return True  # Not an error if file doesn't exist

    try:
        with open(pyproject, 'rb') as f:
            tomllib.load(f)
        print("✓ pyproject.toml valid")
        return True
    except tomllib.TOMLDecodeError as e:
        print(f"FATAL: pyproject.toml is invalid TOML")
        print(f"  {e}")
        print("All Python governance is disabled until this is fixed.")
        return False


def validate_mypy_ini() -> bool:
    """Validate mypy.ini if it exists."""
    mypy_ini = Path('mypy.ini')
    if not mypy_ini.exists():
        return True

    try:
        import configparser
        config = configparser.ConfigParser()
        config.read(mypy_ini)
        print("✓ mypy.ini valid")
        return True
    except Exception as e:
        print(f"FATAL: mypy.ini is invalid")
        print(f"  {e}")
        return False


def main() -> int:
    print("═" * 60)
    print("LAYER 0: Config File Validation")
    print("═" * 60)

    valid = True
    valid = validate_pyproject() and valid
    valid = validate_mypy_ini() and valid

    if not valid:
        return 1

    print("═" * 60)
    print("Layer 0 passed - proceeding to governance checks")
    print("═" * 60)
    return 0


if __name__ == '__main__':
    sys.exit(main())
```

---

## The Ratchet Principle

### How It Works

```
Day 0: Generate baseline
  → Current codebase has 127 type-safety holes
  → Baseline: 127

Day 5: Developer adds feature
  → Feature introduces 2 new `Any` types
  → Total would be: 129
  → PRE-COMMIT BLOCKED: "Ratchet violation: 129 > 127"
  → Developer fixes the types
  → Commit succeeds

Day 10: Developer refactors old code
  → Removes 5 legacy `Any` types
  → Total: 122
  → Baseline updates: 122

Day 30: Overall trend
  → Started: 127
  → Current: 98
  → 23% reduction without dedicated cleanup sprint
```

### The Rule

```
┌─────────────────────────────────────────────────────────────────────┐
│                      THE RATCHET RULE                                │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│   NEW holes BLOCKED           OLD holes GRANDFATHERED               │
│   ─────────────────           ───────────────────────               │
│   Cannot add new `Any`        Existing `Any` allowed                │
│   Cannot add new `ignore`     Existing `ignore` allowed             │
│   Cannot add more `cast()`    Existing `cast()` allowed             │
│                                                                     │
│   Result: Quality can only IMPROVE over time.                       │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

---

## Implementation

### Pre-commit Hook

```yaml
# .pre-commit-config.yaml
repos:
  - repo: local
    hooks:
      - id: iron-dome
        name: Iron Dome (Type Safety)
        entry: python scripts/governance/python/check_iron_dome.py
        language: system
        types: [python]
        pass_filenames: false
        description: |
          Enforces the Iron Dome: Type-safety holes cannot increase.
          If blocked, fix the type properly instead of suppressing.
```

### The Script

```python
#!/usr/bin/env python3
"""
Iron Dome: Type Safety Enforcer

Counts type-safety holes and blocks commits that increase the count.
"""
import json
import re
import subprocess
import sys
from pathlib import Path

BASELINE_PATH = Path('.governance/baselines/iron-dome-baseline.json')

# Patterns to detect (Python)
PATTERNS = [
    {'name': 'type: ignore', 'pattern': r'#\s*type:\s*ignore', 'weight': 1},
    {'name': 'Any import', 'pattern': r'from typing import.*\bAny\b', 'weight': 0.5},
    {'name': 'Any annotation', 'pattern': r':\s*Any\b', 'weight': 1},
    {'name': '-> Any', 'pattern': r'->\s*Any\b', 'weight': 1},
    {'name': 'cast()', 'pattern': r'\bcast\s*\(', 'weight': 1},
    {'name': 'noqa', 'pattern': r'#\s*noqa', 'weight': 0.5},
    {'name': 'pylint: disable', 'pattern': r'#\s*pylint:\s*disable', 'weight': 0.5},
]


def count_holes(file_path: Path) -> tuple[float, dict]:
    """Count type-safety holes in a file."""
    content = file_path.read_text()
    total = 0.0
    breakdown = {}

    for pattern_def in PATTERNS:
        matches = re.findall(pattern_def['pattern'], content)
        count = len(matches)
        if count > 0:
            breakdown[pattern_def['name']] = count
            total += count * pattern_def['weight']

    return total, breakdown


def get_staged_files() -> list[str]:
    """Get list of staged Python files."""
    try:
        result = subprocess.run(
            ['git', 'diff', '--cached', '--name-only', '--diff-filter=ACMR'],
            capture_output=True,
            text=True,
        )
        return [f for f in result.stdout.strip().split('\n') if f.endswith('.py')]
    except Exception:
        return []


def load_baseline() -> dict:
    """Load baseline from file."""
    if not BASELINE_PATH.exists():
        return {'total_holes': 0, 'by_file': {}}
    return json.loads(BASELINE_PATH.read_text())


def save_baseline(data: dict) -> None:
    """Save baseline to file."""
    BASELINE_PATH.parent.mkdir(parents=True, exist_ok=True)
    BASELINE_PATH.write_text(json.dumps(data, indent=2))


def main():
    files = sys.argv[1:] if len(sys.argv) > 1 else get_staged_files()
    baseline = load_baseline()
    violations = []
    current_total = 0

    for file in files:
        file_path = Path(file)
        if not file_path.exists():
            continue

        total, breakdown = count_holes(file_path)
        current_total += total

        baseline_for_file = baseline.get('by_file', {}).get(file, {}).get('total', 0)

        if total > baseline_for_file:
            violations.append({
                'file': file,
                'current': total,
                'baseline': baseline_for_file,
                'breakdown': breakdown,
            })

    if violations:
        print('=' * 60)
        print('IRON DOME: Type Safety Violations')
        print('=' * 60)
        print()

        for v in violations:
            print(f"TYPE-SAFETY: {v['file']}")
            print(f"  Current: {v['current']} holes, Baseline: {v['baseline']} holes")
            print(f"  Breakdown: {v['breakdown']}")
            print(f"  Action: Fix the type properly instead of suppressing.")
            print()

        print('See: docs/guides/project setup/IRON-DOME.md')
        print()
        print('If this is a false positive, add IRON_DOME_EXEMPT comment.')
        sys.exit(1)

    # Success - update baseline if improved
    if current_total < baseline.get('total_holes', 0):
        print(f"Iron Dome: Improved! {baseline['total_holes']} → {current_total} holes")
        baseline['total_holes'] = current_total
        save_baseline(baseline)

    sys.exit(0)


if __name__ == '__main__':
    main()
```

---

## Strict Mode Configuration

### Python (pyproject.toml with mypy)

```toml
[tool.mypy]
python_version = "3.11"
strict = true
warn_return_any = true
warn_unused_ignores = true
disallow_untyped_defs = true
disallow_any_generics = true
no_implicit_optional = true
check_untyped_defs = true

# Per-module overrides for legacy code
[[tool.mypy.overrides]]
module = "legacy_module.*"
ignore_errors = true
```

### Python (Ruff for linting)

```toml
[tool.ruff]
line-length = 100
target-version = "py311"

[tool.ruff.lint]
select = [
    "E",   # pycodestyle errors
    "W",   # pycodestyle warnings
    "F",   # Pyflakes
    "I",   # isort
    "UP",  # pyupgrade
    "ANN", # flake8-annotations (type hints)
    "B",   # flake8-bugbear
    "C4",  # flake8-comprehensions
]

[tool.ruff.lint.per-file-ignores]
"tests/**/*.py" = ["ANN"]  # Don't require annotations in tests
```

---

## Exceptions

### When Type Holes Are Acceptable

1. **Third-party library without stubs**
   ```python
   # IRON_DOME_EXEMPT: Legacy library without type stubs
   from legacy_lib import process  # type: ignore[import-untyped]
   ```

2. **Test mocks** (limited scope)
   ```python
   # IRON_DOME_EXEMPT: Test mock, not production code
   mock_service = cast(PaymentService, mock)
   ```

   > ⚠️ **The `cast()` Trap in Tests:** Even in tests, `cast()` defeats type checking. If the real class changes, tests pass but production breaks. Prefer `create_autospec()`:

   ```python
   # DANGEROUS: defeats type protection
   mock = cast(UserService, Mock())
   # If UserService signature changes, test still passes, production breaks

   # BETTER: Type-safe mock
   from unittest.mock import create_autospec
   mock = create_autospec(UserService, instance=True)
   # Compiler enforces correct signature
   ```

3. **JSON parsing** (runtime validation required anyway)
   ```python
   # IRON_DOME_EXEMPT: Runtime validation via Pydantic
   raw_data: Any = json.loads(response)
   user = User.model_validate(raw_data)  # Pydantic validates
   ```

### Marking Exceptions

```python
# Single line
result = external_lib.call()  # type: ignore  # IRON_DOME_EXEMPT: No stubs

# Block (document at module level)
"""
IRON_DOME_EXEMPT_START: Legacy integration layer
This module interfaces with untyped legacy system.
Plan to add stubs in Q2.
"""
```

---

## Baseline Generation

### Initial Setup

```bash
# Generate baseline for entire codebase
python scripts/governance/python/check_iron_dome.py --generate-baseline

# Output:
# Scanning 342 files...
# Found 127 type-safety holes
# Baseline saved to .governance/baselines/iron-dome-baseline.json
```

### Baseline File Format

```json
{
  "generated": "2025-01-15T10:30:00Z",
  "total_holes": 127,
  "by_file": {
    "core-governance/gaian/services/order.py": {
      "total": 5,
      "breakdown": {
        "Any annotation": 3,
        "type: ignore": 2
      }
    },
    "core-governance/gaian/utils/helpers.py": {
      "total": 2,
      "breakdown": {
        "cast()": 2
      }
    }
  },
  "exemptions": [
    {
      "file": "core-governance/gaian/integrations/legacy.py",
      "reason": "Third-party integration without type stubs",
      "approved": "2025-01-10"
    }
  ]
}
```

---

## Supply Chain Security

> **The Supply Chain Problem:** AI coders hallucinate package names ~5-10% of the time. Attackers register these names on PyPI with malware. If you install them, setup.py executes malware.

### The Attack Vector

```
┌─────────────────────────────────────────────────────────────────────┐
│                    SUPPLY CHAIN ATTACK FLOW                          │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│   1. AI suggests: `from utils_helper import process`                │
│        ↓                                                            │
│   2. Package 'utils-helper' doesn't exist (AI hallucination)        │
│        ↓                                                            │
│   3. Attacker registers 'utils-helper' on PyPI                      │
│        ↓                                                            │
│   4. Developer runs `pip install utils-helper`                      │
│        ↓                                                            │
│   5. setup.py executes malware                                      │
│        ↓                                                            │
│   COMPROMISED                                                       │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

### Defense Layers

| Layer | What It Does | When It Runs |
|-------|--------------|--------------|
| **Hallucination Detector** | Blocks non-existent or very new packages | Pre-commit, CI (before pip install) |
| **pip --require-hashes** | Fails if hash doesn't match lockfile | CI |
| **Requirements Change Detection** | Flags PRs that modify requirements.txt | CI |
| **pip-audit** | Catches known vulnerabilities | CI |

### Hallucination Detector Script

```python
#!/usr/bin/env python3
"""
Supply Chain Security: Package Hallucination Detector

Checks requirements.txt for packages that:
1. Don't exist on PyPI (true hallucinations)
2. Were created < 30 days ago (suspicious timing)
"""

import json
import sys
from datetime import datetime, timedelta
from pathlib import Path
from urllib.request import urlopen
from urllib.error import HTTPError


def check_package(name: str) -> dict:
    """Check if package exists on PyPI and get creation date."""
    url = f"https://pypi.org/pypi/{name}/json"
    try:
        with urlopen(url, timeout=10) as response:
            data = json.loads(response.read())
            # Get first upload date
            releases = data.get('releases', {})
            if not releases:
                return {'exists': True, 'age_days': None}

            first_release = min(releases.keys())
            upload_time = data['releases'][first_release][0]['upload_time']
            created = datetime.fromisoformat(upload_time.replace('Z', '+00:00'))
            age = (datetime.now(created.tzinfo) - created).days

            return {'exists': True, 'age_days': age}
    except HTTPError as e:
        if e.code == 404:
            return {'exists': False, 'age_days': None}
        raise
    except Exception:
        return {'exists': True, 'age_days': None}  # Assume OK on network error


def parse_requirements(filepath: Path) -> list[str]:
    """Parse package names from requirements.txt."""
    packages = []
    for line in filepath.read_text().splitlines():
        line = line.strip()
        if not line or line.startswith('#') or line.startswith('-'):
            continue
        # Extract package name (before version specifier)
        name = line.split('==')[0].split('>=')[0].split('<=')[0].split('~=')[0].split('[')[0]
        packages.append(name.strip())
    return packages


def main() -> int:
    req_file = Path(sys.argv[1]) if len(sys.argv) > 1 else Path('requirements.txt')

    if not req_file.exists():
        print(f"Requirements file not found: {req_file}")
        return 0

    packages = parse_requirements(req_file)
    violations = []
    suspicious = []

    print(f"Checking {len(packages)} packages against PyPI...")

    for name in packages:
        result = check_package(name)

        if not result['exists']:
            violations.append({
                'package': name,
                'issue': 'Package does not exist on PyPI (hallucination?)'
            })
        elif result['age_days'] is not None and result['age_days'] < 30:
            suspicious.append({
                'package': name,
                'age_days': result['age_days'],
                'issue': f'Package is only {result["age_days"]} days old'
            })

    if violations:
        print('\n🚫 SUPPLY CHAIN VIOLATION: Hallucinated Packages\n')
        for v in violations:
            print(f"  {v['package']}: {v['issue']}")
        print('\nThese packages do not exist on PyPI.')
        print('This may be an AI hallucination or a typo.')
        return 1

    if suspicious:
        print('\n⚠️  SUPPLY CHAIN WARNING: Suspicious Packages\n')
        for s in suspicious:
            print(f"  {s['package']}: {s['issue']}")
        print('\nThese packages are very new. Verify they are legitimate.')
        # Warning only, not blocking

    print('✓ Supply chain check passed')
    return 0


if __name__ == '__main__':
    sys.exit(main())
```

### CI Configuration

```yaml
# .github/workflows/governance-ci.yml
- name: "Supply Chain: Hallucination Detector (No pip install)"
  run: python scripts/governance/python/check_supply_chain.py requirements.txt
```

> **Critical:** The hallucination detector runs BEFORE `pip install` to prevent setup.py execution.

---

## The Iron Dome Dashboard

### CI/CD Report Example

```
═══════════════════════════════════════════════════════════════
                    IRON DOME STATUS REPORT
═══════════════════════════════════════════════════════════════

Overall Health: ████████████░░░░ 78% (98/127 holes remaining)

Trend (last 30 days):
  Day  1: ████████████████████████████████ 127
  Day 10: █████████████████████████████ 115
  Day 20: █████████████████████████ 105
  Day 30: ██████████████████████ 98

Top Offenders:
  1. gaian/services/order.py      12 holes
  2. gaian/api/handlers.py         8 holes
  3. gaian/utils/legacy.py         7 holes

Recent Improvements:
  - gaian/models/user.py: 5 → 0 holes (fixed!)
  - gaian/services/auth.py: 3 → 1 holes

═══════════════════════════════════════════════════════════════
```

---

## Summary

| Concept | Description |
|---------|-------------|
| **Iron Dome** | Intercept type-safety violations before they land in master |
| **Layer 0** | Config file validation — prevent governance fail-open |
| **Type Holes** | `Any`, `type: ignore`, `cast()` — breaches in type safety |
| **`cast()` Trap** | Even test mocks should use `create_autospec()` |
| **Ratchet** | Count can only go down, never up |
| **Baseline** | Starting point for existing codebases |
| **Exemptions** | Documented exceptions with reason |

---

## Related

- [GOV-TESTING.md](./GOV-TESTING.md) — Governance testing implementation
- [TDD-GUIDE.md](../development/TDD-GUIDE.md) — Test-driven development practices
- [PRECOMMIT-SETUP.md](./PRECOMMIT-SETUP.md) — Pre-commit hook configuration

> **Note:** Iron Dome guards compile-time type safety (your source code). For runtime type safety at system boundaries (API responses, webhooks, config files), use Pydantic models with validation.

---

*Part of The Analog Economy Production-Readiness Kit*
