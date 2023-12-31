# -*- coding: utf-8 -*-
"""Maria Infante Lina Diaz_reto3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ylTFXM9Ynxm80zLLfmbzGxcWFT_17dlJ
"""

#Desarrollo de una solución  de menú para llevar a cabo la gestión de recolección y mantenimiento de los cultivos de la huerta escolar en Python

# Bloque declaracion de variable con la herramienta Diccionario:
# Crear un diccionario con información de los cultivos de la huerta: Tomate, Lechuga,Zanahoria, Arroz, cada uno de estos cultivos seran
# el key del diccionario y dentro de cada uno se crea otro diccionario que contiene horarios y dias de : Mantenimiento, Regado, Abono y adicionalmente
# contiene una opcion de etapas que contiene una lista de : Siembra, Crecimiento y Cosecha. Siendo Mantenimiento, Regado, Abono  y Etapas key del diccionario.
# Recordar que se distigue el diccionario con corchetes {} separados de comas y las listas se distinguen por [] ,

cultivos = {
    "Tomate": {
        "Mantenimiento": "Lunes, Jueves 4:00 pm",
        "Regado": "Martes, Viernes 3:00 pm",
        "Abono": "Miércoles, Sábado 2:00 pm",
        "Etapas": ["Siembra", "Crecimiento", "Cosecha"]
    },
    "Lechuga": {
        "Mantenimiento": "Lunes, Jueves 5:00 pm",
        "Regado": "Martes, Viernes 4:00 pm",
        "Abono": "Miércoles, Sábado 3:00 pm",
        "Etapas": ["Siembra", "Crecimiento", "Cosecha"]
    },
    "Zanahoria": {
        "Mantenimiento": "Lunes, Jueves 6:00 pm",
        "Regado": "Martes, Viernes 5:00 pm",
        "Abono": "Miércoles, Sábado 4:00 pm",
        "Etapas": ["Siembra", "Crecimiento", "Cosecha"]
    },
    "Arroz": {
        "Mantenimiento": "Jueves, Sabado 7:00 am",
        "Regado": "Martes, Viernes 7:00 pm",
        "Abono": "Miércoles, Sábado 2:00 pm",
        "Etapas": ["Siembra", "Crecimiento", "Cosecha"]
    }
}
#___________________________________________________________________________
#Bloque de funciones : -Funcion Menu principal: mostrar_menu_principa
#                      -Funcion Calculo Contable: calcular_informacion_contable

# Función para mostrar el menú principal, lo que realiza es que va a imprimir las opciones que El usuarios va a tener disponibles, segun la opcion que escoja se tendra
# una accion disponible para Ello, ya sea un submenu o la opcion de salir del menu.

def mostrar_menu_principal():
    print("\nMenú:")
    print("1. Horario de Gestión de Cultivo")
    print("2. Etapas del Cultivo")
    print("3. Información Contable")
    print("4. Salir")

# Función para calcular la información contable
# Identificamos los dos bloques de informacion que se requerian y estos se les solicita al usuario, el primero es los costos fijos como: mano de obra, abono, agua y mantenimiento
# el segundo es la informacion de produccion del arroz: Valor de la arroba (12,5 Kilos) del arroz y los Kilos recolectados.
# Ya teniendo los datos necesarios suministrados por el usuario para el calculo del informe economico  se procede con el bloque del calculo segun las especificaciones del requirimiento reto 3


def calcular_informacion_contable():

#Bloque de suministro de informacion requerida por medio del usuario
    # Costos fijos
    mano_de_obra = float(input("Ingrese el costo de Mano de Obra: "))
    abono = float(input("Ingrese el costo de Abono: "))
    agua = float(input("Ingrese el costo de Agua: "))
    mantenimiento = float(input("Ingrese el costo de Mantenimiento: "))

    # Producción de arroz
    valor_arroba = float(input("Ingrese el valor de la arroba (12.5 kilos) de arroz \n(el valor del mercado del arroba en Colombia 2023 esta entre 30.000 y 34.000): "))
    kilos_recolectados = float(input("Ingrese la cantidad de kilos recolectados: "))

