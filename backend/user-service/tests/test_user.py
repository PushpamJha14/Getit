from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_register_user():
    response = client.post("/users/register", json={
        "name": "John Doe",
        "email": "john@example.com",
        "password": "password123"
    })
    assert response.status_code == 200
    assert response.json()["email"] == "john@example.com"

def test_login_user():
    response = client.post("/users/login", json={
        "email": "john@example.com",
        "password": "password123"
    })
    assert response.status_code == 200
    assert "token" in response.json()
