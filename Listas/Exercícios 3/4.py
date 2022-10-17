# Ler um vetor R de 5 elementos, inteiros, contendo o resultado da LOTO.
# A seguir ler um vetor A de 10 elementos inteiros contendo uma aposta.
# A seguir imprima quantos pontos fez o apostador.

R = []

print("RESULTADO DA LOTTO")
for r in range(1, 6):
    R.append(int(input(f"N[{r}]: ")))

A = []
for a in range(1, 11):
    A.append(int(input(f"Sua aposta [{a}/10]: ")))

pontos = 0

for p in A:
    if p in R:
        pontos += 1

if pontos == 5:
    print(f"VOCÊ ACERTOU TODOS OS NÚMEROS. PARABÉNS!!!")
else:
    print(f"Náo foi dessa vez :/ Você acertou {pontos} números.")