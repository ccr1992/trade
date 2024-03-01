from sqlmodel import Field
from core.models.payment_base import PaymentBase
from typing import Optional
from core.models.pay_types import PayTypes

class FiatPayment(PaymentBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)

    def pay(self, mode: PayTypes):
        self.convert()
        super().pay(mode)

    def convert(self):
        pass