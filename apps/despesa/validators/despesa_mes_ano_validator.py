from ..models.despesa_model import Despesa


def despesa_no_mesmo_mes_e_ano(descricao, data_vencimento, valor):
    """Despesa deve ser unica no mesmo mes e ano"""
    despesa_data_vencimento = Despesa.objects.filter(descricao=descricao, data_vencimento__month=data_vencimento.month,
                                                     data_vencimento__year=data_vencimento.year, valor=valor).exists()
    if despesa_data_vencimento:
        return True
