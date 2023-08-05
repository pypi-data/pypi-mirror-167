import json
import logging
import os
import sys

from asgi_correlation_id import CorrelationIdMiddleware
from asgi_correlation_id.context import correlation_id
from fastapi import FastAPI
from loguru import logger
from starlette.middleware.base import BaseHTTPMiddleware

from .middleware import http_request_context, http_request_middleware_func


class InterceptHandler(logging.Handler):
    """
    Default handler from examples in loguru documentaion.
    See https://loguru.readthedocs.io/en/stable/overview.html#entirely-compatible-with-standard-logging
    """

    def emit(self, record: logging.LogRecord):
        # Get corresponding Loguru level if it exists
        try:
            level = logger.level(record.levelname).name
        except ValueError:
            level = record.levelno

        # Find caller from where originated the logged message
        frame, depth = logging.currentframe(), 2
        while frame.f_code.co_filename == logging.__file__:
            frame = frame.f_back
            depth += 1

        logger.opt(depth=depth, exception=record.exc_info).log(
            level, record.getMessage()
        )


def stackdriver_sink(message):
    record = message.record
    corr_id = correlation_id.get()
    http_request = http_request_context.get()
    log_info = {
        "severity": record["level"].name,
        "message": record["message"],
        "timestamp": record["time"].timestamp(),
        "logging.googleapis.com/sourceLocation": {
            "file": record["file"].name,
            "function": record["function"],
            "line": record["line"],
        },
    }
    if http_request is not None:
        log_info["httpRequest"] = http_request

    if corr_id is not None:
        log_info[
            "logging.googleapis.com/trace"
        ] = f"projects/databutton/traces/{correlation_id.get()}"

    serialized = json.dumps(log_info)
    print(serialized, file=sys.stderr)


def setup_logging_fastapi_gcp(app: FastAPI):
    app.add_middleware(BaseHTTPMiddleware, dispatch=http_request_middleware_func)
    app.add_middleware(CorrelationIdMiddleware)

    loggers = (
        logging.getLogger(name)
        for name in logging.root.manager.loggerDict
        if name.startswith("uvicorn.")
    )
    for uvicorn_logger in loggers:
        uvicorn_logger.handlers = []

    # change handler for default uvicorn logger
    intercept_handler = InterceptHandler()
    logging.getLogger("uvicorn").handlers = [intercept_handler]

    logger.remove()
    logger.add(
        stackdriver_sink,
        serialize=True,
        level=os.environ.get("LOGURU_LEVEL", "INFO"),
    )
