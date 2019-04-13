from django.urls import path
from app.views import index, article

urlpatterns = [
    path('', index),
    path('article/', article)
]