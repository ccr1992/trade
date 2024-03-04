from fastapi import FastAPI, status
from api.routers import user_routers
from api.routers import public_routers
from fastapi.exceptions import RequestValidationError
from api.exceptions import ObjectNotFoundError
from api.exceptions_handlers import (
  request_validation_exception_handler, 
  unhandled_exception_handler,
  handle_object_not_found
)

app = FastAPI(title="Trader",
              description="Trader",
              )
app.include_router(user_routers.router)
app.include_router(public_routers.router)

app.add_exception_handler(RequestValidationError,
                          request_validation_exception_handler)
app.add_exception_handler(ObjectNotFoundError, handle_object_not_found)

app.add_exception_handler(Exception, unhandled_exception_handler)

@app.get("/healthcheck",  status_code=status.HTTP_200_OK)

def healthcheck():
    return {"healthcheck": "Everything OK!"}
