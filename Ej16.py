print("Matriz")
N = int(input("Tamaño de la matriz: "))

M = []
for i in range(N):
    fila = []
    print("Fila", i+1)
    for j in range(N):
        x = int(input(f"Valor ({i+1},{j+1}): "))
        fila.append(x)
    M.append(fila)

ok = True
for i in range(N):
    for j in range(N):
        if i == j:
            if M[i][j] != 1:
                ok = False
        else:
            if M[i][j] != 0:
                ok = False

if ok:
    print("Es una matriz identidad.")
else:
    print("No es una matriz identidad.")
