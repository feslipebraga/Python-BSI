# Faça um algoritmo que lê uma matriz M10x10. Troque a seguir os valores contidos na linha de índice 2 com os da linha de índice 8
# e também troque os valores da linha de índice 5 com os da coluna de índice 9. No final mostre a matriz.

matriz = []
N = 4
for linha in range(N):
    lista = []
    for coluna in range(N):
        lista.append(int(input(f"Valor [{linha}, {coluna}]: ")))
    matriz.append(lista)
print(matriz)

# TROCANDO OS VALORES

aux = matriz[0]
matriz[0] = matriz[1]
matriz[1] = aux

# TROCANDO DE NOVO, OUTROS VALORES

aux2 = matriz[2]
matriz[2] = matriz[3]
matriz[3] = aux2

print(matriz)