from rest_framework import serializers

from .models.income_model import Income
from .validators.income_validations import income_already_exists, income_description_month_and_year_already_exists


class IncomeSerializer(serializers.HyperlinkedModelSerializer):
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)

    class Meta:
        model = Income
        fields = '__all__'

    def validate(self, attrs):
        if income_already_exists(attrs['description'], attrs['value'], attrs['receipt_date']):
            raise serializers.ValidationError('Income already exists')
        return attrs

    def create(self, validated_data):
        if income_description_month_and_year_already_exists(validated_data['description'],
                                                            validated_data['receipt_date']):
            raise serializers.ValidationError('Income description and month and year already exists')
        return Income.objects.create(**validated_data)
