from fastapi import APIRouter, Request, status
from core.models.user import User
from fastapi.exceptions import RequestValidationError

# from src.models.requests import Requests

#TODO MOVER A OBJETO
from sqlmodel import  Session, create_engine, select, SQLModel


router = APIRouter(
    prefix="/users",
    tags=[],
    dependencies=[],
    responses={404: {"description": "Not found"}},
)

@router.post("/create")
async def createUser(request: User):
    try:
      User.validate(request)
    except Exception as e:
        raise RequestValidationError(e)
    create_user(request)


def create_user(user):
    #TODO LLEVAR A CLASE DE MYSQL
    engine = create_engine("sqlite:///database.db")
    SQLModel.metadata.create_all(engine)

    with Session(engine) as session:
        session.add(user)
        session.commit()


