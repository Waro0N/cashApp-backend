from django.contrib import admin
from django.urls import path
from .views import signUpUser

urlpatterns = [
    path('/signup', signUpUser.as_view())
]