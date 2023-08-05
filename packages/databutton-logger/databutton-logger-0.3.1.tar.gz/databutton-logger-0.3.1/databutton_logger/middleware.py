import contextvars
import sys
import traceback
from typing import Awaitable, Callable

from fastapi import Request, Response
from loguru import logger

http_request_context = contextvars.ContextVar("http_request_context", default=None)


async def http_request_middleware_func(
    request: Request, call_next: Callable[[Request], Awaitable[Response]]
):
    """Middleware function that can"""
    http_request = {
        "requestMethod": request.method,
        "requestUrl": request.url.path,
        "requestSize": sys.getsizeof(request),
        "remoteIp": request.client.host,
        "protocol": request.url.scheme,
    }
    if "referrer" in request.headers:
        http_request["referrer"] = request.headers.get("referrer")

    if "user-agent" in request.headers:
        http_request["userAgent"] = request.headers.get("user-agent")
    token = http_request_context.set(http_request)
    try:
        response = await call_next(request)
        logger.info(
            f"{http_request['remoteIp']} - {http_request['requestMethod']} {http_request['requestUrl']}"
            + f" - {response.status_code}"
        )
    except Exception as e:
        # Log the error nicely with loguru
        logger.error(traceback.format_exc())
        raise e
    finally:
        # Reset http_context
        http_request_context.reset(token)
    return response
