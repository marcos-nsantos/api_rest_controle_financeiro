from django.contrib import admin

from .models.receita_model import Receita


@admin.register(Receita)
class Receita(admin.ModelAdmin):
    list_display = ('id', 'descricao', 'valor', 'created_at', 'updated_at')
    list_filter = ('descricao', 'valor')
    search_fields = ('descricao', 'valor')
    list_per_page = 10
