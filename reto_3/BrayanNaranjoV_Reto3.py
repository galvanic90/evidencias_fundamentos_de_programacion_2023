# -*- coding: utf-8 -*-
"""
Created on Mon Sep  4 22:41:20 2023

@author: Brahi
"""

#Lista de los cultivos con los datos iniciales ya establecidos

cultivos = [
    {
        "Nombre": "Maíz",
        "Mantenimiento": "Lunes, Jueves 3:00 pm",
        "Regado": "Martes, Viernes 7:00 pm",
        "Abono": "Miércoles 5:00 am",
        "Etapas": [
            {"Etapa": "Germinación", "Intervalo": "9 a 13 días"},
            {"Etapa": "Crecimiento", "Intervalo": "18 a 30 días"},
        ],
    },
    {
        "Nombre": "Tomate",
        "Mantenimiento": "Lunes, Jueves 3:00 pm",
        "Regado": "Martes, Viernes 6:00 am",
        "Abono": "Miércoles, Sábado 6:00 am",
        "Etapas": [
            {"Etapa": "Fase Vegetativa", "Intervalo": "9-15 días"},
            {"Etapa": "Floración", "Intervalo": "16-25 días"},
            {"Etapa": "Fructificación", "Intervalo": "23-28 días"},
        ]
    },
    {
        "Nombre": "Lechuga",
        "Mantenimiento": "Lunes, Miércoles 5:00 pm",
        "Regado": "Martes, Jueves 7:00 am",
        "Abono": "Sábado 7:00 am",
        "Etapas": [
            {"Etapa": "Germinación", "Intervalo": "8-14 días"},
            {"Etapa": "Crecimiento", "Intervalo": "10-30 días"},
            {"Etapa": "Cosecha", "Intervalo": "19-35 días"},
        ]
    },
    {
        "Nombre": "Arroz",
        "Mantenimiento": "Lunes, Jueves 3:00 pm",
        "Regado": "Martes, Viernes 6:00 am",
        "Abono": "Miércoles, Sábado 7:00 am",
        "Etapas": [
            {"Etapa": "Fase Vegetativa", "Intervalo": "55-60 días"},
            {"Etapa": "Floración", "Intervalo": "30-40 días"},
            {"Etapa": "Fructificación", "Intervalo": "60-70 días"},
        ]
    },
]

# Función para mostrar el menú y recibir la opción del usuario

def mostrar_menu():
    print("Bienvenido a agri-automático.")
    print("Menú de Gestión de Cultivos:")
    print("1. Horario de Gestión de Cultivo")
    print("2. Etapas del Cultivo")
    print("3. Información Contable")
    print("4. Salir")

    opcion = input("Ingrese el número de la tarea que necesita del Menú de Gestión de cultivos: ")
    return opcion

# Función para mostrar los horarios de un cultivo
def mostrar_horarios(cultivo):
    print(f"Horarios de {cultivo['Nombre']}:")
    print(f"Mantenimiento: {cultivo['Mantenimiento']}")
    print(f"Regado: {cultivo['Regado']}")
    print(f"Abono: {cultivo['Abono']}")

# Función para mostrar las etapas de un cultivo
def mostrar_etapas(cultivo):
    print(f"Etapas de {cultivo['Nombre']}:")
    for etapa in cultivo['Etapas']:
        print(f"{etapa['Etapa']} - Intervalo: {etapa['Intervalo']}")

