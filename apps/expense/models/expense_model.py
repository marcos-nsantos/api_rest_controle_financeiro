from django.db import models
from django.utils.translation import gettext_lazy as _


class Expense(models.Model):

    class ExpenseType(models.IntegerChoices):
        FIXED = 1, _('Fixed')
        VARIABLE = 2, _('Variable')

    type = models.IntegerField(choices=ExpenseType.choices, null=False)
    description = models.CharField(max_length=100)
    value = models.DecimalField(max_digits=7, decimal_places=2)
    due_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.description[:10]} - {self.value}'
