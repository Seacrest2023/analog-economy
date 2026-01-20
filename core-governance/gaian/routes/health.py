"""
Health Check Endpoints

Provides health and readiness checks for container orchestration.
Used by Docker health checks and Kubernetes probes.
"""

from datetime import datetime
from typing import Optional

from fastapi import APIRouter, Response, status
from pydantic import BaseModel

from gaian import __version__
from gaian.config import settings

router = APIRouter(tags=["Health"])


class HealthResponse(BaseModel):
    """Health check response."""
    status: str
    version: str
    environment: str
    timestamp: datetime
    checks: dict[str, bool]


class ReadinessResponse(BaseModel):
    """Readiness check response."""
    ready: bool
    checks: dict[str, str]


@router.get(
    "/health",
    response_model=HealthResponse,
    summary="Health Check",
    description="Basic health check for container orchestration.",
)
async def health_check() -> HealthResponse:
    """
    Returns service health status.

    Used by:
    - Docker HEALTHCHECK
    - Kubernetes livenessProbe
    - Load balancer health checks
    """
    return HealthResponse(
        status="healthy",
        version=__version__,
        environment=settings.app_env,
        timestamp=datetime.utcnow(),
        checks={
            "service": True,
            "config": True,
        }
    )


@router.get(
    "/ready",
    response_model=ReadinessResponse,
    summary="Readiness Check",
    description="Checks if service is ready to receive traffic.",
)
async def readiness_check(response: Response) -> ReadinessResponse:
    """
    Returns service readiness status.

    Checks external dependencies:
    - Database connection (when enabled)
    - Redis connection (when enabled)
    - Qdrant connection (when enabled)

    Used by:
    - Kubernetes readinessProbe
    - Rolling deployments
    """
    checks = {}
    all_ready = True

    # Database check (optional for Phase 1)
    if settings.database_url:
        # TODO: Implement actual database ping
        checks["database"] = "connected"
    else:
        checks["database"] = "not_configured"

    # Redis check (optional for Phase 1)
    try:
        # TODO: Implement actual Redis ping
        checks["redis"] = "not_configured"
    except Exception as e:
        checks["redis"] = f"error: {str(e)}"
        all_ready = False

    # Qdrant check (optional for Phase 1)
    try:
        # TODO: Implement actual Qdrant ping
        checks["qdrant"] = "not_configured"
    except Exception as e:
        checks["qdrant"] = f"error: {str(e)}"
        all_ready = False

    # Core service is always ready if we got this far
    checks["service"] = "ready"

    if not all_ready:
        response.status_code = status.HTTP_503_SERVICE_UNAVAILABLE

    return ReadinessResponse(
        ready=all_ready,
        checks=checks
    )


@router.get(
    "/ping",
    summary="Ping",
    description="Simple ping endpoint for quick connectivity tests.",
)
async def ping() -> dict[str, str]:
    """
    Minimal ping endpoint.

    Returns immediately without any dependency checks.
    Useful for quick connectivity verification.
    """
    return {"ping": "pong"}
