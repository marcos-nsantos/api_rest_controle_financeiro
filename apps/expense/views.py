from rest_framework import viewsets

from .models.expense_model import Expense
from .serializer import ExpenseSerializer


class ExpenseViewSet(viewsets.ModelViewSet):
    """API endpoint that allows expense to be viewed, created, deleted, and edited."""
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer
    filterset_fields = ('description',)
