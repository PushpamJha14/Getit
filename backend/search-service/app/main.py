from fastapi import FastAPI
from app.routes import router
import uvicorn

app = FastAPI(title="Search Service", version="1.0")

# Include search routes
app.include_router(router, prefix="/search")

@app.get("/")
def home():
    return {"message": "Search Service is Running"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8004)
