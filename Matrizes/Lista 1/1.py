# Faça um algoritmo que lê uma matriz M5x5 e mostrar os valores digitados para a matriz M.

matriz = []

for l in range(5):
    lista = []
    for c in range(5):
        lista.append(int(input(f"Matriz [{l}, {c}]: ")))
    matriz.append(lista)

for lista in matriz:
    for elemento in lista:
        print(f"{elemento:}", end=" ")
    print()