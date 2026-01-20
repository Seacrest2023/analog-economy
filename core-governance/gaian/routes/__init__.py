"""
Gaian API Routes

FastAPI routers for different API endpoints.
"""

from .health import router as health_router
from .action import router as action_router

__all__ = [
    "health_router",
    "action_router",
]
