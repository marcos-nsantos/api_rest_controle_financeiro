from django.contrib import admin

from .models.despesa_model import Despesa


@admin.register(Despesa)
class DespesaAdmin(admin.ModelAdmin):
    list_display = ('id', 'descricao', 'valor', 'created_at', 'updated_at')
    list_filter = ('descricao', 'valor')
    search_fields = ('descricao', 'valor')
    list_per_page = 10
