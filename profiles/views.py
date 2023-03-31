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

# Create your views here.

class signUpUser(ListCreateAPIView):
    serializer_class = UserSerializer

    def signup_user(self, request):
        pass