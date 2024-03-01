from pydantic import BaseModel, Field
from core.models.fiat_payment import FiatPayment
class Pipeline(BaseModel):
    payment: FiatPayment = Field(
        description="Pago Fiat que inicia el pipeline."
    )
    trade_id: int = Field(
        description="Identificador del trade que se va a usar para efectuar el pago."
    )