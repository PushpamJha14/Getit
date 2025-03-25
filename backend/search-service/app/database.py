from elasticsearch import Elasticsearch
import os

ELASTICSEARCH_URL = os.getenv("ELASTICSEARCH_URL", "http://localhost:9200")

es = Elasticsearch([ELASTICSEARCH_URL])

def init_search_service():
    from app.models import create_index
    create_index()
