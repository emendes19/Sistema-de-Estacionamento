# movimentacoes.py
import datetime
import math
from estado import obter_estacionamento, ocupar_vaga, liberar_vaga, adicionar_faturamento
from calcular_valor import calcular_valor

def registrar_entrada():
    """Busca uma vaga livre e regista a entrada do veículo."""
    estacionamento = obter_estacionamento()
    
    print("\n--- REGISTRAR ENTRADA ---")
    placa = input("Matrícula (Placa) do veículo: ").strip().upper()
    
    # 🔍 VALIDAÇÃO DE VEÍCULO DUPLICADO:
    # Percorre o estacionamento para verificar se a placa já está cadastrada
    for veiculo_existente in estacionamento.values():
        if veiculo_existente is not None and veiculo_existente["placa"] == placa:
            print(f"\n[ERRO] O veículo com a matrícula {placa} já se encontra estacionado!")
            return

    # Procura a primeira vaga livre se o veículo não estiver estacionado
    vaga_livre = None
    for vaga, veiculo in estacionamento.items():
        if veiculo is None:
            vaga_livre = vaga
            break
            
    if vaga_livre is None:
        print("\n[ERRO] O estacionamento está lotado!")
        return

    modelo = input("Modelo do veículo: ").strip()
    agora = datetime.datetime.now()
    
    veiculo_info = {
        "placa": placa,
        "modelo": modelo,
        "hora_entrada": agora
    }
    
    ocupar_vaga(vaga_livre, veiculo_info)
    print(f"[SUCESSO] Veículo {placa} registado na Vaga {vaga_livre} às {agora.strftime('%H:%M:%S')}.")

def registrar_saida():
    """Localiza o veículo, calcula o tempo, cobra, atualiza o faturamento e liberta a vaga."""
    estacionamento = obter_estacionamento()
    placa_busca = input("\nDigite a matrícula (placa) do veículo para saída: ").strip().upper()
    
    vaga_encontrada = None
    for vaga, veiculo in estacionamento.items():
        if veiculo is not None:
            if veiculo["placa"].strip().upper() == placa_busca:
                vaga_encontrada = vaga
                break
            
    if vaga_encontrada is None:
        print(f"\n[ERRO] Veículo com a placa '{placa_busca}' não foi encontrado no estacionamento!")
        return

    veiculo = estacionamento[vaga_encontrada]
    hora_saida = datetime.datetime.now()
    
    tempo_permanencia = (hora_saida - veiculo["hora_entrada"]).total_seconds() / 3600
    horas_cobrar = max(1, math.ceil(tempo_permanencia))
    
    valor = calcular_valor(horas_cobrar)
    
    adicionar_faturamento(valor)
    liberar_vaga(vaga_encontrada)
    
    print(f"\n=== RECIBO DE SAÍDA ===")
    print(f"Vaga Liberta: {vaga_encontrada}")
    print(f"Matrícula: {veiculo['placa']}")
    print(f"Tempo Cobrado: {horas_cobrar} hora(s)")
    print(f"Total a Pagar: R$ {valor:.2f}")
    print("=========================")