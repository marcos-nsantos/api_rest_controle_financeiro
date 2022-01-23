from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action

from .models.expense_model import Expense
from .serializer import ExpenseSerializer


class ExpenseViewSet(viewsets.ModelViewSet):
    """API endpoint that allows expense to be viewed, created, deleted, and edited."""
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer
    filterset_fields = ('description',)

    @action(detail=False, methods=['get'], url_path=r'(?P<year>\d{4})/(?P<month>\d{1,2})')
    def get_expense_by_month(self, request, year, month):
        """Get expense by month."""
        expenses = Expense.objects.filter(due_date__year=year, due_date__month=month)
        if not expenses:
            return Response(status=status.HTTP_404_NOT_FOUND)

        page = self.paginate_queryset(expenses)
        if page is not None:
            serializer = self.get_serializer(page, many=True, context={'request': request})
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(expenses, many=True, context={'request': request})
        return Response(serializer.data)
