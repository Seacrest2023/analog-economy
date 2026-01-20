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

# IRON-DOME.md — Type Safety Philosophy

> **The Iron Dome Strategy:** Every `any`, `type: ignore`, or disabled lint rule is a hole in your defense. Track them. Ratchet them down. Never let them increase.

---

## The Problem: Death by a Thousand Cuts

```
┌─────────────────────────────────────────────────────────────────────┐
│                    THE TYPE SAFETY DECAY SPIRAL                      │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│   Day 1: Clean codebase, strict types                               │
│        ↓                                                            │
│   Day 10: Deadline pressure → "just add `any` for now"              │
│        ↓                                                            │
│   Day 30: 5 `any` types scattered in code                           │
│        ↓                                                            │
│   Day 90: Team sees `any` is "acceptable" → 50 more added           │
│        ↓                                                            │
│   Day 180: Type system provides false confidence                    │
│        ↓                                                            │
│   RUNTIME ERRORS IN PRODUCTION                                      │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

**The Iron Dome Principle:** Intercept type-safety violations before they land in main.

---

## Type Safety Holes by Language

### TypeScript/JavaScript

| Hole | Risk | Example |
|------|------|---------|
| `any` | Complete type erasure | `const data: any = response;` |
| `as` (type assertion) | Lies to compiler | `const user = data as User;` |
| `@ts-ignore` | Suppresses all errors | `// @ts-ignore` |
| `@ts-expect-error` | Better, but still a hole | `// @ts-expect-error` |
| `eslint-disable` | Suppresses lint rules | `// eslint-disable-next-line` |
| `!` (non-null assertion) | Runtime error risk | `user!.name` |

### Python

| Hole | Risk | Example |
|------|------|---------|
| `type: ignore` | Suppresses type error | `x = func()  # type: ignore` |
| `Any` | Explicit any type | `def func(x: Any) -> Any:` |
| `cast()` | Lies to type checker | `cast(User, data)` |
| No annotations | Implicit any | `def func(x):` |
| `# noqa` | Suppresses all lints | `import *  # noqa` |

### Roadmap Languages

Support for additional languages is planned for future releases:

| Language | Type Safety Holes | Status |
|----------|-------------------|--------|
| **Go** | `interface{}`, `any`, type assertions, `//nolint` | Planned |
| **Java/Kotlin** | Raw types, `@SuppressWarnings`, unchecked casts, `!!` | Planned |
| **Rust** | `unsafe` blocks, `.unwrap()` | Planned |
| **C#** | `dynamic`, `as` casts, `#pragma warning disable` | Planned |

---

## The Iron Dome Defense

```
┌─────────────────────────────────────────────────────────────────────┐
│                         IRON DOME LAYERS                             │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  Layer 0: CONFIG FILE VALIDATION                                    │
│    • Validate tsconfig.json, eslint.config.js parse correctly       │
│    • If config is corrupted, all downstream layers fail-open        │
│    • Fastest check — run first, fail fast                           │
│                                                                     │
│  Layer 1: COMPILER STRICTNESS                                       │
│    • Enable strict mode (tsconfig, mypy --strict, etc.)             │
│    • Catches ~80% of issues automatically                           │
│                                                                     │
│  Layer 2: LINT RULES                                                │
│    • no-explicit-any, no-unsafe-* rules                            │
│    • Catches patterns compiler allows                               │
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
│  Layer 5: SUPPLY CHAIN SECURITY (Gap #16)                           │
│    • Detect AI-hallucinated packages BEFORE npm ci                  │
│    • Block packages < 30 days old (suspicious)                      │
│    • Block non-existent packages (true hallucinations)              │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

---

## Layer 0: Config File Validation

> **The Config Fragility Problem:** If `tsconfig.json` or `eslint.config.js` is corrupted, all downstream governance layers fail-open. TypeScript won't enforce strict mode on invalid JSON. ESLint won't enforce rules if config doesn't parse.

### Why Layer 0 Matters

```
┌─────────────────────────────────────────────────────────────────────┐
│                     CONFIG FRAGILITY RISK                            │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│   Scenario: AI accidentally corrupts tsconfig.json                  │
│        ↓                                                            │
│   TypeScript: "tsconfig invalid, using defaults"                    │
│        ↓                                                            │
│   Defaults = no strict mode = `any` allowed everywhere              │
│        ↓                                                            │
│   All Layer 1-5 checks pass (nothing to enforce!)                   │
│        ↓                                                            │
│   GOVERNANCE SILENTLY DISABLED                                      │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

