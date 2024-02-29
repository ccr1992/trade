from typing import Optional
from core.models.pay_types import PayTypes
from pydantic import validator

from sqlmodel import Field, SQLModel

class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    pay_type: PayTypes
    name: Optional[str]
    paid: Optional[float]
    to_pay: Optional[float]

    @validator("pay_type")
    def validate_age(cls, v):
        if v not in PayTypes:
            raise ValueError("Tipo de pago no permitido")
        return v