#Bloque de los calculos necesarios para el informe economico

    # Cálculos
    costos_totales = mano_de_obra + abono + agua + mantenimiento
    promedio_costos_fijos = costos_totales / 4

    ingresos = valor_arroba * kilos_recolectados
    ganancia = ingresos - costos_totales

    nuevo_precio_arroz_incrementado = valor_arroba * 1.37
    nueva_ganancia = nuevo_precio_arroz_incrementado * kilos_recolectados - costos_totales

    reduccion_costos = costos_totales * 0.95
    aumento_produccion = kilos_recolectados * 0.37
    nueva_ganancia_ValoresReducidos = valor_arroba * aumento_produccion - reduccion_costos

# Bloque imprime el resumen del Informe economico requerido
# Adicionamente en l apregunta de si hubo o no ganancia utilizamos la funcion print con un condicional y hacemos un pequeño ciclo de if para que nos imprima
# el valor que dio si hubo ganancia

    print("\nInforme Económico:")
    print("Costos Totales del Cultivo:", costos_totales)
    print("Valor Promedio de Costos Fijos:", promedio_costos_fijos)
    print("¿Hubo Ganancia?", "Si Hubo" if ganancia > 0 else "No Hubo")
    if ganancia > 0:
        print("Ganancia:", ganancia)
    print("Ganancia con Precio Incrementado en un 37%:", nueva_ganancia)
    print("Ganancia con Costos Reducidos en un 5% y Producción Disminuida en un 63%:",  nueva_ganancia_ValoresReducidos)
#___________________________________________________________________________
# Bloque  Ciclo principal
# Utilizamos la opcion de ciclo infinito utilizando la funcion While con un condicional verdadero, donde solo se rompe el ciclo si el usuario decide salir del programa
# hacemos un primer mensaje de bienvenida, seguido del despliegue de opciones del menu principal descrito anteriormente, segun sea la opcion de escogencia entraremos a
# ejecutar un ciclo asi :

while True:
# Bienvenida y muestra menu principal
    print("\nBienvenido a Tu Hurta Sonriente donde juntos cosecharemos")

    mostrar_menu_principal()
    opcion = input("Seleccione una opción (1/2/3/4): ")

# Ciclo que ejecuta el menu de cultivo y los dias y horarios asociados especificamente a dicho cultivo
#- La Opcion 1. Jorario de gestion de cultivo: Le mostramos los cultivos disponibles: tomate, lechuga, zanahoria y arroz esto lo hacemos
# ejecutando un iterador (con un for y la funcion enumerete(no optimiza la iteracion y lo iniciamos en 1 para que el usuario tenga las opciones a escoger))
# que entra al diccionario y nos trae key principales que son dichos nombre del cultivo, luego le pedimos que seleccion el cultivo que quiere indagar y segun esa seleccion
# vamos a imprimir, ya mando una posicion especifica segun se requiera de la informacion de dicho cultivo
    if opcion == "1":
        # Horario de Gestión de Cultivo
        print("\nCultivos Disponibles:")
        for i, cultivo in enumerate(cultivos.keys(),start=1):
            print(f"{i}. {cultivo}")

        seleccion = int(input("Seleccione un cultivo (1/2/3/4): "))
        cultivo_elegido = list(cultivos.keys())[seleccion - 1]

        print(f"\nHorario de Gestión de {cultivo_elegido}:")
        print(f"Mantenimiento: {cultivos[cultivo_elegido]['Mantenimiento']}")
        print(f"Regado: {cultivos[cultivo_elegido]['Regado']}")
        print(f"Abono: {cultivos[cultivo_elegido]['Abono']}")
# - La Opcion 2. Etapas de cultivo seleccionado, y lo que hacemos es una iteracion para acceder e imprimir la lista que tiene esta opcion
    elif opcion == "2":
        # Etapas del Cultivo
        print("\nEtapas del Cultivo:")
        for etapa in cultivos[cultivo_elegido]['Etapas']:
            print(etapa)
# - La Opcion 3. Me imprime el informe contable que esta contenido en la funcion que estamos llamando calcular_informacion_contable
    elif opcion == "3":
        # Información Contable
        calcular_informacion_contable()
# - La Opcion 4. Es un break que lo que hace es que rompe el ciclo infinito del While
    elif opcion == "4":
        # Salir
        break
# - La utilma opcion es si el usuario ingresa un dato invalido
    else:
        print("Opción no válida. Intente nuevamente.")