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

# RATCHET-STRATEGY.md — One-Way Quality Improvement

> **The Ratchet Strategy:** Quality metrics can only improve, never regress. Like a ratchet wrench, you can tighten but never loosen.

---

## The Problem: Quality Decay

```
┌─────────────────────────────────────────────────────────────────────┐
│                    THE QUALITY DECAY SPIRAL                          │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│   Month 1: Team achieves 80% test coverage, zero type errors        │
│        ↓                                                            │
│   Month 2: Deadline → "We'll add tests later" → 78% coverage        │
│        ↓                                                            │
│   Month 3: New hire sees 78% → thinks it's acceptable → 75%         │
│        ↓                                                            │
│   Month 6: "Tests slow us down" → 60% coverage                      │
│        ↓                                                            │
│   Month 12: Legacy codebase, afraid to refactor                     │
│        ↓                                                            │
│   TECHNICAL DEBT CRISIS                                             │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

**The Ratchet Principle:** Capture the current state. Block any change that makes it worse.

---

## How the Ratchet Works

```
┌─────────────────────────────────────────────────────────────────────┐
│                    THE RATCHET MECHANISM                             │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│                         ┌──────────┐                                │
│   Quality Metric ───────► BASELINE │                                │
│                         └────┬─────┘                                │
│                              │                                      │
│                              ▼                                      │
│                    ┌────────────────────┐                           │
│   New Commit ──────► COMPARE TO BASELINE │                          │
│                    └─────────┬──────────┘                           │
│                              │                                      │
│              ┌───────────────┼───────────────┐                      │
│              ▼               ▼               ▼                      │
│         IMPROVED         UNCHANGED        DEGRADED                  │
│              │               │               │                      │
│              ▼               ▼               ▼                      │
│      Update Baseline      PASS         BLOCK COMMIT                 │
│              │               │               │                      │
│              └───────────────┼───────────────┘                      │
│                              │                                      │
│                    ┌─────────▼──────────┐                           │
│                    │  QUALITY CAN ONLY  │                           │
│                    │  GO UP, NEVER DOWN │                           │
│                    └────────────────────┘                           │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

---

## Metrics That Ratchet

### Core Metrics

| Metric | Direction | Example |
|--------|-----------|---------|
| Test Coverage | Must increase or stay same | 80% → 82% ✓, 80% → 78% ✗ |
| Type Safety Holes | Must decrease or stay same | 50 → 48 ✓, 50 → 52 ✗ |
| Mock Tax Violations | Must decrease or stay same | 5 → 4 ✓, 5 → 6 ✗ |
| Lint Warnings | Must decrease or stay same | 100 → 95 ✓, 100 → 105 ✗ |
| TODO Count | Must decrease or stay same | 20 → 18 ✓, 20 → 25 ✗ |
| Cyclomatic Complexity | Must decrease or stay same | Avg 8 → 7 ✓, 8 → 10 ✗ |

### Secondary Metrics (Optional)

| Metric | Direction | Notes |
|--------|-----------|-------|
| Bundle Size | Must decrease or stay same | For frontend apps |
| Dependency Count | Must decrease or stay same | Prevents bloat |
| Dead Code Lines | Must decrease or stay same | Via tree-shaking analysis |
| Security Vulnerabilities | Must decrease or stay same | Via npm audit, safety |

---

## The Three Phases

### Phase 1: Capture Baseline

```bash
# Generate baseline for all metrics
mault baseline --generate

# Output:
# Generating quality baselines...
#
# ┌────────────────────────────────────────────┐
# │ BASELINE GENERATED                          │
# ├────────────────────────────────────────────┤
# │ Test Coverage:      78.3%                   │
# │ Type Safety Holes:  127                     │
# │ Mock Tax Violations: 12                     │
# │ Lint Warnings:      45                      │
# │ TODO Count:         23                      │
# └────────────────────────────────────────────┘
#
# Saved to: .memory-layer/baselines/
```

**Key Point:** The baseline captures reality, not aspirations. You start where you are.

### Phase 2: Block Regressions

