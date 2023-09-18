# Escreva um algoritmo que receba cinco números do usuário e imprima o cubo de cada número.

x = 0
while x < 5:
    x += 1
    numero = int(input("Informe um numero: "))
    print(f"{numero} ao cubo é igual a {numero ** 3}")
print("Fim")