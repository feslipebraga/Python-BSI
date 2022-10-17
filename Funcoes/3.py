# Crie uma sub-rotina que receba como parâmetro uma lista V contendo 25 elementos de números inteiros
# e substitua todos os valores negativos de V por 0.
# A lista deverá ser retornada para quem realizou a chamada desta função.

from random import randint

def lista(lst):
    for pos, x in enumerate(lst):
        if x < 0:
            lst[pos] = 0
    return lst

v = []
for x in range(25):
    v.append(randint(-100, 100))
print(v)
print(lista(v))