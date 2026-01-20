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

# SCHEMA-VALIDATION.md — Runtime Type Safety

> **The Schema Validation Strategy:** TypeScript types disappear at runtime. Every system boundary is a type-safety blind spot. Validate with Zod.

---

## The Problem: Compile-Time vs Runtime

```
┌─────────────────────────────────────────────────────────────────────┐
│                    THE TYPE SAFETY BLIND SPOT                        │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│   COMPILE TIME                        RUNTIME                       │
│   ────────────                        ───────                       │
│   TypeScript knows User has:          API returns:                  │
│     id: string                          { id: 123, ... }            │
│     email: string                       (id is NUMBER!)             │
│     tier: "trial" | "core" | "pro"                                  │
│                                                                     │
│   TypeScript: ✅ Looks good!          Runtime: 💥 Subtle bug!       │
│                                                                     │
│   You trusted `as User` or `JSON.parse()` without validation.       │
│   TypeScript can't protect you from external data.                  │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

**The Iron Dome (type safety) guards your source code. Schema Validation guards your system boundaries.**

---

## System Boundaries Requiring Validation

| Boundary | Risk | Example |
|----------|------|---------|
| API responses | Backend changes break frontend silently | `fetch('/api/user')` |
| Webhook payloads | External systems send unexpected data | Stripe, GitHub webhooks |
| Config files | User edits corrupt format | `mault.yaml`, `settings.json` |
| localStorage/cache | Data persists across code changes | Browser storage |
| URL params | User manipulation | Query strings, route params |
| Form data | User input validation | Contact forms, login |
| Database results | Schema drift | Migrations, manual changes |

**Every boundary is a potential type hole.**

---

## The Solution: Zod Schema Validation

### What is Zod?

[Zod](https://zod.dev) is a TypeScript-first schema validation library that:
1. Validates data at runtime
2. Infers TypeScript types from schemas (DRY)
3. Provides detailed error messages

### Basic Pattern

```typescript
import { z } from 'zod';

// 1. Define schema (single source of truth)
const UserSchema = z.object({
  id: z.string().uuid(),
  email: z.string().email(),
  tier: z.enum(['trial', 'core', 'pro']),
});

// 2. Infer type from schema (DRY - no duplication)
type User = z.infer<typeof UserSchema>;

// 3. Validate at boundary
const response = await fetch('/api/user');
const data = await response.json();
const user = UserSchema.parse(data);  // Throws ZodError if invalid
```

---

## The Rising Tide Protocol for Zod

> "If your process is loose, AI will scale your chaos."
> Stop the bleeding on new code. Manage existing debt as static baseline.

### Green Zone (New Code) — MANDATORY

Any **NEW** code at system boundaries MUST validate inputs using Zod.

```
┌─────────────────────────────────────────────────────────────────────┐
│  GREEN ZONE: New Code                                                │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  ✅ API routes / Server Actions                                     │
│  ✅ Webhook handlers                                                │
│  ✅ Config file loaders                                             │
│  ✅ External API clients                                            │
│  ✅ Form handlers                                                   │
│                                                                     │
│  Rule: NEVER trust req.body, JSON.parse(), or external data.        │
│        ALWAYS define a schema co-located with the handler.          │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

### Yellow Zone (Refactors) — PAY THE TAX

If modifying existing handler's business logic, you MUST add Zod validation.

```
┌─────────────────────────────────────────────────────────────────────┐
│  YELLOW ZONE: Modified Code                                          │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  Scenario: Fixing bug in existing webhook handler                   │
│                                                                     │
│  Before (no validation):                                            │
│    const { userId, action } = req.body;                             │
│    // bug fix here                                                  │
│                                                                     │
│  After (validated):                                                 │
│    const WebhookSchema = z.object({                                 │
│      userId: z.string(),                                            │
│      action: z.enum(['create', 'update', 'delete']),                │
│    });                                                              │
│    const { userId, action } = WebhookSchema.parse(req.body);        │
│    // bug fix here                                                  │
│                                                                     │
│  Rule: Cannot touch the logic without wrapping input in Zod.        │
│        Timebox: If schema takes >30 min, verify with lead first.    │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

### Red Zone (Legacy/Stable) — DO NOT TOUCH

Existing endpoints that are working and untouched stay as-is.

```
┌─────────────────────────────────────────────────────────────────────┐
│  RED ZONE: Stable Legacy Code                                        │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  Reason: Adding Zod to legacy code risks rejecting weird-but-valid  │
│          data that your frontend has been sending for months.       │
│                                                                     │
│          Don't wake the sleeping dragon 15 days before launch.      │
│                                                                     │
│  Rule: Leave working code alone unless actively modifying it.       │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

