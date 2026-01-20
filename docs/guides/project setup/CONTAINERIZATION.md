# Containerization — The Analog Economy

> **Step 3 of 8:** Package services for consistent execution across development, CI, and production.

---

## Overview

The Analog Economy uses containers for backend services while the UE5 client runs natively. This hybrid approach:

- **Containerized:** Gaian governance service, databases, caches
- **Native:** Unreal Engine 5 client (communicates with containers via HTTP/WebSocket)

```
┌─────────────────────────────────────────────────────────────────────────┐
│                    ANALOG ECONOMY ARCHITECTURE                           │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                         │
│   ┌───────────────┐         HTTP/WS          ┌───────────────────────┐ │
│   │   UE5 Client  │ ◄─────────────────────► │   Docker Network      │ │
│   │   (Native)    │      localhost:8000      │                       │ │
│   │               │                          │  ┌─────────────────┐  │ │
│   │  Windows/Mac  │                          │  │  Gaian (8000)   │  │ │
│   │  Development  │                          │  │  Python/FastAPI │  │ │
│   └───────────────┘                          │  └────────┬────────┘  │ │
│                                              │           │           │ │
│                                              │  ┌────────▼────────┐  │ │
│                                              │  │ PostgreSQL(5432)│  │ │
│                                              │  │ Redis (6379)    │  │ │
│                                              │  │ Qdrant (6333)   │  │ │
│                                              │  └─────────────────┘  │ │
│                                              └───────────────────────┘ │
│                                                                         │
└─────────────────────────────────────────────────────────────────────────┘
```

---

## Project Structure

```
analog-economy/
├── core-governance/
│   ├── Dockerfile              # Gaian service container
│   ├── .dockerignore           # Build exclusions
│   ├── requirements.txt        # Python dependencies
│   └── gaian/                  # Python package
│       ├── __init__.py
│       ├── main.py             # FastAPI entry point (to create)
│       ├── config.yaml         # Service configuration
│       └── ...
│
├── docker-compose.yml          # Local development orchestration
├── .env.example                # Environment template
├── .env                        # Local environment (gitignored)
│
└── client-simulation/          # UE5 project (not containerized)
```

---

## Service Configuration

### Gaian Service (core-governance)

The Python/FastAPI governance engine that processes player actions and returns SILA rewards.

**Location:** `core-governance/Dockerfile`

```dockerfile
# =============================================================================
# Analog Economy - Gaian Governance Service
# =============================================================================
# Multi-stage build: builder → production → development
# =============================================================================

# -----------------------------------------------------------------------------
# Stage 1: Builder - Install dependencies
# -----------------------------------------------------------------------------
FROM python:3.12-slim AS builder

WORKDIR /app

# Install build dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Create virtual environment
RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# -----------------------------------------------------------------------------
# Stage 2: Production - Minimal runtime image
# -----------------------------------------------------------------------------
FROM python:3.12-slim AS production

LABEL maintainer="Analog Economy Team"
LABEL description="Gaian Governance Service"
LABEL version="0.1.0"

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONFAULTHANDLER=1 \
    PATH="/opt/venv/bin:$PATH" \
    APP_ENV=production \
    APP_PORT=8000

WORKDIR /app

# Security: Create non-root user
RUN groupadd --gid 1000 gaian && \
    useradd --uid 1000 --gid gaian --shell /bin/bash --create-home gaian

# Copy virtual environment from builder
COPY --from=builder /opt/venv /opt/venv

# Copy application code
COPY --chown=gaian:gaian . .

USER gaian

EXPOSE 8000

HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD python -c "import httpx; httpx.get('http://localhost:8000/health', timeout=5)" || exit 1

CMD ["uvicorn", "gaian.main:app", "--host", "0.0.0.0", "--port", "8000"]

# -----------------------------------------------------------------------------
# Stage 3: Development - Hot reload enabled
# -----------------------------------------------------------------------------
FROM production AS development

USER root
RUN pip install --no-cache-dir watchfiles
USER gaian

ENV APP_ENV=development

CMD ["uvicorn", "gaian.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
```

### Docker Compose (Local Development)

**Location:** `docker-compose.yml`

