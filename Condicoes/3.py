# 3. Faça um algoritmo que lê valores para 5 variáveis A, B, C, D e E.
# Encontrar e mostrar o maior valor digitado.

a = int(input('Informe um numero inteiro: '))
b = int(input('Informe um numero inteiro: '))
c = int(input('Informe um numero inteiro: '))
d = int(input('Informe um numero inteiro: '))
e = int(input('Informe um numero inteiro: '))

if a > b and a > c and a > d and a > e:
    maior = a
if b > a and b > c and b > d and b > e:
    maior = b
if c > a and c > b and c > d and c > e:
    maior = c
if d > a and d > b and d > c and d > e:
    maior = d
if e > a and e > b and e > c and e > d:
    maior = e
print(f'O maior número informado é o {maior}')