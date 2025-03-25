import os

# Microservice URLs
USER_SERVICE_URL = os.getenv("USER_SERVICE_URL", "http://user-service:8001")
ITEM_SERVICE_URL = os.getenv("ITEM_SERVICE_URL", "http://item-service:8002")
RENTAL_SERVICE_URL = os.getenv("RENTAL_SERVICE_URL", "http://rental-service:8003")
PAYMENT_SERVICE_URL = os.getenv("PAYMENT_SERVICE_URL", "http://payment-service:8004")
SEARCH_SERVICE_URL = os.getenv("SEARCH_SERVICE_URL", "http://search-service:8005")
NOTIFICATION_SERVICE_URL = os.getenv("NOTIFICATION_SERVICE_URL", "http://notification-service:8006")
MESSAGING_SERVICE_URL = os.getenv("MESSAGING_SERVICE_URL", "http://messaging-service:8007")
SECRET_KEY = os.getenv("SECRET_KEY", "mysecretkey")
