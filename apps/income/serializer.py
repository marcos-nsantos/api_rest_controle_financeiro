from rest_framework import serializers

from .models.income_model import Income


class IncomeSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)

    class Meta:
        model = Income
        fields = '__all__'
