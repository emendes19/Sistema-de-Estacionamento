from estado import dados_sistema

def listar_vagas():
    """Percorre e exibe o estado atual de todas as vagas."""
    print("\n=== ESTADO DAS VAGAS ===")
    for vaga, veiculo in dados_sistema["estacionamento"].items():
        if veiculo is None:
            print(f"Vaga {vaga:02d}: [ LIVRE ]")
        else:
            entrada_str = veiculo['hora_entrada'].strftime('%H:%M:%S')
            print(f"Vaga {vaga:02d}: [ OCUPADA ] - Matrícula: {veiculo['placa']} | Modelo: {veiculo['modelo']} | Entrada: {entrada_str}")