```
Developer makes commit
     ↓
Pre-commit runs all ratchet checks
     ↓
┌─────────────────────────────────────────────────────────────────────┐
│ RATCHET CHECK: Test Coverage                                         │
│ Baseline: 78.3%                                                      │
│ Current:  77.1%                                                      │
│ Status:   BLOCKED ✗                                                  │
│                                                                      │
│ Your changes reduced test coverage by 1.2%.                          │
│ Add tests for the following files:                                   │
│   - src/services/NewFeature.ts (0% covered)                          │
│   - src/utils/helper.ts (changed, coverage dropped)                  │
│                                                                      │
│ See: docs/production-readiness-kit/RATCHET-STRATEGY.md               │
└─────────────────────────────────────────────────────────────────────┘
     ↓
Commit rejected until coverage restored
```

### Phase 3: Celebrate Improvements

```
┌─────────────────────────────────────────────────────────────────────┐
│ RATCHET UPDATE                                                       │
├─────────────────────────────────────────────────────────────────────┤
│                                                                      │
│ Test Coverage:      78.3% → 79.5% ▲ (+1.2%)                         │
│ Type Safety Holes:  127 → 120   ▼ (-7)                              │
│ Lint Warnings:      45 → 45      (unchanged)                        │
│                                                                      │
│ Baseline updated! Quality ratcheted up.                              │
│                                                                      │
└─────────────────────────────────────────────────────────────────────┘
```

---

## Implementation

### Pre-commit Configuration

```yaml
# .pre-commit-config.yaml
repos:
  - repo: local
    hooks:
      # Ratchet: Test Coverage
      - id: coverage-ratchet
        name: Ratchet (Test Coverage)
        entry: python scripts/governance/check-coverage-ratchet.py
        language: system
        pass_filenames: false
        stages: [pre-commit]

      # Ratchet: Type Safety (see IRON-DOME.md)
      - id: type-safety-ratchet
        name: Ratchet (Type Safety)
        entry: python scripts/governance/check-type-safety.py
        language: system
        files: \.(ts|tsx|py)$

      # Ratchet: Mock Tax (see RISING-TIDE.md)
      - id: mock-tax-ratchet
        name: Ratchet (Mock Tax)
        entry: python scripts/governance/check-mock-tax.py
        language: system
        files: tests/.*\.(ts|py)$

      # Ratchet: Lint Warnings
      - id: lint-ratchet
        name: Ratchet (Lint Warnings)
        entry: python scripts/governance/check-lint-ratchet.py
        language: system
        pass_filenames: false
```

### Baseline File Structure

```
.memory-layer/
└── baselines/
    ├── coverage.json          # Test coverage baseline
    ├── type-safety.json       # Type safety holes baseline
    ├── mock-tax.json          # Mock tax violations baseline
    ├── lint-warnings.json     # Lint warnings baseline
    └── metrics-history.json   # Historical trend data
```

### Coverage Ratchet Script (Python)

```python
#!/usr/bin/env python3
"""
Ratchet: Test Coverage Enforcer

Blocks commits that reduce test coverage below baseline.
"""
import json
import subprocess
import sys
from pathlib import Path

BASELINE_PATH = Path('.memory-layer/baselines/coverage.json')
TOLERANCE = 0.5  # Allow 0.5% variance for floating point issues


def get_current_coverage() -> float:
    """Get current test coverage percentage."""
    # Adjust for your test framework (pytest, jest, go test, etc.)
    result = subprocess.run(
        ['pytest', '--cov=src', '--cov-report=json', '-q'],
        capture_output=True,
        text=True,
    )

    coverage_file = Path('coverage.json')
    if not coverage_file.exists():
        print("ERROR: Could not generate coverage report")
        sys.exit(1)

    data = json.loads(coverage_file.read_text())
    return data['totals']['percent_covered']


def load_baseline() -> dict:
    """Load coverage baseline."""
    if not BASELINE_PATH.exists():
        return {'coverage': 0.0, 'generated': None}
    return json.loads(BASELINE_PATH.read_text())


def save_baseline(data: dict) -> None:
    """Save updated baseline."""
    from datetime import datetime
    data['updated'] = datetime.now().isoformat()
    BASELINE_PATH.parent.mkdir(parents=True, exist_ok=True)
    BASELINE_PATH.write_text(json.dumps(data, indent=2))


def main():
    baseline = load_baseline()
    baseline_coverage = baseline.get('coverage', 0.0)

    print(f"Checking test coverage (baseline: {baseline_coverage:.1f}%)...")

    current_coverage = get_current_coverage()

    print(f"Current coverage: {current_coverage:.1f}%")

    # Check for regression
    if current_coverage < baseline_coverage - TOLERANCE:
        print()
        print('=' * 60)
        print('RATCHET VIOLATION: Test Coverage')
        print('=' * 60)
        print()
        print(f"  Baseline: {baseline_coverage:.1f}%")
        print(f"  Current:  {current_coverage:.1f}%")
        print(f"  Dropped:  {baseline_coverage - current_coverage:.1f}%")
        print()
        print("  Your changes reduced test coverage below the baseline.")
        print("  Add tests for new/changed code before committing.")
        print()
        print("  See: docs/production-readiness-kit/RATCHET-STRATEGY.md")
        sys.exit(1)

    # Check for improvement
    if current_coverage > baseline_coverage + TOLERANCE:
        print()
        print(f"Coverage improved: {baseline_coverage:.1f}% → {current_coverage:.1f}%")
        print("Updating baseline...")
        baseline['coverage'] = current_coverage
        save_baseline(baseline)

    print("Coverage check passed!")
    sys.exit(0)


if __name__ == '__main__':
    main()
```

