from ..models.income_model import Income


def income_already_exists(description, value, receipt_date):
    is_income = Income.objects.filter(description=description, value=value, receipt_date__month=receipt_date.month,
                                      receipt_date__year=receipt_date.year).exists()
    return is_income


def income_description_month_and_year_already_exists(description, receipt_date):
    is_income = Income.objects.filter(description=description, receipt_date__month=receipt_date.month,
                                      receipt_date__year=receipt_date.year).exists()
    return is_income
