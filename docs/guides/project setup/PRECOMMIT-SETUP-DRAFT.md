<!--
╔══════════════════════════════════════════════════════════════════════╗
║  MAULT PRO - Production-Readiness Kit                                ║
║  Copyright © 2025 Mault. All rights reserved.                        ║
║                                                                      ║
║  This document is licensed for use with the Mault VS Code Extension. ║
║  Redistribution or resale is prohibited.                             ║
║                                                                      ║
║  https://mault.dev | support@mault.dev                               ║
╚══════════════════════════════════════════════════════════════════════╝
-->

# Pre-commit Framework Setup Guide

> **Step 6 of 8** in the Production-Readiness Kit
> **Applies to:** Mault Pro ($99 one-time)

---

## Overview

Pre-commit hooks are your first line of defense. They catch issues before code leaves your machine, saving CI time and preventing embarrassing commits.

### Why Pre-commit Matters

| Without Pre-commit | With Pre-commit |
|-------------------|-----------------|
| Push broken code, wait for CI to fail | Catch errors instantly before commit |
| Formatting inconsistencies in PRs | Auto-fix formatting on every commit |
| Secrets accidentally committed | Block secrets before they hit history |
| CI runs for 10 minutes, then fails lint | Fail in 5 seconds locally |

### The Pre-commit Philosophy

**Layers:** Pre-commit runs in layers, from fastest to slowest. The most advanced configuration (TypeScript) has **12 layers** (0-11):

| Layer | Name | Purpose |
|-------|------|---------|
| 0 | Config File Validation | Prevent governance fail-open from corrupted configs |
| 1 | Compilation & Static Analysis | Catch type errors Jest might mask |
| 2 | Rising Tide (Mock Tax) | Block oversized unit tests (2x rule) |
| 3 | Test Impact Analysis (TIA) | Run only affected tests |
| 4 | Adversarial Mock Scan | Prevent mocking reality |
| 5 | Precision Coverage Ratchet | Enforce 80% on new files |
| 6 | Security Gate | npm audit for vulnerabilities |
| 7 | Integration Test Pairing | Buddy System enforcement |
| 8 | Type Safety Gate (any Ratchet) | Block new `any` usage |
| 9 | Dead Code Gate | Detect silent catches |
| 10 | Supply Chain Security | Detect hallucinated packages |
| 11 | Behavioral Test Pairing | Perception-critical files need behavioral tests |

The Python configuration has **10 layers** for parity with TypeScript:

| Layer | Name | Purpose |
|-------|------|---------|
| 1-4 | Style | trailing-whitespace, isort, black, flake8 |
| 5 | Logic | mypy (type checking) |
| 6 | Security | detect-secrets |
| 7 | Branch | branch-name-check |
| 8 | Architecture | SRP Size Guardrails |
| 9 | Architecture | Duplicate Code Detection |
| 10 | Testing | Mock Conformance (create_autospec enforcement) |

---

## Section 1: Installation

### Install pre-commit

**All platforms:**
```bash
pip install pre-commit
```

**Or with pipx (isolated):**
```bash
pipx install pre-commit
```

**Verify installation:**
```bash
pre-commit --version
# pre-commit 3.6.0
```

### Initialize in Your Project

```bash
cd your-project

# Create config file
touch .pre-commit-config.yaml

# Install git hooks
pre-commit install

# Verify
ls -la .git/hooks/pre-commit
```

---

## Section 2: Basic Configuration

### Minimal Configuration

```yaml
# .pre-commit-config.yaml
repos:
  # Basic file hygiene
  - repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v4.5.0
    hooks:
      - id: trailing-whitespace
      - id: end-of-file-fixer
      - id: check-yaml
      - id: check-json
      - id: check-added-large-files
        args: ['--maxkb=500']
```

### Language-Specific Configurations

#### Node.js / TypeScript (Gold Standard - 10 Layers)

This is the most advanced configuration, implementing the Evolved Testing Manifesto v2.9:

