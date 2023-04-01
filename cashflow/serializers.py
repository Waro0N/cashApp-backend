from rest_framework import serializers
from .models import CashFlow

class CashSerializer(serializers.ModelSerializer):
    class Meta:
        model = CashFlow
        fields = "__all__"