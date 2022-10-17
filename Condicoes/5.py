litros_vendidos = float(input('Quantos litros foram vendidos? '))
print('=-' * 15)
print('''Qual o tipo de combustível?
[ A ] Alcool
[ G ] Gasolina''')
print('=-' * 15)
tipo_combustivel = str(input('Escolha uma opção: '))

preco_gasolina = 7.20
preco_alcool = 6.50

#DESCONTOS ALCOOL
ate20alcool = 0.97 * preco_alcool * litros_vendidos
acima20alcool = 0.95 * preco_alcool * litros_vendidos

#DESCONTOS GASOLINA
ate20gasolina = 0.96 * preco_gasolina * litros_vendidos
acima20gasolina = 0.94 * preco_gasolina * litros_vendidos


if tipo_combustivel == "A" or tipo_combustivel == "a":
    if litros_vendidos <= 20:
        print(f'O valor a ser pago será de R${ate20alcool:.2f}')
    elif litros_vendidos > 20:
        print(f'O valor a ser pago será de R${acima20alcool:.2f}')

elif tipo_combustivel == "G" or tipo_combustivel == "g":
    if litros_vendidos <= 20:
        print(f'O valor a ser pago será de R${ate20gasolina:.2f}')
    elif litros_vendidos > 20:
        print(f'O valor a ser pago será de R${acima20gasolina:.2f}')

else:
    print('Inválido! Insira a opção correta.')