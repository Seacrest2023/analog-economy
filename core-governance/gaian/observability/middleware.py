"""
Observability Middleware

Provides request tracing and context binding for structured logging.

Architecture Rules:
- NEVER use datetime. ALWAYS use pendulum.
- NEVER use print or loguru. ALWAYS use structlog.
"""

from uuid import uuid4

import structlog
from starlette.middleware.base import BaseHTTPMiddleware, RequestResponseEndpoint
from starlette.requests import Request
from starlette.responses import Response

logger = structlog.get_logger(__name__)


class TraceIDMiddleware(BaseHTTPMiddleware):
    """
    Middleware that ensures every request has a trace ID.

    - Checks for existing X-Trace-ID header from client
    - Generates a new UUID4 if not present
    - Binds the trace ID to structlog context for all logs
    - Adds X-Trace-ID to response headers
    """

    async def dispatch(self, request: Request, call_next: RequestResponseEndpoint) -> Response:
        """Process request and add trace ID."""
        # Get trace ID from header or generate new one
        trace_id = request.headers.get("X-Trace-ID")
        if not trace_id:
            trace_id = str(uuid4())

        # Bind trace ID to structlog context for this request
        structlog.contextvars.clear_contextvars()
        structlog.contextvars.bind_contextvars(
            trace_id=trace_id,
            method=request.method,
            path=request.url.path,
        )

        # Log request start
        logger.info("request_started")

        # Process request
        response = await call_next(request)

        # Add trace ID to response headers
        response.headers["X-Trace-ID"] = trace_id

        # Log request completion
        logger.info(
            "request_completed",
            status_code=response.status_code,
        )

        return response
