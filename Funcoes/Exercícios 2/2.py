# Escreva um algoritmo que leia um valor para X e uma sub-rotina que imprima todos os números ímpares do intervalo fechado de 1 a X.

def impares(n):
    imp = []
    for x in range(1, n+1):
        if x % 2 == 1:
            imp.append(x)
    return imp

numero = int(input('Informe um número: '))
print(f"Os numeros ímpares no intervalo 1 - {numero} são: {impares(numero)}")