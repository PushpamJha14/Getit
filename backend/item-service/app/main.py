from fastapi import FastAPI
from app.routes import router
import uvicorn

app = FastAPI(title="Item Service", version="1.0")

# Include item routes
app.include_router(router, prefix="/items")

@app.get("/")
def home():
    return {"message": "Item Service is Running"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8001)
