from fastapi import FastAPI
from app.routes import router
import uvicorn

app = FastAPI(title="Payment Service", version="1.0")

# Include payment routes
app.include_router(router, prefix="/payments")

@app.get("/")
def home():
    return {"message": "Payment Service is Running"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8003)
