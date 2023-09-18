# Ler 2 vetores, R de 5 elementos e S de 10 elementos, ambos de inteiros.
# Gere um vetor X que possua os elementos comuns a R e a S.
# Considere que no mesmo vetor não haverá números repetidos. 

R = []
S = []

for c in range(5):
    R.append(int(input(f"Valor [{c}]: ")))

for c in range(10):
    S.append(int(input(f"Valor [{c}]: ")))

X = []

for x in S:
    if x in R:
        X.append(x)

print(R)
print(S)
print(X)