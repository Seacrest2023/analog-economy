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

# RISING-TIDE.md — Mock Tax Philosophy

> **The Rising Tide Strategy:** When tests grow larger than the code they test, something is wrong. Delete the unit test. Write an integration test.

---

## The Problem: Mock Tax

```
┌─────────────────────────────────────────────────────────────────────┐
│                        THE MOCK TAX SPIRAL                          │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│   Source file: 50 lines                                             │
│        ↓                                                            │
│   Unit test: 100 lines (mocking dependencies)                       │
│        ↓                                                            │
│   Source changes → Test breaks → More mocking → 150 lines           │
│        ↓                                                            │
│   Test is now 3x source size                                        │
│        ↓                                                            │
│   Developer stops trusting tests → Skips writing them               │
│        ↓                                                            │
│   QUALITY DEGRADES                                                  │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

**The Mock Tax:** The overhead of maintaining mocks that simulate behavior rather than testing real behavior.

---

## The 2x Rule

**If a unit test is more than 2x the size of the source code, delete the unit test and write an integration test instead.**

### Why 2x?

| Test : Source Ratio | Interpretation | Action |
|---------------------|----------------|--------|
| < 1.0x | Under-tested | Add more test cases |
| 1.0x - 2.0x | **Healthy** | Maintain |
| 2.0x - 3.0x | **Mock Tax Warning** | Consider integration test |
| > 3.0x | **Excessive** | Delete, rewrite as integration |

### The Math

```
Source file: src/services/UserService.ts (50 lines)
Test file: tests/unit/UserService.test.ts (??? lines)

PASS: Test is 75 lines → 1.5x → Healthy
WARN: Test is 120 lines → 2.4x → Mock Tax Warning
FAIL: Test is 200 lines → 4.0x → DELETE AND REWRITE
```

---

## Why Mocks Accumulate

### Pattern 1: Dependency Chaining

```typescript
// Source: 20 lines
export class OrderService {
  constructor(
    private db: Database,
    private payment: PaymentGateway,
    private email: EmailService,
    private inventory: InventoryService
  ) {}

  async placeOrder(order: Order) {
    // 15 lines of business logic
  }
}

// Unit Test: 80 lines (4x!)
describe('OrderService', () => {
  let mockDb: jest.Mocked<Database>;
  let mockPayment: jest.Mocked<PaymentGateway>;
  let mockEmail: jest.Mocked<EmailService>;
  let mockInventory: jest.Mocked<InventoryService>;

  beforeEach(() => {
    mockDb = { query: jest.fn(), ... };           // 10 lines
    mockPayment = { charge: jest.fn(), ... };     // 10 lines
    mockEmail = { send: jest.fn(), ... };         // 10 lines
    mockInventory = { reserve: jest.fn(), ... }; // 10 lines
    // Setup mock return values: 20 more lines
  });

  // Actual tests: 20 lines
});
```

**The problem:** 60 lines of mock setup for 20 lines of test assertions.

### Pattern 2: State Simulation

```typescript
// Mocking database state across multiple operations
mockDb.query
  .mockResolvedValueOnce({ rows: [user] })    // First call: get user
  .mockResolvedValueOnce({ rows: [] })         // Second call: check duplicates
  .mockResolvedValueOnce({ rows: [newUser] }); // Third call: insert result
```

**The problem:** Mock chain must match exact call order. Change source → break test.

### Pattern 3: Framework Mocking

```typescript
// Mocking VS Code APIs
(vscode.window as any).showInformationMessage = jest.fn();
(vscode.workspace as any).getConfiguration = jest.fn().mockReturnValue({
  get: jest.fn().mockReturnValue(true),
  update: jest.fn(),
});
(vscode.commands as any).executeCommand = jest.fn();
// ... 30 more lines of framework mocking
```

**The problem:** You're testing your mock, not the real behavior.

---

## The Integration Test Alternative

### What's an Integration Test?

```
Unit Test:
  ┌──────────────┐
  │ Your Code    │ ←── Tested
  │──────────────│
  │ Mock DB      │ ←── Fake
  │ Mock API     │ ←── Fake
  │ Mock FS      │ ←── Fake
  └──────────────┘

Integration Test:
  ┌──────────────┐
  │ Your Code    │ ←── Tested
  │──────────────│
  │ Real DB      │ ←── Real (test container)
  │ Real API     │ ←── Real (test server)
  │ Real FS      │ ←── Real (temp directory)
  └──────────────┘
