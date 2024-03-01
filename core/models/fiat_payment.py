from sqlmodel import Field
from core.models.payment_base import PaymentBase
from typing import Optional
from core.models.pay_types import PayTypes

class FiatPayment(PaymentBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)

    user_id: int = Field(default=None, foreign_key="user.id")


    def pay(self, price, mode: PayTypes):
        self.convert()
        super().pay(price, mode)

    def convert(self):
        pass