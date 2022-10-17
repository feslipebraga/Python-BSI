# Faça um algoritmo que lê uma matriz M5X5 e crie 2 vetores SL e SC com 5 posições cada.
# Adicionar aos vetores o resultado da soma das linhas e das colunas da matriz, no final mostrar os dois vetores.

matriz = []
N = 3

for l in range(N):
    lista = []
    for c in range(N):
        lista.append(int(input(f"Valor [{l}, {c}]: ")))
    matriz.append(lista)

for l in matriz:
    for e in l:
        print(e, end="  ")
    print()


SL = []
SC = []

for l in range(N):
    cont = 0
    for c in range(N):
        cont += matriz[l][c]
    SL.append(cont)
print(SL)

for l in range(N):
    cont2 = 0
    for c in range(N):
        cont2 += matriz[c][l]
    SC.append(cont2)
print(SC)