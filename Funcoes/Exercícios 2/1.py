# Escreva um algoritmo que imprima todos os números inteiros de 10 a 1 (em ordem decrescente), utilizando recursividade.

def decresce(n):
    print(n)
    if n != 1:
        decresce(n -1)

decresce(10)