from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('projectApp.urls')),
    path('',include('django.contrib.auth.urls')),
]
