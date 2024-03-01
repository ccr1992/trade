from sqlmodel import Field
from sqlmodel import Field, SQLModel
from typing import Optional
from core.models.paymentAbc import PaymentABC
from trade.core.models.blockchain_payment import BlockchainPayment

class Trade(SQLModel, PaymentABC, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)

    tax_block_chain: float = None

    def pay(self, price, mode, user_id):
        payment = BlockchainPayment(value=price, tax=self.tax_block_chain, user_id= user_id)
        payment.pay(price, mode)
        pass