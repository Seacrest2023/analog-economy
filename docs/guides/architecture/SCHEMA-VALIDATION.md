# SCHEMA-VALIDATION.md — Runtime Type Safety

> **The Schema Validation Strategy:** Python type hints disappear at runtime. Every system boundary is a type-safety blind spot. Validate with Pydantic.

---

## The Problem: Compile-Time vs Runtime

```
┌─────────────────────────────────────────────────────────────────────┐
│                    THE TYPE SAFETY BLIND SPOT                        │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│   TYPE CHECKER (mypy)                    RUNTIME                    │
│   ──────────────────                     ───────                    │
│   Python knows User has:                 API returns:               │
│     id: str                                { "id": 123, ... }       │
│     email: str                             (id is INT!)             │
│     tier: Literal["trial", "core"]                                  │
│                                                                     │
│   mypy: ✅ Looks good!                   Runtime: 💥 Subtle bug!    │
│                                                                     │
│   You trusted `json.loads()` without validation.                    │
│   mypy can't protect you from external data.                        │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

**The Iron Dome (type safety) guards your source code. Schema Validation guards your system boundaries.**

---

## System Boundaries Requiring Validation

| Boundary | Risk | Example |
|----------|------|---------|
| API request bodies | Client sends malformed data | FastAPI request body |
| API responses | External APIs return unexpected data | `httpx.get()` responses |
| Webhook payloads | External systems send unexpected data | Stripe, GitHub webhooks |
| Config files | User edits corrupt format | `config.yaml`, `settings.json` |
| Database results | Schema drift | Migrations, manual changes |
| UE5 ↔ Python | Client sends corrupt game state | Telemetry events, crafting requests |

**Every boundary is a potential type hole.**

---

## The Solution: Pydantic Schema Validation

### What is Pydantic?

[Pydantic](https://docs.pydantic.dev/) is Python's standard for data validation:
1. Validates data at runtime
2. Works seamlessly with FastAPI (automatic validation)
3. Provides detailed error messages
4. Serializes to JSON for UE5 communication

### Basic Pattern

```python
from pydantic import BaseModel, EmailStr
from typing import Literal

# 1. Define schema (single source of truth)
class User(BaseModel):
    id: str
    email: EmailStr
    tier: Literal["trial", "core", "pro"]

# 2. FastAPI validates automatically
@app.post("/users")
async def create_user(user: User) -> User:
    # user is already validated!
    return await db.create_user(user)

# 3. Manual validation for external data
response = await httpx.get("/api/external")
user = User.model_validate(response.json())  # Raises ValidationError if invalid
```

---

## FastAPI: Automatic Validation

FastAPI uses Pydantic automatically. The key is configuring **strict schemas**.

### The Strict Schema Rule

```python
from pydantic import BaseModel, ConfigDict

# DANGEROUS: Ignores extra fields (data leakage!)
class UnsafeUser(BaseModel):
    id: str
    email: str

# SAFE: Rejects extra fields
class SafeUser(BaseModel):
    model_config = ConfigDict(extra="forbid")

    id: str
    email: str

# What happens:
data = {"id": "1", "email": "a@b.com", "password": "secret123"}  # pragma: allowlist secret

UnsafeUser.model_validate(data)  # ✅ Passes silently, ignores password
SafeUser.model_validate(data)    # ❌ Raises: extra fields not permitted
```

### Project-Wide Strict Base Model

Create a base class all models inherit from:

```python
# core-governance/gaian/schemas/base.py
from pydantic import BaseModel, ConfigDict


class StrictBaseModel(BaseModel):
    """Base model with strict validation for all schemas."""

    model_config = ConfigDict(
        extra="forbid",           # Reject unknown fields
        str_strip_whitespace=True, # Clean string inputs
        validate_assignment=True,  # Validate on attribute assignment
        frozen=False,             # Mutable by default
    )


class ImmutableBaseModel(StrictBaseModel):
    """Immutable version for value objects."""

    model_config = ConfigDict(
        extra="forbid",
        str_strip_whitespace=True,
        frozen=True,  # Immutable
    )
```

### Using in Routes

```python
# core-governance/gaian/schemas/user.py
from .base import StrictBaseModel
from pydantic import EmailStr


class UserCreate(StrictBaseModel):
    email: EmailStr
    name: str


