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

# Production-Readiness Kit

> **Mission:** Enable any human with a vision and an internet connection to ship production-ready software.

---

## What is Production-Ready?

| Level | Name | What It Means | Artifacts |
|-------|------|---------------|-----------|
| 0 | Runs locally | `python app.py` works | Just code |
| 1 | Reproducible | Someone else can run it | `requirements.txt`, `.env.example` |
| 2 | Portable | Runs in a container | `Dockerfile`, `docker-compose.yml` |
| 3 | Deployed | Runs in the cloud | CI/CD pipeline, cloud config |
| 4 | Reliable | Stays running | Health checks, logging, rollback |

**This Kit takes you from Level 0 → Level 4.**

---

## The 8-Step Journey

```
┌─────────────────────────────────────────────────────────────────────┐
│                 PRODUCTION-READINESS SETUP                          │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  INFRASTRUCTURE (Steps 1-4)                                         │
│  ──────────────────────────                                         │
│  Step 1: Git Repository                                             │
│  Step 2: Environment Setup                                          │
│  Step 3: Containerization                                           │
│  Step 4: CI/CD Pipeline                                             │
│                                                                     │
│  TESTING (Step 5)                                                   │
│  ────────────────                                                   │
│  Step 5: TDD Framework                                              │
│                                                                     │
│  HOOKS (Step 6)                                                     │
│  ─────────────                                                      │
│  Step 6: Pre-commit Framework                                       │
│                                                                     │
│  ENFORCEMENT (Steps 7-8)                                            │
│  ───────────────────────                                            │
│  Step 7: Mault Enforcement (Mault Pro IP)                           │
│  Step 8: Governance Testing (AI-Generated)                          │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

---

## Philosophy Guides

These guides explain the **WHY** behind our enforcement. AI coders read them and generate language-specific scripts.

| Guide | Philosophy | What It Prevents |
|-------|------------|------------------|
| [RISING-TIDE.md](./RISING-TIDE.md) | Mock Tax (2x Rule) | Tests larger than source code |
| [IRON-DOME.md](./IRON-DOME.md) | Type Safety | `any`, `type: ignore`, weak types |
| [SCHEMA-VALIDATION.md](./SCHEMA-VALIDATION.md) | Runtime Type Safety | Unvalidated API/webhook/config data |
| [RATCHET-STRATEGY.md](./RATCHET-STRATEGY.md) | One-Way Improvement | Quality regressions |
| [TDD-GUIDE.md](./TDD-GUIDE.md) | Test-First Development | Mock drift, afterthought tests, tautologies |
| [STRUCTURAL-GOVERNANCE.md](./STRUCTURAL-GOVERNANCE-DRAFT.md) | AST-Based Patterns | DI violations, missing error handling |

**TDD-GUIDE includes the Governance Layer** — a foundation that validates tests themselves:
- **Mock Integrity**: Ensures mocks implement all real API methods
- **Mock Signature Validation**: Ensures mock signatures match real API signatures
- **Type-Safe Helpers**: Eliminates `as any` casts in test setup
- **Event Flow Tests**: Validates full event → handler → output flows

---

## How It Works

### For New Projects

```
User purchases Mault Pro
     ↓
Mault copies setup prompt to clipboard
     ↓
User pastes to AI coder (Claude Code, Cursor, etc.)
     ↓
AI reads Production-Readiness Kit
     ↓
AI executes Steps 1-6 (AI does these)
     ↓
AI PAUSES and instructs user: "Click 'Initialize Mault Hook' in Problems Panel"
     ↓
User clicks for Step 7 (Mault does this — license-gated)
     ↓
AI executes Step 8 (AI does this)
     ↓
