# Environment Configuration — The Analog Economy

> **Step 2 of 8:** Configure environment variables for secure, reproducible development across all services.

---

## Overview

The Analog Economy uses environment variables to:
- Keep secrets out of source code
- Configure services for different environments (dev/staging/prod)
- Enable Docker containers to receive configuration at runtime
- Allow UE5 client to discover backend endpoints

```
┌─────────────────────────────────────────────────────────────────────────┐
│                    ENVIRONMENT CONFIGURATION FLOW                        │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                         │
│   .env.example          .env                 Docker/Runtime             │
│   ─────────────         ────                 ─────────────              │
│   Committed to Git      Your local secrets   Injected at start          │
│   Placeholders only     NEVER committed      From .env or secrets mgr   │
│                                                                         │
│   DATABASE_URL=...      DATABASE_URL=        → Container receives       │
│   (placeholder)         postgresql://...       actual value             │
│                                                                         │
└─────────────────────────────────────────────────────────────────────────┘
```

---

## Project Environment Structure

```
analog-economy/
├── .env.example              # Template (committed)
├── .env                      # Local development (gitignored)
├── .gitignore                # Ensures .env never committed
│
├── core-governance/
│   └── gaian/
│       ├── config.py         # Pydantic Settings validation
│       └── config.yaml       # Game configuration (committed)
│
└── docker-compose.yml        # Passes env vars to containers
```

---

## The Analog Economy .env.example

Our environment template is already established. Here's the complete reference:

```bash
# =============================================================================
# Analog Economy - Environment Configuration
# =============================================================================
# Copy to .env and fill in your values:
#   copy .env.example .env       (Windows)
#   cp .env.example .env         (Mac/Linux)
#
# NEVER commit .env to version control!
# =============================================================================

# =============================================================================
# APPLICATION SETTINGS
# =============================================================================

# Environment: development | staging | production
APP_ENV=development

# Debug mode (disable in production)
APP_DEBUG=true

# Secret key for JWT/session signing (generate with: openssl rand -base64 32)
APP_SECRET_KEY=change-me-in-production-use-strong-random-key

# =============================================================================
# GAIAN SERVICE
# =============================================================================

# Server binding
GAIAN_HOST=0.0.0.0
GAIAN_PORT=8000

# Logging: DEBUG | INFO | WARNING | ERROR
GAIAN_LOG_LEVEL=DEBUG

# Uvicorn workers (use CPU count in production)
GAIAN_WORKERS=1

# =============================================================================
# DATABASE (PostgreSQL)
# =============================================================================

# Connection string format: postgresql://user:password@host:port/database
DATABASE_URL=postgresql://gaian:gaian_dev_password@localhost:5432/analog_economy

# Connection pool settings
DATABASE_POOL_SIZE=5
DATABASE_MAX_OVERFLOW=10

# =============================================================================
# CACHE (Redis)
# =============================================================================

# Connection string format: redis://[:password@]host:port/db
REDIS_URL=redis://localhost:6379/0
REDIS_PASSWORD=

# =============================================================================
# VECTOR DATABASE (Qdrant)
# =============================================================================

# Qdrant connection for training data similarity search
QDRANT_HOST=localhost
QDRANT_PORT=6333
QDRANT_API_KEY=

# =============================================================================
# TRAINING DATA PIPELINE
# =============================================================================

# Where to store training data
TRAINING_DATA_PATH=./data/training

# Output format: jsonl | parquet
TRAINING_LOG_FORMAT=jsonl

# Batch size for processing
TRAINING_BATCH_SIZE=100

# =============================================================================
# SILA TOKEN (Development Mock)
# =============================================================================

# Use mock token for local development
SILA_MOCK_ENABLED=true

# Base reward per action (in SILA)
SILA_BASE_REWARD=0.01

# =============================================================================
# BLOCKCHAIN (Production Only)
# =============================================================================

# Web3 provider (Infura, Alchemy, etc.)
# WEB3_PROVIDER_URL=https://mainnet.infura.io/v3/YOUR_PROJECT_ID

# Contract addresses
# NOVELTY_TOKEN_CONTRACT=0x...
# ITEMS_CONTRACT=0x...
# LAND_CONTRACT=0x...

# Deployer wallet (KEEP SECRET - production only)
# DEPLOYER_PRIVATE_KEY=

# =============================================================================
# EXTERNAL AI SERVICES (Optional)
# =============================================================================

# OpenAI (for NPC dialogue enhancement)
# OPENAI_API_KEY=sk-...

# Anthropic (for ethical reasoning)
# ANTHROPIC_API_KEY=sk-ant-...

# =============================================================================
# AWS (Production Storage)
# =============================================================================

# AWS_ACCESS_KEY_ID=
# AWS_SECRET_ACCESS_KEY=
# AWS_REGION=us-east-1
# AWS_S3_BUCKET=analog-economy-data

# =============================================================================
# MONITORING
# =============================================================================

# Logging
LOG_LEVEL=INFO

# Error tracking
# SENTRY_DSN=

# Metrics
PROMETHEUS_ENABLED=false

# =============================================================================
# SECURITY
# =============================================================================

# JWT configuration
JWT_SECRET_KEY=
JWT_ALGORITHM=HS256
JWT_EXPIRATION_HOURS=24

# CORS (comma-separated origins)
CORS_ORIGINS=http://localhost:3000,http://localhost:8080

# =============================================================================
# FEATURE FLAGS
# =============================================================================

# Biome availability
FEATURE_UPRISING_BIOME=false
FEATURE_THEATER_BIOME=false

# Export functionality
FEATURE_DATA_EXPORT=false
```

