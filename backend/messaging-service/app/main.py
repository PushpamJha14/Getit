from fastapi import FastAPI
from app.routes import router
import uvicorn

app = FastAPI(title="Messaging Service", version="1.0")

# Include messaging routes
app.include_router(router, prefix="/messages")

@app.get("/")
def home():
    return {"message": "Messaging Service is Running"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8006)
