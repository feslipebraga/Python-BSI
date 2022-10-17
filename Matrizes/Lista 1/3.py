# Faça um algoritmo que lê uma matriz M5x5 e mostrar os valores da diagonal principal.

import numpy as np
N = 3
matriz = np.zeros((N, N))

for l in range(N):
    for c in range(N):
        matriz[l][c] = int(input(f"MATRIZ [{l}, {c}]: "))

for l in matriz:
    for e in l:
        print(f"{e:.0f}", end=" ")
    print()

for x in range(len(matriz)):
    print(f"{matriz[x][x]:.0f}", end=" ")