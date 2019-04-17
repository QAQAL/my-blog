from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'app/', include('app.urls')),
    url(r'search/', include('haystack.urls')),
]
