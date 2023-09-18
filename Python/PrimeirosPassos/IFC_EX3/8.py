nota = float(input('Informe a nota: '))
frequencia = int(input('Informe a frequencia: '))

if frequencia < 75:
    print('REPROVADO')

if nota <= 3 and frequencia >= 75:
    print('REPROVADO')

if nota >= 3 and nota <= 7 and frequencia >= 75:
    print('EXAME')

if nota >=7 and frequencia >= 75:
    print('APROVADO')