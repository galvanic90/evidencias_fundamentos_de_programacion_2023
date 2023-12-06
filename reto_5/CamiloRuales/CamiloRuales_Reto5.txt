import statistics
# Diccionario para almacenar los datos de los estudiantes
estudiantes = {}

# Función para agregar un estudiante
def agregar_estudiante():
    identificacion = input("Ingrese la identificación del estudiante: ")
    nombre = input("Ingrese el nombre del estudiante: ")
    correo = input("Ingrese el correo del estudiante: ")
    telefono = input("Ingrese el teléfono del estudiante: ")
    fecha_nacimiento = input("Ingrese la fecha de nacimiento del estudiante: ")
    nota1 = float(input("Ingrese la nota 1 del estudiante: "))
    nota2 = float(input("Ingrese la nota 2 del estudiante: "))
    nota3 = float(input("Ingrese la nota 3 del estudiante: "))
    nota4 = float(input("Ingrese la nota 4 del estudiante: "))
    
    estudiantes[identificacion] = {
        'Nombre': nombre,
        'Correo': correo,
        'Teléfono': telefono,
        'Fecha de nacimiento': fecha_nacimiento,
        'Nota 1': nota1,
        'Nota 2': nota2,
        'Nota 3': nota3,
        'Nota 4': nota4
    }
    print(f"Estudiante con identificación {identificacion} agregado exitosamente.")

# Función para buscar un estudiante por identificación
def buscar_estudiante():
    identificacion = input("Ingrese la identificación del estudiante a buscar: ")
    if identificacion in estudiantes:
        print("Información del estudiante:")
        for key, value in estudiantes[identificacion].items():
            print(f"{key}: {value}")
    else:
        print(f"No se encontró un estudiante con identificación {identificacion}.")

# Función para modificar las notas de un estudiante
def modificar_estudiante():
    identificacion = input("Ingrese la identificación del estudiante a modificar: ")
    if identificacion in estudiantes:
        print("Información actual del estudiante:")
        for key, value in estudiantes[identificacion].items():
            print(f"{key}: {value}")
        
        nota1 = float(input("Ingrese la nueva nota 1 del estudiante: "))
        nota2 = float(input("Ingrese la nueva nota 2 del estudiante: "))
        nota3 = float(input("Ingrese la nueva nota 3 del estudiante: "))
        nota4 = float(input("Ingrese la nueva nota 4 del estudiante: "))
        
        estudiantes[identificacion]['Nota 1'] = nota1
        estudiantes[identificacion]['Nota 2'] = nota2
        estudiantes[identificacion]['Nota 3'] = nota3
        estudiantes[identificacion]['Nota 4'] = nota4
        
        print(f"Notas del estudiante con identificación {identificacion} modificadas exitosamente.")
    else:
        print(f"No se encontró un estudiante con identificación {identificacion}.")

# Función para eliminar un estudiante
def eliminar_estudiante():
    identificacion = input("Ingrese la identificación del estudiante a eliminar: ")
    if identificacion in estudiantes:
        confirmacion = input(f"¿Está seguro de eliminar al estudiante {estudiantes[identificacion]['Nombre']}? (S/N): ")
        if confirmacion.lower() == 's':
            del estudiantes[identificacion]
            print(f"Estudiante con identificación {identificacion} eliminado exitosamente.")
    else:
        print(f"No se encontró un estudiante con identificación {identificacion}.")

# Función para calcular y mostrar resultados por estudiante
def resultados_estudiante():
    identificacion = input("Ingrese la identificación del estudiante para calcular resultados: ")
    if identificacion in estudiantes:
        estudiante = estudiantes[identificacion]
        nota_final = (estudiante['Nota 1'] + estudiante['Nota 2'] + estudiante['Nota 3'] + estudiante['Nota 4']) / 4
        nota_promedio_grupo = sum(estudiante['Nota 1'] + estudiante['Nota 2'] + estudiante['Nota 3'] + estudiante['Nota 4'] for estudiante in estudiantes.values()) / len(estudiantes)
        
        print(f"Nota final del estudiante: {nota_final}")
        print(f"Nota promedio del grupo: {nota_promedio_grupo}")
        
        if nota_final > nota_promedio_grupo:
            print("El estudiante está por encima del promedio del grupo.")
        elif nota_final < nota_promedio_grupo:
            print("El estudiante está por debajo del promedio del grupo.")
        else:
            print("El estudiante tiene la misma nota promedio que el grupo.")
        
        if nota_final >= 3.0:
            print("El estudiante ganó el curso.")
        else:
            print("El estudiante perdió el curso.")
        
        # Aquí puedes calcular el percentil y mostrarlo
        # Por ejemplo, puedes comparar la nota_final con las notas de todos los estudiantes
        
    else:
        print(f"No se encontró un estudiante con identificación {identificacion}.")

