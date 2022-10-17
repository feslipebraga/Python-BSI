numero = int(input("Informe um numero: "))
x = 1

for numero in range (1, numero + 1):
    x = x * numero
    print(numero)
print(f"O fatorial de {numero} é {x}")
