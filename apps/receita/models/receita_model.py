from django.db import models
from django.utils.translation import gettext_lazy as _


class Receita(models.Model):
    """Classe que representa um modelo de receita de um usuário."""

    class TipoRenda(models.IntegerChoices):
        """Enum que representa os tipos de renda."""
        FIXA = 1, _('Fixa')
        VARIAVEL = 2, _('Variavel')

    tipo_renda = models.IntegerField(_('Tipo de renda'), choices=TipoRenda.choices, default=TipoRenda.FIXA)
    descricao = models.TextField(_('Descrição'), max_length=200, unique=True)
    valor = models.DecimalField(_('Valor'), max_digits=10, decimal_places=2)
    data_recebimento = models.DateField(_('Data de recebimento'))
    created_at = models.DateTimeField(_('Criado em'), auto_now_add=True)
    updated_at = models.DateTimeField(_('Atualizado em'), auto_now=True)

    class Meta:
        verbose_name = _('Receita')
        verbose_name_plural = _('Receitas')
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.descricao[:10]} - {self.valor}'