class UserResponse(StrictBaseModel):
    id: str
    email: str
    name: str
    tier: str


# core-governance/gaian/api/users.py
from gaian.schemas.user import UserCreate, UserResponse

@router.post("/users", response_model=UserResponse)
async def create_user(user: UserCreate) -> UserResponse:
    # user is validated, extra fields rejected
    db_user = await user_service.create(user)
    return UserResponse.model_validate(db_user)
```

---

## UE5 Client-Side Validation

The UE5 client (The Body) receives JSON from Python (The Brain). **Never trust incoming data.**

### The Risk

```cpp
// DANGEROUS: No validation
void AGameState::ProcessServerResponse(const FString& JsonString)
{
    TSharedPtr<FJsonObject> JsonObject;
    TSharedRef<TJsonReader<>> Reader = TJsonReaderFactory<>::Create(JsonString);

    if (FJsonSerializer::Deserialize(Reader, JsonObject))
    {
        // Crash if "player_id" is missing or wrong type!
        FString PlayerId = JsonObject->GetStringField(TEXT("player_id"));
        int32 Gold = JsonObject->GetIntegerField(TEXT("gold"));
    }
}
```

### Safe Pattern: Validate Before Deserialize

```cpp
// Source/AnalogEconomy/Validation/JsonValidator.h
#pragma once

#include "CoreMinimal.h"
#include "Dom/JsonObject.h"

/**
 * JSON validation utilities for incoming server data.
 * Prevents crashes from malformed or unexpected data.
 */
class ANALOGECONOMY_API FJsonValidator
{
public:
    /**
     * Validates that all required fields exist with correct types.
     * @param JsonObject The JSON to validate
     * @param RequiredStrings Fields that must be strings
     * @param RequiredInts Fields that must be integers
     * @return True if valid, false otherwise
     */
    static bool ValidateFields(
        const TSharedPtr<FJsonObject>& JsonObject,
        const TArray<FString>& RequiredStrings,
        const TArray<FString>& RequiredInts
    );

    /** Get a string field safely, with default fallback */
    static FString GetStringSafe(
        const TSharedPtr<FJsonObject>& JsonObject,
        const FString& FieldName,
        const FString& Default = TEXT("")
    );

    /** Get an integer field safely, with default fallback */
    static int32 GetIntSafe(
        const TSharedPtr<FJsonObject>& JsonObject,
        const FString& FieldName,
        int32 Default = 0
    );
};
```

```cpp
// Source/AnalogEconomy/Validation/JsonValidator.cpp
#include "JsonValidator.h"

bool FJsonValidator::ValidateFields(
    const TSharedPtr<FJsonObject>& JsonObject,
    const TArray<FString>& RequiredStrings,
    const TArray<FString>& RequiredInts)
{
    if (!JsonObject.IsValid())
    {
        UE_LOG(LogTelemetry, Warning, TEXT("JSON object is null"));
        return false;
    }

    for (const FString& Field : RequiredStrings)
    {
        if (!JsonObject->HasTypedField<EJson::String>(Field))
        {
            UE_LOG(LogTelemetry, Warning,
                TEXT("Missing or invalid string field: %s"), *Field);
            return false;
        }
    }

    for (const FString& Field : RequiredInts)
    {
        if (!JsonObject->HasTypedField<EJson::Number>(Field))
        {
            UE_LOG(LogTelemetry, Warning,
                TEXT("Missing or invalid int field: %s"), *Field);
            return false;
        }
    }

    return true;
}

FString FJsonValidator::GetStringSafe(
    const TSharedPtr<FJsonObject>& JsonObject,
    const FString& FieldName,
    const FString& Default)
{
    if (JsonObject.IsValid() && JsonObject->HasTypedField<EJson::String>(FieldName))
    {
        return JsonObject->GetStringField(FieldName);
    }
    return Default;
}

