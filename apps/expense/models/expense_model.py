from django.db import models
from django.utils.translation import gettext_lazy as _


class Expense(models.Model):
    """Class to represent an expense model"""

    class ExpenseCategory(models.TextChoices):
        """Enum for expense category"""
        FOOD = 'Food', _('Food')
        HEALTH = 'Health', _('Health')
        HOME = 'Home', _('Home')
        TRANSPORT = 'Transport', _('Transport')
        EDUCATION = 'Education', _('Education')
        LEISURE = 'Leisure', _('Leisure')
        UNFORESEEN = 'Unforeseen', _('Unforeseen')
        OTHER = 'Other', _('Other')

    category = models.CharField(max_length=20, choices=ExpenseCategory.choices, default=ExpenseCategory.OTHER)
    description = models.CharField(max_length=100)
    value = models.DecimalField(max_digits=7, decimal_places=2)
    due_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.description[:10]} - {self.value}'
