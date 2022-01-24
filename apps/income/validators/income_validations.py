from ..models.income_model import Income


def income_already_exists(description, receipt_date, value):
    is_income = Income.objects.filter(description=description, value=value, receipt_date__month=receipt_date.month,
                                      receipt_date__year=receipt_date.year).exists()
    return is_income
