# 2. Faça um algoritmo que lê valores para 3 variáveis A, B e C e
# mostra as mesmas em ordem crescente.

a = float(input('Informe um valor: '))
b = float(input('Informe outro valor: '))
c = float(input('Informe mais outro valor: '))

if a > b and a > c: 
    maior = a
    if b > c:
        intermediario = b
        menor = c
    if c > b:
        intermediario = c
        menor = b

if b > a and b > c:
    maior = b
    if a > c:
        intermediario = a
        menor = c
    if c > a:
        intermediario = c
        menor = a

if c > a and c > b:
    maior = c
    if a > b:
        intermediario = a
        menor = b
    if b > a:
        intermediario = b
        menor = a
print(f'Os valores crescentes dos números informados é {menor}, {intermediario} e {maior}')