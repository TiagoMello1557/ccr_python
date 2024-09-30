# Este modelo irá simular situações de alerta no sistema


# Esta função irá verificar dados recebidos e checar se tem alguma anomalia no sistema de trens
def verificar_alerta(linha_trens, linha_status):
    trens_funcionando = int(linha_trens["linha_1"]) + int(linha_trens["linha_2"]) + int(linha_trens["linha_3"])

    if trens_funcionando < 7:
        exibir_alerta("A")
    if (linha_status["linha_1"] == "Falha" or linha_status["linha_1"] == "Nao operante" and
            linha_status["linha_2"] == "Falha" or linha_status["linha_2"] == "Nao operante" and
            linha_status["linha_3"] == "Falha" or linha_status["linha_3"] == "Nao operante"):
        exibir_alerta("B")


# Esta função irá escrever um alerta na linha de comando baseado na anomalia encontrada no sistema
def exibir_alerta(tipo):
    if tipo == "A":
        print("Alerta!")
        print("Número de trens em funcionamento abaixo do recomendado")
        exit()
    elif tipo == "B":
        print("Alerta!")
        print("Todas a linhas estão não operantes")
        exit()
