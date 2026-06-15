from django.urls import path
from .consumers import MySyncConsumer, MyAsyncConsumer

websocket_urlpatterns = [
    path('ws/sc1/<str:group_name>/',
         MySyncConsumer.as_asgi(), name='sync-consumer-1'),
    path('ws/ac1/<str:group_name>/',
         MyAsyncConsumer.as_asgi(), name='async-consumer-1')
]
