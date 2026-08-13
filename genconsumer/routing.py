from django.urls import path
from .consumers import MyWebsocketConsumer, MyAsyncWebsocketConsumer, ChatWebsocketConsumer, ChatAsyncWebsocketConsumer, ChatAsyncJsonWebsocketConsumer

websocket_urlpatters = [
    path('ws/wsc/', MyWebsocketConsumer.as_asgi()),
    path('ws/awsc/', MyAsyncWebsocketConsumer.as_asgi()),
    path('ws/wsc/chat/<str:channel>/',
         ChatWebsocketConsumer.as_asgi(), name='chat-swsc'),
    path('ws/awsc/chat/<str:channel>/',
         ChatAsyncWebsocketConsumer.as_asgi(), name='chat-awsc'),
    path('ws/ajwsc/chat/<str:channel>/',
         ChatAsyncJsonWebsocketConsumer.as_asgi(), name='chat-ajwsc'),
]
