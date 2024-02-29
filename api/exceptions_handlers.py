from fastapi import Request, status
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse


def request_validation_exception_handler(
    request: Request, exc: RequestValidationError
) -> JSONResponse:
    host = getattr(getattr(request, "client", None), "host", None)
    port = getattr(getattr(request, "client", None), "port", None)
    url = (
        f"{request.url.path}?{request.query_params}"
        if request.query_params
        else request.url.path
    )
    msg = (
        f"{host}:{port} - '{request.method} {url}' 422 Unprocessable Entity - "
        f"{exc.errors()} - {exc.body}"
    )
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content=jsonable_encoder(
            {"msg": msg, "detail": exc.errors(), "body": exc.body}
        ),
    )
