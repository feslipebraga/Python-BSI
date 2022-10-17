# Elabore um algoritmo que leia o nome e o ano de nascimento de uma pessoa
# e mostre qual é a sua idade atual.

nome = str(input('Qual o seu nome? '))
ano_nasc = int(input('Em qual ano você nasceu? '))
idade = 2022 - ano_nasc
print(f'A sua idade é {idade}')
