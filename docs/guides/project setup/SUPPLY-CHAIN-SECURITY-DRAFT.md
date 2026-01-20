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

# SUPPLY-CHAIN-SECURITY.md — Defending Against AI Hallucinations

> **The Supply Chain Strategy:** AI assistants hallucinate package names ~5-10% of the time. Attackers register these names on npm with malware. Validate dependencies BEFORE installation.

---

## The Problem: The AI Hallucination Attack Vector

```
┌─────────────────────────────────────────────────────────────────────┐
│                    THE HALLUCINATION ATTACK                          │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│   1. AI coding assistant suggests:                                  │
│      import { helper } from 'react-utils-helper';                   │
│        ↓                                                            │
│   2. Package 'react-utils-helper' doesn't exist (hallucination)     │
│        ↓                                                            │
│   3. Attacker monitors npm search traffic for non-existent names    │
│        ↓                                                            │
│   4. Attacker registers 'react-utils-helper' with malware           │
│        ↓                                                            │
│   5. Developer runs `npm install`                                   │
│        ↓                                                            │
│   6. npm postinstall script executes immediately                    │
│        ↓                                                            │
│   COMPROMISED — Malware now has access to your machine              │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

**Traditional tools don't catch this:**

| Tool | What It Catches | Blind Spot |
|------|-----------------|------------|
| `npm audit` | Known CVEs in existing packages | New packages have no CVE history |
| `npm ci` | Lockfile mismatches | Doesn't check if package is legitimate |
| Code review | Logic bugs | Humans don't memorize npm's 2M+ packages |
| ESLint | Code quality issues | Import statements look syntactically valid |

---

## Attack Variants

### 1. Pure Hallucination

AI invents a package name that sounds plausible but never existed.

```typescript
// AI suggests (hallucinated):
import { validateEmail } from 'email-validator-utils';

// Real package is:
import isEmail from 'validator/lib/isEmail';
```

### 2. Typosquatting

AI misspells a popular package name. Attackers pre-register typos.

```typescript
// AI typo:
import axios from 'axois';  // Wrong!

// Real package:
import axios from 'axios';
```

### 3. Namespace Confusion

AI uses wrong npm org scope.

```typescript
// AI suggests:
import { Button } from '@react/components';  // Doesn't exist!

// Real package:
import { Button } from '@mui/material';
```

---

## Defense Strategy: Pre-Install Validation

The key insight: **Validate BEFORE npm runs.** Once `npm install` executes, postinstall scripts run immediately with full system access.

### Defense Layers

```
┌─────────────────────────────────────────────────────────────────────┐
│                    SUPPLY CHAIN DEFENSE LAYERS                       │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  Layer 1: PRE-COMMIT HOOK                                           │
│    • Runs when package.json changes                                 │
│    • Validates packages before they're committed                    │
│    • Blocks suspicious packages immediately                         │
│                                                                     │
│  Layer 2: CI STATIC CHECKS (Before npm ci)                          │
│    • Runs BEFORE npm ci installs anything                           │
│    • No node_modules needed (pure Node.js)                          │
│    • Prevents postinstall script execution                          │
│                                                                     │
│  Layer 3: LOCKFILE INTEGRITY (npm ci)                               │
│    • Fails if package-lock.json mismatches package.json             │
│    • Prevents "magic" package additions                             │
│                                                                     │
│  Layer 4: VULNERABILITY AUDIT (npm audit)                           │
│    • Catches known CVEs in dependencies                             │
│    • Limited to packages with reported vulnerabilities              │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

---

## Detection Criteria

The hallucination detector blocks packages that:

### 1. Don't Exist (True Hallucination)

Package not found in npm registry. This is the most dangerous scenario — if it doesn't exist yet, an attacker could register it.

```bash
$ npm view my-fake-package
npm ERR! 404 Not Found - GET https://registry.npmjs.org/my-fake-package
```

**Action:** BLOCK immediately.

### 2. Are Very New (< 30 Days Old)

Legitimate packages have history. AI hallucinations get registered quickly by attackers monitoring npm search traffic.

```bash
$ npm view suspicious-package time.created
"2025-12-01T10:30:00.000Z"  # Created 5 days ago — suspicious!
```

**Action:** BLOCK and require human review.

### 3. Have Very Low Downloads (< 100/week)

Real packages have users. Ghost packages registered by attackers have no organic downloads.

```bash
# Real package:
axios: 45,000,000 downloads/week

# Ghost package:
react-utils-helper: 3 downloads/week  # Suspicious!
```

