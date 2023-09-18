# Faça uma sub-rotina que verifique se a matriz informada é simétrica ou não. Uma matriz só pode ser considerada simétrica se A[ i, j ] = A [ j, i ].

'''def simetria(m):
    for l in range(len(m)):
        for c in range(len(m[0])):
            print(m[c][l], end=" ")'''

#########################################

matriz = []

from random import randint
for l in range(2):
    lista = []
    for c in range(2):
        lista.append(randint(1, 10))
    matriz.append(lista)
print(matriz)

'''for linha in matriz:
    for elemento in linha:
        print(elemento, end=" ")
    print()
print()'''

#########################################

matrizReversa = []

for l in range(len(matriz)):
    aux = []
    for c in range(len(matriz)):
        aux.append(matriz[l][c])
    aux.reverse()
    matrizReversa.append(aux)
print(matrizReversa)

# NÃO FINALIZADO, NÃO ENTENDI O CONCEITO DE SIMETRIA EM PYTHON.