from ..models.expense_model import Expense


def expense_already_exists(description, due_date, value):
    is_expense = Expense.objects.filter(description=description, due_date__month=due_date.month,
                                        due_date__year=due_date.year, value=value).exists()
    return is_expense
