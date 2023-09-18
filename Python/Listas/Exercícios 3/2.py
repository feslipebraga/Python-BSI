# Faça um programa que preencha um vetor com 9 números inteiros, calcule e mostre os que são números primos e suas respectivas posições.

vetor = []
primos = []
divisor = 0

for v in range(5):
    numero = int(input(f"Inteiro [{v}]: "))
    vetor.append(numero)
    
for p in vetor:
    print(f"p: {p}")
    if vetor[p] % p == 0:
        divisor = divisor + 1
        print(f"divisor: {divisor}")
    if divisor == 2:
        primos.append(numero)

print(vetor)
print(primos)