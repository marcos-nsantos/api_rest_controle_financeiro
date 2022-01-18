from rest_framework import viewsets

from .models.despesa_model import Despesa
from .serializers import DespesaSerializer


class DespesaViewSet(viewsets.ModelViewSet):
    """API endpoint that allows despesas to be viewed, created, deleted, and edited."""
    queryset = Despesa.objects.all()
    serializer_class = DespesaSerializer
