from django.utils.translation import gettext_lazy as _
from rest_framework import serializers

from .models.income_model import Income
from .validators.income_validations import income_already_exists


class IncomeSerializer(serializers.HyperlinkedModelSerializer):
    """Serializer for Income model"""

    class Meta:
        model = Income
        exclude = ('created_at', 'updated_at')

    def validate(self, attrs):
        if income_already_exists(attrs['description'], attrs['receipt_date'], attrs['value']):
            raise serializers.ValidationError(_('Income already exists'))
        return attrs
