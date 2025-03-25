from fastapi import Request, HTTPException
import time

rate_limits = {}

def rate_limiter(request: Request, limit: int = 10, interval: int = 60):
    """Rate limiting middleware"""
    client_ip = request.client.host
    current_time = time.time()

    if client_ip not in rate_limits:
        rate_limits[client_ip] = []

    rate_limits[client_ip] = [t for t in rate_limits[client_ip] if current_time - t < interval]

    if len(rate_limits[client_ip]) >= limit:
        raise HTTPException(status_code=429, detail="Rate limit exceeded")

    rate_limits[client_ip].append(current_time)
