from django.contrib import admin
from django.urls import path
from .views import CreateCategories

urlpatterns = [
    path('user-categories/', CreateCategories.as_view())
]