```yaml
# .pre-commit-config-ts.yaml
# Implements the Evolved Testing Manifesto v2.9 (Process Isolation Era)
#
# Installation:
#   pip install pre-commit
#   pre-commit install -c .pre-commit-config-ts.yaml

fail_fast: true

repos:
  # =========================================================================
  # LAYER 0: CONFIG FILE VALIDATION (Fail-First Safety)
  # =========================================================================
  # Validates that config files parse correctly BEFORE running heavy tools.
  # If tsconfig.json or eslint.config.js is corrupted, all downstream
  # governance layers fail-open. Catch this first.
  - repo: local
    hooks:
      - id: config-validation
        name: Config File Validation (Layer 0)
        entry: bash -c '
          echo "Validating config files..."
          node -e "JSON.parse(require(\"fs\").readFileSync(\"tsconfig.json\"))" || { echo "FATAL: tsconfig.json is invalid"; exit 1; }
          node -e "require(\"./eslint.config.js\")" || { echo "FATAL: eslint.config.js failed to load"; exit 1; }
          node -e "require(\"./jest.config.js\")" || { echo "FATAL: jest.config.js failed to load"; exit 1; }
          echo "✓ Config files valid"
        '
        language: system
        pass_filenames: false
        stages: [pre-commit]
        description: |
          Validates config files before running heavy governance tools.
          Prevents fail-open scenarios from corrupted configs.

  # =========================================================================
  # LAYER 1: COMPILATION & STATIC ANALYSIS (Fail Fast)
  # =========================================================================
  - repo: local
    hooks:
      - id: typescript-compile
        name: TypeScript Compilation Check
        entry: bash -c 'cd extension && npm run qa:type-check'
        language: system
        files: \.(ts|tsx)$
        pass_filenames: false
        stages: [pre-commit]
        description: |
          Catch compilation issues that Jest might mask.

      - id: eslint-fix
        name: ESLint (with auto-fix)
        entry: bash -c 'cd extension && npm run lint'
        language: system
        files: (src|tests)/.*\.ts$
        stages: [pre-commit]

  # =========================================================================
  # LAYER 2: THE RISING TIDE (Mock Tax)
  # =========================================================================
  - repo: local
    hooks:
      - id: check-mock-tax
        name: Rising Tide Enforcer (Mock Tax)
        entry: bash -c 'cd extension && node scripts/governance/check-mock-tax.js'
        language: system
        files: tests/unit/.*\.test\.ts$
        stages: [pre-commit]
        description: |
          Enforces the "2x Rule": If a unit test is >2x larger than source
          due to heavy mocking, it is rejected.
          Solution: Delete unit test, write Integration Test.

  # =========================================================================
  # LAYER 3: TEST IMPACT ANALYSIS (TIA)
  # =========================================================================
  - repo: local
    hooks:
      - id: jest-tia
        name: Jest TIA (Randomized & Isolated)
        entry: bash -c 'cd extension && npm run test:unit:randomize -- --findRelatedTests --bail 1'
        language: system
        files: \.ts$
        pass_filenames: true
        stages: [pre-commit]
        description: |
          Runs only tests related to staged files.
          - Randomized order (catches contamination)
          - Process Isolation (prevents memory leaks)

  # =========================================================================
  # LAYER 4: ADVERSARIAL MOCK SCAN
  # =========================================================================
  - repo: local
    hooks:
      - id: check-adversarial-mocks
        name: Adversarial Mock Scan
        entry: bash -c 'cd extension && node scripts/governance/check-adversarial-mocks.js'
        language: system
        files: tests/.*\.ts$
        pass_filenames: true
        description: |
          Rule 7: Don't Mock the Truth.
          Prevents mocking process.cwd(), __dirname, etc.

  # =========================================================================
  # LAYER 5: PRECISION COVERAGE (Ratchet)
  # =========================================================================
  - repo: local
    hooks:
      - id: check-coverage-ratchet
        name: Precision Coverage Ratchet
        entry: bash -c 'cd extension && node scripts/coverage/check-changed-files.mjs'
        language: system
        pass_filenames: false
        description: |
          Ensures new files meet 80% coverage, existing files don't regress.

  # =========================================================================
  # LAYER 6: SECURITY GATE
  # =========================================================================
  - repo: local
    hooks:
      - id: npm-audit
        name: Security Audit (npm audit)
        entry: bash -c 'cd extension && npm audit --audit-level=high --omit=dev 2>/dev/null || echo "Security audit skipped"'
        language: system
        pass_filenames: false
        stages: [pre-commit]

  # =========================================================================
  # LAYER 7: INTEGRATION TEST PAIRING (Buddy System)
  # =========================================================================
  - repo: local
    hooks:
      - id: integration-pairing
        name: Integration Test Pairing (Buddy System)
        entry: bash -c 'cd extension && node scripts/governance/verify-integration-pairing.js'
        language: system
        files: (src/commands|src/services/detectors)/.*\.ts$
        pass_filenames: false
        stages: [pre-commit]
        description: |
          Every user-facing feature MUST have integration test.
          Legacy orphans grandfathered in governance-exemptions.json.

  # =========================================================================
  # LAYER 8: TYPE SAFETY GATE (any Ratchet)
  # =========================================================================
  - repo: local
    hooks:
      - id: type-safety-gate
        name: Type Safety Gate (any Ratchet)
        entry: bash -c 'cd extension && node scripts/governance/check-any-usage.js --staged'
        language: system
        files: src/.*\.ts$
        pass_filenames: false
        stages: [pre-commit]
        description: |
          Block commits that increase 'any' usage.
          Baseline tracked in any-baseline.json (ratchet only goes DOWN).

  # =========================================================================
  # LAYER 9: DEAD CODE GATE (Silent Catch Detection)
  # =========================================================================
  - repo: local
    hooks:
      - id: dead-code-gate
        name: Dead Code Gate (Silent Catches)
        entry: bash -c 'cd extension && node scripts/governance/check-silent-catches.js --staged'
        language: system
        files: src/.*\.ts$
        pass_filenames: false
        stages: [pre-commit]
        description: |
          Catch blocks must log, throw, or be explicitly marked silent.
          Mark intentional silent catches with // SILENT_CATCH: reason
```

#### Python (10 Layers)

Production-ready Python configuration with 10-layer parity to TypeScript:

