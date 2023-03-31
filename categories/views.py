from django.shortcuts import render
from rest_framework.generics import (
    ListAPIView,
    ListCreateAPIView
)
from rest_framework.response import Response
from rest_framework import status
from .serializers import CategorySerializer
from .models import Categories
# Create your views here.
class CreateCategories(ListCreateAPIView):
    queryset=Categories.objects.all()
    serializer_class = CategorySerializer


    def create(self, request, *args, **kargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        serializer.save()