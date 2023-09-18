# Faça um programa que crie um arquivo texto e que salve seu nome neste arquivo (o nome deve ser  informado via terminal).Faça um programa que crie um arquivo texto e que salve seu nome neste arquivo (o nome deve ser  informado via terminal).

nome = input("Digite seu nome: ").capitalize()

with open("1", "w") as NOME:
    NOME.write(nome)

with open("1") as NOME:
    print(f"Olá, {NOME.read()}! É um prazer te conhecer.")