```yaml
# .pre-commit-config.yaml
# Implements 10-layer governance for Python (parity with TypeScript)

repos:
  # =========================================================================
  # LAYERS 1-4: STYLE (How code looks)
  # =========================================================================

  # Layer 1: Standard Janitor (Fixes Trailing Lines & file endings)
  - repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v4.4.0
    hooks:
      - id: trailing-whitespace
      - id: end-of-file-fixer
      - id: check-yaml
      - id: check-added-large-files

  # Layer 2: Import Sorter (Fixes "Module import order")
  - repo: https://github.com/pycqa/isort
    rev: 5.12.0
    hooks:
      - id: isort
        args: ["--profile", "black", "--line-length=100"]
        files: ^service/

  # Layer 3: Python Formatter (Fixes Line Length / E501)
  - repo: https://github.com/psf/black
    rev: 25.11.0
    hooks:
      - id: black
        files: ^service/
        args: [--line-length=100]

  # Layer 4: Python Linter (Catches Style Errors)
  - repo: https://github.com/pycqa/flake8
    rev: 6.1.0
    hooks:
      - id: flake8
        files: ^service/
        args: [--max-line-length=100, --extend-ignore=E203]

  # =========================================================================
  # LAYER 5: LOGIC (How code behaves)
  # =========================================================================

  # Layer 5: Static Type Checker (Catches Logic/Type Errors)
  - repo: https://github.com/pre-commit/mirrors-mypy
    rev: v1.13.0
    hooks:
      - id: mypy
        files: ^service/
        args: [--ignore-missing-imports, --no-strict-optional]
        additional_dependencies: [types-requests, types-PyYAML]

  # =========================================================================
  # LAYER 6: SECURITY (Prevents credential leaks)
  # =========================================================================

  # Layer 6: Secret Detection
  - repo: https://github.com/Yelp/detect-secrets
    rev: v1.5.0
    hooks:
      - id: detect-secrets
        args: ['--baseline', '.secrets.baseline']
        exclude: package-lock\.json|\.env\.example

  # =========================================================================
  # LAYER 7: BRANCH VALIDATION
  # =========================================================================

  # Layer 7: Branch Naming Convention
  - repo: local
    hooks:
      - id: branch-name-check
        name: Check branch naming convention
        entry: bash scripts/check-branch-name.sh
        language: system
        always_run: true
        pass_filenames: false
        stages: [commit]

  # =========================================================================
  # LAYERS 8-9: ARCHITECTURE (SRP & Duplication)
  # =========================================================================

  # Layer 8: SRP Size Guardrails
  - repo: local
    hooks:
      - id: python-srp-check
        name: SRP Size Guardrails (Python)
        entry: bash -c 'cd service && python scripts/ci/check_srp_size.py'
        language: system
        files: ^service/.*\.py$
        pass_filenames: false
        stages: [pre-commit]
        description: |
          Enforces Single Responsibility Principle via file size limits.
          Files >300 LOC warn, >600 LOC fail.

  # Layer 9: Duplicate Code Detection
  - repo: local
    hooks:
      - id: python-duplication-check
        name: Duplicate Code Detection (Python)
        entry: bash -c 'cd service && python scripts/ci/check_duplication.py'
        language: system
        files: ^service/.*\.py$
        pass_filenames: false
        stages: [pre-commit]
        description: |
          Detects copy-paste code that should be refactored.

  # =========================================================================
  # LAYER 10: TESTING (Mock Conformance)
  # =========================================================================

  # Layer 10: Mock Conformance Check
  - repo: local
    hooks:
      - id: python-mock-conformance
        name: Mock Conformance Check (Python)
        entry: bash -c 'cd service && python scripts/ci/check_mock_conformance.py'
        language: system
        files: ^service/tests/conftest\.py$
        pass_filenames: false
        stages: [pre-commit]
        description: |
          Enforces create_autospec() instead of bare Mock().
          Prevents mock drift - mocks must match real service interfaces.
          See Issue #1629 for details.

# 10 Layers of Protection:
# 1-4. STYLE: trailing-whitespace, isort, black, flake8 (how code looks)
# 5.   LOGIC: mypy (type checking - catches errors before runtime)
# 6.   SECURITY: detect-secrets (prevents credential leaks)
# 7.   BRANCH: branch-name-check (naming convention validation)
# 8.   ARCHITECTURE: SRP size guardrails (file size limits)
# 9.   ARCHITECTURE: Duplicate code detection (copy-paste prevention)
# 10.  TESTING: Mock conformance (create_autospec enforcement)
```

---

## Section 2.5: Layer 0 Config Validation (All Languages)

> **The Config Fragility Problem:** If configuration files are corrupted, all downstream governance layers fail-open. TypeScript won't enforce strict mode with invalid JSON. ESLint won't run rules if config doesn't parse. **Always validate configs first.**

### Language-Specific Config Validation

| Language | Config Files | Validation Command |
|----------|--------------|-------------------|
| **TypeScript** | `tsconfig.json`, `eslint.config.js`, `jest.config.js` | `node -e "JSON.parse(require('fs').readFileSync('tsconfig.json'))"` |
| **Python** | `pyproject.toml`, `setup.cfg`, `pytest.ini` | `python -c "try: import tomllib; except: import tomli as tomllib; tomllib.load(open('pyproject.toml', 'rb'))"` |

### Python Layer 0 Hook

```yaml
# Add to .pre-commit-config.yaml (Python projects)
# Note: Uses tomllib (Python 3.11+) with tomli fallback (pip install tomli for <3.11)
- repo: local
  hooks:
    - id: config-validation
      name: Config File Validation (Layer 0)
      entry: bash -c '
        echo "Validating config files..."
        python -c "
try:
    import tomllib
except ImportError:
    import tomli as tomllib
tomllib.load(open(\"pyproject.toml\", \"rb\"))
" || { echo "FATAL: pyproject.toml is invalid"; exit 1; }
        echo "✓ Config files valid"
      '
      language: system
      pass_filenames: false
      stages: [pre-commit]
```

