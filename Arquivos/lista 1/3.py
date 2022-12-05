# Escreva um programa que receba do usuário 5 números inteiros e o nome do arquivo no qual eles devem ser armazenados. Em seguida, ler do arquivo os valores armazenados copiando-os para uma lista de inteiros e os imprimindo na tela.

from random import randint
with open("3", "w") as NUMERO:
    for i in range(5):
        numero = randint(1, 10)
        NUMERO.write(f"{numero}\n")

with open("3") as NUMERO:
    linhas = NUMERO.readlines()
print(linhas)

lista = []
for linha in linhas:
    lista.append(int(linha))
print(lista)