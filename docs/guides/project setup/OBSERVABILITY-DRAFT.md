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

# Step 9: Observability Setup Guide

> **Part of the Mault Pro Production-Readiness Kit**
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

### Rule 1: No `console.log` or `print` in Production

**Why:** Unstructured logs are unparseable. When your system emits 10,000 logs per second, you need machines to filter them.

```javascript
// BAD - Human-readable, machine-unreadable
console.log('User login failed for user@example.com');

// GOOD - Structured JSON, machine-parseable
logger.warn({
  event: 'login_failed',
  email: 'user@example.com',
  reason: 'invalid_password',
  attempt: 3
});
```

**Output:**
```json
{"level":"warn","event":"login_failed","email":"user@example.com","reason":"invalid_password","attempt":3,"timestamp":"2025-12-26T10:30:00Z"}
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

```javascript
// BAD - Writing to file
fs.appendFileSync('/var/log/app.log', message);

// GOOD - stdout (let platform handle routing)
process.stdout.write(JSON.stringify(log) + '\n');
```

### Rule 4: Log Levels Have Meaning

| Level | When to Use | Example |
|-------|-------------|---------|
| **error** | System broken, needs attention | Database connection failed |
| **warn** | Degraded but functional | Retry succeeded after failure |
| **info** | Key business events | User signed up, order placed |
| **debug** | Development/troubleshooting | Request payload details |

**Production default:** `info` (debug is too noisy)

---

## Section 1: Structured Logging by Language

### Node.js / TypeScript (Pino)

**Why Pino:** Fastest JSON logger for Node.js, 5x faster than Winston.

**Installation:**
```bash
npm install pino pino-pretty
```

**Configuration:**
```typescript
// src/logger.ts
import pino from 'pino';

// Determine log level from environment
const level = process.env.LOG_LEVEL || 'info';

// Create logger with correlation ID support
export const logger = pino({
  level,
  // In production, output pure JSON
  // In development, use pretty printing
  transport: process.env.NODE_ENV === 'development'
    ? { target: 'pino-pretty', options: { colorize: true } }
    : undefined,
  // Base fields included in every log
  base: {
    service: process.env.SERVICE_NAME || 'unknown',
    version: process.env.APP_VERSION || '0.0.0',
    env: process.env.NODE_ENV || 'development'
  },
  // Timestamp format
  timestamp: pino.stdTimeFunctions.isoTime,
  // Redact sensitive fields
  redact: ['req.headers.authorization', 'password', 'apiKey']
});

// Create child logger with correlation ID
export function createRequestLogger(traceId: string) {
  return logger.child({ traceId });
}
```

**Usage:**
```typescript
import { logger, createRequestLogger } from './logger';

// Application-level logging
logger.info({ event: 'app_started', port: 3000 });

// Request-level logging with trace ID
app.use((req, res, next) => {
  const traceId = req.headers['x-trace-id'] as string || crypto.randomUUID();
  req.log = createRequestLogger(traceId);
  res.setHeader('X-Trace-ID', traceId);

  req.log.info({
    event: 'request_started',
    method: req.method,
    path: req.path
  });

  next();
});
```

**Output:**
```json
{"level":30,"time":"2025-12-26T10:30:00.000Z","service":"api","version":"1.2.3","env":"production","traceId":"abc-123","event":"request_started","method":"GET","path":"/api/users"}
```

---

### Python (structlog)

**Why structlog:** Pythonic API, processors pipeline, integrates with stdlib logging.

**Installation:**
```bash
pip install structlog
```

**Configuration:**
```python
# src/logger.py
import structlog
import logging
import os
import sys