### Why Layer 0 Matters

```
┌─────────────────────────────────────────────────────────────────────┐
│                   CONFIG FRAGILITY RISK                              │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│   Scenario: AI accidentally corrupts tsconfig.json                  │
│        ↓                                                            │
│   TypeScript: "tsconfig invalid, using defaults"                    │
│        ↓                                                            │
│   Defaults = no strict mode = `any` allowed everywhere              │
│        ↓                                                            │
│   All Layer 1-9 checks pass (nothing to enforce!)                   │
│        ↓                                                            │
│   GOVERNANCE SILENTLY DISABLED                                      │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

**Layer 0 is the fastest check.** Run it first, fail fast.

---

## Section 3: Advanced Hooks (Governance Scripts)

The advanced TypeScript configuration uses custom governance scripts. Here's how each works:

### Layer 2: Mock Tax (Rising Tide)

**Purpose:** Reject unit tests that are >2x larger than source code due to excessive mocking.

```javascript
// scripts/governance/check-mock-tax.js
const MAX_RATIO = 2.0;
const MIN_SOURCE_LINES = 15;

stagedFiles.forEach((testFile) => {
  const testLines = countLines(testFile);
  const srcLines = countLines(mapToSourceFile(testFile));
  const hasMocks = testContent.includes('jest.mock');

  if (srcLines > MIN_SOURCE_LINES && hasMocks) {
    const ratio = testLines / srcLines;
    if (ratio > MAX_RATIO) {
      console.error(`REJECTED: ${testFile} - ${ratio.toFixed(1)}x ratio`);
      console.error('Solution: Delete unit test. Write Integration Test.');
      hasErrors = true;
    }
  }
});
```

### Layer 4: Adversarial Mock Scan

**Purpose:** Prevent mocking "reality" - things that should never be mocked.

```javascript
// scripts/governance/check-adversarial-mocks.js
const FORBIDDEN_MOCKS = [
  'process.cwd',
  '__dirname',
  '__filename',
  'Date.now',
  'Math.random'  // unless explicitly seeded
];

// Scan test files for forbidden mock patterns
```

### Layer 5: Coverage Ratchet

**Purpose:** New files must have 80% coverage; existing files cannot regress.

```javascript
// scripts/coverage/check-changed-files.mjs
const THRESHOLD = 80;

changedFiles.forEach(file => {
  if (isNewFile(file)) {
    // New files: must meet 80% threshold
    if (coverage < THRESHOLD) fail();
  } else {
    // Existing files: cannot regress
    if (coverage < baselineCoverage[file]) fail();
  }
});
```

### Layer 7: Integration Test Pairing (Buddy System)

**Purpose:** Every user-facing feature must have an integration test.

```javascript
// scripts/governance/verify-integration-pairing.js
const FEATURE_PATHS = ['src/commands/', 'src/services/detectors/'];
const TEST_PATH = 'tests/integration/';

features.forEach(feature => {
  const expectedTest = mapToIntegrationTest(feature);
  if (!fs.existsSync(expectedTest)) {
    if (!isExempted(feature)) {
      console.error(`Missing integration test for: ${feature}`);
      hasErrors = true;
    }
  }
});
```

### Layer 8: any Ratchet

**Purpose:** Block commits that increase `any` usage. Baseline only goes down.

```javascript
// scripts/governance/check-any-usage.js
const baseline = JSON.parse(fs.readFileSync('any-baseline.json'));
const currentCount = countAnyInFile(file);

if (currentCount > baseline.threshold) {
  console.error('GOVERNANCE BLOCK: any count increased!');
  console.error(`Baseline: ${baseline.threshold}, Current: ${currentCount}`);
  console.error('Instructions: Replace any with proper types');
  process.exit(1);
}
```

### Layer 9: Silent Catch Detection

**Purpose:** Catch blocks must handle errors, not swallow them.

```javascript
// scripts/governance/check-silent-catches.js
// Detects: catch (e) { } or catch (e) { /* empty */ }
// Allowed: catch (e) { logger.error(e); }
// Allowed: catch (e) { /* SILENT_CATCH: intentionally ignored */ }

const SILENT_CATCH_MARKER = '// SILENT_CATCH:';
```

### Branch Naming Hook (Python)

**Purpose:** Enforce branch naming conventions (feat/, fix/, etc.).

```bash
#!/bin/bash
# scripts/check-branch-name.sh
BRANCH=$(git rev-parse --abbrev-ref HEAD)
PATTERN="^(feat|fix|docs|chore|refactor|test|deps)/"

if [[ "$BRANCH" == "main" || "$BRANCH" == "develop" ]]; then
  exit 0  # Allow main branches
fi

if [[ ! "$BRANCH" =~ $PATTERN ]]; then
  echo "Invalid branch name: $BRANCH"
  echo "Must match: feat/, fix/, docs/, chore/, refactor/, test/, deps/"
  exit 1
