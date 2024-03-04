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

@router.post("/create", tags=["database"])
async def createUser(request: User):
    try:
      User.validate(request)
    except Exception as e:
        raise RequestValidationError(e)
    create_user(request)


def create_user(user):
    #TODO LLEVAR A CLASE DE MYSQL
    DatabaseHelper.add(user)

@router.get("/get/{user_id}", status_code=status.HTTP_200_OK, response_model=User, tags=["database"])
async def get(request: Request, user_id):
    return get_user(user_id)

def get_user(user_id):
    engine = create_engine("sqlite:///database.db")

    with Session(engine) as session:
        statement = select(User).where(User.id == user_id)
        result  = session.exec(statement).first()
        return result

