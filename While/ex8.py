# Criar um algoritmo que leia dez números inteiros e imprima o maior e o menor número.

x = 0
maior = 0
menor = 0

while x < 10:
    x += 1
    numero = int(input("Informe um número inteiro: "))
    if x == 1:
        maior = menor = numero
    else:
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero
print(f"O maior valor foi {maior} e o menor foi {menor}")