```yaml
# =============================================================================
# Analog Economy - Local Development Stack
# =============================================================================
# Usage:
#   docker compose up              # Start all services
#   docker compose up gaian        # Start only Gaian
#   docker compose up -d           # Start detached
#   docker compose logs -f gaian   # Follow Gaian logs
#   docker compose down            # Stop all services
#   docker compose down -v         # Stop and remove volumes
# =============================================================================

services:
  # ---------------------------------------------------------------------------
  # Gaian - Core Governance Service
  # ---------------------------------------------------------------------------
  gaian:
    build:
      context: ./core-governance
      dockerfile: Dockerfile
      target: development
    container_name: analog-gaian
    ports:
      - "8000:8000"
    volumes:
      - ./core-governance:/app
      - /app/.venv
    environment:
      - APP_ENV=development
      - APP_PORT=8000
      - LOG_LEVEL=DEBUG
      - DATABASE_URL=postgresql://gaian:gaian@postgres:5432/analog_economy  # pragma: allowlist secret
      - REDIS_URL=redis://redis:6379/0
      - QDRANT_HOST=qdrant
      - QDRANT_PORT=6333
    healthcheck:
      test: ["CMD", "python", "-c", "import httpx; httpx.get('http://localhost:8000/health', timeout=5)"]
      interval: 30s
      timeout: 10s
      retries: 3
      start_period: 10s
    restart: unless-stopped
    depends_on:
      postgres:
        condition: service_healthy
      redis:
        condition: service_healthy
    networks:
      - analog-network

  # ---------------------------------------------------------------------------
  # PostgreSQL - Primary Database
  # ---------------------------------------------------------------------------
  postgres:
    image: postgres:16-alpine
    container_name: analog-postgres
    environment:
      POSTGRES_USER: gaian
      POSTGRES_PASSWORD: gaian_dev_password
      POSTGRES_DB: analog_economy
    ports:
      - "5432:5432"
    volumes:
      - postgres_data:/var/lib/postgresql/data
      - ./ops-infra/db/init:/docker-entrypoint-initdb.d
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U gaian -d analog_economy"]
      interval: 10s
      timeout: 5s
      retries: 5
    restart: unless-stopped
    networks:
      - analog-network

  # ---------------------------------------------------------------------------
  # Redis - Cache & Session Store
  # ---------------------------------------------------------------------------
  redis:
    image: redis:7-alpine
    container_name: analog-redis
    ports:
      - "6379:6379"
    volumes:
      - redis_data:/data
    command: redis-server --appendonly yes
    healthcheck:
      test: ["CMD", "redis-cli", "ping"]
      interval: 10s
      timeout: 5s
      retries: 5
    restart: unless-stopped
    networks:
      - analog-network

  # ---------------------------------------------------------------------------
  # Qdrant - Vector Database for Training Data
  # ---------------------------------------------------------------------------
  qdrant:
    image: qdrant/qdrant:latest
    container_name: analog-qdrant
    ports:
      - "6333:6333"
      - "6334:6334"
    volumes:
      - qdrant_data:/qdrant/storage
    environment:
      - QDRANT__SERVICE__GRPC_PORT=6334
    restart: unless-stopped
    networks:
      - analog-network

networks:
  analog-network:
    driver: bridge
    name: analog-economy-network

volumes:
  postgres_data:
  redis_data:
  qdrant_data:
```

### Docker Ignore

**Location:** `core-governance/.dockerignore`

```dockerignore
# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
.venv/
venv/
ENV/
.eggs/
*.egg-info/
*.egg
.mypy_cache/
.pytest_cache/
.ruff_cache/
.coverage
htmlcov/

# IDE
.idea/
.vscode/
*.swp
*.swo

# Git
.git/
.gitignore

# Docker (prevent recursive)
Dockerfile*
docker-compose*
.docker/

# Documentation
docs/
*.md
!README.md

# Tests (exclude from production)
tests/
test_*.py
*_test.py
conftest.py

# Local config
.env
.env.*
*.local

# Logs
logs/
*.log

# OS
.DS_Store
Thumbs.db
```

---

## Development Workflow

### First-Time Setup

```powershell
# 1. Copy environment template
copy .env.example .env

# 2. Edit .env with your local values
notepad .env

# 3. Build and start services
docker compose up --build

# 4. Verify services are running
docker compose ps
```

### Daily Development

```powershell
# Start services (detached)
docker compose up -d

# View logs
docker compose logs -f gaian

# Restart after code changes (if hot reload isn't working)
docker compose restart gaian

# Stop services
docker compose down
```

### Connecting UE5 Client

The UE5 client runs natively and connects to containerized services:

```cpp
// In your UE5 GaianClient.cpp
const FString GaianEndpoint = TEXT("http://localhost:8000/api/v1/action");
```

Ensure Docker's network allows host access (default configuration works on Windows/Mac).

---

## Service Endpoints

| Service | Internal URL | External URL | Purpose |
|---------|--------------|--------------|---------|
| Gaian | `http://gaian:8000` | `http://localhost:8000` | Governance API |
| PostgreSQL | `postgres:5432` | `localhost:5432` | Primary database |
| Redis | `redis:6379` | `localhost:6379` | Cache/sessions |
| Qdrant | `qdrant:6333` | `localhost:6333` | Vector search |