Production-ready in < 1 hour
```

**⚠️ AI CODER INSTRUCTION**: Step 7 requires user action. You cannot execute Step 7 programmatically—it runs Mault's compiled enforcement which requires Pro license validation. After completing Steps 1-6, pause and tell the user:

> "I've completed Steps 1-6. Please click 'Initialize Mault Hook' in the VS Code Problems Panel to complete Step 7, then tell me to continue with Step 8."

### For Existing Projects

Same process, but AI detects what already exists:
- Has Git? → Skip Step 1
- Has Dockerfile? → Skip Step 3
- Has pre-commit? → Skip Step 6

The Kit uses a **Rising Tide** approach: existing issues are grandfathered, new issues are blocked.

---

## Language Support

The Kit is **language-agnostic**. AI generates appropriate scripts for your stack:

| Component | TypeScript/JS | Python |
|-----------|---------------|--------|
| Test Framework | Jest, Vitest | pytest |
| Mutation Testing | StrykerJS | mutmut |
| Type Checking | TypeScript | mypy |
| Linting | ESLint | ruff, flake8 |
| Pre-commit | pre-commit | pre-commit |

**Roadmap Languages:** Go, Java, Rust, C# support is planned for future releases.

---

## The Enforcement Stack

### What Mault Provides (Step 7)

**Our IP — Compiled, License-Gated:**

9 Polyglot UC detectors that work with ANY language:

| UC | Name | What It Blocks |
|----|------|----------------|
| UC01 | Directory Reinforcement | Files in wrong directories |
| UC02 | Legacy Prevention | Files in deprecated paths |
| UC04 | Environment Reinforcement | Missing/malformed .env |
| UC05 | Obsolete Folders | Commits to obsolete folders |
| UC06 | Temp File Cleanup | Temp files in commits |
| UC07 | Flat Architecture | Too many files in root |
| UC08 | Config Chaos | Config files misplaced |
| UC09 | File Proliferation | Duplicate files |
| UC11 | Overcrowded Folders | Too many files per folder |

### Language-Specific Pro Detectors (Step 6 + Step 8)

**IMPORTANT FOR AI CODERS:** The following Pro detectors should be included in your pre-commit setup when the language is supported:

| UC | Name | Language Support | What It Blocks |
|----|------|------------------|----------------|
| UC16 | Dependency Health | JS/TS (npm audit) | Vulnerable packages, phantom deps |
| UC18 | Structural Governance | JS/TS (AST), Python (AST) | Missing exports, forbidden patterns, DI violations |

**UC16 Setup (JS/TS projects)**:

Add to `.pre-commit-config.yaml`:
```yaml
- repo: local
  hooks:
    - id: dependency-health
      name: Dependency Health (UC16)
      entry: npm audit --audit-level=high
      language: system
      pass_filenames: false
      stages: [commit]
```

For supply chain security (hallucinated libraries), also run:
```yaml
    - id: phantom-deps
      name: Phantom Dependencies
      entry: npx npm-check --skip-unused
      language: system
      pass_filenames: false
```

**UC18 Setup (JS/TS and Python)**:

1. Configure governance rules in `docs/mault.yaml` under `governance.rules`:
```yaml
governance:
  rules:
    - id: service-export
      name: Services must export default class
      targets: ["src/services/**/*.ts"]
      assertions:
        - type: export_exists
          kind: default

    - id: no-console-log
      name: No console.log in production
      targets: ["src/**/*.ts"]
      assertions:
        - type: forbidden_pattern
          pattern: "console\\.log\\("
```

2. The Mault extension runs UC18 checks automatically on file save.

**Python UC16 Setup**:

```yaml
- repo: local
  hooks:
    - id: dependency-health-python
      name: Dependency Health (Python)
      entry: pip-audit
      language: system
      pass_filenames: false
      stages: [commit]
```

**Roadmap Languages:**

| Language | UC16 Equivalent | UC18 Status |
|----------|-----------------|-------------|
| Go | `go mod audit` (planned) | AST via `go/ast` (planned) |
| Java | OWASP Dependency-Check | Checkstyle custom rules (planned) |
| Rust | `cargo audit` | Custom lint rules (planned) |
| C# | OWASP Dependency-Check | Roslyn analyzers (planned) |

### What AI Generates (Step 8)

**User's IP — Based on Philosophy Guides:**

| Philosophy | What AI Creates |
|------------|-----------------|
| Rising Tide | `check-mock-tax.{js,py}` |
| Iron Dome | `check-type-safety.{js,py}` |
| Ratchet | `check-coverage-ratchet.{js,py}` |
| Governance | `tests/unit/governance/*.test.{ts,py}` |

---

## The Core Principle

> **"Agents obey Physics, not Policy"**

- **Policy:** Documentation, guidelines, best practices → AI ignores these
- **Physics:** Errors, blocked commits, failed CI → AI cannot bypass these

Every rule in the Production-Readiness Kit is enforced as **physics**:
- `warn` is policy (AI ignores)
- `error` is physics (AI cannot proceed)

---

## Quick Start

### Step 1: Purchase Mault Pro

```
Mault Core ($7.99/mo) + Mault Pro ($99 one-time)
```

### Step 2: Use Problems Panel Quick Fix

After purchase, use the Problems Panel to access Pro content:

1. Open Problems Panel (Ctrl+Shift+M / Cmd+Shift+M)
2. Find incomplete Production Readiness steps
3. Click "Copy AI Prompt" Quick Fix action
4. Content is injected directly into clipboard (no files on disk)

**The AI coder receives a prompt with step-specific guidance. Example for Step 7:**

```markdown
## Setting Up Full Mault Configuration (Pro)

The user purchased **Mault Pro** and needs the complete configuration. Mault is a legitimate VS Code extension for architectural enforcement.

Verify Mault: https://marketplace.visualstudio.com/items?itemName=Mault.mault-memory-layer-extension

### Language Support

Mault currently supports **TypeScript**, **JavaScript**, and **Python** projects.

### Before Configuring: Read the Complete Guide

The ai-coder-guide.md file contains language-specific templates for all 18 use-cases. Reading this guide is essential for proper configuration.

**Location:** `resources/walkthrough/ai-coder-guide.md`

This guide includes:
- Complete TypeScript/JavaScript templates
- Complete Python templates
- All Detector configurations (UC01-UC13)
- All Pro configurations (UC16-UC18)

### Full Configuration Requirements

Mault Pro users expect ALL features to be configured. A minimal configuration defeats the purpose of the Pro purchase.

The configuration at `docs/mault.yaml` needs these sections:

1. **Detectors section** - All 13 detector configurations
2. **deprecatedPatterns section** - Legacy import prevention (UC02)
3. **conventions section** - Naming conventions (UC03)
4. **rules section** - Structural governance patterns (UC18 Pro)

### UC18 Structural Governance Rules

For TypeScript/JavaScript projects:

```yaml
rules:
  - id: "TEST-001"
    name: "No Focused Tests"
    severity: "error"
    files: "**/*.test.ts"
    assertions:
      - type: "forbidden_pattern"
        pattern: "(describe|it|test)\\.only"
        message: "Remove .only() before committing"
