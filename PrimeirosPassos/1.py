# receba o salário base de um funcionário, calcule e mostre o salário a receber,
# sabendo-se que o funcionário tem gratificação de 5% sobre o salário base
# e paga 7% de imposto também sobre o salário base;

salario_base = float(input('Informe o salário base: R$'))
gratificação = salario_base * 0.05
imposto = salario_base * 0.07
salario_liquido = salario_base - imposto + gratificação
print(f'Com a gratificação da empresa, você recebeu R${gratificação} a mais no seu salário.')
print(f'No entanto, foi descontando R${imposto:.2f} do imposto de renda.')
print(f'Seu salário liquído ficou R${salario_liquido}')

