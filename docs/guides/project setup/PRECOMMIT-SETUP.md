# Pre-commit Framework Setup — The Analog Economy

> **Step 6 of 8:** Install pre-commit hooks for automated code governance.

---

## Overview

Pre-commit hooks are your first line of defense. They catch issues before code leaves your machine, saving CI time and preventing broken commits.

```
┌─────────────────────────────────────────────────────────────────────────┐
│                    GOVERNANCE ARCHITECTURE                               │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                         │
│   Developer writes code                                                 │
│        ↓                                                                │
│   git commit                                                            │
│        ↓                                                                │
│   ┌─────────────────────────────────────────────────────────────────┐   │
│   │              PRE-COMMIT HOOKS (Local)                           │   │
│   │                                                                 │   │
│   │   Layer 0: Config Validation (fail-fast safety)                 │   │
│   │   Layer 1: Janitor (trailing whitespace, YAML check)            │   │
│   │   Layer 2: Iron Dome (type safety ratchet)                      │   │
│   │   Layer 3: Rising Tide (mock tax)                               │   │
│   │   Layer 4: isort (import ordering)                              │   │
│   │   Layer 5: Black (formatting)                                   │   │
│   │   Layer 6: Ruff (linting)                                       │   │
│   │   Layer 7: mypy (type checking)                                 │   │
│   │   Layer 8: detect-secrets (credential leak prevention)          │   │
│   │   Layer 9: SRP Size Guardrails                                  │   │
│   │   Layer 10: Mock Conformance                                    │   │
│   │                                                                 │   │
│   └─────────────────────────────────────────────────────────────────┘   │
│        ↓                                                                │
│   Commit succeeds (or fails with clear error message)                   │
│        ↓                                                                │
│   CI runs full test suite                                               │
│                                                                         │
└─────────────────────────────────────────────────────────────────────────┘
```

---

## Quick Start

### 1. Install pre-commit

```powershell
# Install pre-commit (Python tool)
pip install pre-commit

# Verify installation
pre-commit --version
```

### 2. Install hooks

```powershell
cd analog-economy

# Install git hooks
pre-commit install

# Verify hooks are installed
ls .git/hooks/pre-commit
```

### 3. Run on all files (first time)

```powershell
# Check all existing files
pre-commit run --all-files
```

---

## Governance Layers

### Layer 0: Config Validation

**Purpose:** Prevent governance fail-open from corrupted configs.

If `pyproject.toml` or `config.yaml` is corrupted, all downstream checks fail silently. Layer 0 catches this first.

```
Scenario: AI accidentally corrupts pyproject.toml
    ↓
Without Layer 0: Black uses defaults, strict mode disabled
    ↓
All checks pass, but governance is DISABLED
```

### Layer 2: Iron Dome (Type Safety Ratchet)

**Purpose:** Type-safety holes can only decrease, never increase.

Counts:
- `type: ignore` comments
- `Any` type annotations
- `cast()` calls
- `# noqa` comments

```
Day 0: Baseline = 15 holes
Day 5: Developer adds `# type: ignore` → 16 holes → BLOCKED
Day 10: Developer fixes a `Any` → 14 holes → Baseline updates
```

**Exemption:** Add `# IRON_DOME_EXEMPT: reason` to the line.

### Layer 3: Rising Tide (Mock Tax)

**Purpose:** Tests cannot be >2x larger than source when using mocks.

Heavy mocking indicates tight coupling. If a test needs extensive mocks, write an integration test instead.

```
Source: 50 lines
Test: 150 lines with Mock() → 3.0x → BLOCKED
Solution: Delete unit test, write integration test
```

**Exemption:** Add `# MOCK_TAX_EXEMPT: reason` at file top.

### Layers 4-7: Standard Python Tooling

| Layer | Tool | Purpose |
|-------|------|---------|
| 4 | isort | Import ordering (black-compatible) |
| 5 | Black | Code formatting |
| 6 | Ruff | Fast linting (replaces flake8) |
| 7 | mypy | Static type checking |

### Layer 8: Secret Detection

**Purpose:** Prevent accidental credential commits.

Detects:
- API keys (`sk-...`, `AKIA...`)
- Private keys
- High-entropy strings

**Baseline:** `.secrets.baseline` tracks known false positives.

### Layer 9: SRP Size Guardrails

**Purpose:** Enforce Single Responsibility Principle.

| File Type | Warn | Fail |
|-----------|------|------|
| Implementation | >300 LOC | >600 LOC |
| Test | >200 LOC | >300 LOC |
| Function | - | >75 LOC |

**Exemption:** Add `# SRP_EXEMPT: reason` at file top.

### Layer 10: Mock Conformance

**Purpose:** Ensure mocks match real interfaces.

```python
# BAD: Accepts any method call, even typos
mock_service = Mock()

# GOOD: Validates method names against real class
mock_service = create_autospec(RealService, instance=True)
```

---

## Native Governance Strategy

We utilize a **Native Governance** strategy. Scripts are written in the language best suited to analyze the target code.

| Target Language | Governance Script Language | Location | Reason |
|----------------|----------------------------|----------|--------|
| **Python** (`core-governance/`) | Python (`.py`) | `scripts/governance/python/` | Uses native AST parsing for Iron Dome |
| **TypeScript** (`web-portal/`) | Node.js (`.js`) | `scripts/governance/node/` | Native JSON/Package parsing |
| **C++** (`client-simulation/`) | Python/Shell | `scripts/governance/python/` | Standard for UE5 automation |

