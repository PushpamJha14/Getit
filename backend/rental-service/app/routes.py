from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.schemas import RentalCreate, RentalResponse
from app.services import create_rental, get_all_rentals, get_rental_by_id, cancel_rental
from app.auth import verify_jwt_token

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=RentalResponse)
def rent_item(rental: RentalCreate, db: Session = Depends(get_db), token: dict = Depends(verify_jwt_token)):
    return create_rental(db, rental)

@router.get("/", response_model=list[RentalResponse])
def list_rentals(db: Session = Depends(get_db)):
    return get_all_rentals(db)

@router.get("/{rental_id}", response_model=RentalResponse)
def get_rental(rental_id: int, db: Session = Depends(get_db)):
    rental = get_rental_by_id(db, rental_id)
    if not rental:
        raise HTTPException(status_code=404, detail="Rental not found")
    return rental

@router.put("/{rental_id}/cancel")
def cancel_rental_request(rental_id: int, db: Session = Depends(get_db), token: dict = Depends(verify_jwt_token)):
    rental = cancel_rental(db, rental_id)
    if not rental:
        raise HTTPException(status_code=404, detail="Rental not found")
    return {"message": "Rental canceled"}