### Health Check Endpoints

```bash
# Gaian health
curl http://localhost:8000/health

# PostgreSQL
docker compose exec postgres pg_isready -U gaian

# Redis
docker compose exec redis redis-cli ping

# Qdrant
curl http://localhost:6333/health
```

---

## Environment Configuration

### Required Variables

```env
# Application
APP_ENV=development
APP_PORT=8000
LOG_LEVEL=DEBUG

# Database
DATABASE_URL=postgresql://gaian:gaian_dev_password@postgres:5432/analog_economy  # pragma: allowlist secret

# Redis
REDIS_URL=redis://redis:6379/0

# Qdrant
QDRANT_HOST=qdrant
QDRANT_PORT=6333

# Training Data
TRAINING_DATA_PATH=./data/training
TRAINING_LOG_FORMAT=jsonl
```

### Production Overrides

For production deployment, these change:

```env
APP_ENV=production
LOG_LEVEL=INFO
DATABASE_URL=<production-connection-string>
# etc.
```

---

## Troubleshooting

### Container Won't Start

```powershell
# Check logs
docker compose logs gaian

# Common issues:
# 1. Port already in use → Change port mapping or stop conflicting service
# 2. Missing main.py → Create gaian/main.py with FastAPI app
# 3. Dependency error → Rebuild: docker compose build --no-cache gaian
```

### Database Connection Refused

```powershell
# Verify postgres is healthy
docker compose ps

# Check postgres logs
docker compose logs postgres

# Connect directly
docker compose exec postgres psql -U gaian -d analog_economy
```

### UE5 Can't Connect to Gaian

```powershell
# 1. Verify Gaian is running
curl http://localhost:8000/health

# 2. Check Windows Firewall isn't blocking
# 3. Verify you're using localhost, not 127.0.0.1 in some cases
# 4. Check Docker Desktop is running
```

### Hot Reload Not Working

```powershell
# Restart with rebuild
docker compose down
docker compose up --build gaian

# Or force recreate
docker compose up --force-recreate gaian
```

---

## Production Considerations

### Building Production Image

```powershell
# Build production target
docker build --target production -t analog-gaian:latest ./core-governance

# Tag for registry
docker tag analog-gaian:latest your-registry.io/analog-gaian:v0.1.0

# Push to registry
docker push your-registry.io/analog-gaian:v0.1.0
```

### Security Checklist

- [ ] Non-root user in container (implemented)
- [ ] No secrets in Dockerfile (use environment variables)
- [ ] Minimal base image (python:3.12-slim)
- [ ] Health checks defined
- [ ] Resource limits set (in production compose/k8s)
- [ ] Image scanning enabled in CI/CD
- [ ] TLS termination at load balancer

### Resource Limits (Production)

```yaml
# Add to docker-compose.prod.yml
services:
  gaian:
    deploy:
      resources:
        limits:
          cpus: '2'
          memory: 2G
        reservations:
          cpus: '0.5'
          memory: 512M
```

---

## Commands Reference

```powershell
# Build
docker compose build                    # Build all services
docker compose build gaian              # Build specific service
docker compose build --no-cache         # Build without cache

# Run
docker compose up                       # Start (foreground)
docker compose up -d                    # Start (detached)
docker compose up gaian postgres        # Start specific services

# Logs
docker compose logs                     # All logs
docker compose logs -f gaian            # Follow Gaian logs
docker compose logs --tail=100 gaian    # Last 100 lines

# Execute
docker compose exec gaian bash          # Shell into Gaian
docker compose exec postgres psql -U gaian -d analog_economy

# Stop
docker compose down                     # Stop services
docker compose down -v                  # Stop and remove volumes

# Cleanup
docker system prune                     # Remove unused data
docker volume prune                     # Remove unused volumes
```

---

## Verification Checklist

After setup, verify:

- [ ] `docker compose up` starts without errors
- [ ] `curl http://localhost:8000/health` returns 200
- [ ] PostgreSQL accepts connections
- [ ] Redis responds to PING
- [ ] Qdrant dashboard accessible at `http://localhost:6333/dashboard`
- [ ] UE5 client can reach `http://localhost:8000`
- [ ] Hot reload works (edit Python file, see change)
- [ ] Logs are visible with `docker compose logs -f`

---

## Next Steps

Once containerization is verified:

1. **Create `gaian/main.py`** — FastAPI application entry point
2. **Implement `/health` endpoint** — Required for health checks
3. **Implement `/api/v1/action` endpoint** — Golden Spike target
4. **Test UE5 → Gaian communication** — Validate the pipeline

See: [Phase 1: Golden Spike](../../development/phase-1-golden-spike.md)

---

*Part of The Analog Economy Production-Readiness Setup — Step 3 of 8*
