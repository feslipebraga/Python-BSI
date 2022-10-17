# Altere o algoritmo anterior para que ele realize o produto da primeira lista, pelo inverso da segunda lista.

a = []
b = []
c = []

for n in range(5):
    a.append(int(input(f"LISTA A - Valor[{n}]: ")))

print()

for n in range(5):
    b.append(int(input(f"LISTA B - Valor[{n}]: ")))

print(a)
print(b)

for x in range(5):
    produto = a[x] * b[-x -1]
    c.append(produto)

print(f"""O produto dos indíces das listas entre si é:
{c}""")