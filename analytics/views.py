from django.shortcuts import render
from rest_framework.generics import (
    ListAPIView,
    ListCreateAPIView
)
from rest_framework.response import Response
from cashflow.models import CashFlow
from .serializers import AnalyticsSerializer, MonthlyData
from django.db.models.functions import ExtractMonth
# Create your views here.


class Analytics(ListAPIView):
    queryset = CashFlow.objects.all()
    serializer_class = AnalyticsSerializer

    def get(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        data = serializer.data
        api_data = {}
        for i in data:
            category_item = i['category_dashboard']
            debit_item = i['debit']
            if category_item in api_data:
                api_data[category_item] += debit_item
            else:
                api_data[category_item] = debit_item
        result = [{'category_dashboard': category, 'debit': total}
              for category, total in api_data.items()]
        return Response(result)


class ByMonthAnalytics(ListAPIView):
    queryset=CashFlow.objects.all()
    serializer_class = MonthlyData

    def get(self, request, *args, **kwargs):
        queryset =CashFlow.objects.all()

        month_filter = self.request.GET.get('month')
        if month_filter:
            queryset = queryset.annotate(month=ExtractMonth('date')).filter(month=month_filter) 
        serializer = self.get_serializer(queryset, many=True)
        data=serializer.data
        return Response(data)