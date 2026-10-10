import datetime
import math
from estado import dados_sistema
from calcular_valor import calcular_valor

def registrar_entrada():
    """Busca uma vaga livre e regista a entrada do veículo."""
    estacionamento = dados_sistema["estacionamento"]
    
    vaga_livre = None
    for vaga, veiculo in estacionamento.items():
        if veiculo is None:
            vaga_livre = vaga
            break
            
    if vaga_livre is None:
        print("\n[ERRO] O estacionamento está lotado!")
        return

    print(f"\n--- REGISTAR ENTRADA (Vaga {vaga_livre}) ---")
    placa = input("Matrícula (Placa) do veículo: ").strip().upper()
    modelo = input("Modelo do veículo: ").strip()
    
    agora = datetime.datetime.now()
    
    # Atribuição direta no dicionário global
    dados_sistema["estacionamento"][vaga_livre] = {
        "placa": placa,
        "modelo": modelo,
        "hora_entrada": agora
    }
    print(f"[SUCESSO] Veículo {placa} registado na Vaga {vaga_livre} às {agora.strftime('%H:%M:%S')}.")

def registrar_saida():
    """Localiza o veículo, calcula o tempo, cobra, atualiza o faturamento e liberta a vaga."""
    estacionamento = dados_sistema["estacionamento"]
    placa_busca = input("\nDigite a matrícula (placa) do veículo para saída: ").strip().upper()
    
    vaga_encontrada = None
    for vaga, veiculo in estacionamento.items():
        if veiculo is not None:
            # Compara ignorando espaços extras
            if veiculo["placa"].strip().upper() == placa_busca:
                vaga_encontrada = vaga
                break
            
    if vaga_encontrada is None:
        print(f"\n[ERRO] Veículo com a placa '{placa_busca}' não foi encontrado no estacionamento!")
        return

    veiculo = estacionamento[vaga_encontrada]
    hora_saida = datetime.datetime.now()
    
    # Cálculo do tempo de permanência em horas
    tempo_permanencia = (hora_saida - veiculo["hora_entrada"]).total_seconds() / 3600
    horas_cobrar = max(1, math.ceil(tempo_permanencia))
    
    valor = calcular_valor(horas_cobrar)
    
    # Atualiza o faturamento global de forma segura
    dados_sistema["faturamento_total"] += valor
    
    # Liberta a vaga
    dados_sistema["estacionamento"][vaga_encontrada] = None  
    
    print(f"\n=== RECIBO DE SAÍDA ===")
    print(f"Vaga Liberta: {vaga_encontrada}")
    print(f"Matrícula: {veiculo['placa']}")
    print(f"Tempo Cobrado: {horas_cobrar} hora(s)")
    print(f"Total a Pagar: R$ {valor:.2f}")
    print("=========================")