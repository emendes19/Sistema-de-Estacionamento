import math

def calcular_valor(horas):
    """Calcula o valor da estadia com base nas horas de permanência."""
    if horas <= 1:
        return 5.0
    else:
        return 5.0 + math.ceil(horas - 1) * 2.0