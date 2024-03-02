from core.models.pay_types import PayTypes
from core.models.paymentAbc import PaymentABC
from sqlmodel import Field, SQLModel
from typing import Optional, ClassVar
from pydantic import validator
class PaymentBase(SQLModel, PaymentABC):
    DEFAULT_TAX: ClassVar[float] = 0.01

    value: float
    full_paid: bool | None = False
    tax: float | None = DEFAULT_TAX

    user_id: int = Field(default=None, foreign_key="user.id")

    def pay(self, mode: PayTypes, user_resume):
        match mode:
          case PayTypes.type_A:
              return self._pay_type_a(user_resume)
          case PayTypes.type_B:
              return self._pay_type_b(user_resume)
          case _:
            raise NotImplementedError("No se ha implementado lógica para este método de pago.")
    
    def _pay_type_a(self, user_resume):
       _tax = self.value * self.tax
       user_resume.paid += _tax
       self.full_paid = True
       return user_resume
    
    def _pay_type_b(self, user_resume):
       _tax = self.value * self.tax
       user_resume.to_pay += _tax
       self.full_paid = False
       return user_resume
    
    def price_without_taxes(self):
        return self.value * (1-self.tax)

    @validator("value")
    def validate_value(cls, v):
        if v <= 0:
            raise ValueError("Se requiere una cantidad positiva")
        return v
    
    @validator("tax")
    def validate_tax(cls, v):
        if v is None:
            return cls.DEFAULT_TAX
        if v < 0 or v > 1:
            raise ValueError("Se requiere una cantidad mayor o igual a 0 y menor que 1")
        return v