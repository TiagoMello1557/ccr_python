import time
from .utilidades import limpar_tela
from .status import simulacao_status
from .tabelas import exibir_tabela_status
from .relatorios import carregar_relatorio
from .logs import registrar_logs, consultar_logs


# Este modelo ira cuidar de funções do menu da aplicação


# Esta função vai exibir opções de menu na linha de comando
def exibir_menu():
    limpar_tela()
    print("===Dashboard Interativo de Operações===")
    print("1. Exibir status das linhas")
    print("2. Exibir status em tabelas")
    print("3. Carregar relatorio")
    print("4. Consultar Log")
    print("5. Sair")


# Esta função ira lidar com as escolhas do usuario e encaminhar a funcionalidade correta
def menu_principal():
    while True:
        exibir_menu()
        escolha = input("Selecione uma opção: ")

        if escolha == '1':
            opcao_1()
        elif escolha == '2':
            opcao_2()
        elif escolha == '3':
            opcao_3()
        elif escolha == '4':
            opcao_4()
        elif escolha == '5':
            print("Saindo do programa...")
            time.sleep(1)
            break


# Funções de suporte para redirecionar as funcionalidades
def opcao_1():
    registrar_logs("Exibir status das linhas")
    simulacao_status()


def opcao_2():
    registrar_logs("Exibir status em tabelas")
    exibir_tabela_status()


def opcao_3():
    registrar_logs("Carregar relatorio")
    carregar_relatorio()


def opcao_4():
    consultar_logs()
