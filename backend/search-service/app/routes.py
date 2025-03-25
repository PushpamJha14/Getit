from fastapi import APIRouter, Depends, HTTPException
from app.schemas import ItemCreate, SearchQuery
from app.services import add_item_to_index, search_items
from app.auth import verify_jwt_token

router = APIRouter()

@router.post("/index")
def index_item(item: ItemCreate, token: dict = Depends(verify_jwt_token)):
    add_item_to_index(item)
    return {"message": "Item indexed successfully"}

@router.post("/", response_model=list)
def search_for_items(query: SearchQuery):
    results = search_items(query)
    if not results:
        raise HTTPException(status_code=404, detail="No matching items found")
    return results
