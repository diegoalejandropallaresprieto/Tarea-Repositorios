#CÓDIGO QUE NOS DICE EL PROMEDIO DE UN GRUPO DE ALUMNOS, POR MEDIO DE UN ARCHIVO DE TEXTO
def leer_alumnos(archivo):
    alumnos = []
    try:
        with open(archivo, 'r') as file:
            for linea in file:
                linea = linea.strip()
                if linea:  # Verifica que la línea no esté vacía
                    try:
                        nombre, calificacion = linea.split(',')
                        calificacion = int(calificacion)
                        alumnos.append((nombre, calificacion))
                    except ValueError:
                        print(f"Línea inválida o calificación incorrecta: {linea}")
                else:
                    print("Línea vacía encontrada, omitiendo...")
    except FileNotFoundError:
        print(f"Error: El archivo '{archivo}' no se encontró.")
    except IOError:
        print(f"Error: No se pudo leer el archivo '{archivo}'.")
    
    return alumnos

def calcular_promedio(alumnos):
    if alumnos:
        total_calificaciones = sum(calificacion for _, calificacion in alumnos)
        promedio = total_calificaciones / len(alumnos)
        return promedio
    else:
        return 0

def alumnos_sin_derecho(alumnos):
    return [nombre for nombre, calificacion in alumnos if calificacion <= 6]

# Uso de sorted en lugar de bubble sort
def ordenar_alumnos_por_calificacion(alumnos):
    return sorted(alumnos, key=lambda x: x[1])

# Archivo de texto
archivo = 'alumnos.txt'

# Leer alumnos y calificaciones
alumnos = leer_alumnos(archivo)

if alumnos:
    # Ordenar alumnos por calificación en orden ascendente
    alumnos_ordenados = ordenar_alumnos_por_calificacion(alumnos)

    # Mostrar los alumnos sin derecho a calificación
    sin_derecho = alumnos_sin_derecho(alumnos)
    if sin_derecho:
        print("Alumnos sin derecho a calificación:", ', '.join(sin_derecho))
    else:
        print("Todos los alumnos tienen derecho a calificación.")

    # Calcular el promedio del grupo
    promedio = calcular_promedio(alumnos)
    print(f"Promedio del grupo: {promedio:.2f}")

    # Mostrar los nombres y calificaciones en orden ascendente
    print("Lista de alumnos y calificaciones en orden ascendente:")
    for nombre, calificacion in alumnos_ordenados:
        print(f"{nombre}: {calificacion}")
else:
    print("No se encontraron alumnos en el archivo.")

##Diego Alejandro Pallares Prieto