int32 FJsonValidator::GetIntSafe(
    const TSharedPtr<FJsonObject>& JsonObject,
    const FString& FieldName,
    int32 Default)
{
    if (JsonObject.IsValid() && JsonObject->HasTypedField<EJson::Number>(FieldName))
    {
        return JsonObject->GetIntegerField(FieldName);
    }
    return Default;
}
```

### Usage in Game Code

```cpp
void AGameState::ProcessServerResponse(const FString& JsonString)
{
    TSharedPtr<FJsonObject> JsonObject;
    TSharedRef<TJsonReader<>> Reader = TJsonReaderFactory<>::Create(JsonString);

    if (!FJsonSerializer::Deserialize(Reader, JsonObject))
    {
        UE_LOG(LogTelemetry, Error, TEXT("Failed to parse JSON response"));
        return;
    }

    // Validate required fields BEFORE accessing
    TArray<FString> RequiredStrings = { TEXT("player_id"), TEXT("status") };
    TArray<FString> RequiredInts = { TEXT("gold"), TEXT("experience") };

    if (!FJsonValidator::ValidateFields(JsonObject, RequiredStrings, RequiredInts))
    {
        UE_LOG(LogTelemetry, Error, TEXT("Server response validation failed"));
        // Handle gracefully - don't crash
        return;
    }

    // Safe to access now
    FString PlayerId = JsonObject->GetStringField(TEXT("player_id"));
    int32 Gold = JsonObject->GetIntegerField(TEXT("gold"));

    UpdatePlayerState(PlayerId, Gold);
}
```

---

## Validation Patterns by Boundary

### 1. FastAPI Request Bodies

FastAPI validates automatically with Pydantic:

```python
from pydantic import BaseModel, Field
from gaian.schemas.base import StrictBaseModel


class CraftingRequest(StrictBaseModel):
    recipe_id: str = Field(..., min_length=1)
    quantity: int = Field(..., ge=1, le=100)
    materials: list[str] = Field(..., min_length=1)


@router.post("/craft")
async def craft_item(request: CraftingRequest):
    # Already validated!
    return await crafting_service.craft(request)
```

### 2. External API Responses

Always validate responses from external services:

```python
import httpx
from pydantic import BaseModel, ValidationError


class StripeCustomer(StrictBaseModel):
    id: str
    email: str
    created: int


async def get_stripe_customer(customer_id: str) -> StripeCustomer | None:
    async with httpx.AsyncClient() as client:
        response = await client.get(f"https://api.stripe.com/v1/customers/{customer_id}")

    try:
        return StripeCustomer.model_validate(response.json())
    except ValidationError as e:
        logger.error("stripe_response_invalid", error=str(e), customer_id=customer_id)
        return None
```

### 3. Webhook Payloads

Webhooks from external services need explicit validation:

```python
from fastapi import Request, HTTPException


class StripeWebhookEvent(StrictBaseModel):
    type: str
    data: dict  # We'll validate nested data separately


class CheckoutSession(StrictBaseModel):
    id: str
    customer: str
    mode: Literal["payment", "subscription"]


@router.post("/webhooks/stripe")
async def handle_stripe_webhook(request: Request):
    payload = await request.json()

    try:
        event = StripeWebhookEvent.model_validate(payload)
    except ValidationError as e:
        logger.error("webhook_invalid", error=str(e))
        raise HTTPException(status_code=400, detail="Invalid webhook payload")

    if event.type == "checkout.session.completed":
        session = CheckoutSession.model_validate(event.data["object"])
        await handle_checkout_complete(session)

    return {"status": "ok"}
```

### 4. Configuration Files

Validate config at startup, fail fast:

```python
from pydantic import BaseModel
from pydantic_settings import BaseSettings
import tomllib


class DatabaseConfig(StrictBaseModel):
    host: str
    port: int
    name: str
    pool_size: int = 10


class Settings(BaseSettings):
    database: DatabaseConfig
    debug: bool = False
    log_level: str = "INFO"

    model_config = {"env_prefix": "GAIAN_"}


def load_settings() -> Settings:
    """Load and validate settings at startup."""
    # Pydantic-settings handles environment variables automatically
    return Settings()


# In main.py
settings = load_settings()  # Crashes on invalid config - that's good!
```

---

## The Rising Tide Protocol

> "If your process is loose, AI will scale your chaos."
> Stop the bleeding on new code. Manage existing debt as static baseline.

### Green Zone (New Code) — MANDATORY

Any **NEW** code at system boundaries MUST use Pydantic with strict mode.

```
┌─────────────────────────────────────────────────────────────────────┐
│  GREEN ZONE: New Code                                                │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  ✅ FastAPI routes (inherit StrictBaseModel)                        │
│  ✅ Webhook handlers                                                │
│  ✅ External API clients                                            │
│  ✅ Config loaders                                                  │
│  ✅ UE5 ↔ Python message schemas                                    │
│                                                                     │
│  Rule: NEVER trust request.json(), json.loads(), or external data. │
│        ALWAYS define a Pydantic schema with extra="forbid".        │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

