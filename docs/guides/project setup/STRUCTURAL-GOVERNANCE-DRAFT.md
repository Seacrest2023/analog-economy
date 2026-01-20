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

# STRUCTURAL-GOVERNANCE.md — Enforcing Architectural Patterns

> **The Structural Governance Strategy:** AI coders follow patterns they see.
> If patterns are inconsistent, AI perpetuates inconsistency.
> Enforce structure before logic.

---

## The Problem: Architecturally Blind AI

```
┌─────────────────────────────────────────────────────────────────────┐
│                    THE PATTERN DRIFT CYCLE                          │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│   Day 1: Team agrees on DI pattern                                  │
│        ↓                                                            │
│   AI generates new code following visible patterns                  │
│        ↓                                                            │
│   One developer uses different pattern (it works!)                  │
│        ↓                                                            │
│   AI sees both patterns → picks randomly                            │
│        ↓                                                            │
│   More developers → more variation → AI confusion                   │
│        ↓                                                            │
│   ARCHITECTURAL CHAOS                                               │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

**AI coding tools are fast but don't know your conventions:**
- They follow whatever patterns exist in the codebase (good or bad)
- They can't distinguish "works" from "maintainable"
- They don't enforce DI patterns, error handling wrappers, or naming conventions
- They perpetuate inconsistency when patterns conflict

---

## The Solution: YAML-Driven AST Enforcement

Define structural rules in `mault.yaml` that the Mault extension enforces:

```yaml
version: "1.0"
rules:
  - id: "CMD-001"
    name: "Command Pattern Compliance"
    severity: "error"
    files: "**/commands/*.ts"
    assertions:
      - type: "export_exists"
        pattern: "register*Commands"
        message: "Command modules must export a registerXxxCommands function"
      - type: "function_signature"
        target: "register*Commands"
        requiredParams: ["deps"]
        message: "registerXxxCommands must accept deps parameter for DI"
```

When violations occur, Mault shows them in the Problems Panel with AI-friendly fix prompts.

---

## Core vs Pro

| Feature | Core | Pro |
|---------|------|-----|
| Detection in PROBLEMS panel | ✅ | ✅ |
| Copy AI fix prompt to clipboard | ✅ | ✅ |
| Pre-commit blocking (fail commits) | ❌ | ✅ |
| CI/CD integration (fail builds) | ❌ | ✅ |
| Baseline/amnesty for legacy code | ❌ | ✅ |
| Rule exemptions with justification | ❌ | ✅ |

---

## Assertion Types Reference

Mault supports multiple assertion types for different enforcement needs:

### Phase 1: Export & Signature Assertions

#### `export_exists`

Ensures files export functions/classes matching a pattern.

```yaml
assertions:
  - type: "export_exists"
    pattern: "register*Commands"
    message: "Command modules must export registerXxxCommands"
```

**Use Cases:**
- Enforce factory pattern: `create*Service` exports
- Ensure handler functions: `handle*` exports
- Validate entry points: `main` export

#### `function_signature`

Ensures exported functions have required parameters for DI.

```yaml
assertions:
  - type: "function_signature"
    target: "register*Commands"
    requiredParams: ["deps", "context"]
```

**Use Cases:**
- Enforce dependency injection: `deps` parameter
- Ensure context passing: `context`, `logger`, `config`
- Validate error handlers: `errorHandler` parameter

---

### Phase 2: Import & Structure Assertions

#### `import_exists`

Ensures files import from required modules.

```yaml
assertions:
  - type: "import_exists"
    source: "@/utils/logger"
    message: "All services must use the centralized logger"
```

**Use Cases:**
- Enforce centralized logging: import from `@/utils/logger`
- Ensure error handling: import from `@/errors`
- Validate DI container usage: import from `@/container`

#### `ast_skeleton`

Ensures functions have required AST structure (e.g., try-catch wrappers).

```yaml
assertions:
  - type: "ast_skeleton"
    target: "handle*"
    structure:
      root: "FunctionDeclaration"
      children:
        - position: "first"
          type: "TryStatement"
          children:
            - type: "CatchClause"
```

**Use Cases:**
- Enforce error handling: all handlers wrapped in try-catch
- Ensure logging: first statement is log call
- Validate cleanup: finally blocks in resource handlers

---

### Quick-Win Assertions

#### `forbidden_pattern`

Detects forbidden code patterns via regex (no AST parsing).

```yaml
assertions:
  - type: "forbidden_pattern"
    pattern: "describe\\.only|it\\.only|test\\.only"
    message: "Remove .only() before committing"
