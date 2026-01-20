# Observability Setup Guide

> **The Analog Economy: Production-Readiness Kit**
> **Philosophy:** If you can't debug it at 3:00 AM, it's not production-ready.

---

## Why Observability Matters

You've deployed your code. It starts correctly. But production is hostile territory:
- **Memory leaks** that only appear after 72 hours
- **Race conditions** that hit 0.1% of requests
- **Third-party APIs** that timeout at peak load
- **Database queries** that suddenly take 10x longer

Without observability, you're debugging blind. With it, you know *exactly* what happened, *when*, and *why*.

---

## The Three Pillars

| Pillar | What It Answers | Implementation |
|--------|-----------------|----------------|
| **Logs** | "What happened?" | Structured JSON to stdout |
| **Metrics** | "How much/how often?" | Counters, gauges, histograms |
| **Traces** | "What was the journey?" | Distributed trace IDs |

This guide focuses on **Logs + Traces** (the foundation). Metrics are covered in platform-specific guides.

---

## The Cardinal Rules

### Rule 1: No `print()` in Production Code

**Why:** Unstructured logs are unparseable. When your system emits 10,000 logs per second, you need machines to filter them.

```python
# BAD - Human-readable, machine-unreadable
print(f"User login failed for user@example.com")

# GOOD - Structured JSON, machine-parseable
logger.warning(
    "login_failed",
    email="user@example.com",
    reason="invalid_password",
    attempt=3
)
```

**Output:**
```json
{"level":"warning","event":"login_failed","email":"user@example.com","reason":"invalid_password","attempt":3,"timestamp":"2025-12-26T10:30:00Z"}
```

### Rule 2: Every Request Has a `trace_id`

**Why:** When a user reports "it's broken," you need to find their specific request among millions.

```
Request → API Gateway → Service A → Service B → Database
   └── trace_id: abc-123 propagated through entire chain
```

**Implementation:**
1. Generate `trace_id` at entry point (or accept from upstream)
2. Include in every log line
3. Pass to downstream services via header (`X-Trace-ID` or `traceparent`)
4. Return to client in response headers

### Rule 3: Logs Go to stdout

**Why:**
- Containers are ephemeral (files disappear)
- Log aggregators (Datadog, CloudWatch, ELK) read from stdout
- Separation of concerns (app logs, platform routes)

```python
# BAD - Writing to file
with open('/var/log/app.log', 'a') as f:
    f.write(message)

# GOOD - stdout (let platform handle routing)
# structlog does this automatically
logger.info("event_happened", key="value")
```

### Rule 4: Log Levels Have Meaning

| Level | When to Use | Example |
|-------|-------------|---------|
| **error** | System broken, needs attention | Database connection failed |
| **warning** | Degraded but functional | Retry succeeded after failure |
| **info** | Key business events | User signed up, order placed |
| **debug** | Development/troubleshooting | Request payload details |

**Production default:** `info` (debug is too noisy)

---

## Section 1: Structured Logging - The Brain (Python)

### Python with structlog

**Why structlog:** Pythonic API, processors pipeline, integrates with stdlib logging.

**Installation:**
```bash
pip install structlog
```

