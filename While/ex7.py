# Criar um algoritmo que imprima todos os números de 1 até 10, e a média geral todos eles (intervalo fechado).

s = 0
x = 0
while x < 10:
    x += 1
    print(x)
    s = s + x
print(f"A soma é {s}")
print(f"A média dos valores {s / x}")