---

## Environment Validation (Python)

Use Pydantic Settings to validate environment variables at startup. This ensures fast failure if configuration is missing.

**Create:** `core-governance/gaian/config.py`

```python
"""
Gaian Service Configuration
Validates environment variables at startup using Pydantic Settings.
"""

from functools import lru_cache
from typing import Optional
from pydantic import Field, field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """
    Application settings loaded from environment variables.
    Fails fast if required variables are missing.
    """

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore",
    )

    # -------------------------------------------------------------------------
    # Application
    # -------------------------------------------------------------------------
    app_env: str = Field(default="development", description="Environment name")
    app_debug: bool = Field(default=False, description="Debug mode")
    app_secret_key: str = Field(..., description="Secret key for signing")

    # -------------------------------------------------------------------------
    # Gaian Service
    # -------------------------------------------------------------------------
    gaian_host: str = Field(default="0.0.0.0", description="Server host")
    gaian_port: int = Field(default=8000, description="Server port")
    gaian_log_level: str = Field(default="INFO", description="Log level")
    gaian_workers: int = Field(default=1, description="Uvicorn workers")

    # -------------------------------------------------------------------------
    # Database
    # -------------------------------------------------------------------------
    database_url: str = Field(..., description="PostgreSQL connection string")
    database_pool_size: int = Field(default=5, description="Connection pool size")
    database_max_overflow: int = Field(default=10, description="Max overflow connections")

    # -------------------------------------------------------------------------
    # Redis
    # -------------------------------------------------------------------------
    redis_url: str = Field(default="redis://localhost:6379/0", description="Redis URL")
    redis_password: Optional[str] = Field(default=None, description="Redis password")

    # -------------------------------------------------------------------------
    # Qdrant
    # -------------------------------------------------------------------------
    qdrant_host: str = Field(default="localhost", description="Qdrant host")
    qdrant_port: int = Field(default=6333, description="Qdrant port")
    qdrant_api_key: Optional[str] = Field(default=None, description="Qdrant API key")

    # -------------------------------------------------------------------------
    # Training Data
    # -------------------------------------------------------------------------
    training_data_path: str = Field(default="./data/training", description="Training data directory")
    training_log_format: str = Field(default="jsonl", description="Log format")
    training_batch_size: int = Field(default=100, description="Batch size")

    # -------------------------------------------------------------------------
    # SILA Token
    # -------------------------------------------------------------------------
    sila_mock_enabled: bool = Field(default=True, description="Use mock SILA")
    sila_base_reward: float = Field(default=0.01, description="Base reward per action")

    # -------------------------------------------------------------------------
    # Security
    # -------------------------------------------------------------------------
    jwt_secret_key: Optional[str] = Field(default=None, description="JWT signing key")
    jwt_algorithm: str = Field(default="HS256", description="JWT algorithm")
    jwt_expiration_hours: int = Field(default=24, description="JWT expiration")
    cors_origins: str = Field(default="http://localhost:3000", description="CORS origins")

    # -------------------------------------------------------------------------
    # Feature Flags
    # -------------------------------------------------------------------------
    feature_uprising_biome: bool = Field(default=False)
    feature_theater_biome: bool = Field(default=False)
    feature_data_export: bool = Field(default=False)

    # -------------------------------------------------------------------------
    # Validators
    # -------------------------------------------------------------------------
    @field_validator("app_env")
    @classmethod
    def validate_app_env(cls, v: str) -> str:
        allowed = {"development", "staging", "production"}
        if v not in allowed:
            raise ValueError(f"app_env must be one of {allowed}")
        return v

    @field_validator("gaian_log_level")
    @classmethod
    def validate_log_level(cls, v: str) -> str:
        allowed = {"DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"}
        if v.upper() not in allowed:
            raise ValueError(f"gaian_log_level must be one of {allowed}")
        return v.upper()

    @property
    def is_production(self) -> bool:
        return self.app_env == "production"

    @property
    def is_development(self) -> bool:
        return self.app_env == "development"

    @property
    def cors_origins_list(self) -> list[str]:
        return [origin.strip() for origin in self.cors_origins.split(",")]


@lru_cache
def get_settings() -> Settings:
    """
    Get cached settings instance.
    Raises ValidationError if required variables are missing.
    """
    return Settings()


# Convenience export
settings = get_settings()
```

