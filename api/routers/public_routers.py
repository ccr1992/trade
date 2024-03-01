from fastapi import APIRouter, Request, status
from core.models.imputs.pipeline import Pipeline
from core.models.outputs.user_resume import UserResume
from fastapi.exceptions import RequestValidationError
from core.db.database_helper import DatabaseHelper
from fastapi.responses import JSONResponse
import traceback

router = APIRouter(
    prefix="/public_methods",
    tags=[],
    dependencies=[],
    responses={404: {"description": "Not found"}},
)

@router.post("/create_payment_pipeline")
async def create_payment_pipeline(request: Pipeline):
    try: 
        execute_pipeline(request)
        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content={
                "message": "OK",
                "detail": "Petición realizada correctamente",
            })
    except Exception as E:
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content={
                "message": "Internal Server Error",
                "detail": "Se ha producido un error inesperado",
                "traceback": traceback.format_exc(),
            }
        )

def execute_pipeline(pipeline):
    fiat = pipeline.payment
    user = DatabaseHelper.get_user(fiat.user_id)
    fiat.pay(user.pay_type)
    DatabaseHelper.add(fiat)
    #TODO AÑADIR PAGOS PARA BLOCKCAHIN Y TRADE


@router.get("/get_user_resume/{user_id}", status_code=status.HTTP_200_OK, response_model=UserResume)
async def get_resume(request: Request, user_id):
    return get_user_resume(user_id)

def get_user_resume(user_id):
    pass