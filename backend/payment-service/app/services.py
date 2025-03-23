from sqlalchemy.orm import Session
from app.models import Payment
from app.schemas import PaymentCreate
import random

def process_payment(db: Session, payment: PaymentCreate):
    status = "completed" if random.random() > 0.1 else "failed"  # Simulating random payment success/failure

    db_payment = Payment(rental_id=payment.rental_id, amount=payment.amount, status=status)
    db.add(db_payment)
    db.commit()
    db.refresh(db_payment)
    return db_payment

def get_all_payments(db: Session):
    return db.query(Payment).all()

def get_payment_by_id(db: Session, payment_id: int):
    return db.query(Payment).filter(Payment.id == payment_id).first()