### Why Not Use One Language for All?

The `pre-commit` framework itself requires Python, so Python is already a dependency. Using "native" languages for governance provides:

1. **Accurate Parsing:** Python's `ast` module correctly counts type holes; regex is fragile
2. **Framework Parity:** Node.js natively parses `package.json` and TypeScript configs
3. **Maintainability:** Governance logic matches the code it governs

---

## Path Routing

The pre-commit config routes files to their appropriate governance checks:

| Path Pattern | Language | Checks Applied |
|--------------|----------|----------------|
| `core-governance/**/*.py` | Python | Full Python governance (Layers 0-10) |
| `web-portal/**/*.ts` | TypeScript | Supply chain, ESLint, tsc (future) |
| `client-simulation/**/*.cpp` | C++ | clang-format (future) |

### The Router Configuration

The routing logic is defined in `.pre-commit-config.yaml`:

```yaml
# Python governance
- repo: local
  hooks:
    - id: iron-dome-py
      entry: python scripts/governance/python/check_iron_dome.py
      files: ^core-governance/.*\.py$

# TypeScript governance (future)
- repo: local
  hooks:
    - id: supply-chain-ts
      entry: node scripts/governance/node/check_supply_chain.js
      files: ^web-portal/package\.json$
```

---

## Baseline Management

### Generate Type Safety Baseline

```powershell
cd analog-economy
python scripts/governance/python/check_iron_dome.py --generate-baseline
```

Output: `.governance/type-safety-baseline.json`

### Update After Fixing Issues

When you fix type-safety holes, the baseline auto-updates on successful commit. To manually regenerate:

```powershell
python scripts/governance/python/check_iron_dome.py --generate-baseline
git add .governance/type-safety-baseline.json
git commit -m "chore: update type-safety baseline"
```

---

## Common Commands

```powershell
# Run all hooks on staged files
pre-commit run

# Run all hooks on all files
pre-commit run --all-files

# Run specific hook
pre-commit run black --all-files
pre-commit run iron-dome-py --all-files

# Skip hooks (emergency only!)
git commit --no-verify -m "Emergency fix"

# Update hook versions
pre-commit autoupdate

# Clear cache
pre-commit clean
```

---

## Troubleshooting

### "Hook failed but file looks correct"

Pre-commit only checks **staged** content:

```powershell
# Check what's actually staged
git diff --staged path/to/file

# Stage your fixes
git add -p
```

### "Hook not found"

```powershell
# Clear and reinstall
pre-commit clean
pre-commit install
pre-commit autoupdate
```

### Windows-specific issues

If hooks fail on Windows but pass on Linux:

1. Use `bash -c` wrapper in hook entry
2. Check line endings: `git config core.autocrlf true`
3. Ensure Python/Node are in PATH

### Slow hooks

If commits take >30 seconds:

1. Move slow hooks to `pre-push` stage
2. Run only affected tests with TIA
3. Check for missing caching

---

## Skipping Hooks

**Skip specific hooks:**

```powershell
SKIP=mypy,black git commit -m "WIP"
```

**Skip all hooks (use sparingly):**

```powershell
git commit --no-verify -m "Emergency fix"
```

**Never skip in CI** — CI should always run all hooks.

---

## Project Structure

```
analog-economy/
├── .pre-commit-config.yaml      # Unified governance router
├── .governance/
│   ├── type-safety-baseline.json
│   └── mock-tax-baseline.json
├── .secrets.baseline            # detect-secrets baseline
├── pyproject.toml               # Python tool configs
├── scripts/
│   └── governance/
│       ├── python/              # Python governance scripts
│       │   ├── __init__.py
│       │   ├── validate_config.py    # Layer 0: Config validation
│       │   ├── check_iron_dome.py    # Layer 2: Type safety ratchet
│       │   ├── check_mock_tax.py     # Layer 3: Mock tax (2x rule)
│       │   ├── check_srp_size.py     # Layer 9: SRP guardrails
│       │   └── check_mock_conformance.py  # Layer 10: create_autospec
│       └── node/                # Node.js governance scripts
│           └── check_supply_chain.js  # Supply chain (TS, future)
└── core-governance/
    ├── gaian/                   # Source code
    └── tests/                   # Tests
```

---

## Verification Checklist

After setup, verify:

- [ ] `pre-commit install` runs without errors
- [ ] `pre-commit run --all-files` passes (or shows expected violations)
- [ ] Black auto-fixes formatting on commit
- [ ] Type errors are caught before commit
- [ ] Secrets scanner is active
- [ ] Governance scripts are executable

---

## Philosophy: The Rising Tide

> "A rising tide lifts all boats."

Our governance strategy follows three principles:

1. **Iron Dome:** Type-safety holes are tracked and can only decrease
2. **Rising Tide:** Bloated unit tests naturally get replaced by integration tests
3. **Ratchet:** Quality can only improve, never regress

Legacy code is grandfathered in baselines. New code must meet standards. Over time, the entire codebase improves.

---

## Related

- [IRON-DOME.md](./IRON-DOME-DRAFT.md) — Type safety philosophy
- [RISING-TIDE.md](./RISING-TIDE-DRAFT.md) — Mock tax philosophy
- [SUPPLY-CHAIN-SECURITY.md](./SUPPLY-CHAIN-SECURITY-DRAFT.md) — Hallucination detection

---

*Part of The Analog Economy Production-Readiness Setup — Step 6 of 8*
