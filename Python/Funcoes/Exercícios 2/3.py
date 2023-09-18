# Construa uma função que receba como parâmetro uma matriz quadrada 4 X 4 e retorne a soma dos valores da diagonal principal.

def matriz(l, c):
    m = []
    diag = []
    for linha in range(l):
        lista = []
        for coluna in range(c):
            lista.append(int(input((f"V[{linha}, {coluna}]: "))))
        m.append(lista)
    for x in range(len(m)):
        diag.append(m[x][x])
    print(f"Matriz: {m}")
    print(f"Valores da diagonal principal: {diag}")
    print(f"Soma dos valores da diagonal: {sum(diag)}")

matriz(4, 4)