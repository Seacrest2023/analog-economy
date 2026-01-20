"""
Observability Module

Provides structured logging, tracing, and middleware for the Gaian service.
"""

from .middleware import TraceIDMiddleware
from .structlog_setup import configure_structlog, get_logger

__all__ = [
    "configure_structlog",
    "get_logger",
    "TraceIDMiddleware",
]
