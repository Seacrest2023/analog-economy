# CI/CD Pipeline Guide - The Analog Economy

> **Version:** 1.0
> **Last Updated:** 2026-01-20
> **Status:** Approved

---

## Overview

This guide establishes the CI/CD pipeline for The Analog Economy. Our architecture has two distinct components with different build characteristics:

| Component | Codename | Language | Build Time | Pipeline Type |
|-----------|----------|----------|------------|---------------|
| **Core Governance** | The Brain | Python 3.11+ | Fast (~2 min) | Rapid feedback |
| **Client Simulation** | The Body | C++ (UE5) | Slow (~30+ min) | Batched builds |

This dual nature requires a **tiered CI strategy** that provides fast feedback for The Brain while managing expensive UE5 builds efficiently.

---

## Tiered Guarantee Model

```
+------------------------------------------------------------------+
|                         TIER 3: MAIN                              |
|        Full Test Suite + UE5 Build + Behavioral Tests             |
|                    (Safety Latch - Nightly)                       |
+---------------------------------+--------------------------------+
                                  |
+---------------------------------+--------------------------------+
|                         TIER 2: PULL REQUEST                      |
|            TIA + Changed Tests + Pre-commit Hooks                 |
|                    (Balance - Every PR)                           |
+---------------------------------+--------------------------------+
                                  |
+---------------------------------+--------------------------------+
|                         TIER 1: LOCAL                             |
|        Pre-commit Hooks + Affected Tests Only (TIA)               |
|                    (Speed - Every Commit)                         |
+------------------------------------------------------------------+
```

### Tier Philosophy

| Tier | Trigger | What Runs | Goal |
|------|---------|-----------|------|
| **Tier 1** | Local pre-commit | Affected tests, linting, type check | Developer speed |
| **Tier 2** | PR opened/updated | TIA + governance checks | PR confidence |
| **Tier 3** | Push to master | Full suite + UE5 + E2E | Production safety |

---

## The Brain Pipeline (Python/FastAPI)

### Workflow File

