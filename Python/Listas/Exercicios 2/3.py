# Elabore um algoritmo que leia duas listas de 5 posições, após a leitura realizar a soma e imprima o resultado da soma entre as duas listas de inteiros.

a = []
b = []
c = []

for n in range(1, 6):
    a.append(int(input(f"LISTA A - Valor[{n}]: ")))

print()

for n in range(1, 6):
    b.append(int(input(f"LISTA B - Valor[{n}]: ")))

print(a)
print(b)

for x in range(5):
    soma = a[x] + b[x]
    c.append(soma)

print(f"""A soma dos indíces das listas entre si é:
{c}""")