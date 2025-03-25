from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_user_service_proxy():
    response = client.get("/users/profile")
    assert response.status_code in [200, 401]  # Depends on authentication

def test_rate_limiting():
    for _ in range(11):
        response = client.get("/users/profile")
    assert response.status_code == 429
