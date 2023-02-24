from django.shortcuts import render
from rest_framework.generics import (
    ListAPIView,
    ListCreateAPIView
)
from rest_framework.response import Response
from .serializer import UserSerializer
from rest_framework.views import APIView
from rest_framework import status

# Create your views here.

class signUpUser(APIView):
    serializer_class = UserSerializer
    def signup_user(request):
        username = request.data.get('username')
        email = request.data.get('email')
        password = request.data.get('password')

        serializer = UserSerializer(data={
            'username': username,
            'email': email,
            'password': password,
        })

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)