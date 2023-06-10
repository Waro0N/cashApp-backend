from django.contrib import admin
from django.urls import path
from .views import signUpUser, loggedInUser

urlpatterns = [
    path('users/', signUpUser.as_view()),
    path('loggedin-user/', loggedInUser.as_view())
]