# estado.py

# Dicionário privado encapsulado
_dados = {
    "estacionamento": {i: None for i in range(1, 11)},
    "faturamento_total": 0.0
}

def obter_estacionamento():
    return _dados["estacionamento"]

def obter_faturamento():
    return _dados["faturamento_total"]

def adicionar_faturamento(valor):
    _dados["faturamento_total"] += valor

def ocupar_vaga(vaga, veiculo):
    _dados["estacionamento"][vaga] = veiculo

def liberar_vaga(vaga):
    _dados["estacionamento"][vaga] = None