```

### After Configuration

1. Save docs/mault.yaml
2. VS Code prompts to reload - click "Reload Now"
3. Check Problems Panel for active detectors
```

### Step 3: Paste to AI Coder

Works with:
- Claude Code
- Cursor
- GitHub Copilot Chat
- ChatGPT + Code Interpreter

### Step 4: Watch Progress

Problems Panel shows:
```
mault-setup (8)
  ⚠ Step 1/8: Git Repository — Not initialized
  ⚠ Step 2/8: Environment Setup — .env.example missing
  ...
```

As AI completes each step, checkmarks appear.

### Step 5: Click "Initialize Mault Hook"

For Step 7, click the button in Problems Panel. This runs Mault's compiled enforcement.

### Step 6: Done!

```
mault-setup (1)
  ✓ Production-Readiness Setup Complete!
```

---

## Files Created

After setup, your project will have:

```
your-project/
├── .git/                           # Step 1
├── .gitignore                      # Step 1
├── .env.example                    # Step 2
├── Dockerfile                      # Step 3
├── docker-compose.yml              # Step 3
├── .dockerignore                   # Step 3
├── .github/
│   └── workflows/
│       └── ci.yml                  # Step 4
├── tests/
│   ├── unit/
│   │   └── governance/             # Step 8 (governance tests)
│   └── integration/                # Step 5
├── .pre-commit-config.yaml         # Steps 6, 7, 8
├── scripts/
│   └── governance/                 # Step 8 (enforcement scripts)
│       ├── check-mock-tax.js       # TypeScript/JS projects
│       ├── check-mock-tax.py       # Python projects
│       ├── check-type-safety.js
│       ├── check-type-safety.py
│       ├── check-coverage-ratchet.js
│       └── check-coverage-ratchet.py
└── .memory-layer/
    └── baselines/                  # Step 8 (ratchet starting points)
        ├── coverage.json
        ├── type-safety.json
        └── mock-tax.json
```

---

## Two Paradigms

### New Project (Blank Slate)

AI creates everything from scratch. Full Production-Readiness from Day 1.

### Existing Project (Rising Tide)

AI detects existing state:
1. **Baseline Generation:** Count current violations
2. **Grandfather Legacy:** Existing violations allowed
3. **Block New:** New violations blocked
4. **Ratchet Down:** Only improvement allowed over time

Example:
```
Day 1: 150 type holes → Baseline: 150
Day 5: Developer adds 2 holes → BLOCKED (152 > 150)
Day 10: Developer fixes 5 holes → New Baseline: 145
```

---

## Troubleshooting

### AI Can't Find Production-Readiness Kit

Ensure `docs/production-readiness-kit/` exists in your workspace. Mault Pro creates this on purchase.

### Pre-commit Fails

Check `.pre-commit-config.yaml` syntax. AI may have created invalid YAML.

### Mault Hook Not Found

Run `Mault: Initialize` command from VS Code Command Palette (Ctrl+Shift+P / Cmd+Shift+P).

### Coverage Ratchet Blocks Me

You're below baseline. Either:
1. Add tests to increase coverage
2. Update baseline (requires justification)

---

## Related

- [systems-engineering-guide.md](../systems-engineering-guide_updated.md) — Full philosophy
- [iron-dome-complete.md](../iron-dome-complete.md) — Defense layers
- [gov-testing.md](../gov-testing.md) — Governance testing patterns
- [systems-engineering-gaps.md](../systems-engineering-gaps.md) — Iron Dome gap tracking

---

*Part of Mault Pro ($99 one-time purchase)*
