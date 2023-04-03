from django.shortcuts import render
from rest_framework.generics import (
    ListAPIView,
    ListCreateAPIView
)
from rest_framework.response import Response
from cashflow.models import CashFlow
from .serializers import AnalyticsSerializer
# Create your views here.
class Analytics(ListAPIView):
    queryset=CashFlow.objects.all()
    serializer_class = AnalyticsSerializer

    def get(self, request, *args, **kwargs):
        category_list=[]
        expense=[]
        queryset = self.filter_queryset(self.get_queryset())
        # print(list(queryset))
        serializer = self.get_serializer(queryset, many=True)
        data = serializer.data
        
        return Response(data)