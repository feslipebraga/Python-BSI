# Faça um algoritmo que lê 10 valores para uma variável do tipo lista de nome x.
# Após completar toda a leitura da lista, verificar se cada valor armazenado na lista é par ou ímpar.
# Se for par, fazer com que o valor seja atualizado para o resultado da multiplicação do valor contido pelo índice.
# Se for impar fazer com que a lista receba o valor do seu próprio índice.

x = []

for i in range(1, 4):
    numero = int(input(f"Digite o {i} valor: "))
    if numero % 2 == 0:
        numero = x[i] * numero
        print("O número é par")
        x.append(numero)
    print(x)