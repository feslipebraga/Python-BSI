# MATRIZ:
# O somatório dos valores da coluna 2.
# O somatório dos valores da diagonal principal

# CRIANDO A MATRIZ

import numpy as np
N = 3
matriz = np.zeros((N, N))

for linha in range(N):
    for coluna in range(N):
        matriz[linha][coluna] = int(input(f"MATRIZ [{linha}, {coluna}]: "))

# MOSTRANDO OS VALORES DA MATRIZ

print("-" * 10 )
for lista in matriz:
    for elemento in lista:
        print(f" {elemento:.0f}", end=" ")
    print()
print("-" * 10 )

# SOMA DA COLUNA 2

coluna2 = []
for x in range(len(matriz)):
    coluna2.append(matriz[x][2])
print(f"""A coluna 2 é composta por: {coluna2}
E a soma dos valores é: {sum(coluna2):.0f}""")

# SOMA DOS VALORES DA DIAGONAL

diagonal = []
for x in range(len(matriz)):
    diagonal.append(matriz[x][x])
print(f"""A diagonal principal é composta por: {diagonal}
E a soma dos valores é: {sum(diagonal):.0f}""")