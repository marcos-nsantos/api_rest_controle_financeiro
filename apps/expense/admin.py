from django.contrib import admin

from .models.expense_model import Expense


@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    list_display = ('id', 'description', 'value', 'created_at', 'updated_at')
    list_filter = ('description', 'value')
    search_fields = ('description', 'value')
    list_per_page = 10
