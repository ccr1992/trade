from fastapi import FastAPI, status
from api.routers import user_routers
from fastapi.exceptions import RequestValidationError
from api.exceptions_handlers import request_validation_exception_handler

app = FastAPI(title="Trader",
              description="Trader",
              )
app.include_router(user_routers.router)

app.add_exception_handler(RequestValidationError,
                          request_validation_exception_handler)

@app.get("/healthcheck",  status_code=status.HTTP_200_OK)
def healthcheck():
    return {"healthcheck": "Everything OK!"}
