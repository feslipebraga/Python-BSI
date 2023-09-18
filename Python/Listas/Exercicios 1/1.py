# Faça um algoritmo que lê 10 valores para uma variável do tipo lista de nome x e mostre os 10 valores armazenados.

x = []
for i in range(1, 11):
    x.append(float(input(f"Digite o {i} valor: ")))
print(x)