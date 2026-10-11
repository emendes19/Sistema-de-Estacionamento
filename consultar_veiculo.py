from estado import obter_estacionamento

def consultar_veiculo():
    estacionamento = obter_estacionamento()
    placa_busca = input("\nDigite a matrícula (placa) para consultar: ").strip().upper()

    encontrado = False
    for vaga, veiculo in estacionamento.items():
        if veiculo and veiculo["placa"] == placa_busca:
            print(f"\n[ENCONTRADO] O veículo {placa_busca} está na Vaga {vaga:02d} desde as {veiculo['hora_entrada'].strftime('%H:%M:%S')}.")
            encontrado = True
            break
    if not encontrado:
        print(f"\n[INFO] Nenhum veículo com a placa {placa_busca} foi encontrado no estacionamento.")