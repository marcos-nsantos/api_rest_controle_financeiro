from django.contrib import admin

from .models.income_model import Income


@admin.register(Income)
class IncomeAdmin(admin.ModelAdmin):
    list_display = ('id', 'description', 'value', 'created_at', 'updated_at')
    list_filter = ('description', 'value')
    search_fields = ('description', 'value')
    list_per_page = 10
