acciones = [
    (2,0),
    (0,2),
    (1,1),
    (1,0),
    (0,1)
]

inicio = (3,3,0)
meta = (0,0,1)


def valido(estado):

    m,c,b = estado

    if m < 0 or m > 3:
        return False

    if c < 0 or c > 3:
        return False

    if m > 0 and c > m:
        return False

    md = 3 - m
    cd = 3 - c

    if md > 0 and cd > md:
        return False

    return True


print("Estado inicial:", inicio)
print("Estado meta:", meta)
print()

print(valido(inicio))
print(valido(meta))
print(valido((2,3,0)))

def sucesores(estado):

    m, c, b = estado

    lista = []

    for dm, dc in acciones:

        if b == 0:
            nuevo = (m - dm, c - dc, 1)
        else:
            nuevo = (m + dm, c + dc, 0)

        if valido(nuevo):
            lista.append(nuevo)

    return lista


print()
print("Sucesores del estado inicial:")

for s in sucesores(inicio):
    print(s)

    from collections import deque

def bfs():

    cola = deque()

    cola.append((inicio, [inicio]))

    visitados = set()

    while cola:

        estado, camino = cola.popleft()

        if estado == meta:
            return camino

        if estado in visitados:
            continue

        visitados.add(estado)

        for s in sucesores(estado):

            if s not in visitados:
                cola.append((s, camino + [s]))

camino = bfs()

print("\nSolución encontrada:\n")

for estado in camino:
    print(estado)

print("\nNúmero de cruces:", len(camino)-1)