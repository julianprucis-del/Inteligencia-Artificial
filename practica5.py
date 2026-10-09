grafo = {
    "Morelia":{
        "Toluca":245,
        "Querétaro":195
    },

    "Toluca":{
        "Morelia":245,
        "Querétaro":190,
        "CDMX":66,
        "Cuernavaca":110
    },

    "Querétaro":{
        "Morelia":195,
        "Toluca":190,
        "CDMX":213,
        "Pachuca":240
    },

    "CDMX":{
        "Toluca":66,
        "Querétaro":213,
        "Cuernavaca":89,
        "Pachuca":95,
        "Puebla":130
    },

    "Cuernavaca":{
        "Toluca":110,
        "CDMX":89,
        "Puebla":160
    },

    "Pachuca":{
        "Querétaro":240,
        "CDMX":95,
        "Tlaxcala":150
    },

    "Tlaxcala":{
        "Pachuca":150,
        "Puebla":35
    },

    "Puebla":{
        "CDMX":130,
        "Tlaxcala":35,
        "Cuernavaca":160
    }
}

heuristica = {
    "Morelia":330,
    "Toluca":150,
    "Querétaro":250,
    "CDMX":100,
    "Pachuca":110,
    "Cuernavaca":100,
    "Tlaxcala":30,
    "Puebla":0
}
#HEURÍSTICA CONSISTENTE Y ADMISIBLE
print("Verificación de la heurística\n")

consistente = True

for ciudad in grafo:

    for vecino in grafo[ciudad]:

        costo = grafo[ciudad][vecino]

        if heuristica[ciudad] <= costo + heuristica[vecino]:
            print(ciudad, "->", vecino, "✅ Cumple")
        else:
            print(ciudad, "->", vecino, "❌ No cumple")
            consistente = False

print()


if consistente:
    print("La heurística ES consistente.")
    print("La heurística ES admisible.")
else:
    print("La heurística NO es consistente.")
    print("La heurística NO es admisible.")

#Voraz
import heapq

inicio = "Morelia"
meta = "Puebla"

cola = []
heapq.heappush(cola, (heuristica[inicio], inicio))

visitados = []

while cola:

    h, ciudad = heapq.heappop(cola)

    if ciudad not in visitados:

        print("Visitando:", ciudad, "- h =", h)

        visitados.append(ciudad)

        if ciudad == meta:
            print("¡Llegué a Puebla!")
            break

        for vecino in sorted(grafo[ciudad]):

            if vecino not in visitados:

                heapq.heappush(cola, (heuristica[vecino], vecino))



#A* 
import heapq

inicio = "Morelia"
meta = "Puebla"

cola = []
heapq.heappush(cola, (heuristica[inicio], 0, inicio))

visitados = []

while cola:

    f, g, ciudad = heapq.heappop(cola)

    if ciudad not in visitados:

        print("Visitando:", ciudad,
              "- g =", g,
              "- h =", heuristica[ciudad],
              "- f =", f)

        visitados.append(ciudad)

        if ciudad == meta:
            print("¡Llegué a Puebla!")
            print("Costo total:", g, "km")
            break

        for vecino in sorted(grafo[ciudad]):

            if vecino not in visitados:

                nuevo_g = g + grafo[ciudad][vecino]
                nuevo_f = nuevo_g + heuristica[vecino]

                heapq.heappush(cola, (nuevo_f, nuevo_g, vecino))