from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import Sum

from apps.expense.models.expense_model import Expense
from apps.income.models.income_model import Income


class SummaryView(APIView):
    """
    View to list summary per month
    total expenses per month
    total income per month
    total balance per month
    total expenses per category
    """

    def get(self, request, year, month):
        expenses_total_value = Expense.objects.filter(due_date__year=year, due_date__month=month).aggregate(
            Sum('value'))['value__sum'] or 0
        incomes_total_value = Income.objects.filter(receipt_date__year=year, receipt_date__month=month).aggregate(
            Sum('value'))['value__sum'] or 0
        expense_per_category = Expense.objects.filter(due_date__year=year, due_date__month=month).values(
            'category').annotate(Sum('value'))
        balance_total_value = incomes_total_value - expenses_total_value

        for expense in expense_per_category:
            expense['value'] = expense['value__sum']
            del expense['value__sum']

        return Response({
            'expenses_total_value': expenses_total_value,
            'incomes_total_value': incomes_total_value,
            'balance_total_value': balance_total_value,
            'expense_per_category': expense_per_category
        })
