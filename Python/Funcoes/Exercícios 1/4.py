# Faça uma sub-rotina que imprima todos os números inteiros de 10 a 1 ( ou seja, em ordem decrescente).

from time import sleep

def numeros():
    for x in range(10, 0, -1):
        print(x)
        sleep(1)
    print("\033[31mBOWWW!!!\033[m")

numeros()