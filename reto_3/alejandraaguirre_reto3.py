# -*- coding: utf-8 -*-
"""AlejandraAguirre_Reto3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1uDqQkQmFKcSgN1wPUd7283z1vIBuE2CW
"""

# Crear una lista de cultivos con información predefinida
cultivos = [
    {
        "Nombre": "Tomate",
        "Mantenimiento": "Lunes, Jueves 4:00 pm",
        "Regado": "Martes, Viernes 5:00 pm",
        "Abono": "Miércoles 6:00 pm",
    },
    {
        "Nombre": "Zanahoria",
        "Mantenimiento": "Martes, Viernes 3:00 pm",
        "Regado": "Lunes, Jueves 4:30 pm",
        "Abono": "Miércoles 5:30 pm",
    },
    {
        "Nombre": "Lechuga",
        "Mantenimiento": "Miércoles 4:30 pm",
        "Regado": "Martes, Viernes 4:00 pm",
        "Abono": "Jueves 6:00 pm",
    },
]

# Variables para la información contable
mano_de_obra = 0
abono = 0
agua = 0
mantenimiento = 0
valor_arroba = 0
kilos_recolectados = 0

# Función para calcular los costos totales
def calcular_costos_totales():
    return mano_de_obra + abono + agua + mantenimiento

# Función para calcular la ganancia
def calcular_ganancia(precio_kilo):
    ingresos = kilos_recolectados * precio_kilo
    costos_totales = calcular_costos_totales()
    ganancia = ingresos - costos_totales
    return ganancia

# Función para mostrar el menú principal
def mostrar_menu_principal():
    print("\nMenú de Gestión de Cultivos:")
    print("1. Horario de Gestión de Cultivo")
    print("2. Etapas del Cultivo")
    print("3. Información Contable")
    print("4. Salir")

# Función para mostrar el menú de costos
def mostrar_menu_costos():
    print("\nSubmenú de Costos:")
    print("1. Mano de obra")
    print("2. Agua")
    print("3. Mantenimiento")
    print("4. Abono")
    print("5. Ir atrás")

# Función para mostrar el menú de producción
def mostrar_menu_produccion():
    print("\nSubmenú de Producción:")
    print("A. Valor en mercado del cultivo")
    print("B. Cantidad recogida")
    print("C. Ir atrás")

