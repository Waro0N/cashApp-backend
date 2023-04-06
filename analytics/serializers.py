from rest_framework import serializers
from cashflow.models import CashFlow

class AnalyticsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CashFlow
        fields = ("category_dashboard",'debit')

class MonthlyData(serializers.ModelSerializer):

    class Meta:
        model = CashFlow
        fields= "__all__"