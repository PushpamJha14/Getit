from fastapi import APIRouter, Depends, HTTPException
from app.schemas import EmailNotification, SMSNotification
from app.services import send_email, send_sms
from app.auth import verify_jwt_token

router = APIRouter()

@router.post("/email")
def send_email_notification(notification: EmailNotification, token: dict = Depends(verify_jwt_token)):
    result = send_email(notification)
    if "error" in result:
        raise HTTPException(status_code=500, detail=result["error"])
    return result

@router.post("/sms")
def send_sms_notification(notification: SMSNotification, token: dict = Depends(verify_jwt_token)):
    result = send_sms(notification)
    if "error" in result:
        raise HTTPException(status_code=500, detail=result["error"])
    return result
