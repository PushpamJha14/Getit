from app.database import es
from app.models import INDEX_NAME
from app.schemas import ItemCreate, SearchQuery

def add_item_to_index(item: ItemCreate):
    es.index(index=INDEX_NAME, id=item.id, document=item.dict())

def search_items(query: SearchQuery):
    search_body = {
        "query": {
            "multi_match": {
                "query": query.query,
                "fields": ["name", "description", "category"]
            }
        }
    }
    response = es.search(index=INDEX_NAME, body=search_body)
    return [hit["_source"] for hit in response["hits"]["hits"]]
