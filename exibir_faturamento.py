from estado import dados_sistema

def exibir_faturamento():
    """Exibe o faturamento total acumulado."""
    total = dados_sistema["faturamento_total"]
    print(f"\n[FINANCEIRO] Faturamento total acumulado: R$ {total:.2f}")