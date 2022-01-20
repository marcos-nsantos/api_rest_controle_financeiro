from rest_framework import viewsets

from .models.income_model import Income
from .serializer import IncomeSerializer


class IncomeViewSet(viewsets.ModelViewSet):
    """API endpoint that allows income to be viewed, created, deleted, and edited."""
    queryset = Income.objects.all()
    serializer_class = IncomeSerializer