---

## Standard Helper Pattern

Co-locate these helpers with your validation needs:

```typescript
// src/utils/validateRequest.ts
import { z, ZodSchema, ZodError } from 'zod';

/**
 * Result type for safe validation operations.
 */
export type ValidationResult<T> =
  | { success: true; data: T }
  | { success: false; error: ZodError };

/**
 * Validates data against a Zod schema, throwing on failure.
 * Use for critical paths where invalid data should halt execution.
 *
 * @param schema - Zod schema to validate against
 * @param data - Unknown data from external source
 * @returns Validated and typed data
 * @throws ZodError with detailed validation errors
 *
 * @example
 * const UserSchema = z.object({ id: z.string(), email: z.string().email() });
 * const user = validateRequest(UserSchema, apiResponse); // Throws if invalid
 */
export function validateRequest<T>(schema: ZodSchema<T>, data: unknown): T {
  return schema.parse(data);
}

/**
 * Safely validates data against a Zod schema without throwing.
 * Use for graceful degradation flows where fallback behavior is acceptable.
 *
 * @param schema - Zod schema to validate against
 * @param data - Unknown data from external source
 * @returns Result object with success flag and either data or error
 *
 * @example
 * const result = safeValidateRequest(ConfigSchema, rawConfig);
 * if (!result.success) {
 *   console.warn('Invalid config, using defaults:', result.error.message);
 *   return DEFAULT_CONFIG;
 * }
 * return result.data;
 */
export function safeValidateRequest<T>(
  schema: ZodSchema<T>,
  data: unknown,
): ValidationResult<T> {
  const result = schema.safeParse(data);
  if (result.success) {
    return { success: true, data: result.data };
  }
  return { success: false, error: result.error };
}

/**
 * Formats a ZodError into a human-readable string for logging.
 *
 * @param error - ZodError from failed validation
 * @returns Formatted error message
 */
export function formatValidationError(error: ZodError): string {
  return error.issues
    .map((issue) => `${issue.path.join('.')}: ${issue.message}`)
    .join('; ');
}

// Re-export Zod for convenience (allows co-location of schema and handler)
export { z, ZodError };
export type { ZodSchema };
```

---

## When to Use parse() vs safeParse()

| Method | Behavior | Use Case |
|--------|----------|----------|
| `schema.parse(data)` | Throws on invalid | Critical paths — fail fast |
| `schema.safeParse(data)` | Returns result object | Graceful degradation with fallbacks |

### Critical Path (Fail Fast)

```typescript
// API handler — invalid data should stop execution
export async function createUser(req: Request) {
  const CreateUserSchema = z.object({
    email: z.string().email(),
    name: z.string().min(1),
  });

  const data = CreateUserSchema.parse(req.body);  // Throws if invalid
  return await db.users.create(data);
}
```

### Graceful Degradation (Fallback)

```typescript
// Config loading — invalid config uses defaults
export function loadConfig(): Config {
  const ConfigSchema = z.object({
    timeout: z.number().positive(),
    retries: z.number().int().min(0),
  });

  const rawConfig = JSON.parse(fs.readFileSync('config.json', 'utf8'));
  const result = safeValidateRequest(ConfigSchema, rawConfig);

  if (!result.success) {
    console.warn('Invalid config, using defaults:', formatValidationError(result.error));
    return DEFAULT_CONFIG;
  }

  return result.data;
}
```

---

## Zod Best Practices

### 1. Co-locate Schema with Handler

```typescript
// user-controller.ts
const CreateUserInput = z.object({
  email: z.string().email(),
  name: z.string(),
});

export async function createUser(input: unknown) {
  const data = CreateUserInput.parse(input);
  // ...
}
```

### 2. Use strict() to Reject Unknown Keys

```typescript
const UserSchema = z.object({
  id: z.string(),
  email: z.string().email(),
}).strict();  // Rejects { id: '1', email: 'a@b.com', HACKED: true }
```

### 3. Prefer z.infer<> Over Duplicate Interfaces

```typescript
// BAD: Duplicated type definition
interface User {
  id: string;
  email: string;
}
const UserSchema = z.object({
  id: z.string(),
  email: z.string(),
});

// GOOD: Single source of truth
const UserSchema = z.object({
  id: z.string(),
  email: z.string().email(),
});
type User = z.infer<typeof UserSchema>;
```

