from typing import Optional
from core.models.pay_types import PayTypes
from core.models.user_resume import UserResume
from pydantic import validator

from sqlmodel import Field, SQLModel

class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    pay_type: PayTypes
    name: Optional[str]
    paid: Optional[float] | None = 0.0
    to_pay: Optional[float] | None = 0.0

    @validator("pay_type")
    def validate_age(cls, v):
        if v not in PayTypes:
            raise ValueError("Tipo de pago no permitido")
        return v


    def get_user_resume(self):
        return UserResume(id=self.id, paid=self.paid, to_pay=self.to_pay)
    
    def update_user(self, user_resume):
        self.paid = user_resume.paid
        self.to_pay = user_resume.to_pay
        
