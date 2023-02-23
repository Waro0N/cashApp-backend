from django.shortcuts import render
from rest_framework.generics import (
    ListAPIView,
)

# Create your views here.

class signUpUser(ListAPIView):
    def signup_user(request):
        pass