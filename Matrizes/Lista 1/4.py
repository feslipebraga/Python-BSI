# Faça um algoritmo que lê uma matriz M5x5. Calcular e mostrar a soma de todos os valores da linha 4.

matriz = []
N = 3

for l in range(N):
    linha = []
    for c in range(N):
        linha.append(int(input(f"MATRIZ [{l}, {c}]: ")))
    matriz.append(linha)

for lista in matriz:
    for elemento in lista:
        print(f"{elemento}", end=" ")
    print()

soma = sum(matriz[1])
print(f"""Linha 1: {matriz[1]}
A soma dos valores da linha 1 é: {soma}""")