fi
```

### Test Impact Analysis Hook

Run only tests affected by your changes:

```yaml
- repo: local
  hooks:
    - id: jest-tia
      name: Jest TIA (Randomized & Isolated)
      entry: bash -c 'npm run test:unit:randomize -- --findRelatedTests --bail 1'
      language: system
      files: \.ts$
      pass_filenames: true
      stages: [pre-commit]
```

---

## Section 4: Hook Stages

Pre-commit supports different stages for different operations:

| Stage | When it Runs | Use Case |
|-------|--------------|----------|
| `pre-commit` | Before commit | Formatting, linting, fast checks |
| `pre-push` | Before push | Tests, slow type checks |
| `commit-msg` | After writing message | Commit message format validation |
| `manual` | Only when explicitly called | Long-running checks |

### Example Multi-Stage Configuration

```yaml
repos:
  # Fast checks - run on every commit
  - repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v4.5.0
    hooks:
      - id: trailing-whitespace
      - id: check-yaml

  # Formatting - run on commit
  - repo: https://github.com/psf/black
    rev: 24.1.1
    hooks:
      - id: black

  # Tests - run on push only
  - repo: local
    hooks:
      - id: unit-tests
        name: Unit Tests (TIA)
        entry: npm run test:tia
        language: system
        pass_filenames: false
        stages: [pre-push]

  # Commit message validation
  - repo: https://github.com/commitizen-tools/commitizen
    rev: v3.13.0
    hooks:
      - id: commitizen
        stages: [commit-msg]
```

### Installing Stage-Specific Hooks

```bash
# Install all stages
pre-commit install --hook-type pre-commit
pre-commit install --hook-type pre-push
pre-commit install --hook-type commit-msg

# Or install all at once
pre-commit install --install-hooks
```

---

## Section 5: Secrets Prevention

### Detect-Secrets Setup

**Initialize baseline (first time):**
```bash
# Scan existing codebase and create baseline
detect-secrets scan > .secrets.baseline

# Review and audit baseline
detect-secrets audit .secrets.baseline
```

**Add to .gitignore:**
```
# Keep baseline in repo, but not the actual secrets
!.secrets.baseline
```

**Hook configuration:**
```yaml
- repo: https://github.com/Yelp/detect-secrets
  rev: v1.4.0
  hooks:
    - id: detect-secrets
      args: ['--baseline', '.secrets.baseline']
```

### What Detect-Secrets Catches

- API keys (`sk-...`, `api_key=...`)
- AWS credentials (`AKIA...`)
- Private keys (`-----BEGIN RSA PRIVATE KEY-----`)
- High-entropy strings (potential secrets)
- Common secret patterns

### Handling False Positives

```bash
# Mark a detected secret as a false positive
detect-secrets audit .secrets.baseline

# Or inline exclude (use sparingly)
# pragma: allowlist secret
```

---

## Section 6: Performance Optimization

### Parallel Execution

Pre-commit can run hooks in parallel:

```bash
# Set in environment or pre-commit config
export PRE_COMMIT_ALLOW_PARALLEL=1
```

Or in config:
```yaml
# .pre-commit-config.yaml
default_stages: [commit]
fail_fast: false  # Continue running other hooks on failure
```

### Skipping Hooks

**Skip specific hooks:**
```bash
SKIP=eslint,tsc git commit -m "WIP: quick save"
```

**Skip all hooks:**
```bash
git commit --no-verify -m "Emergency fix"
```

**Never skip in CI** - CI should always run all hooks.

### Hook Timeout

For slow hooks, set a timeout:

```yaml
- repo: local
  hooks:
    - id: slow-check
      name: Slow Check
      entry: ./slow-script.sh
      language: system
      require_serial: true  # Don't run in parallel
```

---

## Section 7: CI Integration

### Running Pre-commit in CI

```yaml
# .github/workflows/ci.yml
jobs:
  pre-commit:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: '3.11'
      - uses: pre-commit/action@v3.0.1
```

### Caching Pre-commit Environments

```yaml
- uses: actions/cache@v4
  with:
    path: ~/.cache/pre-commit
    key: pre-commit-${{ hashFiles('.pre-commit-config.yaml') }}
```

### Auto-fixing in CI

If a hook auto-fixes files, commit the fix:

```yaml
- uses: pre-commit/action@v3.0.1
  with:
    extra_args: --all-files

- name: Commit fixes
  if: failure()
  run: |
    git config user.name github-actions
    git config user.email github-actions@github.com
    git add .
    git commit -m "style: auto-fix from pre-commit"
    git push
```

---

## Section 8: Team Onboarding

### First-Time Setup for New Developers

Add to your README:

```markdown
## Development Setup

1. Install pre-commit:
   ```bash
   pip install pre-commit
   ```

2. Install hooks:
   ```bash
   pre-commit install
   ```

3. (Optional) Run on all files:
   ```bash
   pre-commit run --all-files
   ```
```

### Automatic Installation

Add to package.json (Node.js):
```json
{
  "scripts": {
    "prepare": "pre-commit install || true"
  }
}
```

Add to setup.py (Python):
```python
from setuptools import setup