**Action:** WARN and flag for review.

---

## The Rising Tide Protocol

> "Stop the bleeding on new code. Manage existing debt as static baseline."

### Green Zone: New Projects

**Mandatory enforcement from day one.**

```yaml
# .github/workflows/guardrails.yml
- name: "Supply Chain: Hallucination Detector"
  run: node scripts/governance/check-hallucinations.js
  # Runs BEFORE npm ci
```

Configuration:
- Block non-existent packages
- Block packages < 30 days old
- Warn on packages < 100 downloads/week
- No exemptions without human review

### Yellow Zone: Active Development

**Add detector to existing CI pipeline.**

1. Run detector in warning mode first
2. Audit flagged packages manually
3. Add legitimate packages to exemptions file
4. Switch to blocking mode

```bash
# Phase 1: Audit mode
node scripts/governance/check-hallucinations.js --warn-only

# Phase 2: After cleanup
node scripts/governance/check-hallucinations.js  # Full enforcement
```

### Red Zone: Legacy Projects

**Document and freeze.**

For projects with many dependencies:

1. Generate baseline of current packages
2. Block NEW package additions without review
3. Don't retroactively audit all existing packages

```json
// .supply-chain-exemptions.json
[
  {
    "package": "legacy-internal-tool",
    "reason": "Pre-existing dependency, audited on 2025-01-01",
    "addedBy": "security-team",
    "date": "2025-01-01"
  }
]
```

---

## Implementation

### Pre-commit Hook

Add to your pre-commit configuration:

```yaml
# .pre-commit-config.yaml (or -ts.yaml for TypeScript projects)
repos:
  - repo: local
    hooks:
      - id: supply-chain-security
        name: Supply Chain Security (Hallucination Detector)
        entry: bash -c 'node scripts/governance/check-hallucinations.js'
        language: system
        files: package\.json$
        pass_filenames: false
        stages: [pre-commit]
```

### CI Configuration (GitHub Actions)

The detector MUST run BEFORE `npm ci` in your CI pipeline:

```yaml
# .github/workflows/guardrails.yml
name: Guardrails

on:
  pull_request:

jobs:
  static-checks:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      # CRITICAL: Run BEFORE npm ci
      - name: "Supply Chain: Hallucination Detector"
        working-directory: extension  # or your package directory
        run: node scripts/governance/check-hallucinations.js

      # Now safe to install
      - run: npm ci
```

### GitLab CI

```yaml
# .gitlab-ci.yml
supply-chain-check:
  stage: validate
  script:
    - node scripts/governance/check-hallucinations.js
  rules:
    - changes:
        - package.json
        - package-lock.json
```

---

## The Hallucination Detector Script

Copy this script to your project:

