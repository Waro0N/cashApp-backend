from django.contrib import admin
from django.urls import path
from .views import CalenderDetails

urlpatterns = [
    path('calender-by-month/', CalenderDetails.as_view()),
    
]