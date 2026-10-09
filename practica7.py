variables = [
    "CDMX",
    "Edomex",
    "Morelos",
    "Puebla",
    "Tlaxcala",
    "Hidalgo",
    "Querétaro",
    "Guerrero",
    "Michoacán"
]

# Prueba con 4 colores
dominios = ["Rojo", "Verde", "Azul", "Amarillo"]

restricciones = [
    ("CDMX", "Edomex"),
    ("CDMX", "Morelos"),
    ("CDMX", "Puebla"),

    ("Edomex", "Querétaro"),
    ("Edomex", "Hidalgo"),
    ("Edomex", "Puebla"),
    ("Edomex", "Morelos"),
    ("Edomex", "Guerrero"),
    ("Edomex", "Michoacán"),

    ("Morelos", "Guerrero"),
    ("Morelos", "Puebla"),

    ("Puebla", "Tlaxcala"),

    ("Hidalgo", "Querétaro"),

    ("Guerrero", "Michoacán")
]


def es_valido(region, color, asignacion):

    for r1, r2 in restricciones:

        if r1 == region:
            if r2 in asignacion and asignacion[r2] == color:
                return False

        elif r2 == region:
            if r1 in asignacion and asignacion[r1] == color:
                return False

    return True


# ========= MRV + Grado =========

def seleccionar_variable(asignacion):

    mejor = None
    menor = 100
    mayor_grado = -1

    for region in variables:

        if region not in asignacion:

            disponibles = 0

            for color in dominios:
                if es_valido(region, color, asignacion):
                    disponibles += 1

            grado = 0

            for r1, r2 in restricciones:

                if r1 == region or r2 == region:
                    grado += 1

            if disponibles < menor:

                menor = disponibles
                mayor_grado = grado
                mejor = region

            elif disponibles == menor:

                if grado > mayor_grado:

                    mayor_grado = grado
                    mejor = region

    return mejor


# ========= LCV =========

def ordenar_colores(region, asignacion):

    lista = []

    for color in dominios:

        conflictos = 0

        for r1, r2 in restricciones:

            if r1 == region:
                vecino = r2
            elif r2 == region:
                vecino = r1
            else:
                continue

            if vecino not in asignacion:

                for c in dominios:

                    if c != color and es_valido(vecino, c, asignacion):
                        conflictos += 1

        lista.append((conflictos, color))

    lista.sort()

    colores = []

    for _, color in lista:
        colores.append(color)

    return colores


# ========= Forward Checking =========

def forward_checking(asignacion):

    for region in variables:

        if region not in asignacion:

            puede = False

            for color in dominios:

                if es_valido(region, color, asignacion):
                    puede = True
                    break

            if not puede:
                return False

    return True


# ========= Backtracking =========

def backtracking(asignacion):

    if len(asignacion) == len(variables):
        return asignacion

    region = seleccionar_variable(asignacion)

    for color in ordenar_colores(region, asignacion):

        if es_valido(region, color, asignacion):

            asignacion[region] = color

            if forward_checking(asignacion):

                resultado = backtracking(asignacion)

                if resultado is not None:
                    return resultado

            del asignacion[region]

    return None


print("Variables:")
print(variables)

print("\nDominios:")
print(dominios)

print("\nRestricciones:")
for r in restricciones:
    print(r)

solucion = backtracking({})

print("\nColoreo encontrado:\n")

if solucion:

    for estado in variables:
        print(estado, "->", solucion[estado])

else:
    print("No existe solución.")