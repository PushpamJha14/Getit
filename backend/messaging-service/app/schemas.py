from pydantic import BaseModel
from datetime import datetime

class Message(BaseModel):
    sender_id: int
    receiver_id: int
    content: str
    timestamp: datetime = datetime.utcnow()