```

### Integration Test: Same Logic, Less Code

```typescript
// Integration test: 40 lines (same coverage, less maintenance)
describe('OrderService (integration)', () => {
  let db: TestDatabase;  // Real database in container
  let app: TestApp;      // Real app instance

  beforeAll(async () => {
    db = await TestDatabase.start();  // Docker container
    app = await TestApp.create({ db });
  });

  afterAll(async () => {
    await db.stop();
  });

  it('places order and sends confirmation', async () => {
    // Arrange: Real data in real database
    const user = await db.createUser({ email: 'test@example.com' });
    const product = await db.createProduct({ stock: 10 });

    // Act: Real API call
    const order = await app.orderService.placeOrder({
      userId: user.id,
      productId: product.id,
      quantity: 2,
    });

    // Assert: Real database state
    expect(order.status).toBe('confirmed');
    expect(await db.getProduct(product.id)).toHaveProperty('stock', 8);
    expect(await db.getEmails()).toContainEqual(
      expect.objectContaining({ to: 'test@example.com' })
    );
  });
});
```

**Why this is better:**
- No mock maintenance
- Tests real behavior
- Catches integration bugs mocks would miss
- 40 lines vs 80 lines

---

## The Rising Tide Strategy

### Core Principle

```
┌─────────────────────────────────────────────────────────────────────┐
│                    THE RISING TIDE                                   │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  "A rising tide lifts all boats."                                   │
│                                                                     │
│  As integration test coverage increases, the pressure on            │
│  poorly-designed unit tests increases. Eventually, they sink.       │
│                                                                     │
│  The 2x rule creates natural selection:                             │
│  • Lean unit tests survive                                          │
│  • Bloated unit tests get deleted                                   │
│  • Integration tests replace what was lost                          │
│                                                                     │
│  Over time, test suite becomes:                                     │
│  • Smaller (fewer lines)                                            │
│  • More reliable (less mock brittleness)                            │
│  • More valuable (catches real bugs)                                │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

### Migration Path

```
Week 1: Identify offenders
  → Run mock-tax check
  → List all tests > 2x ratio

Week 2-4: Replace worst offenders
  → Pick top 5 bloated tests
  → Write integration test equivalents
  → Delete unit tests
  → Verify coverage maintained

Week 5+: Enforce going forward
  → Pre-commit blocks new violations
  → New code gets integration tests
  → Legacy tests gradually replaced
```

---

## Implementation

### Pre-commit Hook (AI-Generated)

```yaml
# .pre-commit-config.yaml
- repo: local
  hooks:
    - id: mock-tax
      name: Rising Tide (Mock Tax)
      entry: python scripts/governance/check-mock-tax.py  # Or .js for TS projects
      language: system
      files: tests/.*\.(py|ts|js)$
      description: |
        Enforces the 2x Rule: Tests cannot be >2x source size.
        If blocked, write an integration test instead.
```

**Roadmap Languages:** Go, Java, Rust, and C# support for Mock Tax enforcement is planned for future releases.

### Example Script (Python)

```python
#!/usr/bin/env python3
"""
Rising Tide: Mock Tax Enforcer

Blocks commits where test files exceed 2x the source file size.
"""
import sys
from pathlib import Path

MAX_RATIO = 2.0

def get_source_path(test_path: Path) -> Path | None:
    """Map test file to its source file."""
    # tests/unit/services/UserService.test.ts → src/services/UserService.ts
    name = test_path.stem.replace('.test', '').replace('_test', '')
    # ... mapping logic for your project structure
    return source_path

def count_lines(path: Path) -> int:
    """Count non-empty, non-comment lines."""
    lines = path.read_text().splitlines()
    return sum(1 for line in lines if line.strip() and not line.strip().startswith('#'))

def check_mock_tax(test_files: list[str]) -> list[str]:
    violations = []

    for test_file in test_files:
        test_path = Path(test_file)
        source_path = get_source_path(test_path)

        if not source_path or not source_path.exists():
            continue

        test_lines = count_lines(test_path)
        source_lines = count_lines(source_path)

        if source_lines == 0:
            continue

        ratio = test_lines / source_lines

        if ratio > MAX_RATIO:
            violations.append(
                f"MOCK-TAX: {test_file}\n"
                f"  Test: {test_lines} lines, Source: {source_lines} lines\n"
                f"  Ratio: {ratio:.1f}x (max: {MAX_RATIO}x)\n"
                f"  Action: Delete unit test, write integration test instead.\n"
            )

    return violations

if __name__ == '__main__':
    violations = check_mock_tax(sys.argv[1:])

    if violations:
        print("=" * 60)
        print("RISING TIDE: Mock Tax Violations")
        print("=" * 60)
        for v in violations:
            print(v)
        print("See: docs/production-readiness-kit/RISING-TIDE.md")
        sys.exit(1)

    sys.exit(0)
```

### Example Script (TypeScript/Node.js)

