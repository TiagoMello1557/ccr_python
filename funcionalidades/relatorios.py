import json
import os

# Este modelo irá cuidar da logica para salvar relatórios automaticamente em formato Json e depois visualizalos na
# linha de comando


# Esta função irá preparar o objeto json e guardar em um arquivo gerado automaticamente, se o arquivo existe ele irá
# continuar escrevendo no mesmo
def salvar_relatorio(linhas_trens, linhas_status, data_hora):
    relatorio = {
        "data_hora": data_hora,
        "linhas": {
            "linha_1": {
                f"status": linhas_status["linha_1"],
                "trens_operando": linhas_trens["linha_1"]
            },
            "linha_2": {
                "status": linhas_status["linha_2"],
                "trens_operando": linhas_trens["linha_2"]
            },
            f"linha_3": {
                "status": linhas_status["linha_2"],
                "trens_operando": linhas_trens["linha_3"]
            },
        }
    }
    if os.path.exists("relatorio.json"):
        with open("relatorio.json", "r") as file:
            try:
                data = json.load(file)
            except json.JSONDecodeError:
                data = []
    else:
        data = []

    data.append(relatorio)

    with open("relatorio.json", "w") as file:
        json.dump(data, file, indent=4)

    print("Relatório salvo")


# Esta função irá carregar o arquivo de relatorio e escrevelo na linha de comando
def carregar_relatorio():
    try:
        with open("relatorio.json", "r") as file:
            relatorio = json.load(file)
            print("Relatório carregado:")
            print(json.dumps(relatorio, indent=4))
    except FileNotFoundError:
        print("Nenhum relatório salvo encontrado")
