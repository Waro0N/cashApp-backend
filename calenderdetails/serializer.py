from rest_framework import serializers
from cashflow.models import CashFlow

class CalenderSerializer(serializers.ModelSerializer):
    class Meta:
        model = CashFlow
        fields ='__all__'