### Coverage Ratchet Script (Node.js/Jest)

```javascript
#!/usr/bin/env node
/**
 * Ratchet: Test Coverage Enforcer
 *
 * Blocks commits that reduce test coverage below baseline.
 */
const { execSync } = require('child_process');
const fs = require('fs');
const path = require('path');

const BASELINE_PATH = '.memory-layer/baselines/coverage.json';
const TOLERANCE = 0.5; // Allow 0.5% variance

function getCurrentCoverage() {
  // Run Jest with coverage
  try {
    execSync('npx jest --coverage --coverageReporters=json-summary --silent', {
      stdio: 'pipe',
    });
  } catch (error) {
    // Jest exits with error if tests fail, but coverage might still be generated
  }

  const summaryPath = 'coverage/coverage-summary.json';
  if (!fs.existsSync(summaryPath)) {
    console.error('ERROR: Could not generate coverage report');
    process.exit(1);
  }

  const summary = JSON.parse(fs.readFileSync(summaryPath, 'utf8'));
  return summary.total.lines.pct;
}

function loadBaseline() {
  if (!fs.existsSync(BASELINE_PATH)) {
    return { coverage: 0, generated: null };
  }
  return JSON.parse(fs.readFileSync(BASELINE_PATH, 'utf8'));
}

function saveBaseline(data) {
  const dir = path.dirname(BASELINE_PATH);
  if (!fs.existsSync(dir)) {
    fs.mkdirSync(dir, { recursive: true });
  }
  data.updated = new Date().toISOString();
  fs.writeFileSync(BASELINE_PATH, JSON.stringify(data, null, 2));
}

// Main
const baseline = loadBaseline();
const baselineCoverage = baseline.coverage || 0;

console.log(`Checking test coverage (baseline: ${baselineCoverage.toFixed(1)}%)...`);

const currentCoverage = getCurrentCoverage();

console.log(`Current coverage: ${currentCoverage.toFixed(1)}%`);

// Check for regression
if (currentCoverage < baselineCoverage - TOLERANCE) {
  console.log();
  console.log('='.repeat(60));
  console.log('RATCHET VIOLATION: Test Coverage');
  console.log('='.repeat(60));
  console.log();
  console.log(`  Baseline: ${baselineCoverage.toFixed(1)}%`);
  console.log(`  Current:  ${currentCoverage.toFixed(1)}%`);
  console.log(`  Dropped:  ${(baselineCoverage - currentCoverage).toFixed(1)}%`);
  console.log();
  console.log('  Your changes reduced test coverage below the baseline.');
  console.log('  Add tests for new/changed code before committing.');
  console.log();
  console.log('  See: docs/production-readiness-kit/RATCHET-STRATEGY.md');
  process.exit(1);
}

// Check for improvement
if (currentCoverage > baselineCoverage + TOLERANCE) {
  console.log();
  console.log(`Coverage improved: ${baselineCoverage.toFixed(1)}% → ${currentCoverage.toFixed(1)}%`);
  console.log('Updating baseline...');
  baseline.coverage = currentCoverage;
  saveBaseline(baseline);
}

console.log('Coverage check passed!');
process.exit(0);
```

---

## Granularity Options

### File-Level Ratchet (Recommended for Large Codebases)

Instead of one global baseline, track per-file:

```json
// .memory-layer/baselines/coverage.json
{
  "global": 78.3,
  "byFile": {
    "src/services/OrderService.ts": 85.0,
    "src/services/UserService.ts": 72.0,
    "src/utils/helpers.ts": 90.0
  },
  "newFileThreshold": 80.0
}
```

