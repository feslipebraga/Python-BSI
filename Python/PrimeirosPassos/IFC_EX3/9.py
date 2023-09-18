peso = float(input('Qual o peso em kg do indivíduo? '))
altura = float(input('Qual a altura em metros do indivíduo? '))

imc = peso / (altura**2)

print(f'O resultado do IMC é {imc:.2f}')

if imc < 20:
    print ('abaixo do peso')

if imc >= 20 and imc <= 25:
    print('peso normal')

if imc >= 25 and imc <= 30:
    print('sobre peso')

if imc >= 30 and imc <= 40:
    print('obeso')

if imc >= 40:
    print('obeso mórbido')