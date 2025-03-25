from pydantic import BaseModel, EmailStr

class EmailNotification(BaseModel):
    recipient_email: EmailStr
    subject: str
    message: str

class SMSNotification(BaseModel):
    recipient_phone: str
    message: str
