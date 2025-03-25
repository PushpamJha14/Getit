from fastapi import FastAPI
from app.routes import router
import uvicorn

app = FastAPI(title="User Service", version="1.0")

# Include the user routes
app.include_router(router, prefix="/users")

@app.get("/")
def home():
    return {"message": "User Service is Running"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
