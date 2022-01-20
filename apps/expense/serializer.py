from rest_framework import serializers
from .models.expense_model import Expense

from .validators.expense_validations import expense_already_exists, expense_description_month_and_year_already_exists


class ExpenseSerializer(serializers.HyperlinkedModelSerializer):
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)

    class Meta:
        model = Expense
        fields = ('url', 'description', 'value', 'due_date', 'created_at', 'updated_at')

    def validate(self, attrs):
        if expense_already_exists(attrs['description'], attrs['due_date'], attrs['value']):
            raise serializers.ValidationError('Expense already exists')
        return attrs

    def create(self, validated_data):
        if expense_description_month_and_year_already_exists(validated_data['description'], validated_data['due_date']):
            raise serializers.ValidationError('Already exists a expense with this description and due date')
        return Expense.objects.create(**validated_data)