setup(
    # ...
    setup_requires=['pre-commit'],
)
```

---

## Troubleshooting

### Hook Fails but File Looks Correct

**Symptoms:** Hook fails but the file passes when checked manually

**Causes & Fixes:**
1. **Staged vs. working copy:** Pre-commit only checks staged content
   ```bash
   git add -p  # Stage specific changes
   ```
2. **Partial staging:** File has both staged and unstaged changes
   ```bash
   git diff --staged path/to/file
   ```
3. **Hook caching:** Clear pre-commit cache
   ```bash
   pre-commit clean
   pre-commit run --all-files
   ```

### "Hook not found" Error

**Symptoms:** `[ERROR] Hook 'xxx' not found`

**Fixes:**
1. Update pre-commit config revisions:
   ```bash
   pre-commit autoupdate
   ```
2. Clear and reinstall:
   ```bash
   pre-commit clean
   pre-commit install
   ```

### Slow Hooks

**Symptoms:** Commits take >30 seconds

**Fixes:**
1. Move slow hooks to `pre-push` stage
2. Use TIA for tests (only run affected)
3. Check for missing caching:
   ```yaml
   - repo: local
     hooks:
       - id: slow-hook
         language: system
         require_serial: false  # Allow parallel
   ```

### Windows-Specific Issues

**Symptoms:** Hooks fail on Windows but pass on Linux

**Fixes:**
1. Use `bash -c` wrapper for shell commands:
   ```yaml
   entry: bash -c 'npm run lint'
   ```
2. Use system language for cross-platform:
   ```yaml
   language: system
   ```
3. Check line endings:
   ```bash
   git config core.autocrlf true
   ```

---

## AI Prompts

### Setup Pre-commit
```
Help me set up pre-commit for my [Node.js/Python] project.

Requirements:
- Formatter ([Prettier/Black])
- Linter ([ESLint/Ruff or flake8])
- Type checker if applicable ([TypeScript/mypy])
- Secrets scanner

Current project structure: [describe or paste tree]
```

### Add Custom Hook
```
Help me create a custom pre-commit hook that [describe what it should check].

Requirements:
- Should run on [file types]
- Should [pass/fail] when [condition]
- Runs in [pre-commit/pre-push] stage

My tech stack is [Node.js/Python].
```

### Debug Hook Failure
```
My pre-commit hook is failing with this error: [paste error]

Hook configuration: [paste relevant hook config]

The file passes when I run the check manually: [paste manual check command and output]

Help me understand why the hook is failing and how to fix it.
```

### Migrate to Pre-commit
```
I have existing linting/formatting setup without pre-commit:

Current setup:
- Formatter: [tool and config]
- Linter: [tool and config]
- How I run them: [npm scripts / makefile / etc]

Help me migrate this to pre-commit while keeping the same behavior.
```

---

## Verification Checklist

Before considering pre-commit setup complete:

- [ ] `pre-commit install` runs without errors
- [ ] Formatter hook auto-fixes code
- [ ] Linter hook catches violations
- [ ] Secrets scanner is configured with baseline
- [ ] Hooks pass on clean checkout
- [ ] CI runs pre-commit on all files
- [ ] README includes setup instructions
- [ ] Team has run `pre-commit install`
- [ ] .pre-commit-config.yaml is committed
- [ ] Hook versions are pinned (not `latest`)

---

## Quick Reference

### Common Commands

```bash
# Install hooks
pre-commit install

# Run on all files
pre-commit run --all-files

# Run specific hook
pre-commit run eslint --all-files

# Skip hooks (emergency only)
git commit --no-verify -m "message"

# Update hook versions
pre-commit autoupdate

# Clear cache
pre-commit clean

# Uninstall hooks
pre-commit uninstall
```

### Hook Stages Reference

```yaml
stages: [commit]        # Before commit (default)
stages: [pre-push]      # Before push
stages: [commit-msg]    # After writing commit message
stages: [manual]        # Only when explicitly run
stages: [commit, push]  # Multiple stages
```

---

## Adoption Strategy

### Incremental Adoption Path

Not every project needs 10 layers on day one. Here's how to adopt incrementally:

| Phase | Layers | Time to Implement |
|-------|--------|-------------------|
| **Phase 1: Basics** | Janitor, Formatter, Linter | 15 minutes |
| **Phase 2: Safety** | Type Checker, Secrets Scanner | 30 minutes |
| **Phase 3: Quality** | TIA, Coverage Ratchet | 1 hour |
| **Phase 4: Governance** | Mock Tax, any Ratchet, Integration Pairing | 2-4 hours |
| **Phase 5: Full Suite** | All 10 layers (0-9) | Ongoing |

### Minimum Viable Pre-commit

Start with this and expand:

```yaml
# .pre-commit-config.yaml (Minimum Viable)
repos:
  - repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v4.4.0
    hooks:
      - id: trailing-whitespace
      - id: end-of-file-fixer
      - id: check-yaml
      - id: check-added-large-files

  - repo: https://github.com/Yelp/detect-secrets
    rev: v1.5.0
    hooks:
      - id: detect-secrets
