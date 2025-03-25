from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_item():
    response = client.post("/items/", json={
        "name": "Sofa",
        "description": "A comfortable sofa",
        "price_per_day": 10.5,
        "owner_id": 1
    })
    assert response.status_code == 200
    assert response.json()["name"] == "Sofa"

def test_get_items():
    response = client.get("/items/")
    assert response.status_code == 200
