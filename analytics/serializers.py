from rest_framework import serializers
from cashflow.models import CashFlow

class AnalyticsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CashFlow
        fields = ("category_dashboard",'debit')