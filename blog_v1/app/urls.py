from django.urls import path
from django.conf.urls import include
from app.views import index, article, note

urlpatterns = [
    path('', index),
    path('note/', note),
    path('article/', article),
    path('search/', include('haystack.urls'))
]