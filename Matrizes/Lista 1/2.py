# Faça um algoritmo que lê uma matriz M5x5. A matriz deve ser preenchida através das colunas.

import numpy as np
N = 3
matriz = np.zeros((N, N))

for l in range(N):
    for c in range(N):
        matriz[c][l] = int(input(f"MATRIZ [{c}, {l}]: "))

for lista in matriz:
    for elemento in lista:
        print(f"{elemento:.0f}", end=" ")
    print()