from typing import Optional
from enum import Enum
from pydantic import validator

from sqlmodel import Field, SQLModel
class PayTypes(Enum):
    type_A = 0
    type_B = 1

class User(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    pay_type: PayTypes
    name: Optional[str]
    paid: Optional[float]
    to_pay: Optional[float]

    @validator("pay_type")
    def validate_age(cls, v):
        if v not in PayTypes:
            raise ValueError("Tipo de pago no permitido")
        return v
