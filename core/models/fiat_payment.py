from typing import Optional
from enum import IntEnum
from pydantic import validator

from sqlmodel import Field, SQLModel


class FiatPayment(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    value: int
    full_paid: bool | None = False
    
    user_id: int = Field(default=None, foreign_key="user.id")

    @validator("value")
    def validate_value(cls, v):
        if v <= 0:
            raise ValueError("Se requiere una cantidad positiva")
        return v
    

