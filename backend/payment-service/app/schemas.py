from pydantic import BaseModel
from datetime import datetime

class PaymentCreate(BaseModel):
    rental_id: int
    amount: float

class PaymentResponse(BaseModel):
    id: int
    rental_id: int
    amount: float
    status: str
    payment_date: datetime

    class Config:
        orm_mode = True