```yaml
# .github/workflows/brain-ci.yml
name: Brain CI (Python)

on:
  push:
    branches: [master]
    paths:
      - 'core-governance/**'
      - 'shared/**'
      - 'pyproject.toml'
      - '.pre-commit-config.yaml'
  pull_request:
    branches: [master]
    paths:
      - 'core-governance/**'
      - 'shared/**'
      - 'pyproject.toml'

# Cancel in-progress runs when branch is updated
concurrency:
  group: brain-${{ github.workflow }}-${{ github.head_ref || github.ref }}
  cancel-in-progress: true

jobs:
  # =========================================================================
  # STAGE 1: Fast Checks (Parallel)
  # =========================================================================
  lint:
    name: Lint & Format
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.11'
          cache: 'pip'

      - name: Install dependencies
        run: |
          pip install ruff black isort mypy

      - name: Check formatting (Black)
        run: black --check core-governance/

      - name: Check imports (isort)
        run: isort --check-only core-governance/

      - name: Lint (Ruff)
        run: ruff check core-governance/

  type-check:
    name: Type Check (mypy)
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.11'
          cache: 'pip'

      - name: Install dependencies
        run: |
          pip install -r core-governance/requirements.txt
          pip install mypy pydantic

      - name: Run mypy
        run: mypy core-governance/gaian/ core-governance/app/

  pre-commit:
    name: Pre-commit Hooks
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.11'
          cache: 'pip'

      - name: Install pre-commit
        run: pip install pre-commit

      - name: Run pre-commit
        run: pre-commit run --all-files

  # =========================================================================
  # STAGE 2: Tests (Parallel Shards)
  # =========================================================================
  test:
    name: Tests (Shard ${{ matrix.shard }})
    runs-on: ubuntu-latest
    needs: [lint, type-check]  # Wait for fast checks
    strategy:
      fail-fast: false
      matrix:
        shard: [1, 2, 3, 4]

    services:
      postgres:
        image: postgres:15
        env:
          POSTGRES_USER: test
          POSTGRES_PASSWORD: test
          POSTGRES_DB: analog_test
        options: >-
          --health-cmd pg_isready
          --health-interval 10s
          --health-timeout 5s
          --health-retries 5
        ports:
          - 5432:5432

      redis:
        image: redis:7
        options: >-
          --health-cmd "redis-cli ping"
          --health-interval 10s
          --health-timeout 5s
          --health-retries 5
        ports:
          - 6379:6379

    steps:
      - uses: actions/checkout@v4
        with:
          fetch-depth: 0  # Required for TIA

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.11'
          cache: 'pip'

      - name: Install dependencies
        run: |
          pip install -r core-governance/requirements.txt
          pip install pytest pytest-cov pytest-split pytest-xdist

      - name: Run tests (TIA for PRs, full for master)
        env:
          DATABASE_URL: postgresql://test:test@localhost:5432/analog_test  # pragma: allowlist secret
          REDIS_URL: redis://localhost:6379
        run: |
          cd core-governance
          if [ "${{ github.event_name }}" == "pull_request" ]; then
            # Tier 2: TIA with sharding
            echo "Running TIA tests (shard ${{ matrix.shard }}/4)"
            pytest tests/ --splits 4 --group ${{ matrix.shard }} \
              --cov=gaian --cov-report=xml
          else
            # Tier 3: Safety Latch - full suite
            echo "Running full test suite (shard ${{ matrix.shard }}/4)"
            pytest tests/ --splits 4 --group ${{ matrix.shard }} \
              --cov=gaian --cov-report=xml
          fi

      - name: Upload coverage
        uses: codecov/codecov-action@v4
        with:
          files: core-governance/coverage.xml
          flags: brain-shard-${{ matrix.shard }}

  # =========================================================================
  # STAGE 3: Aggregator (Single Status Check)
  # =========================================================================
  test-results:
    name: Test Results
    needs: [test]
    runs-on: ubuntu-latest
    if: always()
    steps:
      - name: Check test results
        run: |
          if [ "${{ needs.test.result }}" != "success" ]; then
            echo "Tests failed in one or more shards"
            exit 1
          fi
          echo "All test shards passed"

  # =========================================================================
  # STAGE 4: Governance Checks (Rising Tide)
  # =========================================================================
  governance:
    name: Governance Checks
    runs-on: ubuntu-latest
    needs: [lint, type-check]
    steps:
      - uses: actions/checkout@v4
        with:
          fetch-depth: 0

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.11'

      - name: Get changed files
        id: changed
        run: |
          if [ "${{ github.event_name }}" == "pull_request" ]; then
            FILES=$(git diff --name-only origin/${{ github.base_ref }}...HEAD | grep '\.py$' || true)
          else
            FILES=$(git diff --name-only HEAD~1 | grep '\.py$' || true)
          fi
          echo "files<<EOF" >> $GITHUB_OUTPUT
          echo "$FILES" >> $GITHUB_OUTPUT
          echo "EOF" >> $GITHUB_OUTPUT

      - name: Iron Dome (Type Safety)
        env:
          ONLY_CHANGED: ${{ github.event_name == 'pull_request' }}
          CHANGED_FILES: ${{ steps.changed.outputs.files }}
        run: python scripts/governance/python/check_iron_dome.py $CHANGED_FILES

      - name: SRP Guardrails
        run: python scripts/governance/python/check_srp_size.py core-governance/

      - name: Mock Tax
        if: github.event_name == 'pull_request'
        run: python scripts/governance/python/check_mock_tax.py core-governance/
```

### Test Impact Analysis (TIA)

TIA runs only tests affected by your changes, dramatically speeding up PR feedback.

```bash
# Local TIA (pre-commit)
pytest --collect-only -q | head -20  # See what would run

# PR TIA (GitHub Actions)
pytest tests/ --splits 4 --group 1  # Shard 1 of 4
```

