# Faça um programa que preencha dois vetores de dez elementos numéricos cada um e mostre o vetor resultante da intercalação deles:

vetor1 = []
vetor2 = []

print("VETOR UM")
for x in range(3):
    vetor1.append(int(input(f"Valor [{x}]: ")))
print("VETOR DOIS")
for x in range(3):
    vetor2.append(int(input(f"Valor [{x}]: ")))

print(vetor1)
print(vetor2)

for y in range(len(vetor1)):
    print(vetor1[y], end=" ")
    print(vetor2[y], end=" ")