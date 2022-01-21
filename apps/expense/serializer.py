from rest_framework import serializers
from .models.expense_model import Expense

from .validators.expense_validations import expense_already_exists


class ExpenseSerializer(serializers.HyperlinkedModelSerializer):
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)

    class Meta:
        model = Expense
        fields = '__all__'

    def validate(self, attrs):
        if expense_already_exists(attrs['type'], attrs['description'], attrs['due_date'], attrs['value']):
            raise serializers.ValidationError('Expense already exists')
        return attrs

    def create(self, validated_data):
        if expense_already_exists(validated_data['type'], validated_data['description'], validated_data['due_date']):
            raise serializers.ValidationError('Expense already exists')
        return Expense.objects.create(**validated_data)
