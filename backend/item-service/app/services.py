from sqlalchemy.orm import Session
from app.models import Item
from app.schemas import ItemCreate

def create_item(db: Session, item: ItemCreate):
    db_item = Item(**item.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def get_all_items(db: Session):
    return db.query(Item).all()

def get_item_by_id(db: Session, item_id: int):
    return db.query(Item).filter(Item.id == item_id).first()

def update_item_availability(db: Session, item_id: int, availability: bool):
    item = db.query(Item).filter(Item.id == item_id).first()
    if item:
        item.is_available = availability
        db.commit()
        return item
    return None

def delete_item(db: Session, item_id: int):
    item = db.query(Item).filter(Item.id == item_id).first()
    if item:
        db.delete(item)
        db.commit()
        return item
    return None
