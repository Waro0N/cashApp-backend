from django.contrib import admin
from django.urls import path
from .views import CreateCashFlow

urlpatterns = [
    path('dashboard/', CreateCashFlow.as_view())
]