### Pre-commit Hook (Layer 0)

```yaml
# .pre-commit-config.yaml
- repo: local
  hooks:
    - id: config-validation
      name: Layer 0 - Config File Validation
      entry: bash -c '
        echo "Validating config files..."
        node -e "JSON.parse(require(\"fs\").readFileSync(\"tsconfig.json\"))" || exit 1
        node -e "require(\"./eslint.config.js\")" || exit 1
        echo "✓ Config files valid"
      '
      language: system
      files: (tsconfig|eslint\.config)\.(json|js)$
      pass_filenames: false
      description: |
        Validates config files parse correctly before running heavy tools.
        If this fails, all downstream governance is compromised.
```

### Implementation Script

```bash
#!/usr/bin/env bash
# scripts/governance/validate-config.sh
# Layer 0: Run BEFORE any other governance checks

set -e

echo "═══════════════════════════════════════════════════════════"
echo "LAYER 0: Config File Validation"
echo "═══════════════════════════════════════════════════════════"

# TypeScript config
if [ -f "tsconfig.json" ]; then
  if ! node -e "JSON.parse(require('fs').readFileSync('tsconfig.json'))"; then
    echo "FATAL: tsconfig.json is invalid JSON"
    echo "All TypeScript governance is disabled until this is fixed."
    exit 1
  fi
  echo "✓ tsconfig.json valid"
fi

# ESLint config (JS format)
if [ -f "eslint.config.js" ]; then
  if ! node -e "require('./eslint.config.js')"; then
    echo "FATAL: eslint.config.js failed to load"
    echo "All ESLint governance is disabled until this is fixed."
    exit 1
  fi
  echo "✓ eslint.config.js valid"
fi

# ESLint config (JSON format)
if [ -f ".eslintrc.json" ]; then
  if ! node -e "JSON.parse(require('fs').readFileSync('.eslintrc.json'))"; then
    echo "FATAL: .eslintrc.json is invalid JSON"
    exit 1
  fi
  echo "✓ .eslintrc.json valid"
fi

# Jest config
if [ -f "jest.config.js" ]; then
  if ! node -e "require('./jest.config.js')"; then
    echo "FATAL: jest.config.js failed to load"
    exit 1
  fi
  echo "✓ jest.config.js valid"
fi

echo "═══════════════════════════════════════════════════════════"
echo "Layer 0 passed - proceeding to governance checks"
echo "═══════════════════════════════════════════════════════════"
```

### When Layer 0 Fails

```
═══════════════════════════════════════════════════════════
LAYER 0: Config File Validation
═══════════════════════════════════════════════════════════
FATAL: tsconfig.json is invalid JSON

SyntaxError: Unexpected token } in JSON at position 1423

All TypeScript governance is disabled until this is fixed.

Action: Fix the JSON syntax error before committing.
        Run: npx jsonlint tsconfig.json
═══════════════════════════════════════════════════════════
```

---

## The Ratchet Principle

### How It Works

```
Day 0: Generate baseline
  → Current codebase has 127 type-safety holes
  → Baseline: 127

Day 5: Developer adds feature
  → Feature introduces 2 new `any` types
  → Total would be: 129
  → PRE-COMMIT BLOCKED: "Ratchet violation: 129 > 127"
  → Developer fixes the types
  → Commit succeeds

Day 10: Developer refactors old code
  → Removes 5 legacy `any` types
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
│   Cannot add new `any`        Existing `any` allowed                │
│   Cannot add new `ignore`     Existing `ignore` allowed             │
│   Cannot disable more rules   Existing disables allowed             │
│                                                                     │
│   Result: Quality can only IMPROVE over time.                       │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

---

## Implementation

### Pre-commit Hook (AI-Generated)

```yaml
# .pre-commit-config.yaml
- repo: local
  hooks:
    - id: type-safety
      name: Iron Dome (Type Safety)
      entry: python scripts/governance/check-type-safety.py  # Or .js for TS projects
      language: system
      files: \.(ts|tsx|py)$
      description: |
        Enforces the Iron Dome: Type-safety holes cannot increase.
        If blocked, fix the type properly instead of suppressing.
