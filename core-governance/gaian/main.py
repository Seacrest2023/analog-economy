"""
Gaian Governance Service - FastAPI Application

The core governance layer for The Analog Economy.
Processes player actions, calculates rewards, and captures training data.

Run with:
    uvicorn gaian.main:app --host 0.0.0.0 --port 8000 --reload

Architecture Rules:
- NEVER use datetime. ALWAYS use pendulum.
- NEVER use json. ALWAYS use orjson (ORJSONResponse).
- NEVER use print or loguru. ALWAYS use structlog.
"""

from contextlib import asynccontextmanager

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import ORJSONResponse
from gaian import __version__
from gaian.config import settings
from gaian.observability import TraceIDMiddleware, configure_structlog, get_logger
from gaian.routes import action_router, health_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Application lifespan manager.

    Handles startup and shutdown events.
    """
    # Configure structlog before anything else
    configure_structlog(
        log_level=settings.gaian_log_level,
        json_format=not settings.is_development,
    )

    logger = get_logger(__name__)

    # Startup
    logger.info(
        "gaian_service_starting",
        version=__version__,
        environment=settings.app_env,
        debug_mode=settings.app_debug,
        host=settings.gaian_host,
        port=settings.gaian_port,
        log_level=settings.gaian_log_level,
        sila_mock_enabled=settings.sila_mock_enabled,
    )

    # TODO: Initialize database connections
    # TODO: Initialize Redis connection
    # TODO: Initialize Qdrant connection
    # TODO: Load Gaian config from config.yaml

    logger.info("startup_complete", message="Ready to receive actions")

    yield

    # Shutdown
    logger.info("gaian_service_shutting_down")
    # TODO: Close database connections
    # TODO: Close Redis connection
    # TODO: Flush any pending training data


# Create FastAPI application with ORJSONResponse as default
app = FastAPI(
    title="Gaian Governance Service",
    description="""
    The core governance layer for The Analog Economy.

    ## Overview

    Gaian processes player actions from the UE5 client, calculates SILA rewards,
    and captures training data for AI model training.

    ## Key Endpoints

    - **POST /api/v1/action** - Process a player action (Golden Spike)
    - **GET /health** - Health check for container orchestration
    - **GET /ready** - Readiness check for dependencies

    ## Training Data

    All actions are logged in JSONL format for later processing into:
    - SFT (Supervised Fine-Tuning) datasets
    - DPO (Direct Preference Optimization) pairs
    - Trajectory data for embodied AI
    """,
    version=__version__,
    default_response_class=ORJSONResponse,
    docs_url="/docs" if settings.app_debug else None,
    redoc_url="/redoc" if settings.app_debug else None,
    openapi_url="/openapi.json" if settings.app_debug else None,
    lifespan=lifespan,
)


# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins_list,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Add TraceID middleware for request tracing
app.add_middleware(TraceIDMiddleware)


# Include routers
app.include_router(health_router)
app.include_router(action_router)


# Global exception handler
@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    """
    Global exception handler for unhandled errors.

    Logs the error and returns a generic error response.
    In production, this prevents leaking internal details.
    """
    logger = get_logger(__name__)
    logger.error(
        "unhandled_exception",
        exception_type=type(exc).__name__,
        exception_message=str(exc),
        path=request.url.path,
        exc_info=True,
    )

    if settings.app_debug:
        # In debug mode, return detailed error
        return ORJSONResponse(
            status_code=500,
            content={
                "error": "Internal Server Error",
                "detail": str(exc),
                "type": type(exc).__name__,
            },
        )
    else:
        # In production, return generic error
        return ORJSONResponse(
            status_code=500,
            content={
                "error": "Internal Server Error",
                "detail": "An unexpected error occurred",
            },
        )


# Root endpoint
@app.get("/", include_in_schema=False)
async def root():
    """Root endpoint - redirects to health check."""
    return {
        "service": "Gaian Governance Service",
        "version": __version__,
        "status": "running",
        "docs": "/docs" if settings.app_debug else "disabled",
        "health": "/health",
    }


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        "gaian.main:app",
        host=settings.gaian_host,
        port=settings.gaian_port,
        reload=settings.is_development,
        log_level=settings.gaian_log_level.lower(),
    )
