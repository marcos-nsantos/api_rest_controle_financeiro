from ..models.expense_model import Expense


def expense_already_exists(type, description, due_date, value=None):
    if value:
        is_expense = Expense.objects.filter(type=type, description=description, due_date__month=due_date.month,
                                            due_date__year=due_date.year, value=value).exists()
    else:
        is_expense = Expense.objects.filter(type=type, description=description, due_date__month=due_date.month,
                                            due_date__year=due_date.year).exists()
    return is_expense
