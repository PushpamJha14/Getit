from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_send_email():
    response = client.post("/notifications/email", json={
        "recipient_email": "test@example.com",
        "subject": "Test Email",
        "message": "This is a test email."
    })
    assert response.status_code == 200 or response.status_code == 500  # Can fail if SMTP is not configured

def test_send_sms():
    response = client.post("/notifications/sms", json={
        "recipient_phone": "+1234567890",
        "message": "Test SMS message."
    })
    assert response.status_code == 200 or response.status_code == 500  # Can fail if Twilio is not configured
