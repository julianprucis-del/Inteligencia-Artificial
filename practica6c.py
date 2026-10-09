tablero = [
    [" "," "," "],
    [" "," "," "],
    [" "," "," "]
]


def imprimir():
    print()
    for fila in tablero:
        print(fila)
    print()


def ganador(j):

    for i in range(3):
        if tablero[i][0] == tablero[i][1] == tablero[i][2] == j:
            return True

    for i in range(3):
        if tablero[0][i] == tablero[1][i] == tablero[2][i] == j:
            return True

    if tablero[0][0] == tablero[1][1] == tablero[2][2] == j:
        return True

    if tablero[0][2] == tablero[1][1] == tablero[2][0] == j:
        return True

    return False


def terminal():

    if ganador("X"):
        return True

    if ganador("O"):
        return True

    for fila in tablero:
        if " " in fila:
            return False

    return True


def utilidad():

    if ganador("X"):
        return 1

    if ganador("O"):
        return -1

    return 0


def sucesores():

    lista = []

    for i in range(3):
        for j in range(3):
            if tablero[i][j] == " ":
                lista.append((i,j))

    return lista


def alfa_beta(turno, alfa, beta):

    if terminal():
        return utilidad()

    if turno == "X":

        mejor = -100

        for i,j in sucesores():

            tablero[i][j] = "X"

            valor = alfa_beta("O", alfa, beta)

            tablero[i][j] = " "

            if valor > mejor:
                mejor = valor

            if mejor > alfa:
                alfa = mejor

            if beta <= alfa:
                break

        return mejor

    else:

        mejor = 100

        for i,j in sucesores():

            tablero[i][j] = "O"

            valor = alfa_beta("X", alfa, beta)

            tablero[i][j] = " "

            if valor < mejor:
                mejor = valor

            if mejor < beta:
                beta = mejor

            if beta <= alfa:
                break

        return mejor


def mejor_jugada():

    mejor = -100
    movimiento = None

    for i,j in sucesores():

        tablero[i][j] = "X"

        valor = alfa_beta("O",-100,100)

        tablero[i][j] = " "

        if valor > mejor:
            mejor = valor
            movimiento = (i,j)

    return movimiento


print("=== GATO ===")
print("Tú eres O")
print("La computadora es X")

while not terminal():

    imprimir()

    x = int(input("Fila (0-2): "))
    y = int(input("Columna (0-2): "))

    if tablero[x][y] != " ":
        print("Casilla ocupada")
        continue

    tablero[x][y] = "O"

    if terminal():
        break

    mov = mejor_jugada()

    tablero[mov[0]][mov[1]] = "X"

    print("La computadora jugó:", mov)

imprimir()

if ganador("X"):
    print("La computadora ganó.")

elif ganador("O"):
    print("¡Ganaste!")

else:
    print("Empate.")