```

### Example Script (TypeScript)

```javascript
#!/usr/bin/env node
/**
 * Iron Dome: Type Safety Enforcer
 *
 * Counts type-safety holes and blocks commits that increase the count.
 */
const fs = require('fs');
const path = require('path');
const { execSync } = require('child_process');

const BASELINE_PATH = '.memory-layer/baselines/type-safety.json';

// Patterns to detect (TypeScript)
const PATTERNS = [
  { name: 'any', pattern: /:\s*any\b/g, weight: 1 },
  { name: 'any (parameter)', pattern: /\(\s*\w+\s*:\s*any\b/g, weight: 1 },
  { name: 'as any', pattern: /as\s+any\b/g, weight: 1 },
  { name: '@ts-ignore', pattern: /@ts-ignore/g, weight: 2 },
  { name: '@ts-expect-error', pattern: /@ts-expect-error/g, weight: 1 },
  { name: 'eslint-disable', pattern: /eslint-disable/g, weight: 1 },
  { name: 'non-null assertion', pattern: /!\./g, weight: 0.5 },
];

function countHoles(filePath) {
  const content = fs.readFileSync(filePath, 'utf8');
  let total = 0;
  const breakdown = {};

  for (const { name, pattern, weight } of PATTERNS) {
    const matches = content.match(pattern) || [];
    const count = matches.length;
    if (count > 0) {
      breakdown[name] = count;
      total += count * weight;
    }
  }

  return { total, breakdown };
}

function getStagedFiles() {
  try {
    const output = execSync('git diff --cached --name-only --diff-filter=ACMR', {
      encoding: 'utf8',
    });
    return output.split('\n').filter(f => /\.(ts|tsx)$/.test(f));
  } catch {
    return [];
  }
}

function loadBaseline() {
  if (!fs.existsSync(BASELINE_PATH)) {
    return { totalHoles: 0, byFile: {} };
  }
  return JSON.parse(fs.readFileSync(BASELINE_PATH, 'utf8'));
}

function saveBaseline(data) {
  const dir = path.dirname(BASELINE_PATH);
  if (!fs.existsSync(dir)) {
    fs.mkdirSync(dir, { recursive: true });
  }
  fs.writeFileSync(BASELINE_PATH, JSON.stringify(data, null, 2));
}

// Main
const files = process.argv.slice(2).length > 0
  ? process.argv.slice(2)
  : getStagedFiles();

const baseline = loadBaseline();
let currentTotal = 0;
const violations = [];

for (const file of files) {
  if (!fs.existsSync(file)) continue;

  const { total, breakdown } = countHoles(file);
  currentTotal += total;

  const baselineForFile = baseline.byFile[file]?.total || 0;

  if (total > baselineForFile) {
    violations.push({
      file,
      current: total,
      baseline: baselineForFile,
      breakdown,
    });
  }
}

if (violations.length > 0) {
  console.log('='.repeat(60));
  console.log('IRON DOME: Type Safety Violations');
  console.log('='.repeat(60));
  console.log();

  for (const v of violations) {
    console.log(`TYPE-SAFETY: ${v.file}`);
    console.log(`  Current: ${v.current} holes, Baseline: ${v.baseline} holes`);
    console.log(`  Breakdown: ${JSON.stringify(v.breakdown)}`);
    console.log(`  Action: Fix the type properly instead of suppressing.`);
    console.log();
  }

  console.log('See: docs/production-readiness-kit/IRON-DOME.md');
  console.log();
  console.log('If this is a false positive, add IRON_DOME_EXEMPT comment.');
  process.exit(1);
}

// Success - update baseline if improved
if (currentTotal < baseline.totalHoles) {
  console.log(`Iron Dome: Improved! ${baseline.totalHoles} → ${currentTotal} holes`);
  baseline.totalHoles = currentTotal;
  saveBaseline(baseline);
}

process.exit(0);
```

### Example Script (Python)

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

BASELINE_PATH = Path('.memory-layer/baselines/type-safety.json')

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
        return {'totalHoles': 0, 'byFile': {}}
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

        baseline_for_file = baseline.get('byFile', {}).get(file, {}).get('total', 0)

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

        print('See: docs/production-readiness-kit/IRON-DOME.md')
        print()
        print('If this is a false positive, add IRON_DOME_EXEMPT comment.')
        sys.exit(1)

    # Success - update baseline if improved
    if current_total < baseline.get('totalHoles', 0):
        print(f"Iron Dome: Improved! {baseline['totalHoles']} → {current_total} holes")
        baseline['totalHoles'] = current_total
        save_baseline(baseline)

    sys.exit(0)


if __name__ == '__main__':
    main()
```

---

## Strict Mode Configuration

### TypeScript (tsconfig.json)

```json
{
  "compilerOptions": {
    "strict": true,
    "noImplicitAny": true,
    "strictNullChecks": true,
    "strictFunctionTypes": true,
    "strictBindCallApply": true,
    "strictPropertyInitialization": true,
    "noImplicitThis": true,
    "useUnknownInCatchVariables": true,
    "alwaysStrict": true,
    "noUncheckedIndexedAccess": true,
    "noImplicitOverride": true,
    "noPropertyAccessFromIndexSignature": true
  }
}
```

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
```

### ESLint (TypeScript rules)

```json
{
  "rules": {
    "@typescript-eslint/no-explicit-any": "error",
    "@typescript-eslint/no-unsafe-assignment": "error",
    "@typescript-eslint/no-unsafe-member-access": "error",
    "@typescript-eslint/no-unsafe-call": "error",
    "@typescript-eslint/no-unsafe-return": "error",
    "@typescript-eslint/no-unsafe-argument": "error",
    "@typescript-eslint/no-non-null-assertion": "warn"
  }
}
```

---

## Exceptions

### When Type Holes Are Acceptable

1. **Third-party library without types**
   ```typescript
   // IRON_DOME_EXEMPT: Legacy library without @types
   const result = legacyLib.process(data) as unknown as Result;
   ```

2. **Test mocks** (limited scope)
   ```typescript
   // IRON_DOME_EXEMPT: Test mock, not production code
   const mockVscode = { window: {} } as any;
   ```

   > ⚠️ **The `as any` Trap in Tests:** Even in tests, `as any` defeats TypeScript protection. If your mock doesn't match the real interface, tests pass but production breaks. Prefer type-safe mock helpers:

   ```typescript
   // DANGEROUS: defeats TypeScript protection
   (vscode.window as any).showQuickPick = jest.fn();
   // If showQuickPick signature changes, test still passes, production breaks

   // BETTER: Type-safe mock helper
   import { mockQuickPick } from '../mocks/helpers';
   mockQuickPick(selectedItem);  // Compiler enforces correct signature

   // BEST: Mock implements real interface (Mock Integrity pattern)
   // See TDD-GUIDE.md → Mock Integrity Testing
   const _window: typeof vscode.window = mockVscode.window;  // Compile error if mismatch
   ```

3. **JSON parsing** (runtime validation required anyway)
   ```typescript
   // IRON_DOME_EXEMPT: Runtime validation via zod schema
   const data = JSON.parse(response) as unknown;
   const user = UserSchema.parse(data);  // Zod validates
   ```

### Marking Exceptions

```typescript
// Single line
const x = data as any;  // IRON_DOME_EXEMPT: reason

// Block
/* IRON_DOME_EXEMPT_START: Legacy integration layer */
interface LegacyData {
  payload: any;
  metadata: any;
}
/* IRON_DOME_EXEMPT_END */
```

---

## Baseline Generation

### Initial Setup

```bash
# Generate baseline for entire codebase
python scripts/governance/check-type-safety.py --generate-baseline

# Output:
# Scanning 342 files...
# Found 127 type-safety holes
# Baseline saved to .memory-layer/baselines/type-safety.json
```

### Baseline File Format

```json
{
  "generated": "2024-01-15T10:30:00Z",
  "totalHoles": 127,
  "byFile": {
    "src/services/OrderService.ts": {
      "total": 5,
      "breakdown": {
        "any": 3,
        "@ts-ignore": 2
      }
    },
    "src/utils/helpers.ts": {
      "total": 2,
      "breakdown": {
        "as any": 2
      }
    }
  },
  "exemptions": [
    {
      "file": "src/integrations/legacy.ts",
      "reason": "Third-party integration without types",
      "approved": "2024-01-10"
    }
  ]
}
```

---

## The Iron Dome Dashboard (Optional)

### CI/CD Report

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
  1. src/services/OrderService.ts    12 holes
  2. src/api/handlers.ts              8 holes
  3. src/utils/legacy.ts              7 holes

Recent Improvements:
  - src/models/User.ts: 5 → 0 holes (fixed!)
  - src/services/Auth.ts: 3 → 1 holes

═══════════════════════════════════════════════════════════════
```

---

## Summary

| Concept | Description |
|---------|-------------|
| **Iron Dome** | Intercept type-safety violations before they land |
| **Layer 0** | Config file validation — prevent governance fail-open |
| **Type Holes** | `any`, `ignore`, `disable` — breaches in type safety |
| **`as any` Trap** | Even test mocks should use type-safe helpers |
| **Ratchet** | Count can only go down, never up |
| **Baseline** | Starting point for existing codebases |
| **Exemptions** | Documented exceptions with reason |

---

## Supply Chain Security (Gap #16)

> **The Supply Chain Problem:** AI coders hallucinate package names ~5-10% of the time. Attackers register these names on npm with malware. If you install them, postinstall scripts execute malware.

### The Attack Vector

```
┌─────────────────────────────────────────────────────────────────────┐
│                    SUPPLY CHAIN ATTACK FLOW                          │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│   1. AI suggests: `import { helper } from 'react-utils-helper'`     │
│        ↓                                                            │
│   2. Package doesn't exist (AI hallucination)                       │
│        ↓                                                            │
│   3. Attacker registers 'react-utils-helper' on npm                 │
│        ↓                                                            │
│   4. Developer runs `npm install`                                   │
│        ↓                                                            │
│   5. postinstall script executes malware                            │
│        ↓                                                            │
│   COMPROMISED                                                       │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

### Defense Layers

| Layer | What It Does | When It Runs |
|-------|--------------|--------------|
| **Hallucination Detector** | Blocks non-existent or very new packages | Pre-commit, CI (before npm ci) |
| **npm ci** | Fails if lockfile doesn't match package.json | CI |
| **Package Change Detection** | Flags PRs that modify package.json | CI |
| **npm audit** | Catches known vulnerabilities | CI |

### Pre-commit Hook

```yaml
# .pre-commit-config-ts.yaml (Layer 10)
- id: supply-chain-security
  name: Supply Chain Security (Hallucination Detector)
  entry: bash -c 'cd extension && node scripts/governance/check-hallucinations.js'
  language: system
  files: package\.json$
```

### Detection Criteria

The hallucination detector blocks packages that:

1. **Don't exist** in npm registry (true hallucination)
2. **Are < 30 days old** (attackers register hallucinated names quickly)
3. **Have < 100 weekly downloads** (ghosts have no real users) — *future enhancement*

### Exemptions

Add legitimate packages to `.supply-chain-exemptions.json`:

```json
[
  {
    "package": "my-internal-package",
    "reason": "Internal package published to private registry",
    "addedBy": "developer-name",
    "date": "2025-01-15"
  }
]
```

### CI Configuration

```yaml
# .github/workflows/guardrails.yml
- name: "Iron Dome: Hallucination Detector (No npm ci)"
  working-directory: extension
  run: node scripts/governance/check-hallucinations.js
```

> **Critical:** The hallucination detector runs BEFORE `npm ci` to prevent postinstall script execution.

---

## Related

- [SCHEMA-VALIDATION.md](./SCHEMA-VALIDATION.md) — Runtime type safety (Zod validation at boundaries)
- [RISING-TIDE.md](./RISING-TIDE.md) — Mock Tax philosophy
- [RATCHET-STRATEGY.md](./RATCHET-STRATEGY.md) — Baseline improvement philosophy
- [TDD-GUIDE.md](./TDD-GUIDE.md) — Test-driven development practices

> **Note:** Iron Dome guards compile-time type safety (your source code). For runtime type safety at system boundaries (API responses, webhooks, config files), see [SCHEMA-VALIDATION.md](./SCHEMA-VALIDATION.md).

---

*Part of the Mault Production-Readiness Kit*
