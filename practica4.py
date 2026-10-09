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

from collections import deque
import heapq

inicio = "Morelia"
meta = "Puebla"

cola = []
heapq.heappush(cola, (0, inicio))

visitados = []

while cola:

    costo, ciudad = heapq.heappop(cola)

    if ciudad not in visitados:

        print("Visitando:", ciudad, "- Costo:", costo, "km")

        visitados.append(ciudad)

        if ciudad == meta:
            print("¡Llegué a Puebla!")
            print("Costo total:", costo, "km")
            break

        for vecino in sorted(grafo[ciudad]):

            if vecino not in visitados:

                nuevo_costo = costo + grafo[ciudad][vecino]

                heapq.heappush(cola, (nuevo_costo, vecino))