**Configuration:**
```python
# core-governance/gaian/logging.py
"""Structured logging configuration for production."""

import logging
import os
import sys

import structlog


def configure_logging() -> structlog.BoundLogger:
    """Configure structured logging for the application."""

    # Determine environment
    environment = os.getenv('ENVIRONMENT', 'development')
    is_production = environment == 'production'
    log_level = os.getenv('LOG_LEVEL', 'INFO').upper()

    # Processors for all log entries
    shared_processors: list[structlog.types.Processor] = [
        structlog.contextvars.merge_contextvars,  # Merge context (trace_id)
        structlog.processors.add_log_level,
        structlog.processors.TimeStamper(fmt="iso"),
        structlog.stdlib.add_logger_name,
    ]

    if is_production:
        # Production: JSON to stdout
        shared_processors.append(structlog.processors.JSONRenderer())
    else:
        # Development: Pretty console output
        shared_processors.append(structlog.dev.ConsoleRenderer())

    structlog.configure(
        processors=shared_processors,
        wrapper_class=structlog.make_filtering_bound_logger(
            getattr(logging, log_level)
        ),
        context_class=dict,
        logger_factory=structlog.PrintLoggerFactory(),
        cache_logger_on_first_use=True,
    )

    logger = structlog.get_logger()

    # Add base context
    return logger.bind(
        service=os.getenv('SERVICE_NAME', 'gaian-core'),
        version=os.getenv('APP_VERSION', '0.0.0'),
        environment=environment,
    )


# Initialize logger
logger = configure_logging()
```

**Usage:**
```python
from gaian.logging import logger
import structlog
import uuid

# Application-level logging
logger.info("app_started", port=8000)

# Request middleware (FastAPI example)
from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware

class TraceMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        # Extract or generate trace ID
        trace_id = request.headers.get('X-Trace-ID', str(uuid.uuid4()))

        # Bind to context for all logs in this request
        structlog.contextvars.clear_contextvars()
        structlog.contextvars.bind_contextvars(trace_id=trace_id)

        # Log request start
        logger.info(
            "request_started",
            method=request.method,
            path=request.url.path,
        )

        response = await call_next(request)

        # Add trace ID to response
        response.headers['X-Trace-ID'] = trace_id

        logger.info(
            "request_completed",
            status_code=response.status_code,
        )

        return response

# In route handlers
async def get_user(user_id: int):
    logger.info("user_fetch_started", user_id=user_id)
    user = await db.get_user(user_id)
    logger.info("user_fetch_completed", user_id=user_id, found=user is not None)
    return user
```

**Output:**
```json
{"event": "user_fetch_started", "user_id": 123, "trace_id": "abc-123", "service": "gaian-core", "version": "1.2.3", "level": "info", "timestamp": "2025-12-26T10:30:00.000000Z"}
```

---

## Section 2: Structured Logging - The Body (UE5)

### Unreal Engine with UE_LOG

UE5 has its own logging system that needs special handling for production observability.

**Log Categories:**
```cpp
// Source/AnalogEconomy/Logging/GameLogChannels.h
#pragma once

#include "CoreMinimal.h"

// Define custom log categories
DECLARE_LOG_CATEGORY_EXTERN(LogGameplay, Log, All);
DECLARE_LOG_CATEGORY_EXTERN(LogEconomy, Log, All);
DECLARE_LOG_CATEGORY_EXTERN(LogCrafting, Log, All);
DECLARE_LOG_CATEGORY_EXTERN(LogNetwork, Log, All);
DECLARE_LOG_CATEGORY_EXTERN(LogTelemetry, Log, All);
```

```cpp
// Source/AnalogEconomy/Logging/GameLogChannels.cpp
#include "GameLogChannels.h"

DEFINE_LOG_CATEGORY(LogGameplay);
DEFINE_LOG_CATEGORY(LogEconomy);
DEFINE_LOG_CATEGORY(LogCrafting);
DEFINE_LOG_CATEGORY(LogNetwork);
DEFINE_LOG_CATEGORY(LogTelemetry);
```

**Structured Logging Helper:**
```cpp
// Source/AnalogEconomy/Logging/StructuredLogger.h
#pragma once

#include "CoreMinimal.h"
#include "Json.h"

/**
 * Structured logging helper for UE5.
 * Outputs JSON-formatted logs for production observability.
 */
class ANALOGECONOMY_API FStructuredLogger
{
public:
    /** Log with structured data (JSON output) */
    static void Log(
        const FString& Event,
        const TMap<FString, FString>& Fields,
        ELogVerbosity::Type Verbosity = ELogVerbosity::Log
    );

    /** Log with trace ID for request correlation */
    static void LogWithTrace(
        const FString& TraceId,
        const FString& Event,
        const TMap<FString, FString>& Fields
    );

private:
    static FString ToJson(const FString& Event, const TMap<FString, FString>& Fields);
};
```

