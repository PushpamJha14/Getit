from fastapi import FastAPI
from app.routes import router
import uvicorn

app = FastAPI(title="Rental Service", version="1.0")

# Include rental routes
app.include_router(router, prefix="/rentals")

@app.get("/")
def home():
    return {"message": "Rental Service is Running"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8002)