# Función para mostrar el informe de grupo
def informe_grupo():
    if not estudiantes:
        print("No hay estudiantes registrados.")
        return

    # Inicializar listas para almacenar notas finales y estados de ganadores/perdedores
    notas_finales = []
    ganadores = []
    perdedores = []

    # Calcular estadísticas para cada estudiante y recopilar información
    for identificacion, estudiante in estudiantes.items():
        nota_final = (estudiante["Nota 1"] + estudiante["Nota 2"] + estudiante["Nota 3"] + estudiante["Nota 4"]) / 4
        notas_finales.append(nota_final)

        # Determinar si el estudiante ganó o perdió (valor de corte: 3.0)
        if nota_final >= 3.0:
            ganadores.append(identificacion)
        else:
            perdedores.append(identificacion)

    # Calcular estadísticas generales
    nota_promedio = sum(notas_finales) / len(notas_finales)
    numero_estudiantes_por_encima = sum(1 for nota_final in notas_finales if nota_final > nota_promedio)
    numero_estudiantes_por_debajo = sum(1 for nota_final in notas_finales if nota_final < nota_promedio)
    numero_estudiantes_iguales = len(notas_finales) - numero_estudiantes_por_encima - numero_estudiantes_por_debajo

    # Calcular el porcentaje de ganadores y perdedores
    porcentaje_ganadores = (len(ganadores) / len(estudiantes)) * 100
    porcentaje_perdedores = (len(perdedores) / len(estudiantes)) * 100

    # Calcular la moda, mediana y desviación estándar de las notas finales
    moda = statistics.mode(notas_finales)
    mediana = statistics.median(notas_finales)
    desviacion_estandar = statistics.stdev(notas_finales)

    # Imprimir el informe
    print("\nInforme de Grupo:")
    print(f"Nota Promedio: {nota_promedio}")
    print(f"Número de estudiantes por encima del promedio: {numero_estudiantes_por_encima}")
    print(f"Número de estudiantes por debajo del promedio: {numero_estudiantes_por_debajo}")
    print(f"Número de estudiantes iguales al promedio: {numero_estudiantes_iguales}")
    print(f"Número de estudiantes ganadores (notas >= 3.0): {len(ganadores)}")
    print(f"Número de estudiantes perdedores (notas < 3.0): {len(perdedores)}")
    print(f"Porcentaje de ganadores: {porcentaje_ganadores}%")
    print(f"Porcentaje de perdedores: {porcentaje_perdedores}%")
    print(f"Moda de las notas finales: {moda}")
    print(f"Mediana de las notas finales: {mediana}")
    print(f"Desviación Estándar de las notas finales: {desviacion_estandar}")


# Función principal que muestra el menú
def menu_principal():
    while True:
        print("\nMenú Principal:")
        print("1. Agregar Estudiante")
        print("2. Buscar Estudiante")
        print("3. Modificar Notas del Estudiante")
        print("4. Eliminar Estudiante")
        print("5. Resultados por Estudiante")
        print("6. Informe de Grupo")
        print("7. Salir")
        
        opcion = input("Ingrese el número de la opción deseada: ")
        
        if opcion == '1':
            agregar_estudiante()
        elif opcion == '2':
            buscar_estudiante()
        elif opcion == '3':
            modificar_estudiante()
        elif opcion == '4':
            eliminar_estudiante()
        elif opcion == '5':
            resultados_estudiante()
        elif opcion == '6':
            informe_grupo()
        elif opcion == '7':
            print("Saliendo de la aplicación.")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

# Iniciar la aplicación
menu_principal()
