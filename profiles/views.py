from django.shortcuts import render
from rest_framework.generics import (
    ListAPIView,
    ListCreateAPIView
)
from rest_framework.response import Response
from .serializer import UserSerializer
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.decorators import api_view
from .models import CustomUser

# Create your views here.

class signUpUser(ListCreateAPIView):
    queryset=CustomUser.objects.all()
    serializer_class = UserSerializer

    def signup_user(self, request):
        pass