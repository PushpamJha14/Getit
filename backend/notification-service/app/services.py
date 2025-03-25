import os
import smtplib
from twilio.rest import Client
from app.schemas import EmailNotification, SMSNotification

# Twilio SMS configuration
TWILIO_ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
TWILIO_PHONE_NUMBER = os.getenv("TWILIO_PHONE_NUMBER")

# Email SMTP configuration
SMTP_SERVER = os.getenv("SMTP_SERVER", "smtp.gmail.com")
SMTP_PORT = int(os.getenv("SMTP_PORT", 587))
SMTP_USERNAME = os.getenv("SMTP_USERNAME")
SMTP_PASSWORD = os.getenv("SMTP_PASSWORD")

def send_email(notification: EmailNotification):
    """Sends an email notification using SMTP."""
    try:
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(SMTP_USERNAME, SMTP_PASSWORD)
        message = f"Subject: {notification.subject}\n\n{notification.message}"
        server.sendmail(SMTP_USERNAME, notification.recipient_email, message)
        server.quit()
        return {"message": "Email sent successfully"}
    except Exception as e:
        return {"error": str(e)}

def send_sms(notification: SMSNotification):
    """Sends an SMS notification using Twilio."""
    try:
        client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
        message = client.messages.create(
            body=notification.message,
            from_=TWILIO_PHONE_NUMBER,
            to=notification.recipient_phone
        )
        return {"message": "SMS sent successfully", "sid": message.sid}
    except Exception as e:
        return {"error": str(e)}
