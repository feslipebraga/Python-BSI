C = set()

C.add(1)
C.add(8)
C.add(4)
C.add(3)

print(1 in C)

a = set([1, 2, 3])
b = set([3, 4, 5])

print(a - b)        # Mostra os valores de A, e caso em B tenha o mesmo valor, não é mostrado.
print(a | b)        # Une e mostra os dois conjuntos, sem repetir os valores duplicados.
print(a & b)        # Mostra os valores em comum entre A e B