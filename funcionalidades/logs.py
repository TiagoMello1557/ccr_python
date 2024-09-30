from datetime import datetime

# Este modelo ira salvar logs de operação do usuario e permitir que o log seja consultado no programa


# Esta função ira receber a ação executada e salvar em um arquivo txt junto com a data
def registrar_logs(acao):
    # Abrindo o arquivo se existe em 'append'(continuar escrevendo no mesmo arquivo), se não existe ira criar um novo
    with open("log_operacoes.txt", "a") as file:
        # Escreve no arquivo a data atual e a cação recebida
        file.write(f"{datetime.now()} - {acao}\n")
    print(f"Log registrado: {acao}")


# Esta função ira carregar o arquivo log de formato txt, e ira escrever na linha de comando
def consultar_logs():
    try:
        # Abre o arquivo em 'read'(Apenas leitura)
        with open("log_operacoes.txt", "r") as file:
            # Escreve o arquivo na linha de comando
            print(file.read())
    except FileNotFoundError:
        print("Nenhum log encontrado.")
