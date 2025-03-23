from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_index_item():
    response = client.post("/search/index", json={
        "id": 1,
        "name": "Bicycle",
        "description": "A mountain bike for rent.",
        "category": "Outdoor",
        "price_per_day": 15.0,
        "availability": True
    })
    assert response.status_code == 200
    assert response.json()["message"] == "Item indexed successfully"

def test_search_items():
    response = client.post("/search/", json={"query": "bike"})
    assert response.status_code == 200
