from django.urls import path
from .consumers import MySyncConsumer

websocket_urlpatterns = [
    path('ws/sc1/', MySyncConsumer.as_asgi(), name='sync-consumer-1')
]
