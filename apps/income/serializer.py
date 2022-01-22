from rest_framework import serializers

from .models.income_model import Income
from .validators.income_validations import income_already_exists


class IncomeSerializer(serializers.HyperlinkedModelSerializer):
    """Serializer for Income model"""

    class Meta:
        model = Income
        exclude = ('created_at', 'updated_at')

    def validate(self, attrs):
        if income_already_exists(attrs['type'], attrs['description'], attrs['receipt_date'], attrs['value']):
            raise serializers.ValidationError('Income already exists')
        return attrs

    def create(self, validated_data):
        if income_already_exists(validated_data['type'], validated_data['description'], validated_data['receipt_date']):
            raise serializers.ValidationError('Income already exists')
        return Income.objects.create(**validated_data)
