# Utilize os arquivos pares.txt e impares.txt gerados através do código-fonte, apresentado nos slides. Faça a leitura destes dois arquivos e crie um só arquivo denominado de pareseimpares.txt com base em todas as linhas dos dois arquivos lidos e para preservar a ordem numérica.

with open("pares", "w") as pares, open("impares", "w") as impares:
    for x in range(10):
        if x % 2 == 0:
            pares.write(f"{x}\n")
        else:
            impares.write(f"{x}\n")

with open("pares") as pares, open("impares") as impares, open("pareseimpares", "w") as pei:
    x = pares.readlines()
    for a in x:
        pei.write(a)
    y = impares.readlines()
    for b in y:
        pei.write(b)

lista = []
with open("pareseimpares", "r") as pei:
    for x in pei.readlines():
        lista.append(int(x))
print(lista)

listaOrdem = sorted(lista)
print(listaOrdem)

with open("pareseimpares", "w") as pei:
    for x in listaOrdem:
        pei.write(f"{str(x)}\n")