# Escreva um algoritmo que leia 20 números e imprima a soma dos positivos e o total de números negativos.

negativos = 0
soma_positivos = 0
x = 0
while x < 3:
    x += 1
    numero = int(input(f"Informe o {x} numero: "))
    if numero > 0:
        soma_positivos += numero
    if numero < 0:
        negativos += 1
print(f"A soma dos positivos é {soma_positivos} e o total de negativos é {negativos}")
