from pydantic import BaseModel
from datetime import datetime

class RentalCreate(BaseModel):
    renter_id: int
    item_id: int
    start_date: datetime
    end_date: datetime

class RentalResponse(BaseModel):
    id: int
    renter_id: int
    item_id: int
    start_date: datetime
    end_date: datetime
    is_active: bool

    class Config:
        orm_mode = True
