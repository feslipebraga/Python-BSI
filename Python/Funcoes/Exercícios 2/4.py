# Escreva um programa que preencha um vetor de inteiros de 10 posições e solicite ao usuário um valor inteiro para ser procurado no vetor. Crie uma função que receba como parâmetro o vetor e o número a ser procurado. Ao final, retorne quantas vezes o número foi encontrado no vetor.

def procura(vet, num):
    contador = vet.count(num)
    return contador

from random import randint
vetor = []
for c in range(10):
    numero = randint(0, 10)
    vetor.append(numero)
print(f"SEU VETOR {vetor}")
numero = int(input("Qual número você deseja procurar? "))

print(f'O número {numero} foi encontrado {procura(vetor, numero)} vez(es) no vetor.')