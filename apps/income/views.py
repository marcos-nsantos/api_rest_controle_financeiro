from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action

from apps.income.models.income_model import Income
from apps.income.serializer import IncomeSerializer


class IncomeViewSet(viewsets.ModelViewSet):
    """API endpoint that allows income to be viewed, created, deleted, and edited."""
    queryset = Income.objects.all()
    serializer_class = IncomeSerializer
    filterset_fields = ('description',)

    @action(detail=False, methods=['get'], url_path=r'(?P<year>\d{4})/(?P<month>\d{1,2})')
    def get_income_by_month(self, request, year, month):
        """Extra route to get incomes by month."""
        incomes = Income.objects.filter(receipt_date__year=year, receipt_date__month=month)
        if not incomes:
            return Response(status=status.HTTP_404_NOT_FOUND)

        page = self.paginate_queryset(incomes)
        if page is not None:
            serializer = self.get_serializer(page, many=True, context={'request': request})
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(incomes, many=True, context={'request': request})
        return Response(serializer.data)
