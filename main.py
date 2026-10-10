from menu import exibir_menu
from movimentacoes import registrar_entrada, registrar_saida
from listar_vagas import listar_vagas
from exibir_faturamento import exibir_faturamento

def main():
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ").strip()
        
        if opcao == '1':
            registrar_entrada()
        elif opcao == '2':
            registrar_saida()
        elif opcao == '3':
            listar_vagas()
        elif opcao == '4':
            exibir_faturamento()
        elif opcao == '0':
            print("\nA encerra o sistema de estacionamento. Até breve!")
            break
        else:
            print("\n[ERRO] Opção inválida! Escolha entre 0 e 4.")

if __name__ == "__main__":
    main()