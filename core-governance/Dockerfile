# =============================================================================
# Analog Economy - Core Governance (Gaian) Service
# =============================================================================
# Multi-stage build for production-ready Python service
# =============================================================================

# -----------------------------------------------------------------------------
# Stage 1: Builder
# -----------------------------------------------------------------------------
FROM python:3.12-slim as builder

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
# Stage 2: Production
# -----------------------------------------------------------------------------
FROM python:3.12-slim as production

# Labels
LABEL maintainer="Analog Economy Team"
LABEL description="Gaian Governance Service - Core decision engine"
LABEL version="0.1.0"

# Install curl for health checks
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONFAULTHANDLER=1 \
    PYTHONPATH=/app \
    PATH="/opt/venv/bin:$PATH" \
    APP_ENV=production \
    APP_PORT=8000

WORKDIR /app

# Create non-root user for security
RUN groupadd --gid 1000 gaian && \
    useradd --uid 1000 --gid gaian --shell /bin/bash --create-home gaian

# Copy virtual environment from builder
COPY --from=builder /opt/venv /opt/venv

# Copy application code
COPY --chown=gaian:gaian . .

# Switch to non-root user
USER gaian

# Expose port
EXPOSE 8000

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD curl -f http://localhost:8000/health || exit 1

# Run the application
CMD ["uvicorn", "gaian.main:app", "--host", "0.0.0.0", "--port", "8000"]

# -----------------------------------------------------------------------------
# Stage 3: Development (optional, for local dev with hot reload)
# -----------------------------------------------------------------------------
FROM production as development

USER root

# Install dev dependencies
RUN pip install --no-cache-dir watchfiles

USER gaian

ENV APP_ENV=development

# Hot reload for development
CMD ["uvicorn", "gaian.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
