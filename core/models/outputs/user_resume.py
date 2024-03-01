from pydantic import BaseModel, Field
class UserResume(BaseModel):
    user_id: int = Field(
        description="Identificador del usuario."
    )
    pending: float = Field(
        description="Cantidad pendiente por pagar."
    )
    paid: float = Field(
        description="Cantidad pagada."
    )