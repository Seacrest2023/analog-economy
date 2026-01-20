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

# Governance Testing Implementation Guide

> **Step 8 of 8** in the Production-Readiness Kit
> **Applies to:** Mault Pro ($99 one-time)

---

## What Is Governance Testing?

Governance testing is the **foundation layer** of the testing pyramid. Unlike other tests that validate your code, governance tests validate **the tests themselves**.

> "Who watches the watchmen? Governance tests watch the tests."

In AI-assisted development, there's no human reviewer to catch:
- Mocks that drift from real APIs
- Tests that pass but test against stale fakes
- Type holes that defeat TypeScript protection
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
│  □ 3. Implement Type Safety checker (any Ratchet)                   │
│  □ 4. Implement Silent Catch detector                               │
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
your-project/
├── scripts/
│   └── governance/           # ← CREATE THIS
│       ├── check-mock-tax.js
│       ├── check-any-usage.js
│       ├── check-silent-catches.js
│       └── check-hallucinations.js
├── tests/
│   ├── unit/                 # Pure logic ONLY — NO vscode imports
│   │   └── governance/       # ← CREATE THIS
│   │       ├── mock-integrity.test.ts
│   │       └── mock-signature.test.ts
│   ├── integration/          # Gold Standard v3.0 — vscode mocking allowed
│   │   ├── commands/
│   │   └── event-flows/      # Event orchestration tests
│   └── behavioral/           # Detector perception tests
└── .memory-layer/
    └── baselines/            # ← CREATE THIS
        ├── any-baseline.json
        ├── coverage-baseline.json
        └── silent-catch-baseline.json
```

> **CRITICAL:** ESLint governance blocks `import * as vscode from 'vscode'` in `tests/unit/`. If your test needs the vscode API, place it in `tests/integration/`. This ensures unit tests remain pure logic only.

---

## Step 2: Mock Tax Checker (Rising Tide)

**File to create:** `scripts/governance/check-mock-tax.js`

**What it does:** Blocks unit tests that are >2x the size of the source file they test.

**Why:** Heavy mocking is a code smell. If you need 2x the code to test something, convert to integration test.

```javascript
#!/usr/bin/env node
/**
 * Mock Tax Checker (Rising Tide)
 * Blocks unit tests where test LOC > 2x source LOC
 */

const fs = require('fs');
const path = require('path');
const { execSync } = require('child_process');

const MAX_RATIO = 2.0;
const MIN_SOURCE_LINES = 15;  // Only check files >15 lines

// Get staged files or all files
const stagedOnly = process.argv.includes('--staged');
const files = stagedOnly
  ? execSync('git diff --cached --name-only --diff-filter=ACM')
      .toString().trim().split('\n').filter(Boolean)
  : execSync('find src -name "*.ts" -not -name "*.test.ts" -not -name "*.spec.ts"')
      .toString().trim().split('\n').filter(Boolean);

const violations = [];

files.forEach(srcFile => {
  if (!srcFile.endsWith('.ts') || srcFile.includes('.test.') || srcFile.includes('.spec.')) {
    return;
  }

  // Find corresponding test file
  const testFile = srcFile
    .replace('/src/', '/tests/unit/')
    .replace('.ts', '.test.ts');

  if (!fs.existsSync(testFile)) return;

  const srcLines = fs.readFileSync(srcFile, 'utf8').split('\n').length;
  const testLines = fs.readFileSync(testFile, 'utf8').split('\n').length;

  if (srcLines < MIN_SOURCE_LINES) return;

  const ratio = testLines / srcLines;

  if (ratio > MAX_RATIO) {
    violations.push({
      source: srcFile,
      test: testFile,
      srcLines,
      testLines,
      ratio: ratio.toFixed(2)
    });
  }
});

if (violations.length > 0) {
  console.error('\n🚫 MOCK TAX VIOLATION (Rising Tide)\n');
  console.error('The following tests exceed the 2x size limit:\n');

  violations.forEach(v => {
    console.error(`  ${v.test}`);
    console.error(`    Source: ${v.srcLines} lines | Test: ${v.testLines} lines | Ratio: ${v.ratio}x`);
    console.error('');
  });

  console.error('REMEDIATION:');
  console.error('  1. DELETE the unit test file');
  console.error('  2. CREATE an integration test using Gold Standard v3.0');
  console.error('  3. See: docs/patterns/gold-standard-integration.ts\n');

  process.exit(1);
}

console.log('✓ Mock Tax check passed');
```

---

## Step 3: Type Safety Checker (any Ratchet)

**File to create:** `scripts/governance/check-any-usage.js`

**What it does:** Counts `any` usage and blocks if count increases above baseline.

**Why:** Every `any` is a potential runtime crash. Ratchet ensures count only goes down.

```javascript
#!/usr/bin/env node
/**
 * Type Safety Checker (any Ratchet)
 * Blocks commits that increase `any` usage above baseline
 */