# Función para calcular la información contable
def calcular_informacion_contable():
    # Solicitar los gastos y costos
    gastos_mensuales = []
    costos_mensuales = []

    for mes in range(1, 6):  
        print(f"Mes {mes}")
        gasto_medicamentos = float(input("Gasto en Medicamentos: "))
        gasto_imprevistos = float(input("Gasto en Imprevistos: "))
        gastos_mensuales.append(gasto_medicamentos + gasto_imprevistos)

        costo_mano_de_obra = float(input("Costo de Mano de Obra: "))
        costo_abono = float(input("Costo de Abono: "))
        costo_agua = float(input("Costo de Agua: "))
        costo_mantenimiento = float(input("Costo de Mantenimiento: "))
        costos_mensuales.append(
            costo_mano_de_obra + costo_abono + costo_agua + costo_mantenimiento
        )

    valor_arroba_arroz = float(input("Valor de la arroba (12.5 kilos) de arroz: "))
    cantidad_kilos_recolectados = float(input("Cantidad de kilos recolectados: "))

    # Cálculos
    costos_totales_mensuales = [g + c for g, c in zip(gastos_mensuales, costos_mensuales)]
    costo_total_mano_de_obra = sum(costos_mensuales)
    meses_sin_gastos = [mes for mes, gasto in enumerate(gastos_mensuales, start=1) if gasto == 0]
    meses_gasto_menor_100000 = [mes for mes, gasto in enumerate(gastos_mensuales, start=1) if gasto < 100000]
    meses_costo_mayor_gasto = [mes for mes, costo in enumerate(costos_totales_mensuales, start=1) if costo > gastos_mensuales[mes - 1]]

    promedio_costos_fijos = sum(costos_mensuales) / 5
    promedio_costos_variables = sum(gastos_mensuales) / 5

    ingresos = valor_arroba_arroz * (cantidad_kilos_recolectados / 12.5)
    costos_totales = sum(costos_totales_mensuales)
    gastos_totales = sum(gastos_mensuales)
    ganancia = ingresos - costos_totales - gastos_totales

    precio_incrementado = valor_arroba_arroz * 1.37
    ganancia_incremento_precio = (precio_incrementado * (cantidad_kilos_recolectados / 12.5)) - costos_totales - gastos_totales

    costos_reducidos = [(0.95 * costo) for costo in costos_mensuales]
    kilos_incrementados = cantidad_kilos_recolectados * 1.63
    ganancia_costos_reducidos = (valor_arroba_arroz * (kilos_incrementados / 12.5)) - sum(costos_reducidos) - gastos_totales

    # Mostrar resultados
    print("El resultado del Informe Económico es: ")
    print(f"Los costos totales del cultivo por mes fueron: {costos_totales_mensuales}")
    print(f"Los costos totales de mano de obra fueron: {costo_total_mano_de_obra}")
    print(f"Meses en los cuales no hubo gastos: {meses_sin_gastos}")
    print(f"Meses en los cuales el gasto fue menor a 100,000: {meses_gasto_menor_100000}")
    print(f"Meses en los cuales el costo total del mes fue mayor al gasto total del mes: {meses_costo_mayor_gasto}")
    print(f"Valor promedio de costos Fijos: {promedio_costos_fijos}")
    print(f"Valor promedio de costos Variables: {promedio_costos_variables}")
    print(f"¿Hubo ganancia? {'SI' if ganancia > 0 else 'NO'}")
    print(f"Ganancia: {ganancia} pesos")
    print(f"La ganancia con precio de arroz incrementado en 37% es: {ganancia_incremento_precio} pesos")
    print(f"La ganancia con costos y gastos reducidos en 5% y producción incrementada en 63% es: {ganancia_costos_reducidos} pesos")

# Ciclo principal
while True:
    opcion = mostrar_menu()

    if opcion == "1":
        print("Opciones de cultivos:")
        for i, cultivo in enumerate(cultivos, start=1):
            print(f"{i}. {cultivo['Nombre']}")

        num_cultivo = int(input("Seleccione un cultivo: ")) - 1
        if 0 <= num_cultivo < len(cultivos):
            mostrar_horarios(cultivos[num_cultivo])
        else:
            print("Selección inválida, Seleccione una opción valida.")

    elif opcion == "2":
        print("Opciones de cultivos:")
        for i, cultivo in enumerate(cultivos, start=1):
            print(f"{i}. {cultivo['Nombre']}")

        num_cultivo = int(input("Seleccione un cultivo: ")) - 1
        if 0 <= num_cultivo < len(cultivos):
            mostrar_etapas(cultivos[num_cultivo])
        else:
            print("Selección inválida, Seleccione una opción valida.")

    elif opcion == "3":
        calcular_informacion_contable()

    elif opcion == "4":
        print("¡Muchas gracias por usar Agri-automático, Feliz dia!")
        break

    else:
        print("Esta opción no es válida. Por favor, seleccione una opción válida.")