```

**Use Cases:**
- Prevent focused tests: `.only()` detection
- Block debug code: `console.log`, `debugger`
- Catch deprecated APIs: legacy method names

---

## Example Rule Configurations

### Command DI Pattern

```yaml
rules:
  - id: "CMD-001"
    name: "Command Dependency Injection"
    severity: "error"
    files: "**/commands/*.ts"
    description: "All command modules must follow DI pattern"
    assertions:
      - type: "export_exists"
        pattern: "register*Commands"
      - type: "function_signature"
        target: "register*Commands"
        requiredParams: ["deps"]
```

### Service Error Handling

```yaml
rules:
  - id: "SVC-001"
    name: "Service Error Wrapper"
    severity: "warning"
    files: "**/services/*.ts"
    assertions:
      - type: "import_exists"
        source: "@/utils/logger"
      - type: "ast_skeleton"
        target: "exported_function"
        structure:
          root: "FunctionDeclaration"
          children:
            - position: "first"
              type: "TryStatement"
```

### No Debug Code in Production

```yaml
rules:
  - id: "DEBUG-001"
    name: "No Console Logs"
    severity: "error"
    files: "src/**/*.ts"
    assertions:
      - type: "forbidden_pattern"
        pattern: "console\\.(log|debug|info|warn)"
        message: "Use Logger service instead of console methods"
```

### Test Quality Gates

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

---

## How It Works

```
┌─────────────────────────────────────────────────────────────────────┐
│                    STRUCTURAL GOVERNANCE FLOW                       │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│   1. User saves file in VS Code                                     │
│        ↓                                                            │
│   2. Mault parses mault.yaml rules                                  │
│        ↓                                                            │
│   3. Rules filtered by file glob pattern                            │
│        ↓                                                            │
│   4. AST parsed from file content                                   │
│        ↓                                                            │
│   5. Each assertion evaluated                                       │
│        ↓                                                            │
│   6. Violations shown in Problems Panel                             │
│        ↓                                                            │
│   7. User clicks "Copy Fix Prompt"                                  │
│        ↓                                                            │
│   8. AI reads prompt → fixes code                                   │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

---

## Why This Matters

### The Physics Principle

> **"Agents obey Physics, not Policy"**

- **Policy:** Style guides, wiki docs, team agreements → AI ignores these
- **Physics:** Build errors, failed tests, blocked commits → AI must fix these

Structural Governance converts architectural policy into physics:
- `mault.yaml` rules = physics (AI cannot bypass)
- Team wiki = policy (AI doesn't read)

### Pattern Consistency

When AI generates code, it samples from visible patterns. If 3 patterns exist for "how to write a command handler," AI picks randomly.

With Structural Governance:
- Only 1 pattern is valid
- Violations surface immediately
- AI learns to use the correct pattern

### Developer Velocity

Catching architectural drift early:
- **Without Mault:** PR review catches DI violation → rework → delay
- **With Mault:** Save file → violation in Problems → fix immediately

---

## Integration Points

### Pre-commit (Pro)

```yaml
# .pre-commit-config.yaml
repos:
  - repo: local
    hooks:
      - id: mault-structural-governance
        name: Mault Structural Governance
        entry: mault check structural
        language: system
        types: [typescript]
        pass_filenames: false
```

### CI/CD (Pro)

```yaml
# .github/workflows/ci.yml
jobs:
  structural-governance:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Run Mault Structural Check
        run: npx mault check structural --strict
```

---

## Troubleshooting

### Rules Not Triggering

1. Check file glob pattern matches your file path
2. Verify `mault.yaml` is in workspace root
3. Ensure file is saved (unsaved files not analyzed)

### False Positives

1. Use more specific glob patterns: `**/commands/*.ts` not `**/*.ts`
2. Add rule exemptions in `.mault/exemptions.yaml` (Pro)
3. Adjust assertion patterns

### Performance Issues

1. Limit rule scope with specific glob patterns
2. Use `forbidden_pattern` for simple checks (faster than AST)
3. Split large configs into domain-specific files

---

## Related Guides

- [PRECOMMIT-SETUP.md](./PRECOMMIT-SETUP-DRAFT.md) — Integrate with pre-commit
- [CICD.md](./CICD-DRAFT.md) — CI/CD integration
- [RATCHET-STRATEGY.md](./RATCHET-STRATEGY-DRAFT.md) — Gradual enforcement
- [TDD-GUIDE.md](./TDD-GUIDE-DRAFT.md) — Testing governance rules

---

*Part of Mault Pro ($99 one-time purchase)*
