import numpy as np

N = 6
K = np.zeros(N)
impar = []
par = []

print(K)

for x in range(6):
    K[x] = int(input(f"Valor {x}: "))
    if x % 2 == 0:
        par.append(K[x])
    if x % 2 == 1:
        impar.append(K[x])

print(K)
print(par)
print(impar)