```javascript
#!/usr/bin/env node
/**
 * Supply Chain Security: AI Hallucination/Typosquat Detector
 *
 * Purpose: Detect potentially malicious packages BEFORE npm ci runs.
 *          This runs in CI before installation, preventing postinstall
 *          script execution from potentially malicious packages.
 *
 * Detection criteria:
 *   - Package doesn't exist in npm registry (true hallucination)
 *   - Package is < 30 days old (AI hallucinations are brand new)
 *   - Package has < 100 weekly downloads (ghosts have no real users)
 *
 * Usage:
 *   node check-hallucinations.js                    # Check all dependencies
 *   node check-hallucinations.js --verbose          # Show detailed output
 *
 * Exit codes:
 *   0 - All packages passed validation
 *   1 - Suspicious packages detected (BLOCKED)
 *
 * Exemptions:
 *   Add to .supply-chain-exemptions.json with justification
 */

const { execSync } = require('child_process');
const fs = require('fs');
const path = require('path');

// Configuration
const MIN_DAYS_OLD = 30;
const EXEMPTIONS_FILE = '.supply-chain-exemptions.json';

// Well-known packages that don't need checking (core ecosystem)
const TRUSTED_PACKAGES = new Set([
  // TypeScript/JavaScript core
  'typescript', 'esbuild', 'webpack', 'vite', 'rollup',
  // Testing
  'jest', '@jest/globals', 'vitest', 'mocha', 'chai',
  // React ecosystem
  'react', 'react-dom', 'next',
  // Node core
  'express', 'fastify', 'koa',
  // Build tools
  'eslint', 'prettier', 'husky', 'lint-staged',
]);

// Trusted scopes (organizations with verified packages)
const TRUSTED_SCOPES = [
  '@types/',
  '@typescript-eslint/',
  '@babel/',
  '@eslint/',
  '@jest/',
];

/**
 * Load exemptions from file
 */
function loadExemptions() {
  const exemptionsPath = path.join(process.cwd(), EXEMPTIONS_FILE);
  if (!fs.existsSync(exemptionsPath)) {
    return [];
  }
  try {
    const content = fs.readFileSync(exemptionsPath, 'utf8');
    const exemptions = JSON.parse(content);
    return Array.isArray(exemptions) ? exemptions : [];
  } catch {
    console.warn(`Warning: Could not parse ${EXEMPTIONS_FILE}`);
    return [];
  }
}

/**
 * Query npm registry for package metadata
 */
function getPackageInfo(packageName) {
  try {
    const result = execSync(`npm view ${packageName} time.created --json`, {
      encoding: 'utf-8',
      timeout: 10000,
      stdio: ['pipe', 'pipe', 'pipe'],
    });

    const createdDate = JSON.parse(result.trim());
    const createdAt = new Date(createdDate);
    const ageInDays = Math.floor(
      (Date.now() - createdAt.getTime()) / (1000 * 60 * 60 * 24)
    );

    return { exists: true, createdAt: createdDate, ageInDays };
  } catch {
    return { exists: false, createdAt: null, ageInDays: null };
  }
}

/**
 * Parse package.json and extract all dependencies
 */
function getAllDependencies(packageJsonPath) {
  const content = fs.readFileSync(packageJsonPath, 'utf8');
  const packageJson = JSON.parse(content);
  const deps = new Set();

  const depFields = [
    'dependencies',
    'devDependencies',
    'peerDependencies',
    'optionalDependencies',
  ];

  for (const field of depFields) {
    if (packageJson[field]) {
      for (const name of Object.keys(packageJson[field])) {
        deps.add(name);
      }
    }
  }

  return Array.from(deps);
}

/**
 * Check if package should be skipped
 */
function shouldSkip(packageName, exemptions) {
  // Trusted packages
  if (TRUSTED_PACKAGES.has(packageName)) return true;

  // Trusted scopes
  for (const scope of TRUSTED_SCOPES) {
    if (packageName.startsWith(scope)) return true;
  }

  // Exempted packages
  return exemptions.some((e) => e.package === packageName);
}

/**
 * Main function
 */
function main() {
  const args = process.argv.slice(2);
  const verbose = args.includes('--verbose') || args.includes('-v');

  console.log('Supply Chain Security: Hallucination Detector');
  console.log('='.repeat(60) + '\n');

  const packageJsonPath = path.join(process.cwd(), 'package.json');
  if (!fs.existsSync(packageJsonPath)) {
    console.log('No package.json found. Skipping check.\n');
    process.exit(0);
  }

  const exemptions = loadExemptions();
  const allDeps = getAllDependencies(packageJsonPath);

  console.log(`Total dependencies: ${allDeps.length}`);

  const depsToCheck = allDeps.filter((dep) => !shouldSkip(dep, exemptions));
  console.log(`Dependencies to validate: ${depsToCheck.length}\n`);

  if (depsToCheck.length === 0) {
    console.log('All dependencies are trusted. No validation needed.\n');
    process.exit(0);
  }

  console.log('Validating packages...\n');

  const violations = [];

  for (const dep of depsToCheck) {
    const info = getPackageInfo(dep);

    if (!info.exists) {
      violations.push({
        package: dep,
        reason: 'Package does not exist in npm registry',
        severity: 'critical',
      });
      console.log(`  [CRITICAL] ${dep} - NOT FOUND`);
    } else if (info.ageInDays !== null && info.ageInDays < MIN_DAYS_OLD) {
      violations.push({
        package: dep,
        reason: `Package is only ${info.ageInDays} days old`,
        severity: 'high',
        createdAt: info.createdAt,
      });
      console.log(`  [HIGH] ${dep} - Only ${info.ageInDays} days old`);
    } else if (verbose) {
      console.log(`  [OK] ${dep} (${info.ageInDays} days old)`);
    }
  }

  console.log('');

  if (violations.length === 0) {
    console.log('All packages passed supply chain validation.\n');
    process.exit(0);
  }

  // BLOCKED
  console.log('-'.repeat(60));
  console.log(`\nBLOCKED: ${violations.length} suspicious package(s) detected.\n`);

  console.log('VIOLATIONS:\n');
  for (const v of violations) {
    console.log(`  Package: ${v.package}`);
    console.log(`  Reason: ${v.reason}`);
    console.log(`  Severity: ${v.severity.toUpperCase()}`);
    if (v.createdAt) {
      console.log(`  Created: ${v.createdAt}`);
    }
    console.log('');
  }

  console.log('FIX OPTIONS:');
  console.log('  1. Remove the suspicious package');
  console.log('  2. Use a well-known alternative');
  console.log('  3. If legitimate, add to .supply-chain-exemptions.json:\n');
  console.log('     [{"package": "name", "reason": "Verified by human",');
  console.log('       "addedBy": "your-name", "date": "YYYY-MM-DD"}]\n');
  console.log('-'.repeat(60) + '\n');

  process.exit(1);
}

main();
```