**The Safety Latch:** On push to master, run the FULL test suite regardless of changes. This catches transitive dependency bugs that TIA might miss.

---

## The Body Pipeline (UE5/C++)

UE5 builds are expensive. We batch them and run on self-hosted runners or cloud build services.

### Workflow File

```yaml
# .github/workflows/body-ci.yml
name: Body CI (UE5)

on:
  push:
    branches: [master]
    paths:
      - 'client-simulation/**'
  pull_request:
    branches: [master]
    paths:
      - 'client-simulation/**'
  # Nightly full build
  schedule:
    - cron: '0 4 * * *'  # 4 AM UTC daily

# Only one UE5 build at a time (expensive)
concurrency:
  group: body-build
  cancel-in-progress: false  # Don't cancel in-progress builds

jobs:
  # =========================================================================
  # STAGE 1: Fast C++ Checks
  # =========================================================================
  cpp-lint:
    name: C++ Lint
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Install clang-format
        run: sudo apt-get install -y clang-format-15

      - name: Check formatting
        run: |
          find client-simulation/Source -name '*.cpp' -o -name '*.h' | \
            xargs clang-format-15 --dry-run --Werror

  # =========================================================================
  # STAGE 2: UE5 Build (Self-Hosted or Cloud)
  # =========================================================================
  ue5-build:
    name: UE5 Build
    needs: [cpp-lint]
    runs-on: [self-hosted, ue5-builder]  # Self-hosted with UE5 installed
    # Or use cloud build service
    # runs-on: ubuntu-latest
    # container: ghcr.io/epicgames/unreal-engine:5.3

    steps:
      - uses: actions/checkout@v4
        with:
          lfs: true  # Large files for assets

      - name: Build Development Editor
        run: |
          cd client-simulation
          "$UE5_ROOT/Engine/Build/BatchFiles/RunUAT.sh" BuildCookRun \
            -project="$PWD/AnalogEconomy.uproject" \
            -noP4 \
            -platform=Linux \
            -clientconfig=Development \
            -cook -build -stage \
            -pak -archive \
            -archivedirectory="$PWD/Build"

      - name: Upload Build Artifacts
        uses: actions/upload-artifact@v4
        with:
          name: ue5-build-${{ github.sha }}
          path: client-simulation/Build/
          retention-days: 7

  # =========================================================================
  # STAGE 3: UE5 Automation Tests
  # =========================================================================
  ue5-tests:
    name: UE5 Automation Tests
    needs: [ue5-build]
    runs-on: [self-hosted, ue5-builder]

    steps:
      - uses: actions/checkout@v4

      - name: Download Build
        uses: actions/download-artifact@v4
        with:
          name: ue5-build-${{ github.sha }}
          path: client-simulation/Build/

      - name: Run Automation Tests
        run: |
          cd client-simulation
          "$UE5_ROOT/Engine/Binaries/Linux/UnrealEditor-Cmd" \
            "$PWD/AnalogEconomy.uproject" \
            -ExecCmds="Automation RunTests AnalogEconomy" \
            -unattended \
            -nopause \
            -NullRHI \
            -log

      - name: Upload Test Results
        if: always()
        uses: actions/upload-artifact@v4
        with:
          name: ue5-test-results
          path: client-simulation/Saved/Logs/
```

### Build Optimization Strategies

| Strategy | Description | Savings |
|----------|-------------|---------|
| **Path filtering** | Only build when `client-simulation/` changes | Skip 90% of commits |
| **Nightly builds** | Full build once per day, not every PR | Major cost savings |
| **Incremental builds** | Cache intermediate objects | 50-70% faster |
| **Split editor/game** | Build editor separately from packaged game | Faster iteration |

---

## Combined Pipeline (Full Stack)

For releases and master branch, run both pipelines:

