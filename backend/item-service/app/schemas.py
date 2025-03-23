from pydantic import BaseModel
from typing import Optional

class ItemCreate(BaseModel):
    name: str
    description: Optional[str] = None
    price_per_day: float
    owner_id: int

class ItemResponse(BaseModel):
    id: int
    name: str
    description: Optional[str]
    price_per_day: float
    owner_id: int
    is_available: bool

    class Config:
        orm_mode = True
