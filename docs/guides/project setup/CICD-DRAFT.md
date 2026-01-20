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

# CI/CD Pipeline Setup Guide

> **Step 4 of 8** in the Production-Readiness Kit
> **Applies to:** Mault Pro ($99 one-time)

---

## Overview

This guide establishes a **best-in-class CI/CD pipeline** that balances speed with safety. The patterns here are battle-tested across enterprise codebases and apply to any language or framework.

### The Problem with AI-Assisted Codebases

AI coding tools generate code fast, but without guardrails:
- Tests get skipped "to save time"
- Technical debt accumulates silently
- Regressions slip through

**Solution:** A tiered CI pipeline that's fast for developers but strict for production.

### Tiered Guarantee Model

| Tier | Trigger | What Runs | Philosophy |
|------|---------|-----------|------------|
| **Tier 1** | Local (pre-commit) | Affected tests only (TIA) | Speed |
| **Tier 2** | PR opened/updated | TIA + changed-since base | Balance |
| **Tier 3** | Push to main | Full test suite + Behavioral | Safety |

This tiered approach gives developers fast feedback while ensuring nothing reaches production without full validation.

### Behavioral Detector Tests in CI

Behavioral tests validate that detectors **perceive** the environment correctly. These run in CI (not pre-commit) because they require real test workspaces:

```yaml
# .github/workflows/ci.yml
jobs:
  behavioral-tests:
    strategy:
      matrix:
        os: [ubuntu-latest, windows-latest, macos-latest]
    runs-on: ${{ matrix.os }}
    steps:
      - uses: actions/checkout@v4
      - run: npm ci
      - run: npm run test:behavioral
```