```

### Comparison: Python vs TypeScript (10 Layers Each)

| Feature | Python | TypeScript |
|---------|--------|------------|
| **Formatter** | black | ESLint --fix / Prettier |
| **Linter** | flake8 | ESLint |
| **Type Checker** | mypy | tsc |
| **TIA** | pytest-picked | Jest --findRelatedTests |
| **SRP Guardrails** | check_srp_size.py | check-file-size.js |
| **Duplication** | check_duplication.py | - |
| **Mock Conformance** | check_mock_conformance.py | check-mock-tax.js |
| **Coverage Ratchet** | - | check-changed-files.mjs |
| **Buddy System** | - | verify-integration-pairing.js |
| **any Ratchet** | - | check-any-usage.js |

Both TypeScript and Python now have 10-layer configurations for parity. The patterns below are language-agnostic and can be implemented in either language.

---

## Language-Agnostic Governance Patterns

The governance patterns from the TypeScript 9-layer config are **universal algorithms** that can be implemented in any language. This section provides:
1. The **algorithm** (language-independent logic)
2. **Tool mappings** per language
3. **AI prompts** to generate the script

### Pattern 1: Mock Tax (2x Rule)

**Philosophy:** Unit tests bloated with mocks indicate tight coupling. If a test needs >2x the code to mock dependencies, write an integration test instead.

#### Universal Algorithm

```
INPUT: staged test files
FOR EACH test_file:
    source_file = map_test_to_source(test_file)
    IF source_file does not exist: SKIP

    test_lines = count_non_empty_lines(test_file)
    source_lines = count_non_empty_lines(source_file)
    has_mocks = file_contains_mock_pattern(test_file)

    IF source_lines > 15 AND has_mocks:
        ratio = test_lines / source_lines
        IF ratio > 2.0:
            REJECT with message:
                "Test is {ratio}x larger than source (limit: 2.0x)"
                "Solution: Delete unit test, write integration test"
