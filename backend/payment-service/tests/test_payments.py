from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_make_payment():
    response = client.post("/payments/", json={
        "rental_id": 1,
        "amount": 50.0
    })
    assert response.status_code == 200
    assert response.json()["amount"] == 50.0

def test_get_payments():
    response = client.get("/payments/")
    assert response.status_code == 200
