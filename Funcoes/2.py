# Faça um algoritmo contendo uma sub-rotina que receba dois números positivos inteiros por parâmetro e
# retorne a soma dos N números inteiros existentes entre eles, incluindo na soma os dois números informados.

def nPositivos(a, b):
    soma = 0
    for x in range(a, b+1):
        soma += x
    return soma

def error():
    print("\033[31mERRO! Digite um valor maior que 0.\033[m")

while True:
    numero1 = int(input("Informe um número inteiro POSITIVO: "))
    if numero1 < 0:
        error()
        continue
    else:
        break
while True:    
    numero2 = int(input("Informe outro número inteiro POSITIVO: "))
    if numero2 < 0:
        error()
        continue
    else:
        break
print(f"A soma entre os números dos valores {numero1} e {numero2} é = {nPositivos(numero1, numero2)}")