const fs = require('fs');
const path = require('path');
const { execSync } = require('child_process');

const BASELINE_FILE = '.memory-layer/baselines/any-baseline.json';
const ANY_PATTERNS = [': any', 'as any', '<any>'];

function countAnyUsage(filePath) {
  const content = fs.readFileSync(filePath, 'utf8');
  let count = 0;
  ANY_PATTERNS.forEach(pattern => {
    const matches = content.match(new RegExp(pattern.replace(/[.*+?^${}()|[\]\\]/g, '\\$&'), 'g'));
    if (matches) count += matches.length;
  });
  return count;
}

function scanDirectory(dir, extensions = ['.ts', '.tsx']) {
  let total = 0;
  const files = execSync(`find ${dir} -type f \\( -name "*.ts" -o -name "*.tsx" \\) -not -path "*/node_modules/*"`)
    .toString().trim().split('\n').filter(Boolean);

  files.forEach(file => {
    total += countAnyUsage(file);
  });

  return total;
}

// Load or create baseline
let baseline = { threshold: 0, lastUpdated: null };
if (fs.existsSync(BASELINE_FILE)) {
  baseline = JSON.parse(fs.readFileSync(BASELINE_FILE, 'utf8'));
}

// Count current usage
const currentCount = scanDirectory('src');

console.log(`\nType Safety Check (any Ratchet)`);
console.log(`  Baseline: ${baseline.threshold}`);
console.log(`  Current:  ${currentCount}`);

if (currentCount > baseline.threshold) {
  console.error(`\n🚫 TYPE SAFETY VIOLATION\n`);
  console.error(`  any usage INCREASED: ${baseline.threshold} → ${currentCount}`);
  console.error(`  Delta: +${currentCount - baseline.threshold}\n`);
  console.error('REMEDIATION:');
  console.error('  1. Find and fix the new `any` usages');
  console.error('  2. Use proper types or generics instead');
  console.error('  3. If truly unavoidable, reduce existing `any` to offset\n');
  process.exit(1);
}

// Update baseline if count decreased (ratchet down)
if (currentCount < baseline.threshold) {
  baseline.threshold = currentCount;
  baseline.lastUpdated = new Date().toISOString();
  fs.writeFileSync(BASELINE_FILE, JSON.stringify(baseline, null, 2));
  console.log(`\n✓ Baseline ratcheted down: ${baseline.threshold}`);
}

console.log('✓ Type Safety check passed\n');
```

---

## Step 4: Silent Catch Detector

**File to create:** `scripts/governance/check-silent-catches.js`

**What it does:** Detects empty catch blocks that swallow errors.

**Why:** Silent failures are debugging nightmares. Errors should be handled OR propagated.

```javascript
#!/usr/bin/env node
/**
 * Silent Catch Detector
 * Blocks empty catch blocks that swallow errors
 */

const fs = require('fs');
const { execSync } = require('child_process');

const BASELINE_FILE = '.memory-layer/baselines/silent-catch-baseline.json';

// Pattern: catch block with only whitespace or comments
const SILENT_CATCH_PATTERN = /catch\s*\([^)]*\)\s*\{\s*(\/\/[^\n]*\n\s*)?\}/g;

function findSilentCatches(filePath) {
  const content = fs.readFileSync(filePath, 'utf8');
  const matches = content.match(SILENT_CATCH_PATTERN) || [];

  // Filter out legitimate exemptions (marked with // SILENT_CATCH:)
  const exemptPattern = /\/\/\s*SILENT_CATCH:/;
  const violations = matches.filter(m => !exemptPattern.test(m));

  return violations.length;
}

function scanDirectory(dir) {
  let total = 0;
  const files = execSync(`find ${dir} -type f \\( -name "*.ts" -o -name "*.tsx" -o -name "*.js" \\) -not -path "*/node_modules/*"`)
    .toString().trim().split('\n').filter(Boolean);

  const details = [];
  files.forEach(file => {
    const count = findSilentCatches(file);
    if (count > 0) {
      total += count;
      details.push({ file, count });
    }
  });

  return { total, details };
}

// Load or create baseline
let baseline = { threshold: 0, lastUpdated: null };
if (fs.existsSync(BASELINE_FILE)) {
  baseline = JSON.parse(fs.readFileSync(BASELINE_FILE, 'utf8'));
}

const { total, details } = scanDirectory('src');

console.log(`\nSilent Catch Detection`);
console.log(`  Baseline: ${baseline.threshold}`);
console.log(`  Current:  ${total}`);

