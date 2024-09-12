#CÓDIGO QUE NOS DICE EL PROMEDIO DE UN GRUPO DE ALUMNOS, POR MEDIO DE UN ARCHIVO DE TEXTO
def leer_alumnos(archivo):
    alumnos = []
    with open(archivo, 'r') as file:
        for linea in file:
            linea = linea.strip()
            if linea:  # Verifica que la línea no esté vacía
                if ',' in linea:  # Verifica que haya un separador ','
                    nombre, calificacion = linea.split(',')
                    alumnos.append((nombre, int(calificacion)))
                else:
                    print(f"Línea inválida (sin separador ','): {linea}")
            else:
                print("Línea vacía encontrada, omitiendo...")
    return alumnos

def calcular_promedio(alumnos):
    total_calificaciones = sum(calificacion for nombre, calificacion in alumnos)
    promedio = total_calificaciones / len(alumnos)
    return promedio

def alumnos_sin_derecho(alumnos):
    sin_derecho = [nombre for nombre, calificacion in alumnos if calificacion <= 6]
    return sin_derecho

def bubble_sort(alumnos):
    n = len(alumnos)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if alumnos[j][1] > alumnos[j+1][1]:
                alumnos[j], alumnos[j+1] = alumnos[j+1], alumnos[j]

# Archivo de texto
archivo = 'alumnos.txt'

# Leer alumnos y calificaciones
alumnos = leer_alumnos(archivo)

# Ordenar alumnos por calificación en orden ascendente
bubble_sort(alumnos)

# Mostrar los alumnos sin derecho a calificación
sin_derecho = alumnos_sin_derecho(alumnos)
print("Alumnos sin derecho a calificación:", sin_derecho)

# Calcular el promedio del grupo
promedio = calcular_promedio(alumnos)
print(f"Promedio del grupo: {promedio:.2f}")

# Mostrar los nombres y calificaciones en orden ascendente
print("Lista de alumnos y calificaciones en orden ascendente:")
for nombre, calificacion in alumnos:
    print(f"{nombre}: {calificacion}")

##Diego Alejandro Pallares Prieto
