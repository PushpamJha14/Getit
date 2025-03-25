from fastapi import FastAPI
from app.routes import router
import uvicorn

app = FastAPI(title="API Gateway", version="1.0")

# Include API Gateway routes
app.include_router(router)

@app.get("/")
def home():
    return {"message": "API Gateway is Running"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
