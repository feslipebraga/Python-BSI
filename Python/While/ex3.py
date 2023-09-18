# Escreva um algoritmo que imprima todos os números ímpares do intervalo fechado de 1 a 100.

x = 0
while x < 100:
    x = x + 1
    if x % 2 != 0:
        print(x)