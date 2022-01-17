from rest_framework import serializers
from .models.despesa_model import Despesa


class DespesaSerializer(serializers.HyperlinkedModelSerializer):
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)

    class Meta:
        model = Despesa
        fields = ('descricao', 'valor', 'created_at', 'updated_at')
