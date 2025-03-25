from fastapi import APIRouter, Depends, WebSocket, WebSocketDisconnect
from app.schemas import Message
from app.services import save_message, get_chat_history
from app.auth import verify_jwt_token

router = APIRouter()
active_connections = {}

@router.websocket("/ws/{user_id}")
async def websocket_endpoint(websocket: WebSocket, user_id: int):
    """Handles real-time messaging using WebSockets."""
    await websocket.accept()
    active_connections[user_id] = websocket
    try:
        while True:
            data = await websocket.receive_json()
            message = Message(**data)
            save_message(message)
            
            # Send message to receiver if online
            if message.receiver_id in active_connections:
                await active_connections[message.receiver_id].send_json(message.dict())

    except WebSocketDisconnect:
        del active_connections[user_id]

@router.get("/{sender_id}/{receiver_id}")
def fetch_chat_history(sender_id: int, receiver_id: int, token: dict = Depends(verify_jwt_token)):
    """Fetches chat history between two users."""
    return get_chat_history(sender_id, receiver_id)
