from django.db import models
from django.utils.translation import gettext_lazy as _


class Income(models.Model):
    """Class to represent an income model."""

    class IncomeType(models.IntegerChoices):
        FIXED = 1, _('Fixed')
        VARIABLE = 2, _('Variable')

    type = models.IntegerField(choices=IncomeType.choices, null=False)
    description = models.CharField(max_length=100)
    value = models.DecimalField(max_digits=7, decimal_places=2)
    receipt_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.description
