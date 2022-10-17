# Faça um algoritmo que receba um valor N correspondente ao tamanho de duas matrizes quadradas de ordem N (MNxN).
# Leia os valores inteiros para preencher todas as posições de cada uma das matrizes, e calcule a SOMA das matrizes.

matrizA = []
matrizB = []
matriz = []
N = int(input(f"Número de elementos para cada matriz: "))

for l in range(N):
    lista = []
    for c in range(N):
        lista.append(int(input(f"MATRIZ A [{l}, {c}]: ")))
    matrizA.append(lista)

for l in range(N):
    lista = []
    for c in range(N):
        lista.append(int(input(f"MATRIZ A [{l}, {c}]: ")))
    matrizB.append(lista)

print(f"MATRIZ A = {matrizA}")
print(f"MATRIZ B = {matrizB}")

for l in range(N):
    lista = []
    for c in range(N):
        lista.append(matrizA[l][c] + matrizB[l][c])
    matriz.append(lista)

print(f"A SOMA DOS VALORES É = {matriz}")