"""
Gaian API Routes

FastAPI routers for different API endpoints.
"""

from .action import router as action_router
from .health import router as health_router

__all__ = [
    "health_router",
    "action_router",
]
