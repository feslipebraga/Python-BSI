# Faça um algoritmo que lê valores para uma matriz M4X4 e um valor para a variável “a”
# (do tipo simples, pode ser: inteiro, float). Multiplicar cada valor contido na matriz pelo valor da variável e
# colocar os resultados num vetor(lista) V com 16 elementos. Mostre no final o vetor(lista).

matriz = []
N = 2           # Tamanho da matriz

a = int(input("Informe um valor para a variável: "))

for l in range(N):
    lista = []
    for c in range(N):
        lista.append(int(input(f"Valor [{l}, {c}]: ")))
    matriz.append(lista)

print(matriz)

V = []

for lista in matriz:
    for elemento in lista:
        V.append(elemento * a)

print(V)