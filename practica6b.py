tablero = [
    [" "," "," "],
    [" "," "," "],
    [" "," "," "]
]

nodos = 0

def imprimir():

    for fila in tablero:
        print(fila)


def ganador(jugador):

    # Filas
    for i in range(3):
        if tablero[i][0] == tablero[i][1] == tablero[i][2] == jugador:
            return True

    # Columnas
    for i in range(3):
        if tablero[0][i] == tablero[1][i] == tablero[2][i] == jugador:
            return True

    # Diagonal principal
    if tablero[0][0] == tablero[1][1] == tablero[2][2] == jugador:
        return True

    # Diagonal secundaria
    if tablero[0][2] == tablero[1][1] == tablero[2][0] == jugador:
        return True

    return False


# terminal()
def terminal():

    if ganador("X"):
        return True

    if ganador("O"):
        return True

    for fila in tablero:
        if " " in fila:
            return False

    return True


# utilidad()
def utilidad():

    if ganador("X"):
        return 1

    if ganador("O"):
        return -1

    return 0


# sucesores()
def sucesores():

    lista = []

    for i in range(3):
        for j in range(3):

            if tablero[i][j] == " ":
                lista.append((i, j))

    return lista

#Minimax
def minimax(turno):

    global nodos

    nodos += 1

    if terminal():
        return utilidad()

    if turno == "X":

        mejor = -100

        for i, j in sucesores():

            tablero[i][j] = "X"

            valor = minimax("O")

            tablero[i][j] = " "

            if valor > mejor:
                mejor = valor

        return mejor

    else:

        mejor = 100

        for i, j in sucesores():

            tablero[i][j] = "O"

            valor = minimax("X")

            tablero[i][j] = " "

            if valor < mejor:
                mejor = valor

        return mejor


#poda alfa-beta.
nodos_ab = 0

def alfa_beta(turno, alfa, beta):

    global nodos_ab

    nodos_ab += 1

    if terminal():
        return utilidad()

    if turno == "X":

        mejor = -100

        for i, j in sucesores():

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

        for i, j in sucesores():

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


# -------- PRUEBAS --------

print("Tablero:")

imprimir()

print()

print("Terminal:", terminal())
print("Utilidad:", utilidad())
print("Sucesores:", sucesores())

print()

resultado = minimax("X")

print("Resultado Minimax:", resultado)

print("Nodos visitados:", nodos)

print()

resultado = alfa_beta("X", -100, 100)

print("Resultado Alfa-Beta:", resultado)

print("Nodos visitados:", nodos_ab)