```cpp
// Source/AnalogEconomy/Logging/StructuredLogger.cpp
#include "StructuredLogger.h"

void FStructuredLogger::Log(
    const FString& Event,
    const TMap<FString, FString>& Fields,
    ELogVerbosity::Type Verbosity)
{
    FString JsonLog = ToJson(Event, Fields);

    // In shipping builds, output JSON for log aggregators
    #if UE_BUILD_SHIPPING
        // JSON output to stdout
        FPlatformMisc::LowLevelOutputDebugString(*JsonLog);
    #else
        // Development: human-readable
        UE_LOG(LogTelemetry, Log, TEXT("%s: %s"), *Event, *JsonLog);
    #endif
}

void FStructuredLogger::LogWithTrace(
    const FString& TraceId,
    const FString& Event,
    const TMap<FString, FString>& Fields)
{
    TMap<FString, FString> FieldsWithTrace = Fields;
    FieldsWithTrace.Add(TEXT("trace_id"), TraceId);
    Log(Event, FieldsWithTrace);
}

FString FStructuredLogger::ToJson(const FString& Event, const TMap<FString, FString>& Fields)
{
    TSharedPtr<FJsonObject> JsonObject = MakeShared<FJsonObject>();

    JsonObject->SetStringField(TEXT("event"), Event);
    JsonObject->SetStringField(TEXT("timestamp"), FDateTime::UtcNow().ToIso8601());
    JsonObject->SetStringField(TEXT("service"), TEXT("analog-economy-ue5"));

    for (const auto& Pair : Fields)
    {
        JsonObject->SetStringField(Pair.Key, Pair.Value);
    }

    FString OutputString;
    TSharedRef<TJsonWriter<>> Writer = TJsonWriterFactory<>::Create(&OutputString);
    FJsonSerializer::Serialize(JsonObject.ToSharedRef(), Writer);

    return OutputString;
}
```

**Usage in Game Code:**
```cpp
// In gameplay code
void ACraftingStation::OnCraftingComplete(const FCraftingRecipe& Recipe)
{
    TMap<FString, FString> Fields;
    Fields.Add(TEXT("recipe_id"), Recipe.RecipeId);
    Fields.Add(TEXT("player_id"), GetOwningPlayerId());
    Fields.Add(TEXT("crafting_time_ms"), FString::FromInt(CraftingTimeMs));

    FStructuredLogger::Log(TEXT("crafting_completed"), Fields);
}

// With trace ID for network operations
void APlayerController::OnServerResponse(const FString& TraceId, const FServerResponse& Response)
{
    TMap<FString, FString> Fields;
    Fields.Add(TEXT("status_code"), FString::FromInt(Response.StatusCode));
    Fields.Add(TEXT("latency_ms"), FString::FromInt(Response.LatencyMs));

    FStructuredLogger::LogWithTrace(TraceId, TEXT("server_response_received"), Fields);
}
```

---

## Section 3: Trace ID Propagation

### The Pattern

```
┌─────────────┐     ┌─────────────┐     ┌─────────────┐
│   Client    │────▶│  API GW     │────▶│  Service A  │
│   (UE5)     │     │             │     │  (Python)   │
│ X-Trace-ID: │     │ X-Trace-ID: │     │ X-Trace-ID: │
│   abc-123   │     │   abc-123   │     │   abc-123   │
└─────────────┘     └─────────────┘     └─────────────┘
                                               │
                                               ▼
                    ┌─────────────┐     ┌─────────────┐
                    │  Service C  │◀────│  Service B  │
                    │             │     │             │
                    │ X-Trace-ID: │     │ X-Trace-ID: │
                    │   abc-123   │     │   abc-123   │
                    └─────────────┘     └─────────────┘
```

