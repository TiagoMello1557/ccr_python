from rich.console import Console
from rich.table import Table
from .utilidades import limpar_tela
from .relatorios import salvar_relatorio
from datetime import datetime
from .alertas import verificar_alerta
import time
import random


# Este modelo ira cuidar da visualização de status das linhas em tabelas

# Inicia a variavel do console
console = Console()


# Esta função esta cuidadndo da logica de construção da tabela
def exibir_tabela_status():
    count = 0
    while True:
        limpar_tela()
        data_hora_atual = datetime.now()
        data_hora_formatada = data_hora_atual.strftime("%Y-%m-%d %H:%M:%S")

        # Construindo a tabela
        table = Table(title="Status das Linhas")

        # Adicionando colunas a table
        table.add_column("Linha", justify="right", style="cyan", no_wrap=True)
        table.add_column("Status", style="magenta")
        table.add_column("Trens Operando", style="magenta")

        # Preparando lista de dados
        status = ["Operando normalmente", "Atrasada", "Falha tecnica", "Nao operante"]

        row_1 = ["1", f"{random.choice(status)}", str(random.randint(1, 10))]
        row_2 = ["2", f"{random.choice(status)}", str(random.randint(1, 10))]
        row_3 = ["3", f"{random.choice(status)}", str(random.randint(1, 10))]

        # Adicionando linhas a tabela
        table.add_row(row_1[0], row_1[1], row_1[2])
        table.add_row(row_2[0], row_2[1], row_2[2])
        table.add_row(row_3[0], row_3[1], row_3[2])

        # Sequencia para salvar dados no relatorio
        linha_trens = {"linha_1": row_1[2], "linha_2": row_2[2], "linha_3": row_3[2]}
        lista_status = {"linha_1": row_1[1], "linha_2": row_2[1], "linha_3": row_3[1]}
        salvar_relatorio(linha_trens, lista_status, data_hora_formatada)
        verificar_alerta(linha_trens, lista_status)

        console.print(table)
        print("\nAtualizando em 5 segundos... (Pressione Ctrl+C para parar)")
        count += 1
        time.sleep(5)
        if count == 3:
            return
