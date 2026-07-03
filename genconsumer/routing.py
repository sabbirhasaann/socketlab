from django.urls import path
from .consumers import MyWebsocketConsumer, MyAsyncWebsocketConsumer

websocket_urlpatters = [
    path('ws/wsc/', MyWebsocketConsumer.as_asgi()),
    path('ws/awsc/', MyAsyncWebsocketConsumer.as_asgi()),
]
