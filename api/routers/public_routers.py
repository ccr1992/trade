from fastapi import APIRouter, Request, status
from core.models.imputs.pipeline import Pipeline
from core.models.outputs.user_resume import UserResume
from fastapi.exceptions import RequestValidationError


router = APIRouter(
    prefix="/public_methods",
    tags=[],
    dependencies=[],
    responses={404: {"description": "Not found"}},
)

@router.post("/create_payment_pipeline")
async def create_payment_pipeline(request: Pipeline):
    pass



@router.get("/get_user_resume/{user_id}", status_code=status.HTTP_200_OK, response_model=UserResume)
async def get_resume(request: Request, user_id):
    return get_user_resume(user_id)

def get_user_resume(user_id):
    pass