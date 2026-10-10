# exibir_faturamento.py
from estado import obter_faturamento

def exibir_faturamento():
    """Exibe o faturamento total acumulado."""
    total = obter_faturamento()
    print(f"\n[FINANCEIRO] Faturamento total acumulado: R$ {total:.2f}")