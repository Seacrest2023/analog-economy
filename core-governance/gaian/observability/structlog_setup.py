"""
Structlog Configuration

Configures structlog for JSON-formatted logging with pendulum timestamps.
Redirects stdlib logging to structlog for unified log output.

Architecture Rules:
- NEVER use datetime. ALWAYS use pendulum.
- NEVER use print or loguru. ALWAYS use structlog.
"""

import logging
import sys

import pendulum
import structlog
from structlog.types import EventDict, Processor


def pendulum_timestamper(
    logger: logging.Logger, method_name: str, event_dict: EventDict
) -> EventDict:
    """
    Add a UTC timestamp to log events using pendulum.

    Uses pendulum.now("UTC") for consistent, timezone-aware timestamps.
    """
    event_dict["timestamp"] = pendulum.now("UTC").isoformat()
    return event_dict


def configure_structlog(
    log_level: str = "INFO",
    json_format: bool = True,
) -> None:
    """
    Configure structlog with JSON output and pendulum timestamps.

    Args:
        log_level: The logging level (DEBUG, INFO, WARNING, ERROR, CRITICAL)
        json_format: If True, output JSON. If False, output colored console logs.
    """
    # Common processors for all configurations
    shared_processors: list[Processor] = [
        structlog.contextvars.merge_contextvars,
        structlog.stdlib.add_log_level,
        structlog.stdlib.add_logger_name,
        structlog.stdlib.PositionalArgumentsFormatter(),
        pendulum_timestamper,
        structlog.processors.StackInfoRenderer(),
        structlog.processors.UnicodeDecoder(),
    ]

    if json_format:
        # JSON format for production
        processors: list[Processor] = [
            *shared_processors,
            structlog.processors.format_exc_info,
            structlog.processors.JSONRenderer(),
        ]
    else:
        # Colored console output for development
        processors = [
            *shared_processors,
            structlog.dev.ConsoleRenderer(colors=True),
        ]

    # Configure structlog
    structlog.configure(
        processors=processors,
        wrapper_class=structlog.stdlib.BoundLogger,
        context_class=dict,
        logger_factory=structlog.stdlib.LoggerFactory(),
        cache_logger_on_first_use=True,
    )

    # Redirect stdlib logging to structlog
    logging.basicConfig(
        format="%(message)s",
        stream=sys.stdout,
        level=getattr(logging, log_level.upper()),
    )

    # Silence noisy loggers
    logging.getLogger("uvicorn.access").setLevel(logging.WARNING)
    logging.getLogger("httpx").setLevel(logging.WARNING)


def get_logger(name: str | None = None) -> structlog.stdlib.BoundLogger:
    """
    Get a structlog logger instance.

    Args:
        name: Optional logger name. If None, uses the calling module's name.

    Returns:
        A bound structlog logger.
    """
    # structlog.get_logger() returns Any due to missing type stubs
    return structlog.get_logger(name)  # type: ignore[no-any-return]  # IRON_DOME_EXEMPT: structlog lacks type stubs
