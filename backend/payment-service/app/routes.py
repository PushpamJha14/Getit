from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.schemas import PaymentCreate, PaymentResponse
from app.services import process_payment, get_all_payments, get_payment_by_id
from app.auth import verify_jwt_token

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=PaymentResponse)
def make_payment(payment: PaymentCreate, db: Session = Depends(get_db), token: dict = Depends(verify_jwt_token)):
    return process_payment(db, payment)

@router.get("/", response_model=list[PaymentResponse])
def list_payments(db: Session = Depends(get_db)):
    return get_all_payments(db)

@router.get("/{payment_id}", response_model=PaymentResponse)
def get_payment(payment_id: int, db: Session = Depends(get_db)):
    payment = get_payment_by_id(db, payment_id)
    if not payment:
        raise HTTPException(status_code=404, detail="Payment not found")
    return payment
