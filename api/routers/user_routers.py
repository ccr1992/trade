from fastapi import APIRouter, Request, status
from core.models.user import User
from fastapi.exceptions import RequestValidationError

# from src.models.requests import Requests

#TODO MOVER A OBJETO
from sqlmodel import  Session, create_engine, select, SQLModel
from core.db.database_helper import DatabaseHelper

router = APIRouter(
    prefix="/users",
    tags=[],
    dependencies=[],
    responses={404: {"description": "Not found"}},
)

@router.post("/create", tags=["database"], status_code=status.HTTP_200_OK)
async def createUser(request: User):
    try:
      User.validate(request)
    except Exception as e:
        raise RequestValidationError(e)
    create_user(request)

    return {"healthcheck": "Everything OK!"}


def create_user(user):
    DatabaseHelper.add(user)

@router.get("/get/{user_id}", status_code=status.HTTP_200_OK, response_model=User, tags=["database"])
async def get(request: Request, user_id):
    return get_user(user_id)

def get_user(user_id):
    return DatabaseHelper.get_user(user_id)

