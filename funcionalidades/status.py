import time
import random
from .relatorios import salvar_relatorio
from .utilidades import limpar_tela
from .alertas import verificar_alerta
from datetime import datetime

# Esse modelo irá exibir os status das linhas de trem na linha de comando de forma simplificada


# Esta função ira cuidar da logica para exibir os dados(dados são gerados de forma aleatoria para simulação)
def simulacao_status():
    count = 0
    while True:
        limpar_tela()
        # Cria dict de status e trens das linhas
        linhas_status = {}
        linhas_trens = {}

        # Cria e formata variaveis de data e hora atual
        data_hora_atual = datetime.now()
        data_hora_formatada = data_hora_atual.strftime("%Y-%m-%d %H:%M:%S")
        print(data_hora_formatada)
        # Ira repetir os status para cada linha de trem
        for linha in range(1, 4):
            trens_operando = random.randint(1, 10)
            status = random.choice(["Operando normalmente",
                                    "Atrasada",
                                    "Falha",
                                    "Nao operante"])
            print(f"\nlinha {linha}")
            print(f"status: {status}")
            print(f"trens: {trens_operando}")
            # Adicionando dados a dict para depois salvar como relatorio
            linhas_status[f"linha_{linha}"] = status
            linhas_trens[f"linha_{linha}"] = trens_operando

        # Passando as dict para a func de salvar relatorio
        salvar_relatorio(linhas_trens, linhas_status, data_hora_formatada)
        verificar_alerta(linhas_trens, linhas_status)
        print("\nAtualizando em 5 segundos... (Pressione Ctrl+C para parar)")
        count += 1
        time.sleep(5)
        if count == 3:
            return
