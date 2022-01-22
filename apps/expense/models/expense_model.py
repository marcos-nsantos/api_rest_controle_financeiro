from django.db import models
from django.utils.translation import gettext_lazy as _


class Expense(models.Model):
    """Class to represent an expense model"""

    class ExpenseType(models.IntegerChoices):
        """Enum for expense type"""
        FIXED = 1, _('Fixed')
        VARIABLE = 2, _('Variable')

    class ExpenseCategory(models.TextChoices):
        """Enum for expense category"""
        FOOD = 'FO', _('Food')
        HEALTH = 'HE', _('Health')
        HOME = 'HO', _('Home')
        TRANSPORT = 'TR', _('Transport')
        EDUCATION = 'ED', _('Education')
        LEISURE = 'LE', _('Leisure')
        UNFORESEEN = 'UN', _('Unforeseen')
        OTHER = 'OT', _('Other')

    type = models.IntegerField(choices=ExpenseType.choices, null=False)
    category = models.CharField(max_length=2, choices=ExpenseCategory.choices, default=ExpenseCategory.OTHER)
    description = models.CharField(max_length=100)
    value = models.DecimalField(max_digits=7, decimal_places=2)
    due_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.description[:10]} - {self.value}'