if (total > baseline.threshold) {
  console.error(`\n🚫 SILENT CATCH VIOLATION\n`);
  console.error(`  Silent catches INCREASED: ${baseline.threshold} → ${total}\n`);

  details.forEach(d => {
    console.error(`  ${d.file}: ${d.count} silent catch(es)`);
  });

  console.error('\nREMEDIATION:');
  console.error('  Option 1: Log the error → catch (e) { console.error(e); }');
  console.error('  Option 2: Rethrow → catch (e) { throw e; }');
  console.error('  Option 3: Mark as intentional → // SILENT_CATCH: <reason>\n');
  process.exit(1);
}

// Ratchet down
if (total < baseline.threshold) {
  baseline.threshold = total;
  baseline.lastUpdated = new Date().toISOString();
  fs.writeFileSync(BASELINE_FILE, JSON.stringify(baseline, null, 2));
  console.log(`✓ Baseline ratcheted down: ${baseline.threshold}`);
}

console.log('✓ Silent Catch check passed\n');
```

---

## Step 5: Create Baseline Files

**Files to create:** Initialize baselines with current counts.

### any-baseline.json

```json
{
  "threshold": 0,
  "lastUpdated": null,
  "note": "Run check-any-usage.js to set initial baseline"
}
```

### silent-catch-baseline.json

```json
{
  "threshold": 0,
  "lastUpdated": null,
  "note": "Run check-silent-catches.js to set initial baseline"
}
```

### Initialize Baselines

After creating the scripts, run them once to establish baselines:

```bash
# Set initial baselines (first run stores current counts)
node scripts/governance/check-any-usage.js --init
node scripts/governance/check-silent-catches.js --init
```

---

## Step 6: Governance Tests (Tests That Test Tests)

**File to create:** `tests/unit/governance/mock-integrity.test.ts`

**What it does:** Validates that your shared mock implements the expected API surface.

```typescript
/**
 * Mock Integrity Test
 * Validates shared mock implements expected API surface
 */

import * as vscode from 'vscode'; // Uses shared mock via moduleNameMapper

describe('Governance: Mock Integrity', () => {
  describe('vscode.workspace', () => {
    it('should have workspaceFolders property', () => {
      expect(vscode.workspace).toHaveProperty('workspaceFolders');
    });

    it('should have getConfiguration method', () => {
      expect(typeof vscode.workspace.getConfiguration).toBe('function');
    });

    it('should have findFiles method', () => {
      expect(typeof vscode.workspace.findFiles).toBe('function');
    });

    it('should have openTextDocument method', () => {
      expect(typeof vscode.workspace.openTextDocument).toBe('function');
    });
  });

  describe('vscode.window', () => {
    it('should have showInformationMessage method', () => {
      expect(typeof vscode.window.showInformationMessage).toBe('function');
    });

    it('should have showErrorMessage method', () => {
      expect(typeof vscode.window.showErrorMessage).toBe('function');
    });

    it('should have showQuickPick method', () => {
      expect(typeof vscode.window.showQuickPick).toBe('function');
    });

    it('should have createOutputChannel method', () => {
      expect(typeof vscode.window.createOutputChannel).toBe('function');
    });
  });

  describe('vscode.Uri', () => {
    it('should have file static method', () => {
      expect(typeof vscode.Uri.file).toBe('function');
    });

    it('should create Uri with fsPath', () => {
      const uri = vscode.Uri.file('/test/path');
      expect(uri.fsPath).toBeDefined();
    });
  });

  describe('vscode.languages', () => {
    it('should have createDiagnosticCollection method', () => {
      expect(typeof vscode.languages.createDiagnosticCollection).toBe('function');
    });

    it('should have registerCodeActionsProvider method', () => {
      expect(typeof vscode.languages.registerCodeActionsProvider).toBe('function');
    });
  });

  describe('vscode classes', () => {
    it('should have Position class', () => {
      const pos = new vscode.Position(1, 0);
      expect(pos.line).toBe(1);
      expect(pos.character).toBe(0);
    });

    it('should have Range class', () => {
      const range = new vscode.Range(
        new vscode.Position(0, 0),
        new vscode.Position(1, 0)
      );
      expect(range.start).toBeDefined();
      expect(range.end).toBeDefined();
    });

    it('should have Diagnostic class', () => {
      const diag = new vscode.Diagnostic(
        new vscode.Range(new vscode.Position(0, 0), new vscode.Position(0, 10)),
        'Test message',
        vscode.DiagnosticSeverity.Warning
      );
      expect(diag.message).toBe('Test message');
    });
  });

  describe('vscode enums', () => {
    it('should have DiagnosticSeverity enum', () => {
      expect(vscode.DiagnosticSeverity.Error).toBeDefined();
      expect(vscode.DiagnosticSeverity.Warning).toBeDefined();
      expect(vscode.DiagnosticSeverity.Information).toBeDefined();
      expect(vscode.DiagnosticSeverity.Hint).toBeDefined();
    });
  });
});
```

---

## Step 7: Wire Into Pre-commit

Add governance checks to `.pre-commit-config.yaml`:

```yaml
# Governance Checks (Step 8 of Production-Readiness Kit)
- repo: local
  hooks:
    # Mock Tax (Rising Tide)
    - id: mock-tax
      name: Mock Tax Check (Rising Tide)
      entry: node scripts/governance/check-mock-tax.js --staged
      language: system
      pass_filenames: false
      stages: [commit]

    # Type Safety (any Ratchet)
    - id: type-safety
      name: Type Safety Check (any Ratchet)
      entry: node scripts/governance/check-any-usage.js
      language: system
      pass_filenames: false
      stages: [commit]

    # Silent Catches
    - id: silent-catches
      name: Silent Catch Detection
      entry: node scripts/governance/check-silent-catches.js
      language: system
      pass_filenames: false
      stages: [commit]

    # Governance Tests
    - id: governance-tests
      name: Governance Tests
      entry: npm test -- --testPathPattern=governance
      language: system
      pass_filenames: false
      stages: [commit]
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
│   Example (any-baseline.json):                                      │
│   ┌────────────────────────────────────────────────────────┐        │
│   │  Day 1: Count = 50 → Set baseline = 50                 │        │
│   │  Day 2: Add 3 `any` → Count = 53 → BLOCKED!            │        │
│   │  Day 3: Remove 10 → Count = 40 → Baseline now 40       │        │
│   │  Day 4: Add 5 → Count = 45 → Still > 40 → BLOCKED!     │        │
│   └────────────────────────────────────────────────────────┘        │
│                                                                     │
│   The ratchet ONLY turns one way — toward improvement.              │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

