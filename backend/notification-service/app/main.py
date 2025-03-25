from fastapi import FastAPI
from app.routes import router
import uvicorn

app = FastAPI(title="Notification Service", version="1.0")

# Include notification routes
app.include_router(router, prefix="/notifications")

@app.get("/")
def home():
    return {"message": "Notification Service is Running"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8005)
