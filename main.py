import time
import random

# Implementação da busca sequencial
def busca_sequencial(lista, alvo):
    visitados = 0
    for i, item in enumerate(lista):
        visitados += 1
        if item == alvo:
            return i, visitados
    return -1, visitados

# Implementação da busca binária
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

# Função para medir tempo e posições visitadas
def testar_buscas(tamanho, caso):
    lista = list(range(tamanho))

    if caso == "medio":
        alvo = random.choice(lista)
    elif caso == "pior":
        alvo = -1  # elemento que não existe

    print(f"\n--- Tamanho: {tamanho}, Caso: {caso.upper()} ---")

    # Busca Sequencial
    t0 = time.perf_counter()
    _, visitados_seq = busca_sequencial(lista, alvo)
    t1 = time.perf_counter()
    tempo_seq = t1 - t0
    print(f"Sequencial: Tempo = {tempo_seq:.6f}s, Visitados = {visitados_seq}")

    # Busca Binária
    t0 = time.perf_counter()
    _, visitados_bin = busca_binaria(lista, alvo)
    t1 = time.perf_counter()
    tempo_bin = t1 - t0
    print(f"Binária:    Tempo = {tempo_bin:.6f}s, Visitados = {visitados_bin}")

# Testar para diferentes tamanhos e casos
for tamanho in [1000, 10000, 100000]:
    testar_buscas(tamanho, "medio")
    testar_buscas(tamanho, "pior")