```javascript
#!/usr/bin/env node
/**
 * Rising Tide: Mock Tax Enforcer
 *
 * Blocks commits where test files exceed 2x the source file size.
 */
const fs = require('fs');
const path = require('path');

const MAX_RATIO = 2.0;

function getSourcePath(testPath) {
  // tests/unit/services/UserService.test.ts → src/services/UserService.ts
  const name = path.basename(testPath)
    .replace('.test.ts', '.ts')
    .replace('.test.js', '.js')
    .replace('.spec.ts', '.ts')
    .replace('.spec.js', '.js');

  // Adjust path mapping for your project structure
  const sourcePath = testPath
    .replace('tests/unit/', 'src/')
    .replace('tests/', 'src/')
    .replace('.test.ts', '.ts')
    .replace('.test.js', '.js');

  return sourcePath;
}

function countLines(filePath) {
  const content = fs.readFileSync(filePath, 'utf8');
  const lines = content.split('\n');
  return lines.filter(line => {
    const trimmed = line.trim();
    return trimmed && !trimmed.startsWith('//') && !trimmed.startsWith('/*');
  }).length;
}

function checkMockTax(testFiles) {
  const violations = [];

  for (const testFile of testFiles) {
    const sourcePath = getSourcePath(testFile);

    if (!fs.existsSync(sourcePath)) {
      continue;
    }

    const testLines = countLines(testFile);
    const sourceLines = countLines(sourcePath);

    if (sourceLines === 0) continue;

    const ratio = testLines / sourceLines;

    if (ratio > MAX_RATIO) {
      violations.push({
        testFile,
        testLines,
        sourceLines,
        ratio: ratio.toFixed(1),
      });
    }
  }

  return violations;
}

// Main
const testFiles = process.argv.slice(2);
const violations = checkMockTax(testFiles);

if (violations.length > 0) {
  console.log('='.repeat(60));
  console.log('RISING TIDE: Mock Tax Violations');
  console.log('='.repeat(60));

  for (const v of violations) {
    console.log(`MOCK-TAX: ${v.testFile}`);
    console.log(`  Test: ${v.testLines} lines, Source: ${v.sourceLines} lines`);
    console.log(`  Ratio: ${v.ratio}x (max: ${MAX_RATIO}x)`);
    console.log(`  Action: Delete unit test, write integration test instead.`);
    console.log();
  }

  console.log('See: docs/production-readiness-kit/RISING-TIDE.md');
  process.exit(1);
}

process.exit(0);
```

---

## Exceptions

### When to Override the 2x Rule

1. **Pure utility functions** — Some utilities legitimately need many test cases:
   ```typescript
   // parseDate.ts: 20 lines
   // parseDate.test.ts: 50 lines (2.5x) — ACCEPTABLE
   // Many edge cases: timezones, formats, invalid inputs
   ```

2. **Complex algorithms** — State machines, parsers:
   ```typescript
   // stateMachine.ts: 100 lines
   // stateMachine.test.ts: 250 lines (2.5x) — ACCEPTABLE
   // Many state transitions to verify
   ```

### Marking Exceptions

```typescript
// tests/unit/parseDate.test.ts
// MOCK-TAX-EXEMPT: Pure utility with many edge cases

describe('parseDate', () => {
  // ... extensive tests
});
```

The governance script should skip files with `MOCK-TAX-EXEMPT` comment.

---

## Baseline + Ratchet

### For Existing Projects

1. **Generate baseline** — Current mock tax violations
2. **Ratchet down** — New commits cannot increase violations
3. **Gradual improvement** — Address legacy tests over time

```json
// .memory-layer/baselines/mock-tax.json
{
  "generated": "2024-01-15",
  "violations": [
    {
      "file": "tests/unit/OrderService.test.ts",
      "ratio": 3.2,
      "exempt": false,
      "note": "Legacy - scheduled for Q1 refactor"
    }
  ],
  "totalViolations": 12
}
```

### Ratchet Enforcement

```python
# In check-mock-tax.py

def check_ratchet(current_violations, baseline_path):
    """Ensure violations don't increase."""
    baseline = json.load(open(baseline_path))
    baseline_count = baseline['totalViolations']

    if len(current_violations) > baseline_count:
        print(f"RATCHET VIOLATION: {len(current_violations)} > {baseline_count}")
        print("New mock-tax violations are not allowed until baseline is reduced.")
        sys.exit(1)
```

---

## Summary

| Concept | Description |
|---------|-------------|
| **Mock Tax** | Overhead of maintaining mocks in tests |
| **2x Rule** | Test cannot be >2x source size |
| **Rising Tide** | As integration coverage rises, bloated unit tests naturally get replaced |
| **Migration Path** | Identify → Replace → Enforce |
| **Baseline + Ratchet** | For existing projects, only improve, never regress |

---

## Related

- [IRON-DOME.md](./IRON-DOME.md) — Type Safety philosophy
- [SCHEMA-VALIDATION.md](./SCHEMA-VALIDATION.md) — Runtime type safety (applies Rising Tide to Zod)
- [RATCHET-STRATEGY.md](./RATCHET-STRATEGY.md) — Baseline improvement philosophy
- [TDD-GUIDE.md](./TDD-GUIDE.md) — Test-driven development practices

> **Note:** The Rising Tide philosophy applies beyond mock tax. It's also used for Zod schema validation at system boundaries. See [SCHEMA-VALIDATION.md](./SCHEMA-VALIDATION.md) for details.

---

*Part of the Mault Production-Readiness Kit*