### 4. Use Transforms for Type Coercion

```typescript
// URL params come as strings, coerce to numbers
const PaginationSchema = z.object({
  page: z.coerce.number().int().positive(),
  limit: z.coerce.number().int().min(1).max(100),
});

// Works with: ?page=2&limit=10
```

### 5. Use Defaults for Optional Fields

```typescript
const ConfigSchema = z.object({
  enabled: z.boolean(),
  timeout: z.number().default(5000),
  retries: z.number().default(3),
});

// Input: { enabled: true }
// Output: { enabled: true, timeout: 5000, retries: 3 }
```

---

## Real-World Examples

### API Response Validation

```typescript
const ApiResponseSchema = z.object({
  success: z.boolean(),
  data: z.object({
    user: z.object({
      id: z.string(),
      email: z.string().email(),
      tier: z.enum(['trial', 'core', 'pro']),
    }),
  }),
});

async function fetchUser(userId: string) {
  const response = await fetch(`/api/users/${userId}`);
  const json = await response.json();
  return ApiResponseSchema.parse(json).data.user;
}
```

### Webhook Payload Validation

```typescript
const StripeWebhookSchema = z.object({
  type: z.string(),
  data: z.object({
    object: z.object({
      id: z.string(),
      customer: z.string(),
      mode: z.enum(['payment', 'subscription']),
    }),
  }),
});

export async function handleStripeWebhook(payload: unknown) {
  const event = StripeWebhookSchema.parse(payload);

  if (event.type === 'checkout.session.completed') {
    const { customer, mode } = event.data.object;
    // ...
  }
}
```

### Environment Variable Validation

```typescript
const EnvSchema = z.object({
  NODE_ENV: z.enum(['development', 'test', 'production']),
  DATABASE_URL: z.string().url(),
  API_KEY: z.string().min(1),
  PORT: z.coerce.number().int().positive().default(3000),
});

// Validate at app startup
export const env = EnvSchema.parse(process.env);
```

---

## AI Agent Instructions

Add to your System Prompt / Cursor Rules:

```markdown
## Zod Implementation Standards (Rising Tide Policy)

1. **New Inputs:** ALL new public-facing functions (API routes, Server Actions)
   MUST validate inputs using Zod.
   - NEVER trust req.body or input directly.
   - ALWAYS define a schema co-located with the handler.

2. **Legacy Code:** Do NOT refactor existing controllers to add Zod unless
   you are actively modifying the business logic of that controller.

3. **Validation Strategy:**
   - Use z.object({ ... }).strict() to reject unknown keys.
   - Use schema.parse(data) for critical paths (fail fast).
   - Use schema.safeParse(data) only if you have a fallback logic flow.

4. **Type Inference:**
   - Use `type X = z.infer<typeof XSchema>` instead of duplicate interfaces.
   - Co-locate schema with handler for discoverability.
```

---

## Governance: Pre-commit Enforcement

### Detection Script

Script: `scripts/governance/check-zod-boundaries.js`

Detects `JSON.parse()` or `req.body` in new/modified files without adjacent `.parse()` call.

```javascript
#!/usr/bin/env node
/**
 * Schema Validation Boundary Check
 *
 * Detects unvalidated system boundaries in new/modified code.
 * Part of the Rising Tide Protocol for Zod.
 */
const fs = require('fs');
const path = require('path');
const { execSync } = require('child_process');

const BASELINE_PATH = '.memory-layer/baselines/schema-validation.json';

// Patterns indicating unvalidated boundaries
const BOUNDARY_PATTERNS = [
  { name: 'JSON.parse without validation', pattern: /JSON\.parse\([^)]+\)(?!.*\.parse\()/ },
  { name: 'req.body without validation', pattern: /req\.body(?!.*Schema\.parse)/ },
  { name: 'response.json() without validation', pattern: /\.json\(\)(?!.*\.parse\()/ },
  { name: 'as Type assertion on external data', pattern: /as\s+\w+(?!.*\.parse\()/ },
];

// Patterns indicating proper validation
const VALIDATION_PATTERNS = [
  /\.parse\(/,
  /\.safeParse\(/,
  /validateRequest\(/,
  /safeValidateRequest\(/,
];

function hasValidation(content) {
  return VALIDATION_PATTERNS.some(pattern => pattern.test(content));
}

function checkFile(filePath) {
  const content = fs.readFileSync(filePath, 'utf8');
  const violations = [];

  // Skip if file has validation
  if (hasValidation(content)) {
    return violations;
  }

  for (const { name, pattern } of BOUNDARY_PATTERNS) {
    if (pattern.test(content)) {
      violations.push({ file: filePath, issue: name });
    }
  }

  return violations;
}

function getStagedFiles() {
  try {
    const output = execSync('git diff --cached --name-only --diff-filter=ACMR', {
      encoding: 'utf8',
    });
    return output.split('\n').filter(f => /\.(ts|tsx|js|jsx)$/.test(f));
  } catch {
    return [];
  }
}

// Main
const files = process.argv.slice(2).length > 0
  ? process.argv.slice(2)
  : getStagedFiles();

const allViolations = [];
for (const file of files) {
  if (!fs.existsSync(file)) continue;
  allViolations.push(...checkFile(file));
}

if (allViolations.length > 0) {
  console.log('='.repeat(60));
  console.log('SCHEMA VALIDATION: Unvalidated Boundaries Detected');
  console.log('='.repeat(60));
  console.log();

  for (const v of allViolations) {
    console.log(`BOUNDARY: ${v.file}`);
    console.log(`  Issue: ${v.issue}`);
    console.log(`  Action: Add Zod schema validation at this boundary.`);
    console.log();
  }

  console.log('See: docs/production-readiness-kit/SCHEMA-VALIDATION.md');
  process.exit(1);
}

process.exit(0);
```

