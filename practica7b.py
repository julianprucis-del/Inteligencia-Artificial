import random
import math
import matplotlib.pyplot as plt

random.seed(42)

# ==========================
# Generar 15 ciudades
# ==========================

ciudades = []

for i in range(15):
    x = random.randint(0,100)
    y = random.randint(0,100)
    ciudades.append((x,y))

# ==========================
# Distancia
# ==========================

def distancia(a,b):

    x1,y1 = ciudades[a]
    x2,y2 = ciudades[b]

    return math.sqrt((x2-x1)**2+(y2-y1)**2)

# ==========================
# Costo de una ruta
# ==========================

def costo(ruta):

    total=0

    for i in range(len(ruta)-1):
        total+=distancia(ruta[i],ruta[i+1])

    total+=distancia(ruta[-1],ruta[0])

    return total

# ==========================
# Crear población
# ==========================

def crear_poblacion(n):

    poblacion=[]

    for i in range(n):

        ruta=list(range(len(ciudades)))

        random.shuffle(ruta)

        poblacion.append(ruta)

    return poblacion

# ==========================
# Torneo
# ==========================

def torneo(poblacion):

    candidatos=random.sample(poblacion,3)

    return min(candidatos,key=costo)

# ==========================
# Cruza OX
# ==========================

def cruza(p1,p2):

    inicio=random.randint(0,len(p1)-2)
    fin=random.randint(inicio+1,len(p1)-1)

    hijo=[-1]*len(p1)

    hijo[inicio:fin]=p1[inicio:fin]

    indice=fin

    for ciudad in p2:

        if ciudad not in hijo:

            if indice>=len(hijo):
                indice=0

            while hijo[indice]!=-1:

                indice+=1

                if indice>=len(hijo):
                    indice=0

            hijo[indice]=ciudad

    return hijo

# ==========================
# Mutación
# ==========================

def mutacion(ruta):

    a=random.randint(0,len(ruta)-2)
    b=random.randint(a+1,len(ruta)-1)

    ruta[a:b]=reversed(ruta[a:b])

# ==========================
# Búsqueda aleatoria
# ==========================

def busqueda_aleatoria():

    mejor=999999

    for i in range(100):

        ruta=list(range(len(ciudades)))

        random.shuffle(ruta)

        c=costo(ruta)

        if c<mejor:
            mejor=c

    return mejor

# ==========================
# Algoritmo Genético
# ==========================

poblacion=crear_poblacion(30)

historial=[]

for g in range(100):

    nueva=[]

    mejor=min(poblacion,key=costo)

    nueva.append(mejor)

    while len(nueva)<30:

        padre1=torneo(poblacion)
        padre2=torneo(poblacion)

        hijo=cruza(padre1,padre2)

        if random.random()<0.2:
            mutacion(hijo)

        nueva.append(hijo)

    poblacion=nueva

    historial.append(costo(min(poblacion,key=costo)))

# ==========================
# Resultado
# ==========================

mejor=min(poblacion,key=costo)

print("Ciudades:\n")

for i,c in enumerate(ciudades):
    print(i,c)

print("\nMejor ruta:")
print(mejor)

print("\nDistancia:")
print(round(costo(mejor),2))

print("\nCosto AG:",round(costo(mejor),2))
print("Costo Aleatorio:",round(busqueda_aleatoria(),2))

# ==========================
# Gráfica de convergencia
# ==========================

plt.figure()

plt.plot(historial)

plt.title("Convergencia")

plt.xlabel("Generación")

plt.ylabel("Distancia")

plt.grid()

# ==========================
# Mejor ruta
# ==========================

plt.figure()

x=[]
y=[]

for ciudad in mejor:

    x.append(ciudades[ciudad][0])
    y.append(ciudades[ciudad][1])

x.append(ciudades[mejor[0]][0])
y.append(ciudades[mejor[0]][1])

plt.plot(x,y,"o-")

plt.title("Mejor Ruta")

plt.grid()

plt.show()