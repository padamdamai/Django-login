from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,name="home"),
    path('login/',views.logUser,name='login'),
    path('register',views.Register,name='register'),
]