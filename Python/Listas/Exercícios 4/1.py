R = set()      # 5
S = set()      # 10

for r in range(5):
    R.add(int(input(f"Valor {r+1}: ")))
for s in range(10):
    S.add(int(input(f"Valor {s+1}: ")))
print(R)
print(S)
X = R & S
print(f"Os valores em comum entre as 2 listas são {X}")