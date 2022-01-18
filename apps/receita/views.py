from rest_framework import viewsets

from .models.receita_model import Receita
from .serializer import ReceitaSerializer


class ReceitaViewSet(viewsets.ModelViewSet):
    """API endpoint that allows receitas to be viewed, created, deleted, and edited."""
    queryset = Receita.objects.all()
    serializer_class = ReceitaSerializer
