idade = int(input('Informe sua idade: '))
sexo = str(input('Informe seu sexo: F ou M? '))

if sexo == "F" or sexo == "f":
    if idade == 0 and idade < 12:
        mensagem = "menina"
    elif idade >= 12 and idade <= 24:
        mensagem = "moça"
    else:
        mensagem = "mulher"
    print(mensagem)

elif sexo == "M" or sexo == "m":
    if idade == 0 and idade < 12:
        mensagem = "menino"
    elif idade >= 12 and idade <= 24:
        mensagem = "rapaz"
    else:
        mensagem = "homem"
    print(mensagem)

else:
    print('Inválido!')