# -*- coding: utf-8 -*-
"""
Created on Sun Sep 10 17:45:41 2023

@author: JorvinZ
"""
# a continuación se crearán las funciones para gestionar nuestro cultivo

def mostrar_cultivo_info(cultivo, mantenimiento, regado, abono):
    '''Esta función solo imprime información referente a un cultivo, en específico
    obteniendo sus parámetros de la función gestionar_cultivo()'''
    print(f"\nCultivo: {cultivo}")
    print(f"Días y Horario de Mantenimiento: {mantenimiento}")
    print(f"Días y Horario de Regado: {regado}")
    print(f"Días y Horario de Abono: {abono}")

def gestionar_cultivo(cultivo, cultivo_info):
    '''Esta función toma dos argumentos, el cultivo que el usuario desea ver, y cultivo_info
    que es un diccionario que contiene toda la info de los diferentes cultivos. Esta funcíon
    verifica si el cultivo ingresado por el usuario se encuentra en el diccionario, si está ahí
    obtiene la info referente a ese cultivo y llama a la función mostrar_cultivo_info() pa que imprima
    esa info accediendo a sus claves'''
    if cultivo in cultivo_info:
        info = cultivo_info[cultivo]
        mostrar_cultivo_info(cultivo, info["mantenimiento"], info["regado"], info["abono"])
    else:
        print("Selección no válida.")

def calcular_costos(mano_de_obra, abono, agua, mantenimiento):
    '''Esta función calcula los costos totales que el usuario ingresó en cada
    categoría en el menú principal'''
    costos_totales = mano_de_obra + abono + agua + mantenimiento
    return costos_totales

def calcular_ganancia(valor_arroba, kilos_recolectados, costos_totales):
    '''Esta función calcula las ganancias de acuerdo a la info suministrada
    por el usuario en la función del menu principal'''
    ingresos = valor_arroba * (kilos_recolectados / 12.5)
    ganancia = ingresos - costos_totales
    return ingresos, ganancia

def informe_economico(ingresos, costos_totales, ganancia):
    '''Esta función me da un informe económico de todos los datos que ingresé
    previamente en el menu principal'''
    promedio_costos_fijos = costos_totales / 4
    nuevo_precio_arroba = valor_arroba * 1.37
    ganancia_con_incremento = (nuevo_precio_arroba * (kilos_recolectados / 12.5)) - costos_totales
    costos_disminuidos = costos_totales * 0.95
    produccion_disminuida = kilos_recolectados * 0.63
    ganancia_disminuida = (valor_arroba * (produccion_disminuida / 12.5)) - costos_disminuidos

    print("\nInforme Económico")
    print(f"Costos Totales del Cultivo: {costos_totales} COP")
    print(f"Valor Promedio de Costos Fijos: {promedio_costos_fijos} COP")
    print(f"¿Hubo Ganancia? {'SI' if ganancia > 0 else 'NO'}")
    print(f"Ganancia: {int(ganancia)}")
    print(f"Ganancia con Incremento del 37% en el Precio del Arroz: {ganancia_con_incremento} COP")
    print(f"Ganancia con Disminución del 5% en Costos y 63% en Producción: {ganancia_disminuida} COP")

#el diccionario que cree para reducir la info y no tener variables globales. Dentro de este diccionario los cultivos funcionan como llaves y la info de estos cultivos como otros diccionarios
cultivo_info = {
    "Platano": {"mantenimiento": "Lunes, Jueves 4:00 pm", "regado": "Martes, Viernes 5:00 pm", "abono": "Miércoles, Sábado 3:00 pm"},
    "Maracuya": {"mantenimiento": "Lunes, Miércoles 3:00 pm", "regado": "Martes, Jueves 4:00 pm", "abono": "Sábado 2:00 pm"},
    "Yuca": {"mantenimiento": "Martes, Jueves 4:30 pm", "regado": "Lunes, Viernes 4:00 pm", "abono": "Miércoles, Sábado 2:30 pm"}
}

#defino variables globales para estos valores
valor_arroba = 0  
kilos_recolectados = 0  

#hago el menu principal
def main():
    global valor_arroba, kilos_recolectados  # Declarar que estamos usando las variables globales
#muestro un ciclo infinito para que siempre se me imprima el menú a menos que se encuentre un brake

    while True:
        print("")
        print('''Bienvenido a el programa "\n "Siembra en la Escuela" \n------------------------ \n El software que te ayudará a gestionar tu huerta escolar de una mejor manera''')
        print("")

        opcion = int(input('''Menu principal, opciones: 
        1. Horario de Gestión de Cultivo
        2. Etapas del Cultivo
        3. Información Contable
        4. Salir
        Selecciona una opcion: 
        '''))

        print("")
# A partir de aquí comienzo a utilizar las funciones que cree anteriormente.
        if opcion == 1:
            print("\nCultivos disponibles: \nPlatano \nMaracuya \nYuca\n")
            seleccion = input("Seleccione un cultivo: ")
            gestionar_cultivo(seleccion, cultivo_info)
        elif opcion == 2:
            print("\nEtapas del Cultivo:\nSiembra\nCrecimiento\nCosecha")
            etapa_de_cultivo = input('Mencione la etapa de cultivo que desea: ')
            print(f'La etapa del cultivo seleccionada fue {etapa_de_cultivo}')
        elif opcion == 3:
            print('Seleccione una opción del Menú:\nA - Costos y Producción\nB - Información Contable')
            submenu_opcion = input('Opción: ')
            #con este submenu voy ingresando uno por uno cada uno de los costos y la información contable
            if submenu_opcion == 'A':
                print('Submenú - Costos y Producción:')
                print('1. Mano de Obra')
                print('2. Agua')
                print('3. Mantenimiento')
                print('4. Abono')
                print('5. Ir atrás')
                costo_opcion = input('Seleccione una opción: ')

                if costo_opcion == '1':
                    mano_de_obra = float(input("Ingrese el costo de Mano de Obra (mensual): "))
                elif costo_opcion == '2':
                    agua = float(input("Ingrese el costo de Agua de Riego (mensual): "))
                elif costo_opcion == '3':
                    mantenimiento = float(input("Ingrese el costo de Mantenimiento (mensual): "))
                elif costo_opcion == '4':
                    abono = float(input("Ingrese el costo de Abono (mensual): "))
                elif costo_opcion == '5':
                    continue  # Volver al menú principal
                else:
                    print("Opción no válida.")
            elif submenu_opcion == 'B':
                print('Submenú - Información Contable:')
                print('a - Valor en Mercado del Cultivo')
                print('b - Cantidad Recogida')
                print('c - Ir atrás')
                informacion_opcion = input('Seleccione una opción: ')

                if informacion_opcion == 'a':
                    valor_arroba = float(input("Ingrese el valor de la arroba (12.5 kilos): "))
                elif informacion_opcion == 'b':
                    kilos_recolectados = float(input("Ingrese la cantidad de kilos recolectados: "))
                elif informacion_opcion == 'c':
                    continue  # Volver al menú principal
                else:
                    print("Opción no válida.")
            else:
                print("Opción no válida.")
        elif opcion == 4:
            print("Saliendo de la aplicación.")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    main()
