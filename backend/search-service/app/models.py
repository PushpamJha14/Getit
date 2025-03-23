from app.database import es

INDEX_NAME = "items"

MAPPING = {
    "mappings": {
        "properties": {
            "id": {"type": "integer"},
            "name": {"type": "text"},
            "description": {"type": "text"},
            "category": {"type": "keyword"},
            "price_per_day": {"type": "float"},
            "availability": {"type": "boolean"}
        }
    }
}

def create_index():
    if not es.indices.exists(index=INDEX_NAME):
        es.indices.create(index=INDEX_NAME, body=MAPPING)
