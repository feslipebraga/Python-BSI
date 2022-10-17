# Faça um algoritmo que lê 10 valores para uma variável do tipo lista de nome x e mostre os 10 valores armazenados.

x = []

for n in range(1, 11):
    x.append(int(input(f"Valor [{n}]: ")))
print(x)