```yaml
# .github/workflows/full-ci.yml
name: Full Stack CI

on:
  push:
    branches: [master]
  release:
    types: [published]

jobs:
  brain:
    uses: ./.github/workflows/brain-ci.yml

  body:
    uses: ./.github/workflows/body-ci.yml

  # E2E tests require both Brain and Body
  e2e:
    name: E2E Tests
    needs: [brain, body]
    runs-on: [self-hosted, e2e-runner]
    steps:
      - uses: actions/checkout@v4

      - name: Download Brain artifacts
        uses: actions/download-artifact@v4
        with:
          name: brain-build

      - name: Download Body artifacts
        uses: actions/download-artifact@v4
        with:
          name: ue5-build-${{ github.sha }}

      - name: Start services
        run: docker-compose -f ops-infra/docker/docker-compose.e2e.yml up -d

      - name: Run E2E tests
        run: |
          cd tests/e2e
          pytest test_player_session_flow.py --timeout=300

      - name: Cleanup
        if: always()
        run: docker-compose -f ops-infra/docker/docker-compose.e2e.yml down
```

---

## Rising Tide: Changed-Files-Only Governance

For governance checks, only validate files that changed. This prevents legacy technical debt from blocking every PR.

### Philosophy

**Rising Tide:** New code must meet current standards. Old code gets grandfathered until touched.

### Implementation

```yaml
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
  run: python scripts/governance/python/check_iron_dome.py
```

### What to Gate with Rising Tide

| Check | Rising Tide? | Reason |
|-------|--------------|--------|
| Type safety (`Any` count) | Yes | Legacy code may have `Any` |
| Test-to-code ratio | Yes | Legacy tests may be oversized |
| File size (SRP) | Yes | Can't refactor everything at once |
| Secrets in code | **No** | Zero-tolerance (immediate fix) |
| Security vulnerabilities | **No** | Zero-tolerance |

---

## Pre-commit in CI

Run the same hooks in CI that developers run locally:

```yaml
pre-commit:
  name: Pre-commit Hooks
  runs-on: ubuntu-latest
  steps:
    - uses: actions/checkout@v4

    - name: Set up Python
      uses: actions/setup-python@v5
      with:
        python-version: '3.11'

    - name: Set up Node.js
      uses: actions/setup-node@v4
      with:
        node-version: '20'

    - name: Install pre-commit
      run: pip install pre-commit

    - name: Run pre-commit on all files
      run: pre-commit run --all-files
```

---

## Exemptions Pattern

Sometimes you need to temporarily bypass a check. Use exemptions with expiry dates.

### Exemption File Schema

```json
// .governance/exemptions.json
[
  {
    "path": "core-governance/gaian/legacy_module.py",
    "rule": "srp-line-limit",
    "justification": "Legacy migration in progress - Issue #1234",
    "expiresAt": "2026-03-01",
    "author": "team@analogeconomy.dev"
  }
]
```

### Checking Exemptions in CI

```yaml
- name: Check exemption expiry
  run: |
    python -c "
    import json
    from datetime import datetime

    with open('.governance/exemptions.json') as f:
        exemptions = json.load(f)

    now = datetime.now()
    expired = [e for e in exemptions if datetime.fromisoformat(e['expiresAt']) < now]

    if expired:
        print('Expired exemptions found:')
        for e in expired:
            print(f\"  - {e['path']} ({e['rule']}) expired {e['expiresAt']}\")
        exit(1)
    "
```

---

## Caching Strategy

### Python Dependencies

```yaml
- name: Set up Python
  uses: actions/setup-python@v5
  with:
    python-version: '3.11'
    cache: 'pip'
    cache-dependency-path: |
      core-governance/requirements.txt
      core-governance/requirements-dev.txt
```

### UE5 Build Cache

```yaml
- name: Cache UE5 DDC
  uses: actions/cache@v4
  with:
    path: |
      ~/.cache/UnrealEngine/DerivedDataCache
      client-simulation/Intermediate
    key: ue5-ddc-${{ hashFiles('client-simulation/Source/**/*.cpp') }}
    restore-keys: |
      ue5-ddc-
```

