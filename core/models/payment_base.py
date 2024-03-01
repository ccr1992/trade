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

    def pay(self, mode: PayTypes):
        match mode:
          case PayTypes.type_A:
              self._pay_type_a()
          case PayTypes.type_B:
              self._pay_type_b()
          case _:
            raise NotImplementedError("No se ha implementado lógica para este método de pago.")
    
    def _pay_type_a(self):
       pass
    
    def _pay_type_b(self):
       pass
    
    @validator("value")
    def validate_value(cls, v):
        if v <= 0:
            raise ValueError("Se requiere una cantidad positiva")
        return v
    
    @validator("tax")
    def validate_tax(cls, v):
        if v < 0:
            raise ValueError("Se requiere una cantidad mayor o igual a 0")
        return v