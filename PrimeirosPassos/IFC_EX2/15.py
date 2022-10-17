# Faça um programa que leia o nome de um aluno e duas notas,
# calcule e mostre a média ponderada dessas notas,
# considerando peso 2 para a primeira nota e peso 3 para a segunda nota.

# Mp = (x1 * p1 + x2 * p2) / (p1 + p2)

nome = str(input('Qual o nome do aluno? '))
nota1 = float(input('Informe a nota 1: '))
nota2 = float(input('Informe a nota 2: '))
media_ponderada = (nota1 * 2 + nota2 * 3) / (2 + 3)
print(f'O aluno {nome} obteve a média ponderada: {media_ponderada:.2f}')
