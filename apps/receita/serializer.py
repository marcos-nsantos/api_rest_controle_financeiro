from rest_framework import serializers

from .models.receita_model import Receita


class ReceitaSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)

    class Meta:
        model = Receita
        fields = '__all__'