### Yellow Zone (Refactors) — PAY THE TAX

If modifying existing handler's business logic, you MUST add Pydantic validation.

### Red Zone (Legacy/Stable) — DO NOT TOUCH

Existing endpoints that are working and untouched stay as-is.

---

## Governance: Pre-commit Enforcement

### Detection Script

```python
#!/usr/bin/env python3
"""
Schema Validation Boundary Check

Detects unvalidated system boundaries in new/modified code.
"""

import ast
import sys
from pathlib import Path


class BoundaryVisitor(ast.NodeVisitor):
    """Detects json.loads() and dict access without Pydantic validation."""

    def __init__(self, filepath: Path):
        self.filepath = filepath
        self.violations: list[dict] = []
        self.has_pydantic = False

    def visit_Import(self, node: ast.Import) -> None:
        for alias in node.names:
            if 'pydantic' in alias.name:
                self.has_pydantic = True
        self.generic_visit(node)

    def visit_ImportFrom(self, node: ast.ImportFrom) -> None:
        if node.module and 'pydantic' in node.module:
            self.has_pydantic = True
        self.generic_visit(node)

    def visit_Call(self, node: ast.Call) -> None:
        # Detect json.loads() without nearby Pydantic
        if isinstance(node.func, ast.Attribute):
            if node.func.attr == 'loads' and not self.has_pydantic:
                self.violations.append({
                    'file': str(self.filepath),
                    'line': node.lineno,
                    'issue': 'json.loads() without Pydantic validation'
                })
        self.generic_visit(node)


def check_file(filepath: Path) -> list[dict]:
    """Check a file for boundary violations."""
    try:
        content = filepath.read_text()
        tree = ast.parse(content)
        visitor = BoundaryVisitor(filepath)
        visitor.visit(tree)
        return visitor.violations
    except SyntaxError:
        return []


def main() -> int:
    source_dir = Path(sys.argv[1]) if len(sys.argv) > 1 else Path('core-governance/gaian')

    if not source_dir.exists():
        return 0

    all_violations: list[dict] = []

    for py_file in source_dir.rglob('*.py'):
        if '__pycache__' in str(py_file) or 'test' in py_file.name:
            continue
        violations = check_file(py_file)
        all_violations.extend(violations)

    if all_violations:
        print('\n🚫 SCHEMA VALIDATION: Unvalidated Boundaries Detected\n')
        for v in all_violations:
            print(f"  {v['file']}:{v['line']}")
            print(f"    {v['issue']}\n")
        print('REMEDIATION:')
        print('  Add Pydantic model validation at this boundary.')
        print('  See: docs/guides/architecture/SCHEMA-VALIDATION.md\n')
        return 1

    print('✓ Schema validation check passed')
    return 0


if __name__ == '__main__':
    sys.exit(main())
```

---

## Relationship to Iron Dome

```
┌─────────────────────────────────────────────────────────────────────┐
│              TYPE SAFETY LAYERS                                      │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  IRON DOME (Compile-Time)                                           │
│  ────────────────────────                                           │
│  • Catches `Any`, `type: ignore`, `cast()`                          │
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
| **The Blind Spot** | Python type hints don't exist at runtime |
| **Pydantic** | Runtime validation with automatic FastAPI integration |
| **Strict Mode** | `extra="forbid"` rejects unknown fields |
| **StrictBaseModel** | Project-wide base class for all schemas |
| **UE5 Validation** | Validate JSON before deserializing to UStructs |
| **Rising Tide** | Enforce on new code, grandfather legacy |

---

## Related

- [IRON-DOME.md](../project%20setup/IRON-DOME.md) — Compile-time type safety
- [TDD-GUIDE.md](../development/TDD-GUIDE.md) — Testing validation schemas
- [OBSERVABILITY.md](../project%20setup/OBSERVABILITY.md) — Logging validation errors

---

*Part of The Analog Economy Production-Readiness Kit*