**Usage in FastAPI:**

```python
# gaian/main.py
from fastapi import FastAPI
from gaian.config import settings

app = FastAPI(
    title="Gaian Governance Service",
    debug=settings.app_debug,
)

@app.get("/health")
async def health():
    return {
        "status": "healthy",
        "environment": settings.app_env,
        "version": "0.1.0",
    }
```

---

## Docker Environment Integration

Docker Compose passes environment variables to containers from `.env`:

```yaml
# docker-compose.yml (relevant section)
services:
  gaian:
    environment:
      - APP_ENV=development
      - APP_DEBUG=true
      - DATABASE_URL=postgresql://gaian:gaian_dev_password@postgres:5432/analog_economy
      - REDIS_URL=redis://redis:6379/0
      - QDRANT_HOST=qdrant
      - QDRANT_PORT=6333
```

**Note:** Inside Docker network, use service names (`postgres`, `redis`, `qdrant`) not `localhost`.

---

## UE5 Client Configuration

The UE5 client needs to know where to find the Gaian service. This is configured via:

**Option 1: DefaultGame.ini**
```ini
[/Script/AnalogEconomy.GaianSettings]
GaianEndpoint=http://localhost:8000
GaianTimeout=30
```

**Option 2: Command Line**
```powershell
# Launch with custom endpoint
.\AnalogEconomy.exe -GaianEndpoint=http://localhost:8000
```

**Option 3: In-Game Settings**
Store in player preferences, editable from settings menu.

---

## Environment-Specific Configuration

### Development (Local)

```bash
# .env (local development)
APP_ENV=development
APP_DEBUG=true
DATABASE_URL=postgresql://gaian:gaian_dev_password@localhost:5432/analog_economy
SILA_MOCK_ENABLED=true
```

### Staging

```bash
# .env.staging
APP_ENV=staging
APP_DEBUG=false
DATABASE_URL=postgresql://gaian:staging_password@staging-db.example.com:5432/analog_economy
SILA_MOCK_ENABLED=true  # Still mock in staging
```