**Why Cross-Platform?** Path separators (`\` vs `/`), case sensitivity, and line endings vary by OS. Behavioral tests catch these bugs before production.

See [TDD-GUIDE.md](./TDD-GUIDE.md#behavioral-detector-tests-inputoutput-verification) for detailed patterns.

---

## Section 1: Workflow Foundation

### Basic GitHub Actions Structure

```yaml
# .github/workflows/ci.yml
name: CI Pipeline

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

# Cancel in-progress runs when branch is updated
concurrency:
  group: ${{ github.workflow }}-${{ github.ref }}
  cancel-in-progress: true

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Setup Node
        uses: actions/setup-node@v4
        with:
          node-version: '20'
          cache: 'npm'
      - run: npm ci
      - run: npm test
```

### Path-Based Filtering

Skip CI entirely when only non-code files change:

```yaml
# .github/workflows/ci.yml
name: CI Pipeline

on:
  push:
    branches: [main]
    paths-ignore:
      - '**.md'
      - 'docs/**'
      - '.github/ISSUE_TEMPLATE/**'
  pull_request:
    branches: [main]
    paths-ignore:
      - '**.md'
      - 'docs/**'
```

For more granular control, use path detection:

```yaml
jobs:
  detect-changes:
    runs-on: ubuntu-latest
    outputs:
      src-changed: ${{ steps.filter.outputs.src }}
      tests-changed: ${{ steps.filter.outputs.tests }}
    steps:
      - uses: actions/checkout@v4
      - uses: dorny/paths-filter@v3
        id: filter
        with:
          filters: |
            src:
              - 'src/**'
            tests:
              - 'tests/**'
              - '*.config.js'

  test:
    needs: detect-changes
    if: needs.detect-changes.outputs.src-changed == 'true'
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - run: npm ci
      - run: npm test
```

### Concurrency Control

Prevent resource waste by canceling outdated runs:

```yaml
concurrency:
  # Group by workflow + branch (PRs) or workflow alone (main)
  group: ${{ github.workflow }}-${{ github.head_ref || github.ref }}
  cancel-in-progress: true
```

**Why this matters:** When a developer pushes 3 commits quickly, only the last one needs to run. Without this, you're paying for 3 redundant CI runs.

---

## Section 2: Test Execution Strategy

### Test Impact Analysis (TIA)

TIA runs only the tests affected by your changes. This is the single biggest CI optimization.

#### 3-Tier TIA Model

```
Local (Tier 1):    npm test -- --findRelatedTests src/changed-file.ts
PR (Tier 2):       npm test -- --changedSince=origin/main
Main (Tier 3):     npm test                    # Full suite (Safety Latch)
```

#### Implementation

**Local (pre-commit):**
```bash
#!/bin/bash
# scripts/test-impact-analysis.sh

# Get changed source files
CHANGED=$(git diff --name-only HEAD | grep -E '^src/.*\.ts$' | grep -v '\.test\.ts$')

if [ -z "$CHANGED" ]; then
  echo "No source files changed, skipping tests"
  exit 0
fi

# Run only affected tests
npx jest --findRelatedTests $CHANGED --passWithNoTests
```

**CI Workflow:**
```yaml
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
        with:
          fetch-depth: 0  # Required for --changedSince

      - name: Install dependencies
        run: npm ci

      - name: Run tests (TIA for PRs, full for main)
        run: |
          if [ "${{ github.event_name }}" == "pull_request" ]; then
            # Tier 2: TIA with changed-since
            BASE_REF="${{ github.base_ref }}"
            npm test -- --changedSince=origin/${BASE_REF}
          else
            # Tier 3: Safety Latch - full suite on main
            npm test
          fi
```

#### The Safety Latch

**Critical:** Always run the full test suite on pushes to main. TIA can miss transitive dependency changes.

**Why This Matters (AI Hallucination Counter-Measure):**

TIA is brilliant for speed, but it has a blind spot: **AI coding assistants can hallucinate passing TIA runs.**

When an AI modifies `utils.ts` and its test file, TIA says "all affected tests pass." But the AI might have:
- Broken a downstream consumer that imports `utils.ts`
- Introduced a subtle type change that compiles but fails at runtime
- Created a test that passes but doesn't actually test the code

The Safety Latch catches these failures by running ALL tests on main — regardless of what TIA reported on the PR. If TIA missed something, the Safety Latch catches it before it becomes a production incident.

```
┌─────────────────────────────────────────────────────────────────────┐
│                    TIA + SAFETY LATCH PATTERN                        │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│   PR: TIA reports "3/3 tests pass"                                  │
│        ↓                                                            │
│   Merge to main: Safety Latch runs ALL 500 tests                    │
│        ↓                                                            │
│   Result: Catch the 1 test TIA missed (downstream consumer)         │
│                                                                     │
│   Without Safety Latch: Bug ships to production                     │
│   With Safety Latch: Bug caught before release                      │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

```javascript
// scripts/governance/test-impact-analysis.js
const IS_CI = process.env.CI === 'true';
const IS_MAIN = process.env.GITHUB_REF === 'refs/heads/main';

if (IS_CI && IS_MAIN) {
  // SAFETY LATCH: Counter-measure for AI hallucinations and TIA blind spots
  console.log('Safety Latch engaged: Running ALL tests');
  runAllTests();
} else {
  console.log('TIA Mode: Running affected tests only');
  runTiaTests(changedFiles);
}
```

### Language-Specific TIA

| Language | Local TIA | PR TIA | Full Suite |
|----------|-----------|--------|------------|
| **Jest (TS/JS)** | `--findRelatedTests` | `--changedSince=origin/main` | `jest` |
| **pytest (Python)** | `pytest-picked` | `pytest --co -q \| filter` | `pytest` |

**Python Example:**
```yaml
- name: Run tests (TIA for PRs)
  run: |
    if [ "${{ github.event_name }}" == "pull_request" ]; then
      # Get changed Python files
      CHANGED=$(git diff --name-only origin/${{ github.base_ref }}...HEAD | grep '\.py$' || true)
      if [ -n "$CHANGED" ]; then
        python -m pytest $CHANGED --ignore=tests/
        python -m pytest tests/ -k "$(echo $CHANGED | xargs -n1 basename | sed 's/.py//' | tr '\n' ' or ')"
      fi
    else
      python -m pytest
    fi
```

### Matrix Sharding (Parallel Execution)

Split your test suite across multiple runners:

```yaml
jobs:
  test:
    runs-on: ubuntu-latest
    strategy:
      fail-fast: false  # Don't cancel siblings on first failure
      matrix:
        shard: [1/4, 2/4, 3/4, 4/4]
    steps:
      - uses: actions/checkout@v4
      - run: npm ci
      - name: Run tests (shard ${{ matrix.shard }})
        run: npm test -- --shard=${{ matrix.shard }}

  # Aggregator job - provides single status check
  test-results:
    needs: test
    runs-on: ubuntu-latest
    if: always()
    steps:
      - name: Check test results
        run: |
          if [ "${{ needs.test.result }}" != "success" ]; then
            echo "Tests failed"
            exit 1
          fi
          echo "All test shards passed"
```

#### Why the Aggregator Pattern?

Without it, you get 4 separate status checks. With it, you get one "Tests" check that passes only when all shards pass. This simplifies branch protection rules.

#### Sharding by Language

| Language | Sharding Flag | Notes |
|----------|---------------|-------|
| **Jest** | `--shard=1/4` | Built-in since Jest 28 |
| **pytest** | `pytest-split` | `pip install pytest-split` |

**pytest Example:**
```yaml
strategy:
  matrix:
    shard: [1, 2, 3, 4]
steps:
  - run: pip install pytest-split
  - run: pytest --splits 4 --group ${{ matrix.shard }}
```

### Combining TIA + Sharding

The most efficient configuration uses both:

```yaml
jobs:
  test:
    strategy:
      matrix:
        shard: [1/4, 2/4, 3/4, 4/4]
    steps:
      - uses: actions/checkout@v4
        with:
          fetch-depth: 0

      - name: Run tests
        run: |
          if [ "${{ github.event_name }}" == "pull_request" ]; then
            # TIA + Sharding
            npm test -- --changedSince=origin/${{ github.base_ref }} --shard=${{ matrix.shard }}
          else
            # Full suite + Sharding (Safety Latch)
            npm test -- --shard=${{ matrix.shard }}
          fi
```

---

## Section 3: Changed-Files-Only Pattern (Rising Tide)

For governance checks, only validate files that changed. This prevents legacy tech debt from blocking every PR.

### The Philosophy

**Rising Tide:** New code must meet current standards. Old code gets grandfathered until touched.

### Implementation

```yaml
jobs:
  governance:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
        with:
          fetch-depth: 0

      - name: Get changed files
        id: changed
        run: |
          if [ "${{ github.event_name }}" == "pull_request" ]; then
            FILES=$(git diff --name-only origin/${{ github.base_ref }}...HEAD)
          else
            FILES=$(git diff --name-only HEAD~1)
          fi
          echo "files<<EOF" >> $GITHUB_OUTPUT
          echo "$FILES" >> $GITHUB_OUTPUT
          echo "EOF" >> $GITHUB_OUTPUT

      - name: Run governance checks
        env:
          ONLY_CHANGED: 'true'
          CHANGED_FILE_LIST: ${{ steps.changed.outputs.files }}
        run: node scripts/ci/code-health-check.js
```

### Governance Script Pattern

```javascript
// scripts/ci/governance-check.js
const onlyChanged = process.env.ONLY_CHANGED === 'true';
const changedFiles = (process.env.CHANGED_FILE_LIST || '')
  .split('\n')
  .filter(Boolean);

function shouldCheck(file) {
  if (!onlyChanged) return true;  // Full scan mode
  return changedFiles.includes(file);
}

// Check each file
allFiles.forEach(file => {
  if (!shouldCheck(file)) return;  // Skip unchanged files

  const violations = checkFile(file);
  if (violations.length > 0) {
    failures.push({ file, violations });
  }
});
```

### What to Gate with Rising Tide

| Check | Rising Tide? | Reason |
|-------|--------------|--------|
| Type safety (`any` count) | Yes | Legacy code may have `any` |
| Test-to-code ratio | Yes | Legacy tests may be oversized |
| Code duplication | Yes | Can't fix all dupes at once |
| Orphaned files | **No** | Zero-tolerance (delete them) |
| Secrets in code | **No** | Zero-tolerance (immediate fix) |

---

## Section 4: Governance in CI

### Pre-commit Hooks in CI

Run the same hooks CI that developers run locally:

```yaml
jobs:
  lint:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: '3.11'
      - run: pip install pre-commit
      - run: pre-commit run --all-files
```

### Code Health Checks

Run governance scripts that enforce architectural standards:

```yaml
jobs:
  code-health:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
        with:
          fetch-depth: 0

      - name: Get changed files
        id: changed
        run: |
          FILES=$(git diff --name-only origin/${{ github.base_ref }}...HEAD)
          echo "files<<EOF" >> $GITHUB_OUTPUT
          echo "$FILES" >> $GITHUB_OUTPUT
          echo "EOF" >> $GITHUB_OUTPUT

      - name: Install dependencies
        run: npm ci

      - name: Code Health Check
        env:
          ONLY_CHANGED: 'true'
          CHANGED_FILE_LIST: ${{ steps.changed.outputs.files }}
        run: node scripts/ci/code-health-check.js

      - name: Guardrails Check
        run: node scripts/ci/guardrails-check.js

      - name: Dead-ends Check
        run: node scripts/ci/deadends-cli-runner.js
```

### Guardrails Examples

**SRP (Single Responsibility):**
```javascript
// Block files over 300 lines
const MAX_LINES = 300;
const lines = content.split('\n').length;
if (lines > MAX_LINES) {
  violations.push(`File exceeds ${MAX_LINES} lines (${lines})`);
}
```

**Type Safety (any Ratchet):**
```javascript
// Block new `any` usage
const anyCount = countAnyUsage(content);
if (anyCount > baseline[file]) {
  violations.push(`any count increased: ${baseline[file]} → ${anyCount}`);
}
```

---

## Section 5: Exemptions Pattern

Sometimes you need to temporarily bypass a check. Use exemptions with expiry dates.

### Exemption File Schema

```json
// .governance-exemptions.json
[
  {
    "path": "src/legacy/OldModule.ts",
    "rule": "srp-line-limit",
    "justification": "Legacy migration in progress - Issue #1234",
    "expiresAt": "2025-03-01",
    "author": "team@company.com"
  },
  {
    "path": "src/utils/helpers.ts",
    "rule": "any-usage",
    "justification": "Third-party type definitions incomplete",
    "expiresAt": "2025-02-15",
    "author": "dev@company.com"
  }
]
```

### Checking Exemptions

```javascript
// scripts/ci/check-exemptions.js
const exemptions = JSON.parse(fs.readFileSync('.governance-exemptions.json'));
const now = new Date();

// Check for expired exemptions
const expired = exemptions.filter(e => new Date(e.expiresAt) < now);
if (expired.length > 0) {
  console.error('Expired exemptions found:');
  expired.forEach(e => {
    console.error(`  - ${e.path} (${e.rule}) expired ${e.expiresAt}`);
  });
  process.exit(1);
}

// Check if file is exempted
function isExempted(file, rule) {
  return exemptions.some(e =>
    e.path === file &&
    e.rule === rule &&
    new Date(e.expiresAt) >= now
  );
}
```

### CI Integration

```yaml
- name: Check exemptions
  run: node scripts/ci/check-exemptions.js

- name: Run checks with exemptions
  env:
    EXEMPTIONS_FILE: .governance-exemptions.json
  run: node scripts/ci/guardrails-check.js
```

---

## Section 6: Multi-Language Examples

### Complete Node.js/TypeScript Workflow

```yaml
# .github/workflows/ci.yml
name: CI

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

concurrency:
  group: ${{ github.workflow }}-${{ github.head_ref || github.ref }}
  cancel-in-progress: true

jobs:
  lint:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: '20'
          cache: 'npm'
      - run: npm ci
      - run: npm run lint

  test:
    runs-on: ubuntu-latest
    strategy:
      fail-fast: false
      matrix:
        shard: [1/4, 2/4, 3/4, 4/4]
    steps:
      - uses: actions/checkout@v4
        with:
          fetch-depth: 0
      - uses: actions/setup-node@v4
        with:
          node-version: '20'
          cache: 'npm'
      - run: npm ci
      - name: Run tests
        run: |
          if [ "${{ github.event_name }}" == "pull_request" ]; then
            npm test -- --changedSince=origin/${{ github.base_ref }} --shard=${{ matrix.shard }}
          else
            npm test -- --shard=${{ matrix.shard }}
          fi

  test-results:
    needs: test
    runs-on: ubuntu-latest
    if: always()
    steps:
      - run: |
          if [ "${{ needs.test.result }}" != "success" ]; then
            exit 1
          fi

  governance:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
        with:
          fetch-depth: 0
      - uses: actions/setup-node@v4
        with:
          node-version: '20'
          cache: 'npm'
      - run: npm ci
      - name: Get changed files
        id: changed
        run: |
          FILES=$(git diff --name-only origin/${{ github.base_ref || 'main' }}...HEAD || echo "")
          echo "files<<EOF" >> $GITHUB_OUTPUT
          echo "$FILES" >> $GITHUB_OUTPUT
          echo "EOF" >> $GITHUB_OUTPUT
      - name: Code health
        env:
          ONLY_CHANGED: ${{ github.event_name == 'pull_request' }}
          CHANGED_FILE_LIST: ${{ steps.changed.outputs.files }}
        run: node scripts/ci/code-health-check.js
```

### Complete Python Workflow

```yaml
# .github/workflows/ci.yml
name: CI

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

concurrency:
  group: ${{ github.workflow }}-${{ github.head_ref || github.ref }}
  cancel-in-progress: true

jobs:
  lint:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: '3.11'
      - run: pip install ruff mypy
      - run: ruff check .
      - run: mypy src/

  test:
    runs-on: ubuntu-latest
    strategy:
      fail-fast: false
      matrix:
        shard: [1, 2, 3, 4]
    steps:
      - uses: actions/checkout@v4
        with:
          fetch-depth: 0
      - uses: actions/setup-python@v5
        with:
          python-version: '3.11'
      - run: pip install pytest pytest-split pytest-cov
      - name: Run tests
        run: |
          if [ "${{ github.event_name }}" == "pull_request" ]; then
            # TIA: Run tests for changed files
            CHANGED=$(git diff --name-only origin/${{ github.base_ref }}...HEAD | grep '\.py$' || true)
            if [ -n "$CHANGED" ]; then
              pytest --splits 4 --group ${{ matrix.shard }} tests/
            fi
          else
            pytest --splits 4 --group ${{ matrix.shard }} tests/
          fi

  test-results:
    needs: test
    runs-on: ubuntu-latest
    if: always()
    steps:
      - run: |
          if [ "${{ needs.test.result }}" != "success" ]; then
            exit 1
          fi
```

---

## Section 7: Mault Enforcement in CI

### Running Mault Pre-commit in CI

Mault's detectors run as a pre-commit hook. Include this in CI:

```yaml
jobs:
  mault:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Run Mault pre-commit
        run: mault pre-commit
```

### License Validation

Mault Pro requires a valid license. CI should validate:

```yaml
- name: Validate Mault license
  env:
    MAULT_LICENSE_KEY: ${{ secrets.MAULT_LICENSE_KEY }}
  run: |
    if [ -z "$MAULT_LICENSE_KEY" ]; then
      echo "Warning: MAULT_LICENSE_KEY not set"
      echo "Mault enforcement will be skipped"
    else
      mault pre-commit
    fi
```

### Failure Modes

| Scenario | Behavior |
|----------|----------|
| No license key | Warning, skip Mault checks |
| Invalid license | Error, fail CI |
| Mault violation | Error, fail CI with fix instructions |
| Mault not installed | Error, provide install instructions |

---

## Troubleshooting

### CI is Too Slow

**Symptoms:** PR checks take >10 minutes

**Solutions:**
1. Enable TIA (`--changedSince` for PRs)
2. Add matrix sharding (4-way parallel)
3. Use path-based filtering to skip irrelevant runs
4. Enable dependency caching (`cache: 'npm'`)
5. Review if full test suite is running on PRs (should be TIA)

### Tests Pass Locally, Fail in CI

**Symptoms:** `npm test` passes locally but fails in GitHub Actions

**Causes & Fixes:**
1. **Missing fetch depth:** Add `fetch-depth: 0` for TIA
2. **Different Node version:** Match CI version to local
3. **Test order dependency:** Run with `--randomize` locally
4. **Missing environment variables:** Check `env:` in workflow

### Governance Check Keeps Failing

**Symptoms:** Code health or guardrails check fails on every PR

**Solutions:**
1. Check if `ONLY_CHANGED=true` is set (Rising Tide mode)
2. Verify changed files are being passed correctly
3. Check for expired exemptions
4. Run the script locally to see full error output:
   ```bash
   ONLY_CHANGED=true CHANGED_FILE_LIST="src/file.ts" node scripts/ci/code-health-check.js
   ```

### Sharding Produces Different Results

**Symptoms:** Some shards pass, others fail inconsistently

**Causes & Fixes:**
1. **Shared state between tests:** Ensure test isolation
2. **Race conditions:** Use `--runInBand` to debug
3. **Flaky tests:** Add retry logic or fix the test

---

## AI Prompts

### Setup CI Pipeline
```
Help me set up a GitHub Actions CI pipeline for my [Node.js/Python] project.

Requirements:
- Run tests on PR and push to main
- Use TIA (Test Impact Analysis) for PRs
- Full test suite on main (Safety Latch)
- Cancel in-progress runs on new pushes
- Cache dependencies

My test command is: [npm test / pytest]
```

### Add Matrix Sharding
```
Help me add matrix sharding to my GitHub Actions workflow to run tests in parallel.

Current workflow file: [paste workflow]

Requirements:
- Split tests across 4 runners
- Add aggregator job for single status check
- Combine with existing TIA logic
```

### Debug CI Failure
```
My CI is failing with this error: [paste error]

Workflow file: [paste workflow]
Local test output: [paste local result]

The tests pass locally but fail in CI. Help me identify the cause.
```

### Add Governance Checks
```
Help me add governance checks to my CI pipeline.

Checks I want:
- [ ] File length limit (300 lines)
- [ ] Type safety (no new `any` usage)
- [ ] Code duplication detection
- [ ] Orphaned file detection

I want Rising Tide mode (only check changed files on PRs).
```

---

## Verification Checklist

Before merging your CI setup:

- [ ] CI runs on both PR and push to main
- [ ] TIA enabled for PRs (`--changedSince` or equivalent)
- [ ] Full suite runs on main (Safety Latch)
- [ ] Concurrency control enabled (`cancel-in-progress`)
- [ ] Path filtering skips docs-only changes
- [ ] Dependency caching enabled
- [ ] Tests pass both locally and in CI
- [ ] Governance checks use Rising Tide mode
- [ ] Branch protection requires CI pass
- [ ] Secrets are in GitHub Secrets, not code

---

*Part of Mault Pro Production-Readiness Kit*
