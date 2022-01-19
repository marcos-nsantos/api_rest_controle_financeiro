from rest_framework import serializers
from .models.despesa_model import Despesa

from .validators.despesa_mes_ano_validator import despesa_no_mesmo_mes_e_ano


class DespesaSerializer(serializers.HyperlinkedModelSerializer):
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)

    class Meta:
        model = Despesa
        fields = ('url', 'descricao', 'valor', 'data_vencimento', 'created_at', 'updated_at')

    def validate(self, attrs):
        if despesa_no_mesmo_mes_e_ano(attrs['descricao'], attrs['data_vencimento'], attrs['valor']):
            raise serializers.ValidationError('Despesa já cadastrada para este mês e ano')
        return attrs
