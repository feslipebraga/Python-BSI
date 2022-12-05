# Faça um programa que crie um arquivo texto e que salve seu nome neste arquivo, após sobrescreva o conteúdo deste arquivo com a frase “Eu amo algoritmos!”.

nome = input("Digite seu nome: ").capitalize()

with open("2", "w") as NOME:
    NOME.write(nome)

with open("2") as NOME:
    print(f"Olá, {NOME.read()}! É um prazer te conhecer.")

with open("2", "w") as NOME:
    NOME.write("Eu amo algoritmos!")

with open("2") as NOME:
    print(NOME.read())