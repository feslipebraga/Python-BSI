# Pergunte a que velocidade do carro de um usuário. Caso o valor informado seja maior que 80km/h, exiba uma mensagem dizendo que o usuário foi multado.
# Neste caso, exiba o valor da multa , cobrando R$ 5,00 por Km acima dos 80 km/h

velocidade = float(input('Qual a velocidade do carro em km/h? '))
km = velocidade - 80
multa = 5 * km

if velocidade > 80:
    print(f'O usuário foi multado em R${multa}!')