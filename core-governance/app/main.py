"""
Analog Economy - Core Governance API

FastAPI application serving as the central governance layer
for The Analog Economy game.
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Application metadata
APP_NAME = "Analog Economy Governance API"
APP_VERSION = "0.1.0"
APP_DESCRIPTION = """
The governance layer for The Analog Economy.

## Features

* **Telemetry Ingestion** - Receive and validate game telemetry
* **Gaian Governance** - Ethics filtering and policy enforcement
* **Novelty Scoring** - Calculate token rewards for player solutions
* **Data Export** - Package and deliver training data to buyers
"""

# Create FastAPI application
app = FastAPI(
    title=APP_NAME,
    version=APP_VERSION,
    description=APP_DESCRIPTION,
    docs_url="/docs",
    redoc_url="/redoc",
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # TODO: Restrict in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    """Root endpoint - health check."""
    return {"name": APP_NAME, "version": APP_VERSION, "status": "operational"}


@app.get("/health")
async def health_check():
    """Detailed health check endpoint."""
    return {
        "status": "healthy",
        "components": {
            "api": "operational",
            "gaian": "operational",
            "database": "not_configured",
            "ml_pipeline": "not_configured",
        },
    }


# TODO: Include routers from api/v1/
# from app.api.v1 import telemetry, payouts, exports
# app.include_router(telemetry.router, prefix="/api/v1")
# app.include_router(payouts.router, prefix="/api/v1")
# app.include_router(exports.router, prefix="/api/v1")


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
