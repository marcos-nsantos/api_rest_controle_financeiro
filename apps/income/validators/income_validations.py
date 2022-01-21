from ..models.income_model import Income


def income_already_exists(type, description, receipt_date, value=None):
    if value:
        is_income = Income.objects.filter(type=type, description=description, value=value,
                                          receipt_date__month=receipt_date.month,
                                          receipt_date__year=receipt_date.year).exists()
    else:
        is_income = Income.objects.filter(type=type, description=description, receipt_date__month=receipt_date.month,
                                          receipt_date__year=receipt_date.year).exists()
    return is_income
