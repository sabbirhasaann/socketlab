from django.urls import path
from . import views

urlpatterns = [
    path('rt/', views.index, name='gen-real-time-data'),
    path('chat/', views.chatHome, name='gen-chat-home-page'),
    path('chat/channels/<str:channel>/', views.chat, name='gen-chat-page')
]
