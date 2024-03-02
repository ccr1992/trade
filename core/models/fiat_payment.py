from sqlmodel import Field
from core.models.payment_base import PaymentBase
from typing import Optional
from core.models.pay_types import PayTypes

class FiatPayment(PaymentBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    currency_code: Optional[str] = Field(default='USD') 

    def pay(self, mode: PayTypes, user_resume):
        self.convert()
        return super().pay(mode, user_resume)

    def convert(self):
        pass