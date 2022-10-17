# Criar um algoritmo que leia os limites inferior e superior de um intervalo e imprima todos os
# números pares no intervalo aberto e seu somatório.
# Suponha que os dados digitados são para um intervalo crescente, ou seja, o primeiro valor é menor que o segundo.

inferior = int(input("Informe o menor numero do intervalo: "))
superior = int(input("Informe o maior numero do intervalo: "))
soma = 0

for x in range (inferior, superior + 1):
    if x % 2 == 0:
        soma = soma + x
        print(x)
print(f"A soma dos valores é {soma}")