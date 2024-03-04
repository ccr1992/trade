from fastapi import APIRouter, Request, status
from core.models.trade import Trade
from fastapi.exceptions import RequestValidationError
from api.docs import examples_trade
from typing import Annotated
from fastapi import Body

# from src.models.requests import Requests

#TODO MOVER A OBJETO
from sqlmodel import  Session, create_engine, select, SQLModel
from core.db.database_helper import DatabaseHelper

router = APIRouter(
    prefix="/trades",
    tags=[],
    dependencies=[],
    responses={404: {"description": "Not found"}},
)


@router.post("/create", tags=["database"], status_code=status.HTTP_200_OK)
async def createTrade(request: Annotated[Trade,
        Body(examples=examples_trade)]):
    try:
      Trade.validate(request)
    except Exception as e:
        raise RequestValidationError(e)
    create_trade(request)
    return {"healthcheck": "Everything OK!"}

def create_trade(trade):
    DatabaseHelper.add(trade)

@router.get("/get/{trade_id}", status_code=status.HTTP_200_OK, response_model=Trade, tags=["database"])
async def get(request: Request, trade_id):
    return get_trade(trade_id)

def get_trade(trade_id):
    return DatabaseHelper.get_trade(trade_id)