### Pre-commit Hook

```yaml
# .pre-commit-config.yaml (TypeScript/JavaScript)
- repo: local
  hooks:
    - id: schema-validation
      name: Schema Validation (Rising Tide)
      entry: node scripts/governance/check-zod-boundaries.js
      language: system
      files: \.(ts|tsx|js|jsx)$
      description: |
        Enforces Zod validation at system boundaries.
        If blocked, add schema validation using validateRequest().
```

### Python Equivalent (Pydantic)

For Python projects, use [Pydantic](https://docs.pydantic.dev/) for runtime validation:

```python
# src/schemas/user.py
from pydantic import BaseModel, EmailStr

class UserCreate(BaseModel):
    email: EmailStr
    name: str

# In route handler
from schemas.user import UserCreate

@app.post("/users")
def create_user(user: UserCreate):  # Pydantic validates automatically
    return db.create_user(user.model_dump())
```

```yaml
# .pre-commit-config.yaml (Python)
- repo: local
  hooks:
    - id: schema-validation-python
      name: Schema Validation (Python)
      entry: python scripts/governance/check-pydantic-boundaries.py
      language: system
      files: \.py$
      description: |
        Enforces Pydantic validation at system boundaries.
```

**Roadmap Languages:** Go (go-playground/validator), Java (Jakarta Bean Validation), Rust (serde + validator), C# (FluentValidation) support is planned for future releases.

---

## Relationship to Iron Dome

```
┌─────────────────────────────────────────────────────────────────────┐
│              TYPE SAFETY LAYERS                                      │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  IRON DOME (Compile-Time)                                           │
│  ────────────────────────                                           │
│  • Catches `any`, `as`, `@ts-ignore`                                │
│  • Guards YOUR source code                                          │
│  • See: IRON-DOME.md                                                │
│                                                                     │
│  SCHEMA VALIDATION (Runtime)                                        │
│  ──────────────────────────                                         │
│  • Catches invalid external data                                    │
│  • Guards SYSTEM BOUNDARIES                                         │
│  • See: This document                                               │
│                                                                     │
│  Together they form complete type safety:                           │
│  • Iron Dome: Your code → Your code (compile-time)                  │
│  • Schema Validation: External → Your code (runtime)                │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

---

## Summary

| Concept | Description |
|---------|-------------|
| **The Blind Spot** | TypeScript types don't exist at runtime |
| **Zod** | Runtime validation that infers TypeScript types |
| **Rising Tide** | Enforce on new code, grandfather legacy |
| **Green Zone** | New code = mandatory validation |
| **Yellow Zone** | Modified code = pay the tax |
| **Red Zone** | Stable legacy = don't touch |
| **parse()** | Critical paths — fail fast |
| **safeParse()** | Graceful degradation with fallbacks |

---

## Related

- [IRON-DOME.md](./IRON-DOME.md) — Compile-time type safety (any ratchet)
- [RISING-TIDE.md](./RISING-TIDE.md) — Mock tax philosophy (same Rising Tide pattern)
- [RATCHET-STRATEGY.md](./RATCHET-STRATEGY.md) — Baseline improvement philosophy

---

*Part of the Mault Production-Readiness Kit*
