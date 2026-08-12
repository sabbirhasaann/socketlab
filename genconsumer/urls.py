from django.urls import path
from . import views

urlpatterns = [
    path('rt/', views.index, name='gen-real-time-data'),
]
