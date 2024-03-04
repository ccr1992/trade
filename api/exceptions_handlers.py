from fastapi import Request, status
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
import sys
import traceback
from api.exceptions import ObjectNotFoundError


def request_validation_exception_handler(
    request: Request, exc: RequestValidationError
) -> JSONResponse:
    host, port, url = get_request_data(request)
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


def unhandled_exception_handler(
    request: Request, exc: Exception
) -> JSONResponse:
    host, port, url = get_request_data(request)
    msg = (
        f"{host}:{port} - '{request.method} {url}' 500 Internal Server Error "
        
    )
    return JSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        content={
            "message": "Internal Server Error",
            "detail": msg,
            "traceback": traceback.format_exc(),
        },
    )


async def handle_object_not_found(
     request: Request, exc: ObjectNotFoundError
) -> JSONResponse:
    host, port, url = get_request_data(request)
    msg = (
        f"{host}:{port} - '{request.method} {url}' 404 Not Found - "
    )
    response = JSONResponse(
        status_code=404, 
        content={
            "message": f"Object of type {exc.class_name} with ID {exc.object_id} not found",
            "detail": msg,
            "traceback": traceback.format_exc(),
        })
    return  response

def get_request_data(request):
    host = getattr(getattr(request, "client", None), "host", None)
    port = getattr(getattr(request, "client", None), "port", None)
    url = (
        f"{request.url.path}?{request.query_params}"
        if request.query_params
        else request.url.path
    )
    return host, port, url
