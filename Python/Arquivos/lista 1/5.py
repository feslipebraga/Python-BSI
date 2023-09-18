# Crie um programa que inverta a ordem das linhas do arquivo pares.txt. A primeira linha deverá conter o maior número; e a última, o menor.

par = []
with open("pares") as pares:
    for x in pares.readlines():
        par.append(int(x))
print(par)

listaReversa = list(reversed(par))
print(listaReversa)

with open("pares", "w") as pares:
    for x in listaReversa:
        pares.write(f"{str(x)}\n")