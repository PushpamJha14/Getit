from sqlalchemy.orm import Session
from app.models import Rental
from app.schemas import RentalCreate

def create_rental(db: Session, rental: RentalCreate):
    db_rental = Rental(**rental.dict())
    db.add(db_rental)
    db.commit()
    db.refresh(db_rental)
    return db_rental

def get_all_rentals(db: Session):
    return db.query(Rental).all()

def get_rental_by_id(db: Session, rental_id: int):
    return db.query(Rental).filter(Rental.id == rental_id).first()

def cancel_rental(db: Session, rental_id: int):
    rental = db.query(Rental).filter(Rental.id == rental_id).first()
    if rental:
        rental.is_active = False
        db.commit()
        return rental
    return None
