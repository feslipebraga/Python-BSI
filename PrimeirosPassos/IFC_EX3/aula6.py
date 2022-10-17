nota1 = float(input('Informe a primeira nota: '))
nota2 = float(input('Informe a segunda nota: '))
media = (nota1 + nota2) / 2
print(f'A média é {media}')

if media < 7.0:
    print('Aluno em exame')
else:
    print('Você está aprovado')