### Python (FastAPI) Implementation

```python
# Outgoing HTTP calls with trace propagation
import httpx
import structlog

async def call_downstream_service(endpoint: str, data: dict) -> dict:
    """Make HTTP call with trace ID propagation."""
    # Get trace_id from current context
    ctx = structlog.contextvars.get_contextvars()
    trace_id = ctx.get('trace_id', 'unknown')

    async with httpx.AsyncClient() as client:
        response = await client.post(
            endpoint,
            json=data,
            headers={'X-Trace-ID': trace_id}
        )
        return response.json()
```

### UE5 Implementation

```cpp
// HTTP client with trace propagation
void UGameHttpClient::SendRequest(
    const FString& Endpoint,
    const FString& TraceId,
    const TSharedPtr<FJsonObject>& Payload)
{
    TSharedRef<IHttpRequest> Request = FHttpModule::Get().CreateRequest();
    Request->SetURL(Endpoint);
    Request->SetVerb(TEXT("POST"));
    Request->SetHeader(TEXT("Content-Type"), TEXT("application/json"));
    Request->SetHeader(TEXT("X-Trace-ID"), TraceId);

    FString PayloadString;
    TSharedRef<TJsonWriter<>> Writer = TJsonWriterFactory<>::Create(&PayloadString);
    FJsonSerializer::Serialize(Payload.ToSharedRef(), Writer);
    Request->SetContentAsString(PayloadString);

    Request->OnProcessRequestComplete().BindUObject(
        this, &UGameHttpClient::OnResponseReceived, TraceId
    );

    Request->ProcessRequest();
}
```

---

## Section 4: What to Log

### Always Log (Business Events)

```python
# User actions
logger.info("user_registered", user_id=user_id, email=redact(email))
logger.info("order_placed", order_id=order_id, total=total, item_count=item_count)
logger.info("payment_processed", order_id=order_id, amount=amount, provider=provider)

# Game events (UE5 → Python telemetry)
logger.info("crafting_started", player_id=player_id, recipe_id=recipe_id)
logger.info("era_transition", player_id=player_id, from_era="ancient", to_era="classical")
```

### Always Log (Errors)

```python
try:
    await process_payment(order)
except PaymentError as error:
    logger.error(
        "payment_failed",
        order_id=order.id,
        error=str(error),
        error_type=type(error).__name__,
        provider="stripe",
        # Context for debugging
        amount=order.total,
        currency=order.currency,
    )
    raise
```

### Log at Boundaries

```python
# Incoming request
logger.info("request_started", method=method, path=path, user_agent=user_agent)

# Outgoing HTTP call
logger.info("http_call_started", service="payment-api", endpoint="/charge")
logger.info("http_call_completed", service="payment-api", status_code=200, duration_ms=150)

# Database query
logger.debug("db_query", query=query, duration_ms=5)
```

### Never Log

```python
# Passwords, tokens, API keys
logger.info("login", password="***")  # NEVER

# Full credit card numbers
logger.info("payment", card_number="4111111111111111")  # NEVER

# PII without redaction
logger.info("user", ssn="123-45-6789")  # NEVER

# Excessive debug logs in production
logger.debug("request_body", body=huge_object)  # Set LOG_LEVEL=info in prod
```

---

## Section 5: Debugging Workflow

### When Something Breaks at 3:00 AM

1. **Get the trace ID** (from error alert, user report, or response header)
   ```
   X-Trace-ID: abc-123
   ```

2. **Search logs by trace ID**
   ```bash
   # CloudWatch
   aws logs filter-log-events --log-group-name /app/api \
     --filter-pattern '{ $.trace_id = "abc-123" }'

   # Datadog
   trace_id:abc-123

   # ELK/Kibana
   trace_id: "abc-123"
   ```

