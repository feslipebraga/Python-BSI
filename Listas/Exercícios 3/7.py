# Faça um programa que preencha dois vetores, X e Y, com dez números inteiros cada.
# Calcule e mostre os seguintes vetores resultantes: A diferença entre X e Y

X = []
Y = []
Z = []

for i in range(1, 11):
    X.append(int(input(f"Valor [{i}]: ")))
for i in range(1,11):
    Y.append(int(input(f"Valor [{i}]: ")))

for x in X:
    if x not in Y and x not in Z:
        Z.append(x)

print(X)
print(Y)
print(Z)