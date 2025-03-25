from app.database import redis_client
from app.schemas import Message
import json

def save_message(message: Message):
    """Stores messages in Redis"""
    chat_key = f"chat:{message.sender_id}:{message.receiver_id}"
    redis_client.rpush(chat_key, json.dumps(message.dict()))

def get_chat_history(sender_id: int, receiver_id: int):
    """Retrieves chat history between two users"""
    chat_key = f"chat:{sender_id}:{receiver_id}"
    messages = redis_client.lrange(chat_key, 0, -1)
    return [json.loads(msg) for msg in messages]
