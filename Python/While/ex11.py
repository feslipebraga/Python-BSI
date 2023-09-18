# Escreva um algoritmo que receba 15 números e imprima quantos números maiores que 30 foram digitados.

maiorque30 = 0
x = 0
while x < 5:
    x += 1
    numero = int(input(f"Informe o {x} numero: "))
    if numero > 30:
        maiorque30 = maiorque30 + 1
print(f"Você digitiou {maiorque30} números maior que 30")