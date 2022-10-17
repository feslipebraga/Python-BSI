# Criar um algoritmo que imprima todos os números de 1 até 100, e a soma de todos eles (intervalo fechado).

soma = 0
contador = 0
while contador < 100:
    contador += 1
    print(contador)
    soma = soma + contador
print(f"a soma de todos os números é {soma}")