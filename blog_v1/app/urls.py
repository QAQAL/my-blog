from django.urls import path
from app import views

urlpatterns = [
    path('', views.index),
    path('article/', views.article),
    path('search/', views.search)
]