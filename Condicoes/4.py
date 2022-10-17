'''Faça um algoritmo que lê valores para duas variáveis X e Y. Se o
valor correspondente a 30% da soma de x por y for maior que 500
trocar os valores entre X e Y, senão mostrar o menor valor entre as
duas variáveis.'''

x = int(input('Informe um valor: '))
y = int(input('Informe outro: '))

if x < y:
    menor = x
else:
    menor = y

soma = x + y
porcentagem = 0.3 * soma

if porcentagem > 500:
    print(f'30% da soma dos valores é {porcentagem}. Excedeu o limite de 500. É necessário trocar os valores.')
else:
    print(f'O menor valor entre as duas variáveis é {menor}')
