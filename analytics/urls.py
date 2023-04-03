from django.contrib import admin
from django.urls import path
from .views import Analytics

urlpatterns = [
    path('pie-graph/', Analytics.as_view())
]