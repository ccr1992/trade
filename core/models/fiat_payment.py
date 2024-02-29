from sqlmodel import Field
from core.models.payment_base import PaymentBase
from typing import Optional

class FiatPayment(PaymentBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)

    user_id: int = Field(default=None, foreign_key="user.id")



