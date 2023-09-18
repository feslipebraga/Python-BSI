R = [] # 5. resultado da lotto
A = [] # 10. APOSTA.
print("     RESULTADO DA LOTTO")
for r in range(1, 6):
    R.append(int(input(f"Número {r}/5: ")))
print("     SUA APOSTA")
for a in range(1, 11):
    A.append(int(input(f"Aposta {a}/10: ")))
pontos = 0
for x in range(len(R)):
    if R[x] in A:
        pontos += 1
print(R)
print(A)
print(f"Sua pontuação: {pontos}pts")