from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.schemas import ItemCreate, ItemResponse
from app.services import create_item, get_all_items, get_item_by_id, update_item_availability, delete_item
from app.auth import verify_jwt_token

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=ItemResponse)
def add_item(item: ItemCreate, db: Session = Depends(get_db), token: dict = Depends(verify_jwt_token)):
    return create_item(db, item)

@router.get("/", response_model=list[ItemResponse])
def list_items(db: Session = Depends(get_db)):
    return get_all_items(db)

@router.get("/{item_id}", response_model=ItemResponse)
def get_item(item_id: int, db: Session = Depends(get_db)):
    item = get_item_by_id(db, item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item

@router.put("/{item_id}/availability")
def update_availability(item_id: int, availability: bool, db: Session = Depends(get_db), token: dict = Depends(verify_jwt_token)):
    item = update_item_availability(db, item_id, availability)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"message": "Item availability updated"}

@router.delete("/{item_id}")
def remove_item(item_id: int, db: Session = Depends(get_db), token: dict = Depends(verify_jwt_token)):
    item = delete_item(db, item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"message": "Item deleted"}
