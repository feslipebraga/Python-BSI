# Elabore um algoritmo que receba as 3 notas de um aluno e uma letra. Se a letra for “A”,
# deve-se chamar uma sub-rotina que deverá calcular a média aritmética das notas dos alunos;
# Se a letra for “P”, deverá calcular a média ponderada, com pesos 5, 3 e 2.
# A média calculada deverá ser devolvida ao programa principal para, então, ser mostrada.

def mediaAritmetica(a, b, c):
    lista = [a, b, c]
    media = sum(lista) / len(lista)
    return media

def mediaPonderada(a, b, c):
    p1, p2, p3 = 5, 3, 2
    media = ((a*p1) + (b*p2) + (c*p3)) / (p1 + p2 + p3)
    return media

nota1 = int(input("Informe a 1ª nota: "))
nota2 = int(input("Informe a 2ª nota: "))
nota3 = int(input("Informe a 3ª nota: "))
while True:
    letra = input("Digite [A] ou [P]: ").upper()[0]
    if letra == "A":
        print(f"A média aritmética das notas é {mediaAritmetica(nota1, nota2, nota3)}")
        break
    elif letra == "P":
        print(f"A média ponderada das notas é {mediaPonderada(nota1, nota2, nota3)}")
        break
    else:
        print("Opção inválida. Digite 'A' ou 'P'.")