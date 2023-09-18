# Escreva um algoritmo, que leia um conjunto de 10 fichas, cada uma contendo, a altura e o código do sexo de uma pessoa
# (código = 1 se for masculino e 2 se for feminino), e calcule e imprima:
# ● a maior e a menor altura da turma;
# ● a média de altura das mulheres;
# ● a média de altura da turma.

x = 0
maior_altura = 0
menor_altura = 0
altura_mulheres = 0
soma_alturas_mulheres = 0

while x < 3:
    x += 1
    altura = float(input("Informe sua altura: "))
    codigo = int(input('''Qual o sexo?
1 MASCULINO
2 FEMININO
Qual a opcão: '''))

    # Maior e menor altura
    if x == 1:
        maior_altura = menor_altura = altura
    if altura > maior_altura:
        maior_altura = altura
    if altura < menor_altura:
        menor_altura = altura

    # Media altura das mulheres
    if codigo == 2:
        soma_alturas_mulheres = soma_alturas_mulheres + altura
        altura_mulheres = altura_mulheres + 1
        print(soma_alturas_mulheres)
        print(altura_mulheres)
        print(f"A media da altura das mulheres é {soma_alturas_mulheres / altura_mulheres}")

print(f"A maior altura é {maior_altura} e a menor é {menor_altura}")
