from rest_framework import viewsets

from .models.receita_model import Receita
from .serializer import ReceitaSerializer


class ReceitaViewSet(viewsets.ModelViewSet):
    queryset = Receita.objects.all()
    serializer_class = ReceitaSerializer
