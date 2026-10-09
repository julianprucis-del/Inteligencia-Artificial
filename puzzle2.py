import heapq
import time

inicio = (
    (7,2,4),
    (5,0,6),
    (8,3,1)
)

meta = (
    (0,1,2),
    (3,4,5),
    (6,7,8)
)

#---------------- HEURÍSTICAS ----------------#

def h1(estado):
    c = 0
    for i in range(3):
        for j in range(3):
            if estado[i][j] != 0 and estado[i][j] != meta[i][j]:
                c += 1
    return c

def h2(estado):

    posiciones = {}

    for i in range(3):
        for j in range(3):
            posiciones[meta[i][j]] = (i,j)

    distancia = 0

    for i in range(3):
        for j in range(3):

            valor = estado[i][j]

            if valor != 0:

                x,y = posiciones[valor]

                distancia += abs(i-x)+abs(j-y)

    return distancia

#--------------- MOVIMIENTOS ----------------#

def vecinos(estado):

    estado = [list(f) for f in estado]

    for i in range(3):
        for j in range(3):
            if estado[i][j] == 0:
                x,y = i,j

    movimientos = [(-1,0),(1,0),(0,-1),(0,1)]

    lista = []

    for dx,dy in movimientos:

        nx = x + dx
        ny = y + dy

        if 0 <= nx < 3 and 0 <= ny < 3:

            nuevo = [fila[:] for fila in estado]

            nuevo[x][y],nuevo[nx][ny] = nuevo[nx][ny],nuevo[x][y]

            lista.append(tuple(tuple(f) for f in nuevo))

    return lista

#--------------- BUSCADOR ----------------#

def buscar(nombre,heuristica,tipo):

    inicio_t = time.time()

    cola=[]

    heapq.heappush(cola,(heuristica(inicio),0,inicio))

    visitados=set()

    expandidos=0

    while cola:

        f,g,estado = heapq.heappop(cola)

        if estado in visitados:
            continue

        visitados.add(estado)

        expandidos += 1

        if estado == meta:

            print("\n",nombre)
            print("Costo:",g)
            print("Nodos expandidos:",expandidos)
            print("Tiempo:",round(time.time()-inicio_t,4),"seg")
            return

        for v in vecinos(estado):

            if v not in visitados:

                nuevo_g = g + 1

                if tipo=="ucs":
                    nuevo_f = nuevo_g

                elif tipo=="voraz":
                    nuevo_f = heuristica(v)

                else:
                    nuevo_f = nuevo_g + heuristica(v)

                heapq.heappush(cola,(nuevo_f,nuevo_g,v))

#---------------- EJECUCIÓN ----------------#

buscar("Costo Uniforme",lambda x:0,"ucs")

buscar("Voraz h2",h2,"voraz")

buscar("A* h1",h1,"astar")

buscar("A* h2",h2,"astar")