### Pre-commit Cache

```yaml
- name: Cache pre-commit
  uses: actions/cache@v4
  with:
    path: ~/.cache/pre-commit
    key: pre-commit-${{ hashFiles('.pre-commit-config.yaml') }}
```

---

## Branch Protection Rules

Configure GitHub branch protection for `master`:

| Rule | Setting | Reason |
|------|---------|--------|
| Require PR reviews | 1 approval | Code review |
| Require status checks | brain-ci, pre-commit | Tests must pass |
| Require up-to-date branch | Yes | No stale merges |
| Require linear history | Yes | Clean git history |
| Include administrators | Yes | No bypassing |

```bash
# Configure via GitHub CLI
gh api repos/:owner/:repo/branches/master/protection -X PUT \
  -f required_status_checks='{"strict":true,"contexts":["Test Results","Pre-commit Hooks"]}' \
  -f required_pull_request_reviews='{"required_approving_review_count":1}' \
  -F enforce_admins=true
```

---

## Secrets Management

### Required Secrets

| Secret | Purpose | Where to Set |
|--------|---------|--------------|
| `CODECOV_TOKEN` | Coverage reporting | Repository settings |
| `DOCKER_USERNAME` | Container registry | Repository settings |
| `DOCKER_PASSWORD` | Container registry | Repository settings |
| `AWS_ACCESS_KEY_ID` | Infrastructure deployment | Environment secrets |
| `AWS_SECRET_ACCESS_KEY` | Infrastructure deployment | Environment secrets |

### Usage

```yaml
- name: Login to Docker Hub
  uses: docker/login-action@v3
  with:
    username: ${{ secrets.DOCKER_USERNAME }}
    password: ${{ secrets.DOCKER_PASSWORD }}
```

**NEVER** hardcode secrets in workflow files. The `detect-secrets` pre-commit hook will catch this.

---

## Troubleshooting

### CI is Too Slow

**Symptoms:** PR checks take >10 minutes for The Brain

**Solutions:**
1. Enable TIA (`pytest-split` for PRs)
2. Add matrix sharding (4-way parallel)
3. Use path-based filtering to skip irrelevant runs
4. Enable dependency caching
5. Review if full test suite is running on PRs (should be TIA)

### Tests Pass Locally, Fail in CI

**Symptoms:** `pytest` passes locally but fails in GitHub Actions

**Causes & Fixes:**
1. **Missing fetch depth:** Add `fetch-depth: 0` for TIA
2. **Different Python version:** Match CI version (3.11) to local
3. **Missing services:** Ensure Postgres/Redis are available in CI
4. **Environment variables:** Check `env:` in workflow

### UE5 Build Fails

**Symptoms:** C++ compilation errors in CI

**Causes & Fixes:**
1. **Different UE5 version:** Pin exact version in both environments
2. **Missing LFS files:** Ensure `lfs: true` in checkout
3. **Plugin dependencies:** Verify all plugins are committed
4. **Platform differences:** Windows vs Linux build settings

---

## Verification Checklist

Before considering CI/CD setup complete:

- [ ] Brain CI runs on both PR and push to master
- [ ] TIA enabled for PRs (pytest-split)
- [ ] Full suite runs on main (Safety Latch)
- [ ] Concurrency control enabled
- [ ] Path filtering skips docs-only changes
- [ ] Dependency caching enabled
- [ ] Pre-commit hooks run in CI
- [ ] Governance checks use Rising Tide mode
- [ ] Branch protection requires CI pass
- [ ] Secrets are in GitHub Secrets, not code
- [ ] UE5 builds are batched (nightly or on-demand)
- [ ] E2E tests run on master merges

---

## Related Documentation

- [TDD Guide](./TDD-GUIDE.md) - Testing philosophy and patterns
- [Pre-commit Setup](../project%20setup/PRECOMMIT-SETUP.md) - Local governance hooks
- [Directory Structure](../architecture/directory-structure.md) - Project organization