**Rules:**
- Existing files: Cannot drop below their baseline
- New files: Must meet 80% threshold
- Global: Cannot drop below global baseline

### PR-Level Ratchet (For CI/CD)

```yaml
# .github/workflows/ratchet.yml
name: Ratchet Check

on: [pull_request]

jobs:
  ratchet:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Run Tests with Coverage
        run: npm test -- --coverage

      - name: Check Coverage Ratchet
        run: node scripts/governance/check-coverage-ratchet.js

      - name: Check Type Safety Ratchet
        run: node scripts/governance/check-type-safety.js

      - name: Check Mock Tax Ratchet
        run: node scripts/governance/check-mock-tax.js
```

---

## Exception Handling

### Temporary Exceptions

Sometimes you need to temporarily lower the bar (e.g., major refactor):

```json
// .memory-layer/baselines/coverage.json
{
  "coverage": 78.3,
  "exceptions": [
    {
      "file": "src/services/LegacyRefactor.ts",
      "reason": "Major refactor in progress, tests coming in follow-up PR",
      "expires": "2024-02-15",
      "approved_by": "tech-lead@company.com",
      "pr": "#1234"
    }
  ]
}
```

**Rules for Exceptions:**
- Must have expiration date
- Must have reason
- Must have approver
- Auto-expires and blocks future commits after date

### Permanent Exemptions

For code that legitimately can't be tested:

```json
// .memory-layer/baselines/coverage.json
{
  "exemptions": [
    {
      "file": "src/integrations/vendor-sdk.ts",
      "reason": "Vendor SDK wrapper, tested via integration tests only",
      "approved": "2024-01-15"
    }
  ]
}
```

---

## Trend Reporting

### Historical Tracking

```json
// .memory-layer/baselines/metrics-history.json
{
  "entries": [
    {
      "date": "2024-01-01",
      "coverage": 70.0,
      "typeSafety": 150,
      "mockTax": 20
    },
    {
      "date": "2024-01-15",
      "coverage": 75.0,
      "typeSafety": 130,
      "mockTax": 15
    },
    {
      "date": "2024-02-01",
      "coverage": 78.3,
      "typeSafety": 127,
      "mockTax": 12
    }
  ]
}
```

### Trend Visualization

```
═══════════════════════════════════════════════════════════════
                    RATCHET TREND REPORT
═══════════════════════════════════════════════════════════════

Test Coverage (target: 80%):
  Jan 01: ██████████████░░░░░░ 70.0%
  Jan 15: ███████████████░░░░░ 75.0%
  Feb 01: ███████████████░░░░░ 78.3%  ← Current

Type Safety Holes (target: 0):
  Jan 01: 150 ████████████████████████████████████████
  Jan 15: 130 ██████████████████████████████████
  Feb 01: 127 █████████████████████████████████  ← Current

Mock Tax Violations (target: 0):
  Jan 01: 20 ████████████████████
  Jan 15: 15 ███████████████
  Feb 01: 12 ████████████  ← Current

Overall Health: IMPROVING ▲
  Coverage:    +8.3% since baseline
  Type Safety: -15% holes since baseline
  Mock Tax:    -40% violations since baseline

═══════════════════════════════════════════════════════════════
```

---

## The Ratchet Mindset

### Why It Works

```
┌─────────────────────────────────────────────────────────────────────┐
│                    PSYCHOLOGY OF THE RATCHET                         │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  Without Ratchet:                                                   │
│    "Coverage dropped 2%. No big deal, we'll fix it later."          │
│    "Later" never comes. Decay accelerates.                          │
│                                                                     │
│  With Ratchet:                                                      │
│    "Coverage dropped 2%. Commit blocked."                           │
│    Developer MUST address it NOW.                                   │
│    Technical debt is paid at the point of creation.                 │
│                                                                     │
│  Key Insight:                                                       │
│    The cost of fixing now is ALWAYS lower than fixing later.        │
│    The ratchet forces "now."                                        │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

### The Compound Effect

```
Month 1: Ratchet blocks 5 regressions
         → Each would have cost 2 hours to fix later
         → Saved: 10 hours

Month 2: Quality mindset shifts
         → Developers write tests upfront
         → Ratchet blocks only 2 regressions
         → Saved: 4 hours + avoided future debt

Month 6: Ratchet rarely triggers
         → Team internalized quality standards
         → Codebase is healthier than it's ever been
         → New features ship faster (less debugging)
