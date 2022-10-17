# receba o valor de um depósito e o valor da taxa de juros anual,
# calcule e mostre o valor do rendimento e o valor total depois do rendimento (após 1 ano);

deposito = float(input('Quanto você quer depositar? R$'))
taxa_juros = float(input('Qual a taxa de juros anual? (em porcentagem) '))
rendimento = deposito * taxa_juros/100 * 1 # 1 ano
valor_total = rendimento + deposito
print(f'O valor depositado, em 1 ano, aplicado sobre o porcentual de juros {taxa_juros},')
print(f'terá um rendimento de R${rendimento} e o valor total será R${valor_total}')