def configure_logging():
    """Configure structured logging for production."""

    # Determine environment
    is_production = os.getenv('ENVIRONMENT', 'development') == 'production'
    log_level = os.getenv('LOG_LEVEL', 'INFO').upper()

    # Processors for all log entries
    shared_processors = [
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

    return structlog.get_logger()

# Initialize logger
logger = configure_logging()

# Add base context
logger = logger.bind(
    service=os.getenv('SERVICE_NAME', 'unknown'),
    version=os.getenv('APP_VERSION', '0.0.0'),
)
```

**Usage:**
```python
from logger import logger
import structlog
import uuid

# Application-level logging
logger.info("app_started", port=8000)

# Request middleware (Flask example)
@app.before_request
def add_trace_id():
    trace_id = request.headers.get('X-Trace-ID', str(uuid.uuid4()))
    structlog.contextvars.clear_contextvars()
    structlog.contextvars.bind_contextvars(trace_id=trace_id)
    g.trace_id = trace_id

@app.after_request
def add_trace_header(response):
    response.headers['X-Trace-ID'] = g.trace_id
    return response

# In route handlers
def get_user(user_id):
    logger.info("user_fetch_started", user_id=user_id)
    user = db.get_user(user_id)
    logger.info("user_fetch_completed", user_id=user_id, found=user is not None)
    return user
```

**Output:**
```json
{"event": "user_fetch_started", "user_id": 123, "trace_id": "abc-123", "service": "api", "version": "1.2.3", "level": "info", "timestamp": "2025-12-26T10:30:00.000000Z"}
```

---

### Roadmap Languages

Support for additional languages is planned for future releases:

| Language | Recommended Logger | Status |
|----------|-------------------|--------|
| **Go** | zerolog (zero-allocation JSON logger) | Planned |
| **Java** | Logback + SLF4J + MDC | Planned |
| **Rust** | tracing + tracing-subscriber | Planned |
| **C#** | Serilog | Planned |

---

## Section 2: Trace ID Propagation

### The Pattern

```
┌─────────────┐     ┌─────────────┐     ┌─────────────┐
│   Client    │────▶│  API GW     │────▶│  Service A  │
│             │     │             │     │             │
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

### Implementation Checklist

1. **Entry Point (API Gateway / First Service)**
   ```javascript
   const traceId = req.headers['x-trace-id'] || crypto.randomUUID();
   ```

2. **Outgoing HTTP Calls**
   ```javascript
   axios.get('http://service-b/api', {
     headers: { 'X-Trace-ID': traceId }
   });
   ```

3. **Message Queues**
   ```javascript
   channel.publish('events', '', message, {
     headers: { 'x-trace-id': traceId }
   });
   ```

4. **Background Jobs**
   ```javascript
   queue.add('processOrder', { orderId }, {
     jobId: traceId  // Or pass as data
   });
   ```

5. **Response Headers**
   ```javascript
   res.setHeader('X-Trace-ID', traceId);
   ```

### W3C Trace Context (Standard)

For OpenTelemetry compatibility, use the `traceparent` header:

```
traceparent: 00-{trace-id}-{span-id}-{flags}
traceparent: 00-0af7651916cd43dd8448eb211c80319c-b7ad6b7169203331-01
```

---

## Section 3: What to Log

### Always Log (Business Events)

```javascript
// User actions
logger.info({ event: 'user_registered', userId, email: redact(email) });
logger.info({ event: 'order_placed', orderId, total, itemCount });
logger.info({ event: 'payment_processed', orderId, amount, provider });

// System state changes
logger.info({ event: 'cache_cleared', reason: 'manual', clearedKeys: 150 });
logger.info({ event: 'feature_flag_changed', flag: 'dark_mode', value: true });
```

### Always Log (Errors)

```javascript
try {
  await processPayment(order);
} catch (error) {
  logger.error({
    event: 'payment_failed',
    orderId: order.id,
    error: error.message,
    stack: error.stack,
    provider: 'stripe',
    // Context for debugging
    amount: order.total,
    currency: order.currency
  });
  throw error;
}
```

### Log at Boundaries

```javascript
// Incoming request
logger.info({ event: 'request_started', method, path, userAgent });

// Outgoing HTTP call
logger.info({ event: 'http_call_started', service: 'payment-api', endpoint: '/charge' });
logger.info({ event: 'http_call_completed', service: 'payment-api', statusCode: 200, durationMs: 150 });

// Database query
logger.debug({ event: 'db_query', query: 'SELECT * FROM users', durationMs: 5 });
```

### Never Log

```javascript
// Passwords, tokens, API keys
logger.info({ password: '***' }); // NEVER

// Full credit card numbers
logger.info({ cardNumber: '4111111111111111' }); // NEVER

// PII without redaction
logger.info({ ssn: '123-45-6789' }); // NEVER

// Excessive debug logs in production
logger.debug({ requestBody: hugeObject }); // Set LOG_LEVEL=info in prod
```

---

## Section 4: Log Aggregation Patterns

### Docker Compose (Development)

```yaml
# docker-compose.yml
services:
  app:
    build: .
    environment:
      - LOG_LEVEL=debug
      - NODE_ENV=development
    # Logs visible via: docker compose logs -f app

  # Optional: Local log viewer
  dozzle:
    image: amir20/dozzle:latest
    ports:
      - "8080:8080"
    volumes:
      - /var/run/docker.sock:/var/run/docker.sock
```

### Cloud Run / Kubernetes

Logs automatically captured from stdout. Configure log router:

```yaml
# Cloud Run
apiVersion: serving.knative.dev/v1
kind: Service
metadata:
  annotations:
    run.googleapis.com/execution-environment: gen2
spec:
  template:
    spec:
      containers:
        - env:
            - name: LOG_LEVEL
              value: "info"
```

### AWS CloudWatch

```javascript
// Logs to stdout are automatically sent to CloudWatch
// Configure log group in SAM/CDK:
{
  "LogGroupName": "/aws/lambda/my-function",
  "RetentionInDays": 30
}
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
     --filter-pattern '{ $.traceId = "abc-123" }'

   # Datadog
   trace_id:abc-123

   # ELK/Kibana
   traceId: "abc-123"
   ```

3. **Follow the timeline**
   ```json
   {"timestamp":"10:30:00.100","event":"request_started","traceId":"abc-123"}
   {"timestamp":"10:30:00.150","event":"db_query_started","traceId":"abc-123"}
   {"timestamp":"10:30:05.200","event":"db_query_timeout","traceId":"abc-123","error":"Connection timed out after 5000ms"}
   {"timestamp":"10:30:05.201","event":"request_failed","traceId":"abc-123","statusCode":500}
   ```

4. **Identify root cause**
   - Database connection pool exhausted? → Scale pool or fix leak
   - Third-party API timeout? → Add circuit breaker
   - Memory spike? → Check for large payload or leak

---

## AI Prompts

### Generate Structured Logger

```
Configure a structured logger for my [Node.js/Python] application:

Requirements:
1. Output JSON to stdout (for production log aggregators)
2. Include these base fields in every log: service name, version, environment
3. Support trace_id (correlation ID) propagation via context
4. Redact sensitive fields: password, apiKey, authorization headers
5. Use [Pino/structlog] as the logger

Environment variables:
- LOG_LEVEL: info (default), debug, warn, error
- SERVICE_NAME: name of this service
- APP_VERSION: current version
- NODE_ENV/ENVIRONMENT: development or production

Include:
- Logger initialization code
- Middleware for HTTP trace ID extraction/propagation
- Example usage in a route handler
```

### Generate Trace ID Middleware

```
Create middleware for my [Express/FastAPI] application that:

1. Extracts X-Trace-ID from incoming request headers
2. Generates a UUID if no trace ID is present
3. Adds trace ID to response headers
4. Makes trace ID available to all log statements in the request context
5. Propagates trace ID to outgoing HTTP calls

Include example of:
- Making an HTTP call to another service with trace ID
- Logging with trace ID in a service method
```

### Migrate from console.log

```
I have a [Node.js/Python] application that uses console.log/print everywhere.

Help me migrate to structured logging:

1. Find all console.log/print statements
2. Convert to structured log calls with appropriate level (info, warn, error)
3. Add context objects instead of string interpolation
4. Ensure errors include stack traces

Example to convert:
console.log(`User ${userId} logged in from ${ip}`);

Should become:
logger.info({ event: 'user_login', userId, ip });
```

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
3. Is context being cleared between requests? (structlog: `clear_contextvars()`)

### Problem: Logs too verbose / too expensive

**Solutions:**
1. Set `LOG_LEVEL=warn` in production
2. Use sampling for debug logs (log 1% of requests)
3. Redact large objects before logging
4. Use log rate limiting for noisy events

### Problem: Can't find logs for specific request

**Solutions:**
1. Ensure trace ID is returned to client (for support tickets)
2. Include trace ID in error responses
3. Set up alerts that include trace ID

---

## Quick Reference

### Environment Variables

| Variable | Default | Description |
|----------|---------|-------------|
| `LOG_LEVEL` | `info` | Minimum log level (debug, info, warn, error) |
| `SERVICE_NAME` | `unknown` | Name of service (for filtering) |
| `APP_VERSION` | `0.0.0` | Version for tracking deployments |
| `NODE_ENV` / `ENVIRONMENT` | `development` | Environment (affects formatting) |

### Log Fields (Required)

| Field | Description | Example |
|-------|-------------|---------|
| `timestamp` | ISO8601 timestamp | `2025-12-26T10:30:00Z` |
| `level` | Log level | `info`, `error` |
| `event` | What happened | `user_login`, `payment_failed` |
| `traceId` | Correlation ID | `abc-123` |
| `service` | Service name | `api`, `worker` |

### Headers

| Header | Direction | Description |
|--------|-----------|-------------|
| `X-Trace-ID` | In/Out | Simple trace ID |
| `traceparent` | In/Out | W3C standard (OpenTelemetry) |

---

## Verification Checklist

Before going to production:

- [ ] All `console.log` / `print` statements removed or converted
- [ ] Logs output JSON to stdout
- [ ] Every log line includes `traceId`
- [ ] Sensitive fields are redacted (password, apiKey, etc.)
- [ ] Error logs include stack traces
- [ ] Trace ID propagates to downstream services
- [ ] Trace ID returned in response headers
- [ ] LOG_LEVEL configurable via environment variable
- [ ] Logs viewable in aggregator (CloudWatch, Datadog, etc.)
- [ ] Can search logs by trace ID to follow a request

---

*Part of Mault Pro Production-Readiness Kit*
*Step 9 of 9 — Observability*
