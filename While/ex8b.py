# 8) Criar um algoritmo que leia dez números inteiros e imprima o maior e o menor número.

x = maior = menor = 0

while x < 3:
    x = x + 1
    numero: int = int(input("Informe um número: "))
    if x == 1:
        maior = menor = numero
    else:
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero
print(f"O maior valor foi {maior} e o menor foi {menor}")