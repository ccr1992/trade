from sqlmodel import Field
from sqlmodel import Field, SQLModel
from typing import Optional
from core.models.blockchain_payment import BlockchainPayment
from core.models.paymentAbc import PaymentABC
from core.models.trade_payment import TradePayment
from core.models.pay_types import PayTypes
from pydantic import ValidationError
from fastapi.exceptions import RequestValidationError

class Trade(SQLModel, PaymentABC, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)

    tax_trade: Optional[float] = None
    tax_block_chain: Optional[float] = None

    def pay(self, price, mode, user_resume):
        try:
            payment = TradePayment.validate({"value": price, "tax": self.tax_trade, "user_id": user_resume.id})
            # EN EL TRADE SIEMPRE SE COBRA TASA AL MOMENTO(TIPO A)
            user_resume = payment.pay(PayTypes.type_A, user_resume)
            paymentB = BlockchainPayment.validate({"value": payment.price_without_taxes(), "tax": self.tax_block_chain, "user_id": user_resume.id})
            user_resume = paymentB.pay(mode, user_resume)
            payments = [payment, paymentB]
            return user_resume, payments
        except ValidationError as e:
            raise RequestValidationError(e)
