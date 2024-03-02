from pydantic import BaseModel, Field
from typing import Optional

class UserResume(BaseModel):
    id: Optional[int] = Field(default=None, primary_key=True)

    to_pay: float = Field(
        description="Pago pendiente de cobro."
    )
    paid: float = Field(
        description="Pago realizado."
    )