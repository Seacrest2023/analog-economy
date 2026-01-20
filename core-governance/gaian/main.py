"""
Gaian Governance Service - FastAPI Application

The core governance layer for The Analog Economy.
Processes player actions, calculates rewards, and captures training data.

Run with:
    uvicorn gaian.main:app --host 0.0.0.0 --port 8000 --reload
"""

from contextlib import asynccontextmanager

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from loguru import logger

from gaian import __version__
from gaian.config import settings
from gaian.routes import action_router, health_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Application lifespan manager.

    Handles startup and shutdown events.
    """
    # Startup
    logger.info("=" * 60)
    logger.info("Gaian Governance Service Starting")
    logger.info("=" * 60)
    logger.info(f"Version: {__version__}")
    logger.info(f"Environment: {settings.app_env}")
    logger.info(f"Debug Mode: {settings.app_debug}")
    logger.info(f"Host: {settings.gaian_host}:{settings.gaian_port}")
    logger.info(f"Log Level: {settings.gaian_log_level}")
    logger.info(f"SILA Mock: {settings.sila_mock_enabled}")
    logger.info("=" * 60)

    # TODO: Initialize database connections
    # TODO: Initialize Redis connection
    # TODO: Initialize Qdrant connection
    # TODO: Load Gaian config from config.yaml

    logger.info("Startup complete - Ready to receive actions")

    yield

    # Shutdown
    logger.info("Gaian Governance Service Shutting Down")
    # TODO: Close database connections
    # TODO: Close Redis connection
    # TODO: Flush any pending training data


# Create FastAPI application
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
    logger.error(f"Unhandled exception: {exc}", exc_info=True)

    if settings.app_debug:
        # In debug mode, return detailed error
        return JSONResponse(
            status_code=500,
            content={
                "error": "Internal Server Error",
                "detail": str(exc),
                "type": type(exc).__name__,
            },
        )
    else:
        # In production, return generic error
        return JSONResponse(
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