# Ciclo infinito para mantener la aplicación en ejecución
while True:
    mostrar_menu_principal()
    opcion = input("Seleccione una opción (1/2/3/4): ")

    if opcion == "1":
        print("\nLista de cultivos:")
        for i, cultivo in enumerate(cultivos, 1):
            print(f"{i}. {cultivo['Nombre']}")

        seleccion = int(input("Seleccione un cultivo (1/2/3): "))
        if 1 <= seleccion <= len(cultivos):
            cultivo_seleccionado = cultivos[seleccion - 1]
            print(f"\nNombre del cultivo: {cultivo_seleccionado['Nombre']}")
            print(f"Días y Horario de Mantenimiento: {cultivo_seleccionado['Mantenimiento']}")
            print(f"Días y Horario de Regado: {cultivo_seleccionado['Regado']}")
            print(f"Días y Horario de Abono: {cultivo_seleccionado['Abono']}")
        else:
            print("Opción inválida.")

    elif opcion == "2":
        print("\nEtapas del Cultivo:")
        for i, etapa in enumerate(["Siembra", "Crecimiento", "Cosecha"], 1):
            print(f"{i}. {etapa}")

        seleccion_etapa = int(input("Seleccione una etapa (1/2/3): "))
        if 1 <= seleccion_etapa <= 3:
            etapa_de_cultivo = ["Siembra", "Crecimiento", "Cosecha"][seleccion_etapa - 1]
            print(f"Etapa de cultivo seleccionada: {etapa_de_cultivo}")
        else:
            print("Opción inválida.")

    elif opcion == "3":
        while True:
            print("\nMenú de Información Contable:")
            print("A. Costos")
            print("B. Producción")
            print("C. Mostrar Informe Económico")
            print("D. Ir atrás")

            opcion_contable = input("Seleccione una opción (A/B/C/D): ")

            if opcion_contable == "A":
                mostrar_menu_costos()
                opcion_costo = input("Seleccione un costo (1/2/3/4/5): ")
                if opcion_costo == "1":
                    mano_de_obra = float(input("Ingrese el valor de la mano de obra: "))
                elif opcion_costo == "2":
                    agua = float(input("Ingrese el valor del agua: "))
                elif opcion_costo == "3":
                    mantenimiento = float(input("Ingrese el valor del mantenimiento: "))
                elif opcion_costo == "4":
                    abono = float(input("Ingrese el valor del abono: "))
                elif opcion_costo == "5":
                    break
                else:
                    print("Opción inválida.")
            elif opcion_contable == "B":
                mostrar_menu_produccion()
                opcion_produccion = input("Seleccione una opción (A/B/C): ")
                if opcion_produccion == "A":
                    valor_arroba = float(input("Ingrese el valor de la arroba de arroz: "))
                elif opcion_produccion == "B":
                    kilos_recolectados = float(input("Ingrese la cantidad de kilos recolectados: "))
                elif opcion_produccion == "C":
                    break
                else:
                    print("Opción inválida.")
            elif opcion_contable == "C":
                costos_totales = calcular_costos_totales()
                promedio_costos = costos_totales / 4

                precio_kilo_incrementado = valor_arroba * 12.5 * 1.37
                ganancia_incremento_precio = calcular_ganancia(precio_kilo_incrementado)

                costos_disminuidos = costos_totales * 0.95
                produccion_disminuida = kilos_recolectados * 0.63
                ganancia_disminucion_costos = calcular_ganancia(valor_arroba * 12.5)

                print("\nInforme Económico:")
                print(f"Costos Totales: {costos_totales}")
                print(f"Valor Promedio de Costos Fijos: {promedio_costos}")
                print(f"¿Hubo Ganancia? {'SI' if ganancia_disminucion_costos > 0 else 'NO'}")
                print(f"Ganancia (Cultivo Actual): {ganancia_disminucion_costos}")
                print(f"Ganancia (Precio Kilo Incrementado): {ganancia_incremento_precio}")
                print(f"Ganancia (Costos y Producción Disminuidos): {calcular_ganancia(valor_arroba * 12.5)}")
            elif opcion_contable == "D":
                break
            else:
                print("Opción inválida.")
    elif opcion == "4":
        print("Saliendo de la aplicación.")
        break
    else:
        print("Opción inválida.")

# Crear una lista de cultivos con información predefinida
cultivos = [
    {
        "Nombre": "Tomate",
        "Mantenimiento": "Lunes, Jueves 4:00 pm",
        "Regado": "Martes, Viernes 5:00 pm",
        "Abono": "Miércoles 6:00 pm",
    },
    {
        "Nombre": "Zanahoria",
        "Mantenimiento": "Martes, Viernes 3:00 pm",
        "Regado": "Lunes, Jueves 4:30 pm",
        "Abono": "Miércoles 5:30 pm",
    },
    {
        "Nombre": "Lechuga",
        "Mantenimiento": "Miércoles 4:30 pm",
        "Regado": "Martes, Viernes 4:00 pm",
        "Abono": "Jueves 6:00 pm",
    },
]

# Variables para la información contable
mano_de_obra = 0
abono = 0
agua = 0
mantenimiento = 0
valor_arroba = 0
kilos_recolectados = 0

# Función para calcular los costos totales
def calcular_costos_totales():
    return mano_de_obra + abono + agua + mantenimiento

# Función para calcular la ganancia
def calcular_ganancia(precio_kilo):
    ingresos = kilos_recolectados * precio_kilo
    costos_totales = calcular_costos_totales()
    ganancia = ingresos - costos_totales
    return ganancia

# Función para mostrar el menú principal
def mostrar_menu_principal():
    print("\nMenú de Gestión de Cultivos:")
    print("1. Horario de Gestión de Cultivo")
    print("2. Etapas del Cultivo")
    print("3. Información Contable")
    print("4. Salir")

# Función para mostrar el menú de costos
def mostrar_menu_costos():
    print("\nSubmenú de Costos:")
    print("1. Mano de obra")
    print("2. Agua")
    print("3. Mantenimiento")
    print("4. Abono")
    print("5. Ir atrás")

# Función para mostrar el menú de producción
def mostrar_menu_produccion():
    print("\nSubmenú de Producción:")
    print("A. Valor en mercado del cultivo")
    print("B. Cantidad recogida")
    print("C. Ir atrás")

# Mensaje de bienvenida
print("Bienvenido a la aplicación de gestión de cultivos y contabilidad.")