```

#### Language Tool Mapping

| Language | Mock Detection Pattern | Test → Source Mapping | Test Framework |
|----------|----------------------|----------------------|----------------|
| **TypeScript** | `jest.mock(`, `vi.mock(` | `tests/unit/X.test.ts` → `src/X.ts` | Jest, Vitest |
| **Python** | `@patch`, `@mock.patch`, `Mock(` | `tests/test_X.py` → `src/X.py` | pytest, unittest |

#### AI Prompt to Generate Script

```
Create a pre-commit hook script in [Python/Go/Bash] that enforces the Mock Tax rule:

Requirements:
1. Get list of staged test files from git
2. For each test file, find the corresponding source file using this mapping:
   [INSERT YOUR PROJECT'S TEST-TO-SOURCE MAPPING]
3. Count non-empty lines in both files
4. Check if test file contains mock patterns: [INSERT PATTERNS FOR YOUR FRAMEWORK]
5. If source > 15 lines AND has mocks AND ratio > 2.0, reject with clear message
6. Exit 0 if all pass, exit 1 if any fail

Output should be human-readable with the file path, ratio, and recommended action.
```

---

### Pattern 2: Type Safety Ratchet

**Philosophy:** Unsafe type assertions (`any`, `Object`, `interface{}`) create blind spots. Count them, set a baseline, and never let the count increase.

#### Universal Algorithm

```
INPUT: staged source files, baseline.json
current_count = 0

FOR EACH source_file:
    content = read_file(source_file)
    content = remove_comments(content)
    content = remove_legitimate_patterns(content)  # e.g., catch (e: any)

    count = count_unsafe_type_patterns(content)
    current_count += count

baseline = load_baseline("type-safety-baseline.json")

IF current_count > baseline.threshold:
    REJECT with message:
        "Type safety violations increased!"
        "Baseline: {baseline.threshold}, Current: {current_count}"
        "Fix: Replace unsafe types with proper interfaces"
```

#### Language Tool Mapping

| Language | Unsafe Type Patterns | Legitimate Exceptions | Baseline File |
|----------|---------------------|----------------------|---------------|
| **TypeScript** | `: any`, `as any`, `<any>` | `catch (e: any)` | `any-baseline.json` |
| **Python** | `: Any`, `# type: ignore`, `cast(Any,` | Type stubs, protocols | `type-ignore-baseline.json` |

#### AI Prompt to Generate Script

```
Create a pre-commit hook script in [Python/Go/Bash] that enforces a type safety ratchet:

Requirements:
1. Load baseline count from [baseline-file.json]
2. Get list of staged source files (not test files)
3. For each file, count occurrences of these unsafe patterns:
   [INSERT PATTERNS FOR YOUR LANGUAGE]
4. Exclude these legitimate patterns from the count:
   [INSERT EXCEPTIONS]
5. If total count > baseline, reject with clear message showing delta
6. Include instructions for fixing (use proper types, create interfaces)

The baseline file format is: { "threshold": NUMBER, "updated": "ISO-DATE" }
```

---

### Pattern 3: Coverage Ratchet

**Philosophy:** New code must meet 80% coverage. Existing code cannot regress. Quality only goes up.

#### Universal Algorithm

```
INPUT: staged files, coverage-baseline.json, coverage-report

FOR EACH staged_file:
    IF is_new_file(staged_file):
        coverage = get_coverage(staged_file, coverage_report)
        IF coverage < 80:
            REJECT: "New file {file} has {coverage}% coverage (minimum: 80%)"
    ELSE:
        current_coverage = get_coverage(staged_file, coverage_report)
        baseline_coverage = baseline[staged_file] OR 0
        IF current_coverage < baseline_coverage:
            REJECT: "Coverage regression: {file} dropped from {baseline}% to {current}%"
```

#### Language Tool Mapping

| Language | Coverage Tool | Report Format | Coverage Command |
|----------|--------------|---------------|------------------|
| **TypeScript** | Jest, c8, nyc | JSON, lcov | `jest --coverage --json` |
| **Python** | coverage.py, pytest-cov | JSON, XML | `pytest --cov --cov-report=json` |

#### AI Prompt to Generate Script

```
Create a pre-commit hook script in [Python/Go/Bash] that enforces coverage ratchet:

Requirements:
1. Run tests with coverage: [INSERT YOUR COVERAGE COMMAND]
2. Parse coverage report from [INSERT REPORT PATH/FORMAT]
3. Load baseline from coverage-baseline.json
4. For each staged source file:
   - If new (not in baseline): require >= 80% coverage
   - If existing: require >= baseline coverage (no regression)
5. Reject with clear message showing file, current %, required %
6. On success, optionally update baseline with improved coverage

Baseline format: { "files": { "path/to/file.ext": 85.5 }, "updated": "ISO-DATE" }
```

---

### Pattern 4: Integration Test Pairing (Buddy System)

**Philosophy:** Every user-facing feature must have an integration test. Unit tests alone don't guarantee the feature works end-to-end.

#### Universal Algorithm

```
INPUT: staged feature files, exemptions.json

feature_paths = ["src/commands/", "src/handlers/", "src/api/"]
test_path = "tests/integration/"

FOR EACH staged_file:
    IF staged_file starts with any feature_path:
        expected_test = map_to_integration_test(staged_file)
        IF NOT exists(expected_test):
            IF NOT is_exempted(staged_file, exemptions):
                REJECT: "Missing integration test for {staged_file}"
                        "Expected: {expected_test}"
                        "Add test or add exemption with justification"
```

#### Language Tool Mapping

| Language | Feature Paths | Test Path | Mapping Pattern |
|----------|--------------|-----------|-----------------|
| **TypeScript** | `src/commands/`, `src/services/` | `tests/integration/` | `src/X.ts` → `tests/integration/X.int.test.ts` |
| **Python** | `src/handlers/`, `src/api/` | `tests/integration/` | `src/X.py` → `tests/integration/test_X_integration.py` |

#### Exemptions File Format

```json
{
  "exemptions": [
    {
      "path": "src/commands/legacyCommand.ts",
      "reason": "Legacy code, migration planned for Q2",
      "expiresAt": "2025-06-01",
      "author": "team@company.com"
    }
  ]
}
```

---

### Pattern 5: Silent Catch Detection

**Philosophy:** Empty catch blocks hide errors. Every catch must log, throw, or be explicitly marked as intentionally silent.

#### Universal Algorithm

```
INPUT: staged source files

silent_marker = "SILENT_CATCH:" or "@SuppressWarnings" or "# noqa"

FOR EACH source_file:
    catches = find_catch_blocks(source_file)
    FOR EACH catch_block:
        IF catch_block.body is empty OR only whitespace:
            IF NOT contains(catch_block, silent_marker):
                REJECT: "Silent catch at {file}:{line}"
                        "Either handle the error or mark with {silent_marker}"
```

#### Language Tool Mapping

| Language | Catch Syntax | Silent Marker | Detection Regex |
|----------|-------------|---------------|-----------------|
| **TypeScript** | `catch (e) { }` | `// SILENT_CATCH:` | `catch\s*\([^)]*\)\s*\{\s*\}` |
| **Python** | `except: pass` | `# SILENT_CATCH:` | `except.*:\s*pass` |

---

### Pattern 6: Test Impact Analysis (TIA)

**Philosophy:** Run only tests affected by your changes locally. Run all tests in CI (Safety Latch).

#### Universal Algorithm

```
IF running_in_ci AND branch == "main":
    # Safety Latch: Full suite on main
    run_all_tests()
ELSE:
    changed_files = git_diff_staged()
    source_files = filter_source_files(changed_files)
    IF source_files is empty:
        exit(0)  # No tests needed
    run_tests_for_files(source_files)
```

#### Language Tool Mapping

| Language | TIA Flag | Full Suite | Framework |
|----------|----------|------------|-----------|
| **TypeScript** | `jest --findRelatedTests src/file.ts` | `jest` | Jest |
| **Python** | `pytest --collect-only -q \| filter` | `pytest` | pytest |

---

## Governance Script Templates

### Bash Template (Universal)

Most governance checks can be implemented as bash scripts that work across languages:

```bash
#!/bin/bash
# Generic governance check template
# Usage: ./check-governance.sh [--staged]

set -e

# Configuration (customize per project)
MAX_RATIO=2.0
BASELINE_FILE=".governance-baseline.json"

# Get staged files
if [[ "$1" == "--staged" ]]; then
    FILES=$(git diff --cached --name-only --diff-filter=ACM)
else
    FILES=$(git diff --name-only HEAD)
fi

# Filter to source files (customize pattern)
SOURCE_FILES=$(echo "$FILES" | grep -E '\.(ts|py)$' | grep -v test || true)

if [[ -z "$SOURCE_FILES" ]]; then
    echo "No source files to check"
    exit 0
fi

# Run check (customize logic)
ERRORS=0
for file in $SOURCE_FILES; do
    # Your check logic here
    echo "Checking $file..."
done

if [[ $ERRORS -gt 0 ]]; then
    echo "Governance check failed with $ERRORS errors"
    exit 1
fi

echo "Governance check passed"
exit 0
```

---

*Part of Mault Pro Production-Readiness Kit*
