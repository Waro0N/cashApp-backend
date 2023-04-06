from django.contrib import admin
from django.urls import path
from .views import Analytics, ByMonthAnalytics

urlpatterns = [
    path('pie-graph/', Analytics.as_view()),
    path('month-data/', ByMonthAnalytics.as_view())
]