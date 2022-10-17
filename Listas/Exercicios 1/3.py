# Elabore um algoritmo que leia duas listas de 5 posições,
# após a leitura realizar a soma e imprima o resultado da soma entre as duas listas de inteiros.

lista_a = []
lista_b = []

soma_a = 0
soma_b = 0

for i in range(1, 6):
    numero = int(input(f"Digite o {i} valor para a lista A: "))
    lista_a.append(numero)
    soma_a += numero

for i in range(1, 6):
    numero = int(input(f"Digite o {i} valor para a lista B: "))
    lista_b.append(numero)
    soma_b += numero

print(f"""Lista A
{lista_a}
A soma dos valores da lista: {soma_a}""")

print(f"""Lista B
{lista_b}
A soma dos valores da lista: {soma_b}""")