3. **Follow the timeline**
   ```json
   {"timestamp":"10:30:00.100","event":"request_started","trace_id":"abc-123"}
   {"timestamp":"10:30:00.150","event":"db_query_started","trace_id":"abc-123"}
   {"timestamp":"10:30:05.200","event":"db_query_timeout","trace_id":"abc-123","error":"Connection timed out after 5000ms"}
   {"timestamp":"10:30:05.201","event":"request_failed","trace_id":"abc-123","status_code":500}
   ```

4. **Identify root cause**
   - Database connection pool exhausted? → Scale pool or fix leak
   - Third-party API timeout? → Add circuit breaker
   - Memory spike? → Check for large payload or leak

---

## Section 6: Environment Configuration

### Environment Variables

| Variable | Default | Description |
|----------|---------|-------------|
| `LOG_LEVEL` | `INFO` | Minimum log level (DEBUG, INFO, WARNING, ERROR) |
| `SERVICE_NAME` | `unknown` | Name of service (for filtering) |
| `APP_VERSION` | `0.0.0` | Version for tracking deployments |
| `ENVIRONMENT` | `development` | Environment (affects formatting) |

### Development vs Production

```python
# Development: Pretty console output
2025-01-20 10:30:00 [info     ] request_started    method=GET path=/api/users trace_id=abc-123

# Production: JSON for log aggregators
{"level":"info","event":"request_started","method":"GET","path":"/api/users","trace_id":"abc-123","timestamp":"2025-01-20T10:30:00.000000Z"}
```

---

## Quick Reference

### Log Fields (Required)

| Field | Description | Example |
|-------|-------------|---------|
| `timestamp` | ISO8601 timestamp | `2025-12-26T10:30:00Z` |
| `level` | Log level | `info`, `error` |
| `event` | What happened | `user_login`, `payment_failed` |
| `trace_id` | Correlation ID | `abc-123` |
| `service` | Service name | `gaian-core`, `analog-economy-ue5` |

### Headers

| Header | Direction | Description |
|--------|-----------|-------------|
| `X-Trace-ID` | In/Out | Simple trace ID |
| `traceparent` | In/Out | W3C standard (OpenTelemetry) |

---

## Verification Checklist

Before going to production:

- [ ] All `print()` statements removed or converted to logger
- [ ] Logs output JSON to stdout
- [ ] Every log line includes `trace_id`
- [ ] Sensitive fields are redacted (password, api_key, etc.)
- [ ] Error logs include exception info
- [ ] Trace ID propagates to downstream services
- [ ] Trace ID returned in response headers
- [ ] LOG_LEVEL configurable via environment variable
- [ ] Logs viewable in aggregator (CloudWatch, Datadog, etc.)
- [ ] Can search logs by trace ID to follow a request
- [ ] UE5 logs use structured format in shipping builds

---

## Troubleshooting

### Problem: Logs not appearing in aggregator

**Check:**
1. Are logs going to stdout? `docker logs <container>`
2. Is LOG_LEVEL set correctly? Debug logs don't show at info level
3. Is JSON valid? Malformed JSON may be dropped

### Problem: Trace ID not propagating

**Check:**
1. Are you passing headers to downstream services?
2. Is middleware running before route handlers?
3. Is context being cleared between requests? (`structlog.contextvars.clear_contextvars()`)

### Problem: Logs too verbose / too expensive

**Solutions:**
1. Set `LOG_LEVEL=WARNING` in production
2. Use sampling for debug logs (log 1% of requests)
3. Redact large objects before logging
4. Use log rate limiting for noisy events

---

## Related

- [TDD-GUIDE.md](../development/TDD-GUIDE.md) — Test-driven development practices
- [CICD.md](../development/CICD.md) — CI/CD pipeline configuration
- [GOV-TESTING.md](./GOV-TESTING.md) — Governance testing implementation

---

*Part of The Analog Economy Production-Readiness Kit*
