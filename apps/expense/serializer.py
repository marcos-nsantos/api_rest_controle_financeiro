from django.utils.translation import gettext_lazy as _
from rest_framework import serializers
from .models.expense_model import Expense

from .validators.expense_validations import expense_already_exists


class ExpenseSerializer(serializers.HyperlinkedModelSerializer):
    """Serializer for Expense Model"""

    class Meta:
        model = Expense
        exclude = ('created_at', 'updated_at')

    def validate(self, attrs):
        if expense_already_exists(attrs['category'], attrs['description'], attrs['due_date'], attrs['value']):
            raise serializers.ValidationError(_('Expense already exists'))
        return attrs