# Ciclo infinito para mantener la aplicación en ejecución
while True:
    mostrar_menu_principal()
    opcion = input("Seleccione una opción (1/2/3/4): ")

    if opcion == "1":
        print("\nLista de cultivos:")
        for i, cultivo in enumerate(cultivos, 1):
            print(f"{i}. {cultivo['Nombre']}")

        seleccion = int(input("Seleccione un cultivo (1/2/3): "))
        if 1 <= seleccion <= len(cultivos):
            cultivo_seleccionado = cultivos[seleccion - 1]
            print(f"\nNombre del cultivo: {cultivo_seleccionado['Nombre']}")
            print(f"Días y Horario de Mantenimiento: {cultivo_seleccionado['Mantenimiento']}")
            print(f"Días y Horario de Regado: {cultivo_seleccionado['Regado']}")
            print(f"Días y Horario de Abono: {cultivo_seleccionado['Abono']}")
        else:
            print("Opción inválida.")

    elif opcion == "2":
        print("\nEtapas del Cultivo:")
        for i, etapa in enumerate(["Siembra", "Crecimiento", "Cosecha"], 1):
            print(f"{i}. {etapa}")

        seleccion_etapa = int(input("Seleccione una etapa (1/2/3): "))
        if 1 <= seleccion_etapa <= 3:
            etapa_de_cultivo = ["Siembra", "Crecimiento", "Cosecha"][seleccion_etapa - 1]
            print(f"Etapa de cultivo seleccionada: {etapa_de_cultivo}")
        else:
            print("Opción inválida.")

    elif opcion == "3":
        while True:
            print("\nMenú de Información Contable:")
            print("A. Costos")
            print("B. Producción")
            print("C. Mostrar Informe Económico")
            print("D. Ir atrás")

            opcion_contable = input("Seleccione una opción (A/B/C/D): ")

            if opcion_contable == "A":
                mostrar_menu_costos()
                opcion_costo = input("Seleccione un costo (1/2/3/4/5): ")
                if opcion_costo == "1":
                    mano_de_obra = float(input("Ingrese el valor de la mano de obra: "))
                elif opcion_costo == "2":
                    agua = float(input("Ingrese el valor del agua: "))
                elif opcion_costo == "3":
                    mantenimiento = float(input("Ingrese el valor del mantenimiento: "))
                elif opcion_costo == "4":
                    abono = float(input("Ingrese el valor del abono: "))
                elif opcion_costo == "5":
                    break
                else:
                    print("Opción inválida.")
            elif opcion_contable == "B":
                mostrar_menu_produccion()
                opcion_produccion = input("Seleccione una opción (A/B/C): ")
                if opcion_produccion == "A":
                    valor_arroba = float(input("Ingrese el valor de la arroba de arroz: "))
                elif opcion_produccion == "B":
                    kilos_recolectados = float(input("Ingrese la cantidad de kilos recolectados: "))
                elif opcion_produccion == "C":
                    break
                else:
                    print("Opción inválida.")
            elif opcion_contable == "C":
                costos_totales = calcular_costos_totales()
                promedio_costos = costos_totales / 4

                precio_kilo_incrementado = valor_arroba * 12.5 * 1.37
                ganancia_incremento_precio = calcular_ganancia(precio_kilo_incrementado)

                costos_disminuidos = costos_totales * 0.95
                produccion_disminuida = kilos_recolectados * 0.63
                ganancia_disminucion_costos = calcular_ganancia(valor_arroba * 12.5)

                print("\nInforme Económico:")
                print(f"Costos Totales: {costos_totales}")
                print(f"Valor Promedio de Costos Fijos: {promedio_costos}")
                print(f"¿Hubo Ganancia? {'SI' if ganancia_disminucion_costos > 0 else 'NO'}")
                print(f"Ganancia (Cultivo Actual): {ganancia_disminucion_costos}")
                print(f"Ganancia (Precio Kilo Incrementado): {ganancia_incremento_precio}")
                print(f"Ganancia (Costos y Producción Disminuidos): {calcular_ganancia(valor_arroba * 12.5)}")
            elif opcion_contable == "D":
                break
            else:
                print("Opción inválida.")
    elif opcion == "4":
        print("Gracias por usar la aplicación. ¡Hasta luego!")
        break
    else:
        print("Opción inválida.")