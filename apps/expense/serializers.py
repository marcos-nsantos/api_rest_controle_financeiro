from rest_framework import serializers
from .models.expense_model import Expense

from .validators.expense_already_exists import expense_already_exists


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
