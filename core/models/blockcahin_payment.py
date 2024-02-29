from typing import Optional
from core.models.payment_base import PaymentBase

from sqlmodel import Field


class BlockchainPayment(PaymentBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
