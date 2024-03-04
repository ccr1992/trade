from fastapi import APIRouter, Request, status
from core.models.imputs.pipeline import Pipeline
from core.models.user_resume import UserResume
from fastapi.exceptions import RequestValidationError
from core.db.database_helper import DatabaseHelper
from fastapi.responses import JSONResponse
import traceback
from typing import Annotated
from api.docs import examples_pipeline
from fastapi import Body

router = APIRouter(
    prefix="/public_methods",
    tags=[],
    dependencies=[],
    responses={404: {"description": "Not found"}},
)

@router.post("/create_payment_pipeline", tags=["publics"])
async def create_payment_pipeline(request:  Annotated[Pipeline ,
        Body(examples=examples_pipeline)]):
    execute_pipeline(request)
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={
            "message": "OK",
            "detail": "Petición realizada correctamente",
        })
   

def execute_pipeline(pipeline):
    fiat = pipeline.payment
    user = DatabaseHelper.get_user(fiat.user_id)
    user_resume = fiat.pay(user.pay_type, user.get_user_resume())
    trade = DatabaseHelper.get_trade(pipeline.trade_id)
    user_resume, payments = trade.pay(fiat.price_without_taxes(), user.pay_type, user_resume)
    DatabaseHelper.add(fiat)
    for payment in payments:
        DatabaseHelper.add(payment)
    user.update_user(user_resume)
    DatabaseHelper.update(user)
    return user_resume


@router.get("/get_user_resume/{user_id}", status_code=status.HTTP_200_OK, response_model=UserResume, tags=["publics"])
async def get_resume(request: Request, user_id):
    return get_user_resume(user_id)

def get_user_resume(user_id):
    return DatabaseHelper.get_user(user_id).get_user_resume()

