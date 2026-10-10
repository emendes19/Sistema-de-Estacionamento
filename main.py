import os
from menu import exibir_menu
from movimentacoes import registrar_entrada, registrar_saida
from listar_vagas import listar_vagas
from exibir_faturamento import exibir_faturamento

def limpar_tela():
    """Limpa o terminal."""
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    while True:
        limpar_tela()
        exibir_menu()
        opcao = input("\nEscolha uma opção: ").strip()
        
        print("\n" + "-"*40)
        
        if opcao == '1':
            registrar_entrada()
        elif opcao == '2':
            registrar_saida()
        elif opcao == '3':
            listar_vagas()
        elif opcao == '4':
            exibir_faturamento()
        elif opcao == '0':
            print("\nEncerrando o sistema de estacionamento. Até breve!")
            break
        else:
            print("[ERRO] Opção inválida! Escolha entre 0 e 4.")
            
        print("-"*40)
        
        # Loop que obriga o usuário a digitar 0 para conseguir voltar ao menu
        while True:
            voltar = input("\nDigite 0 para voltar ao menu: ").strip()
            if voltar == '0':
                break
            print("[AVISO] Você precisa digitar 0 para retornar ao menu.")

if __name__ == "__main__":
    main()