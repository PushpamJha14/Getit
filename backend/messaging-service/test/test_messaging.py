from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_fetch_chat_history():
    response = client.get("/messages/1/2")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
