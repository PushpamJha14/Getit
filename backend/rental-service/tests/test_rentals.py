from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_rental():
    response = client.post("/rentals/", json={
        "renter_id": 1,
        "item_id": 1,
        "start_date": "2025-03-25T10:00:00",
        "end_date": "2025-03-30T10:00:00"
    })
    assert response.status_code == 200
    assert response.json()["renter_id"] == 1

def test_get_rentals():
    response = client.get("/rentals/")
    assert response.status_code == 200
