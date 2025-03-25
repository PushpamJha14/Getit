from fastapi import APIRouter, Depends, Request
import httpx
from app.auth import verify_jwt_token
from app.config import (
    USER_SERVICE_URL, ITEM_SERVICE_URL, RENTAL_SERVICE_URL, 
    PAYMENT_SERVICE_URL, SEARCH_SERVICE_URL, NOTIFICATION_SERVICE_URL, 
    MESSAGING_SERVICE_URL
)
from app.rate_limit import rate_limiter

router = APIRouter()

async def forward_request(request: Request, service_url: str):
    """Forward request to the respective microservice."""
    async with httpx.AsyncClient() as client:
        response = await client.request(
            method=request.method,
            url=f"{service_url}{request.url.path}",
            headers=request.headers.raw,
            content=await request.body()
        )
    return response.json()

@router.get("/users/{path:path}", dependencies=[Depends(rate_limiter)])
@router.post("/users/{path:path}", dependencies=[Depends(rate_limiter)])
async def user_service_proxy(request: Request, path: str):
    return await forward_request(request, USER_SERVICE_URL)

@router.get("/items/{path:path}", dependencies=[Depends(rate_limiter)])
@router.post("/items/{path:path}", dependencies=[Depends(rate_limiter)])
async def item_service_proxy(request: Request, path: str):
    return await forward_request(request, ITEM_SERVICE_URL)

@router.get("/rentals/{path:path}", dependencies=[Depends(rate_limiter)])
@router.post("/rentals/{path:path}", dependencies=[Depends(rate_limiter)])
async def rental_service_proxy(request: Request, path: str):
    return await forward_request(request, RENTAL_SERVICE_URL)

@router.get("/payments/{path:path}", dependencies=[Depends(rate_limiter)])
@router.post("/payments/{path:path}", dependencies=[Depends(rate_limiter)])
async def payment_service_proxy(request: Request, path: str):
    return await forward_request(request, PAYMENT_SERVICE_URL)

@router.get("/search/{path:path}", dependencies=[Depends(rate_limiter)])
@router.post("/search/{path:path}", dependencies=[Depends(rate_limiter)])
async def search_service_proxy(request: Request, path: str):
    return await forward_request(request, SEARCH_SERVICE_URL)

@router.get("/notifications/{path:path}", dependencies=[Depends(rate_limiter)])
@router.post("/notifications/{path:path}", dependencies=[Depends(rate_limiter)])
async def notification_service_proxy(request: Request, path: str):
    return await forward_request(request, NOTIFICATION_SERVICE_URL)

@router.websocket("/messaging/ws/{user_id}")
async def messaging_ws_proxy(user_id: int):
    """Proxy WebSocket connections to messaging-service."""
    async with httpx.AsyncClient() as client:
        async with client.websocket_connect(f"{MESSAGING_SERVICE_URL}/ws/{user_id}") as ws:
            async for message in ws.iter_text():
                yield message