**Layers using ratchets:**
- Mock Tax: Test/source ratio can only go down
- Type Safety: `any` count can only go down
- Silent Catches: Empty catch count can only go down
- Coverage: Percentage can only go up

---

## Python Governance Implementation

For Python projects, create equivalent scripts:

### check_mock_conformance.py

```python
#!/usr/bin/env python3
"""
Mock Conformance Checker
Ensures tests use create_autospec instead of bare Mock()
"""

import ast
import sys
from pathlib import Path

VIOLATIONS = []

class MockVisitor(ast.NodeVisitor):
    def __init__(self, filepath):
        self.filepath = filepath

    def visit_Call(self, node):
        # Check for bare Mock() calls
        if isinstance(node.func, ast.Name) and node.func.id == 'Mock':
            # Check if it's not create_autospec
            VIOLATIONS.append({
                'file': str(self.filepath),
                'line': node.lineno,
                'issue': 'Bare Mock() usage - use create_autospec instead'
            })
        self.generic_visit(node)

def check_file(filepath):
    with open(filepath) as f:
        try:
            tree = ast.parse(f.read())
            visitor = MockVisitor(filepath)
            visitor.visit(tree)
        except SyntaxError:
            pass

def main():
    test_dir = Path('tests')
    if not test_dir.exists():
        print('No tests directory found')
        return 0

    for pyfile in test_dir.rglob('*.py'):
        check_file(pyfile)

    if VIOLATIONS:
        print('\n Mock Conformance Violations\n')
        for v in VIOLATIONS:
            print(f"  {v['file']}:{v['line']}")
            print(f"    {v['issue']}\n")
        print('REMEDIATION:')
        print('  Replace Mock() with create_autospec(RealClass, instance=True)')
        return 1

    print(' Mock Conformance check passed')
    return 0

if __name__ == '__main__':
    sys.exit(main())
```

---

## Verification Checklist

Before completing Step 8:

- [ ] `scripts/governance/` directory exists with all scripts
- [ ] `tests/unit/governance/` contains mock-integrity tests
- [ ] `.memory-layer/baselines/` contains initialized baseline files
- [ ] Pre-commit hooks include all governance checks
- [ ] Running `pre-commit run --all-files` passes
- [ ] Governance tests pass: `npm test -- --testPathPattern=governance`

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
│           - Mock Tax? → DELETE unit test, write integration test    │
│           - any count? → Fix the types                              │
│           - Silent catch? → Add proper error handling               │
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
| `check-mock-tax.js` | Test LOC <= 2x Source LOC | N/A (hard limit) |
| `check-any-usage.js` | `any` count doesn't increase | `any-baseline.json` |
| `check-silent-catches.js` | Empty catches don't increase | `silent-catch-baseline.json` |
| `mock-integrity.test.ts` | Shared mock implements real API | N/A (test) |

---

## Related

- [TDD-GUIDE.md](./TDD-GUIDE.md) — Test-First philosophy
- [RISING-TIDE.md](./RISING-TIDE.md) — Mock Tax (2x rule)
- [PRECOMMIT-SETUP.md](./PRECOMMIT-SETUP.md) — Pre-commit hook configuration

---

*Part of Mault Pro Production-Readiness Kit*
