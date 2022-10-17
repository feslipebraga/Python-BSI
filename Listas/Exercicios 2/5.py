# Faça um algoritmo que lê duas listas A e B com 5 elementos cada.
# Construir uma lista C, sendo este a junção das duas outras listas, ou seja,
# a lista C deverá conter 10 elementos. Mostre no final a lista C.

a = [0, 0, 0, 0, 0]
b = [0, 0, 0, 0, 0]

for x in range(len(a)):
    a[x] = int(input(f"Valor [{x}]: "))
print(a)

for x in range(len(b)):
    b[x] = int(input(f"Valor [{x}]: "))
print(b)
print()

c = []

for x in range(5):
    c.append(a[x])
for x in range(5):
    c.append(b[x])
print(c)