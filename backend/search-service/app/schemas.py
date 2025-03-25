from pydantic import BaseModel

class ItemCreate(BaseModel):
    id: int
    name: str
    description: str
    category: str
    price_per_day: float
    availability: bool

class SearchQuery(BaseModel):
    query: str