```

---

## Summary

| Concept | Description |
|---------|-------------|
| **Ratchet** | One-way quality improvement mechanism |
| **Baseline** | Starting point captured from current state |
| **Block** | Reject commits that regress below baseline |
| **Update** | Automatically raise baseline on improvement |
| **Exception** | Temporary bypass with expiration date |
| **Trend** | Track improvement over time |
| **Time Determinism** | Control time in tests to avoid flaky failures |

---

## Advanced: Time Determinism (Optional)

> **The Flaky Test Problem:** Tests using `new Date()` or `Date.now()` directly can pass at 11:59 PM but fail at midnight, pass on weekdays but fail on weekends, or pass in one timezone but fail in another.

### The Problem

```typescript
// This test passes at 11:59 PM, fails at 12:01 AM
describe('isExpired', () => {
  it('should detect expired tokens', () => {
    const token = { expiresAt: new Date('2024-01-15T23:59:59') };
    expect(isExpired(token)).toBe(true);  // Depends on current time!
  });
});
```

### Defense: Time Provider Pattern

Instead of using `new Date()` directly:

```typescript
// BEFORE: Non-deterministic
function isExpired(expiresAt: Date): boolean {
  return new Date() > expiresAt;  // What time is "now"?
}

// AFTER: Testable
function isExpired(expiresAt: Date, now: Date = new Date()): boolean {
  return now > expiresAt;  // Caller controls "now"
}

// Test with deterministic time
it('should detect expired tokens', () => {
  const fixedNow = new Date('2024-01-16T00:00:00');
  const expiresAt = new Date('2024-01-15T23:59:59');
  expect(isExpired(expiresAt, fixedNow)).toBe(true);  // Always passes
});
```

### Language-Agnostic Pattern

| Language | Time Injection | Test Helper |
|----------|---------------|-------------|
| **TypeScript** | Optional `now` parameter | `jest.useFakeTimers()`, `vi.useFakeTimers()` |
| **Python** | `freezegun`, `time-machine` | `@freeze_time('2024-01-15')` |
| **Go** | `clockwork` package | Interface injection |
| **Java** | `java.time.Clock` | `Clock.fixed(instant, zone)` |
| **Rust** | `chrono::TimeZone` | `MockClock` crate |

### Jest/Vitest Implementation

```typescript
// Option 1: Fake timers (recommended)
describe('Token expiration', () => {
  beforeEach(() => {
    jest.useFakeTimers();
    jest.setSystemTime(new Date('2024-01-16T00:00:00'));
  });

  afterEach(() => {
    jest.useRealTimers();
  });

  it('should detect expired tokens', () => {
    const token = { expiresAt: new Date('2024-01-15T23:59:59') };
    expect(isExpired(token)).toBe(true);  // Deterministic!
  });
});

// Option 2: Dependency injection
function isExpired(token: Token, clock = Date): boolean {
  return clock.now() > token.expiresAt.getTime();
}
```

### Python Implementation (freezegun)

```python
from freezegun import freeze_time

@freeze_time("2024-01-16 00:00:00")
def test_expired_token():
    token = Token(expires_at=datetime(2024, 1, 15, 23, 59, 59))
    assert is_expired(token) is True  # Deterministic!
```

### When to Apply Time Determinism

**Apply when:**
- Business logic involves dates/times
- Token expiration checks
- Cron-like scheduling
- Date-based filtering/sorting
- Time-sensitive billing calculations

**Skip when:**
- Simple logging timestamps (non-critical)
- One-off scripts
- Audit trails (actual time is correct)

### Ratchet Integration

Add time determinism violations to your ratchet:

```json
// .memory-layer/baselines/time-safety.json
{
  "directDateCalls": 15,
  "exemptions": [
    {
      "file": "src/utils/logger.ts",
      "reason": "Logging timestamps should be real time"
    }
  ]
}
```

Detect pattern with grep:
```bash
# Find direct Date calls in source (not tests)
grep -r "new Date()" src/ --include="*.ts" | grep -v ".test." | wc -l
```

---

## Related

- [RISING-TIDE.md](./RISING-TIDE.md) — Mock Tax philosophy (ratchets test/source ratio)
- [IRON-DOME.md](./IRON-DOME.md) — Type Safety philosophy (ratchets type holes)
- [TDD-GUIDE.md](./TDD-GUIDE.md) — Test-driven development practices

---

*Part of the Mault Production-Readiness Kit*
