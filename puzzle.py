objetivo = [
    [0,1,2],
    [3,4,5],
    [6,7,8]
]

inicio = [
    [7,2,4],
    [5,0,6],
    [8,3,1]
]
# h1: fichas mal colocadas
def h1(estado):

    contador = 0

    for i in range(3):
        for j in range(3):

            if estado[i][j] != 0 and estado[i][j] != objetivo[i][j]:
                contador += 1

    return contador


# h2: distancia Manhattan
def h2(estado):

    distancia = 0

    posiciones = {}

    for i in range(3):
        for j in range(3):
            posiciones[objetivo[i][j]] = (i, j)

    for i in range(3):
        for j in range(3):

            valor = estado[i][j]

            if valor != 0:

                x, y = posiciones[valor]

                distancia += abs(i - x) + abs(j - y)

    return distancia


print("Estado inicial:")

for fila in inicio:
    print(fila)

print()

print("h1 (Fichas mal colocadas):", h1(inicio))
print("h2 (Distancia Manhattan):", h2(inicio))