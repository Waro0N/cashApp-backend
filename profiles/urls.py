from django.contrib import admin
from django.urls import path
from .views import signUpUser

urlpatterns = [
    path('users/', signUpUser.as_view())
]