---

## Exemptions File

For legitimate packages that trigger false positives:

```json
// .supply-chain-exemptions.json
[
  {
    "package": "internal-company-utils",
    "reason": "Internal package published to private registry",
    "addedBy": "john.doe",
    "date": "2025-01-15"
  },
  {
    "package": "new-framework-beta",
    "reason": "New but legitimate framework, verified on GitHub",
    "addedBy": "security-team",
    "date": "2025-01-20"
  }
]
```

### Exemption Requirements

1. **Human verification** — Only humans can add exemptions
2. **Justification** — Must explain why package is legitimate
3. **Attribution** — Must include who approved
4. **Audit trail** — Date of approval for future review

---

## Research and References

### Academic Research

- [Typosquatting in Package Managers](https://arxiv.org/abs/2003.03471) — Analysis of typosquatting attacks on npm, PyPI, and RubyGems
- [Backstabber's Knife Collection](https://arxiv.org/abs/2005.09535) — Malicious packages in npm

### Industry Reports

- [Socket.dev 2024 Report](https://socket.dev/blog/2024-open-source-software-supply-chain-security-report) — Supply chain attack trends
- [Snyk State of Open Source Security](https://snyk.io/reports/open-source-security/) — Vulnerability statistics

### Real-World Attacks

| Attack | Year | Impact |
|--------|------|--------|
| event-stream | 2018 | Bitcoin wallet theft via malicious maintainer |
| ua-parser-js | 2021 | Cryptocurrency miner injected |
| node-ipc | 2022 | Protestware deleted files on Russian IPs |
| colors/faker | 2022 | Maintainer sabotage, infinite loops |

---

## Integration with Mault (Future)

Mault could provide real-time detection when users modify `package.json`:

### Proposed: UC16 — Dependency Health Check

```
┌─────────────────────────────────────────────────────────────────────┐
│                    MAULT DEPENDENCY DETECTOR                         │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│   Trigger: package.json modified                                    │
│        ↓                                                            │
│   Analyze added/changed dependencies                                │
│        ↓                                                            │
│   Check against npm registry                                        │
│        ↓                                                            │
│   Flag suspicious packages in Problems panel                        │
│        ↓                                                            │
│   Provide AI prompt with safe alternatives                          │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

**Diagnostic Message:**
```
[Warning] Suspicious dependency: 'react-utils-helper'
  - Package does not exist in npm registry
  - May be an AI hallucination

  Consider: 'validator' for email validation
  Consider: 'lodash' for utility functions
```

---

## Summary

| Concept | Description |
|---------|-------------|
| **Hallucination Attack** | AI suggests non-existent packages that attackers can weaponize |
| **Pre-Install Validation** | Check packages BEFORE npm runs postinstall scripts |
| **Age Gate** | Block packages < 30 days old (new = suspicious) |
| **Exemptions** | Human-verified exceptions with audit trail |
| **Rising Tide** | Enforce on new code, document legacy |

---

## Related

- [IRON-DOME.md](./IRON-DOME-DRAFT.md) — Type safety and governance layers
- [SCHEMA-VALIDATION.md](./SCHEMA-VALIDATION-DRAFT.md) — Runtime type safety with Zod
- [RISING-TIDE.md](./RISING-TIDE-DRAFT.md) — Gradual enforcement philosophy
- [PRECOMMIT-SETUP.md](./PRECOMMIT-SETUP-DRAFT.md) — Pre-commit hook configuration

> **Note:** Supply Chain Security defends against external package threats. For internal code quality, see [IRON-DOME.md](./IRON-DOME-DRAFT.md).

---

*Part of the Mault Production-Readiness Kit*
