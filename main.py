import time
import random
import matplotlib.pyplot as plt
import pandas as pd
from tabulate import tabulate

# Busca Sequencial
def busca_sequencial(lista, alvo):
    visitados = 0
    for i, item in enumerate(lista):
        visitados += 1
        if item == alvo:
            return i, visitados
    return -1, visitados

# Busca Binária
def busca_binaria(lista, alvo):
    inicio = 0
    fim = len(lista) - 1
    visitados = 0
    while inicio <= fim:
        meio = (inicio + fim) // 2
        visitados += 1
        if lista[meio] == alvo:
            return meio, visitados
        elif lista[meio] < alvo:
            inicio = meio + 1
        else:
            fim = meio - 1
    return -1, visitados

# Coleta de dados
tamanhos = [1000, 10000, 100000]
dados = []

for tamanho in tamanhos:
    for caso in ['medio', 'pior']:
        lista = list(range(tamanho))
        alvo = random.choice(lista) if caso == 'medio' else -1

        # Sequencial
        t0 = time.perf_counter()
        _, vis_seq = busca_sequencial(lista, alvo)
        t1 = time.perf_counter()
        tempo_seq = t1 - t0

        # Binária
        t0 = time.perf_counter()
        _, vis_bin = busca_binaria(lista, alvo)
        t1 = time.perf_counter()
        tempo_bin = t1 - t0

        dados.append({
            'Tamanho': tamanho,
            'Caso': caso,
            'Tempo Sequencial': tempo_seq,
            'Visitados Sequencial': vis_seq,
            'Tempo Binária': tempo_bin,
            'Visitados Binária': vis_bin
        })

# DataFrame
df = pd.DataFrame(dados)

# ===== TABELA =====
print("\n===== TABELA DE RESULTADOS =====\n")
pivotada = df.pivot(index='Tamanho', columns='Caso')[
    ['Tempo Sequencial', 'Visitados Sequencial', 'Tempo Binária', 'Visitados Binária']
]
print(tabulate(pivotada, headers='keys', tablefmt='fancy_grid', showindex=True, floatfmt=".6f"))

# ===== GRÁFICOS DE LINHA =====
fig, axs = plt.subplots(2, 2, figsize=(14, 10))
casos = ['medio', 'pior']

for i, caso in enumerate(casos):
    df_caso = df[df['Caso'] == caso]

    # Tempo
    axs[0, i].plot(df_caso['Tamanho'], df_caso['Tempo Sequencial'], marker='o', label='Sequencial')
    axs[0, i].plot(df_caso['Tamanho'], df_caso['Tempo Binária'], marker='s', label='Binária')
    axs[0, i].set_title(f'Tempo de Execução - Caso {caso.title()}')
    axs[0, i].set_xlabel('Tamanho da Entrada')
    axs[0, i].set_ylabel('Tempo (s)')
    axs[0, i].legend()
    axs[0, i].grid(True)

    # Visitados
    axs[1, i].plot(df_caso['Tamanho'], df_caso['Visitados Sequencial'], marker='o', label='Sequencial')
    axs[1, i].plot(df_caso['Tamanho'], df_caso['Visitados Binária'], marker='s', label='Binária')
    axs[1, i].set_title(f'Comparações - Caso {caso.title()}')
    axs[1, i].set_xlabel('Tamanho da Entrada')
    axs[1, i].set_ylabel('Posições Visitadas')
    axs[1, i].legend()
    axs[1, i].grid(True)

plt.tight_layout()
plt.show()
