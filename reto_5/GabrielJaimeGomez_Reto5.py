# -*- coding: utf-8 -*-
"""Untitled18.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1EBTT6tj7UNwiCw6BQ0ijwxav8GbdBuwt
"""

import statistics

# Estructura de datos para almacenar estudiantes
estudiantes = {}

# Función para agregar un estudiante
def agregar_estudiante():
    identificacion = input("Identificación: ")
    nombre = input("Nombre: ")
    correo = input("Correo: ")
    telefono = input("Teléfono: ")
    fecha_nacimiento = input("Fecha de nacimiento: ")
    nota1 = float(input("Nota 1: "))
    nota2 = float(input("Nota 2: "))
    nota3 = float(input("Nota 3: "))
    nota4 = float(input("Nota 4: "))

    estudiante = {
        "Identificación": identificacion,
        "Nombre": nombre,
        "Correo": correo,
        "Teléfono": telefono,
        "Fecha de nacimiento": fecha_nacimiento,
        "Nota 1": nota1,
        "Nota 2": nota2,
        "Nota 3": nota3,
        "Nota 4": nota4
    }

    estudiantes[identificacion] = estudiante
    print("Estudiante agregado exitosamente.")

# Función para buscar un estudiante por identificación
def buscar_estudiante():
    identificacion_buscar = input("Ingrese la identificación del estudiante a buscar: ")
    if identificacion_buscar in estudiantes:
        estudiante = estudiantes[identificacion_buscar]
        print("Información del estudiante:")
        for clave, valor in estudiante.items():
            print(clave + ":", valor)
    else:
        print("El estudiante no se encuentra en la base de datos.")

# Función para modificar las notas de un estudiante
def modificar_notas_estudiante():
    identificacion_buscar = input("Ingrese la identificación del estudiante a modificar: ")
    if identificacion_buscar in estudiantes:
        estudiante = estudiantes[identificacion_buscar]
        print("Estudiante encontrado. Ingrese las nuevas notas:")
        estudiante["Nota 1"] = float(input("Nueva Nota 1: "))
        estudiante["Nota 2"] = float(input("Nueva Nota 2: "))
        estudiante["Nota 3"] = float(input("Nueva Nota 3: "))
        estudiante["Nota 4"] = float(input("Nueva Nota 4: "))
        print("Notas modificadas exitosamente.")
    else:
        print("El estudiante no se encuentra en la base de datos.")

# Función para cancelar un estudiante
def cancelar_estudiante():
    identificacion_buscar = input("Ingrese la identificación del estudiante a eliminar: ")
    if identificacion_buscar in estudiantes:
        del estudiantes[identificacion_buscar]
        print("Estudiante eliminado exitosamente.")
    else:
        print("El estudiante no se encuentra en la base de datos.")

# Función para calcular y mostrar resultados por estudiante
def resultados_por_estudiante():
    identificacion_buscar = input("Ingrese la identificación del estudiante para ver los resultados: ")
    if identificacion_buscar in estudiantes:
        estudiante = estudiantes[identificacion_buscar]
        notas = [estudiante["Nota 1"], estudiante["Nota 2"], estudiante["Nota 3"], estudiante["Nota 4"]]
        nota_final = sum(notas) / len(notas)
        nota_promedio_grupo = sum([estudiantes[ident]["Nota 1"] for ident in estudiantes]) / len(estudiantes)
        por_encima_promedio = nota_final > nota_promedio_grupo
        estado_curso = "Aprobado" if nota_final >= 60 else "Reprobado"

        notas_ordenadas = sorted([estudiantes[ident]["Nota 1"] for ident in estudiantes])
        percentil = notas_ordenadas.index(estudiante["Nota 1"]) / len(estudiantes) * 100

        print("Nota Final del Estudiante:", nota_final)
        print("Nota Promedio del Grupo:", nota_promedio_grupo)
        print("Estudiante por encima del promedio del grupo:", por_encima_promedio)
        print("Estado del Curso del Estudiante:", estado_curso)
        print("Percentil del Estudiante:", percentil)
    else:
        print("El estudiante no se encuentra en la base de datos.")



# Menú principal
while True:
    print("\nMenú Principal")
    print("1. Agregar Estudiante")
    print("2. Buscar Estudiante")
    print("3. Modificar Notas de Estudiante")
    print("4. Cancelar Estudiante")
    print("5. Resultados por Estudiante")
    print("6. Salir")
    opcion = input("Elija una opción (1/2/3/4/5/6): ")
    if opcion == "1":
        agregar_estudiante()
    elif opcion == "2":
        buscar_estudiante()
    elif opcion == "3":
        modificar_notas_estudiante()
    elif opcion == "4":
        cancelar_estudiante()
    elif opcion == "5":
        resultados_por_estudiante()
    elif opcion == "6":
        break
    else:
        print("Opción no válida. Por favor, elija una opción válida.")