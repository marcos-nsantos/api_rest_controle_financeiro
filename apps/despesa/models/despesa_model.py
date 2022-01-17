from django.db import models
from django.utils.translation import gettext_lazy as _


class Despesa(models.Model):
    """Classe que representa a tabela despesa do usuário"""

    descricao = models.TextField(_('Descrição'), max_length=100)
    valor = models.DecimalField(_('Valor'), max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(_('Criado em'), auto_now_add=True)
    updated_at = models.DateTimeField(_('Atualizado em'), auto_now=True)

    class Meta:
        verbose_name = _('Despesa')
        verbose_name_plural = _('Despesas')

    def __str__(self):
        return f'{self.descricao[:10]} - {self.valor}'