### Production

```bash
# .env.production (or cloud secrets manager)
APP_ENV=production
APP_DEBUG=false
DATABASE_URL=<from-secrets-manager>
SILA_MOCK_ENABLED=false
WEB3_PROVIDER_URL=https://mainnet.infura.io/v3/...
```

---

## Secret Management

### Development: .env Files

For local development, `.env` files are sufficient. Ensure:
- `.env` is in `.gitignore`
- Never commit real secrets
- Use `.env.example` as documentation

### Production: Cloud Secret Managers

| Provider | Service | Integration |
|----------|---------|-------------|
| AWS | Secrets Manager | boto3, IAM roles |
| GCP | Secret Manager | google-cloud-secret-manager |
| Azure | Key Vault | azure-identity |

**Example: AWS Secrets Manager**

```python
import boto3
import json

def get_secret(secret_name: str) -> dict:
    """Retrieve secret from AWS Secrets Manager."""
    client = boto3.client("secretsmanager")
    response = client.get_secret_value(SecretId=secret_name)
    return json.loads(response["SecretString"])

# Usage
if settings.is_production:
    secrets = get_secret("analog-economy/production")
    database_url = secrets["DATABASE_URL"]
```

---

## Generating Secrets

Use cryptographically secure methods to generate secrets:

```powershell
# Windows PowerShell - Generate 32-byte base64 secret
[Convert]::ToBase64String((1..32 | ForEach-Object { Get-Random -Maximum 256 }))

# Or use OpenSSL (if installed)
openssl rand -base64 32
```

```bash
# Mac/Linux
openssl rand -base64 32

# Python
python -c "import secrets; print(secrets.token_urlsafe(32))"
```

---

## Troubleshooting

### Variable Not Loading

```powershell
# Check if .env exists
dir .env

# Check if variable is set in environment
$env:DATABASE_URL

# In Python, debug loading
python -c "from gaian.config import settings; print(settings.database_url)"
```

### Docker Container Can't Connect

```powershell
# Inside Docker, use service names not localhost
# Wrong: DATABASE_URL=postgresql://...@localhost:5432/...
# Right: DATABASE_URL=postgresql://...@postgres:5432/...

# Check container networking
docker compose exec gaian ping postgres
```

### Pydantic Validation Error

```
pydantic_core._pydantic_core.ValidationError: 1 validation error for Settings
app_secret_key
  Field required [type=missing, input_value={...}]
```

**Fix:** Ensure all required variables are in `.env`:
```bash
# Check .env has the variable
cat .env | findstr APP_SECRET_KEY
```

---

## Verification Checklist

After environment setup, verify:

- [ ] `.env.example` exists with all variables documented
- [ ] `.env` created from `.env.example`
- [ ] `.env` is in `.gitignore`
- [ ] `git status` does NOT show `.env`
- [ ] `docker compose config` shows correct environment values
- [ ] Application starts without validation errors
- [ ] Health endpoint responds: `curl http://localhost:8000/health`
- [ ] No secrets in `.env.example` (only placeholders)

---

## Quick Reference

```powershell
# Copy template to create local .env
copy .env.example .env

# Edit with your values
notepad .env

# Verify gitignore is working
git status  # Should NOT show .env

# Start services with environment
docker compose up -d

# Check if container received variables
docker compose exec gaian env | findstr DATABASE

# Validate Python can load settings
docker compose exec gaian python -c "from gaian.config import settings; print(settings.app_env)"
```

---

## Next Steps

Once environment is configured:

1. **Run Docker stack:** `docker compose up -d`
2. **Verify health:** `curl http://localhost:8000/health`
3. **Proceed to Phase 1:** Create `gaian/main.py` FastAPI application

See: [Phase 1: Golden Spike](../../development/phase-1-golden-spike.md)

---

*Part of The Analog Economy Production-Readiness Setup — Step 2 of 8*
