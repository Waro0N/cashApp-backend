from django.shortcuts import render
from rest_framework.generics import (
    ListAPIView,
    ListCreateAPIView
)
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import status
from .serializers import CashSerializer
from .models import CashFlow
# Create your views here.
class CreateCashFlow(ListCreateAPIView):
    queryset=CashFlow.objects.all()
    serializer_class = CashSerializer

    def create(self, request, *args, **kargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        serializer.save()

    def get_queryset(self):
        if "all" in self.request.GET:
            queryset=CashFlow.objects.all()
        if "created_by" in self.request.GET:
            created_by = self.request.GET['created_by']
            queryset=CashFlow.objects.filter(created_by=created_by)
        if 'ordering' in self.request.GET and self.request.GET['ordering'] == '-id':
            queryset = queryset.order_by('-id')
        return queryset