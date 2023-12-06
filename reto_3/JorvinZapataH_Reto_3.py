# -*- coding: utf-8 -*-
"""
Created on Sun Sep  3 18:13:20 2023

@author: JorvinZ
"""
#Información de los cultivos. Elegí no ingresarlos por consola si no establecerlos de una vez
cultivo1 = "Platano"
mantenimiento1 = "Lunes, Jueves 4:00 pm"
regado1 = "Martes, Viernes 5:00 pm"
abono1 = "Miércoles, Sábado 3:00 pm"
etapas1 = ["Siembra", "Crecimiento", "Cosecha"]

cultivo2 = "Maracuya"
mantenimiento2 = "Lunes, Miércoles 3:00 pm"
regado2 = "Martes, Jueves 4:00 pm"
abono2 = "Sábado 2:00 pm"
etapas2 = ["Siembra", "Crecimiento", "Cosecha"]

cultivo3 = "Yuca"
mantenimiento3 = "Martes, Jueves 4:30 pm"
regado3 = "Lunes, Viernes 4:00 pm"
abono3 = "Miércoles, Sábado 2:30 pm"
etapas3 = ["Siembra", "Crecimiento", "Cosecha"]


# Menú principal para la huerta escolar. Lo que hace el while es ejecutar siempre el Menu a menos que haya un "Break" que termine el bucle
while True:
    print("")
    print('''Bienvenido a el programa "\n "Siembra en la Escuela" \n------------------------ \n El software que te ayudará a gestionar tu huerta escolare de una mejor manera''')
    print("")
    
    #Menu para gestionar los cultivos
    opcion = int(input('''Menu principal, opciones: 
    1. Horario de Gestión de Cultivo
    2. Etapas del Cultivo
    3. Información Contable
    4. Salir
    Selecciona una opcion: 
    '''))
    
    print("")
 # A partir de aquí se empiezan a desarrollar los contenidos de cada una de las opciones que se dieron anteriormente
    if opcion == 1:
        print(f"\nCultivos disponibles: \n{cultivo1} \n{cultivo2} \n{cultivo3}")
        print("")
        
        seleccion = int(input("Seleccione un cultivo \n1: Platano \n2: Maracuya \n3: Yuca \n: "))
        
        if seleccion == 1:
            print(f"\nCultivo: {cultivo1}")
            print(f"Días y Horario de Mantenimiento: {mantenimiento1}")
            print(f"Días y Horario de Regado: {regado1}")
            print(f"Días y Horario de Abono: {abono1}")
        elif seleccion == 2:
            print(f"\nCultivo: {cultivo2}")
            print(f"Días y Horario de Mantenimiento: {mantenimiento2}")
            print(f"Días y Horario de Regado: {regado2}")
            print(f"Días y Horario de Abono: {abono2}")
        elif seleccion == 3:
            print(f"\nCultivo: {cultivo3}")
            print(f"Días y Horario de Mantenimiento: {mantenimiento3}")
            print(f"Días y Horario de Regado: {regado3}")
            print(f"Días y Horario de Abono: {abono3}")
        else:
            print("Selección no válida.")
            seleccion = int(input("Seleccione un cultivo \n1: Platano \n2: Maracuya \n3: Yuca \n: "))
    
    elif opcion ==2:
        print("\nEtapas del Cultivo: n\Siembra \nCrecimiento \nCosecha")
        etapa_de_cultivo = input('Mencione la etapa de cultivo que desea: ')
        print(f'La etapa del cultivo seleccionada fue {etapa_de_cultivo}')
  
    elif opcion ==3:
        print('ingrese el valor de los costos fijos')
        mano_de_obra = float(input("Ingrese el costo de Mano de Obra (mensual): "))
        abono = float(input("Ingrese el costo de Abono (mensual): "))
        agua = float(input("Ingrese el costo de Agua de Riego (mensual): "))
        mantenimiento = float(input("Ingrese el costo de Mantenimiento (mensual): "))
        
        print(" ")
        
        #produccion
        print('ingrese el valor de los costos de producción')
        valor_arroba = float(input("Ingrese el valor de la arroba (12.5 kilos): "))
        kilos_recolectados = float(input("Ingrese la cantidad de kilos recolectados: "))
        
        select = input('seleccione una opción del Menú: \nA- Costos \nB- Producción: ')
        print(" ")
        #Acá muestro los valores que se acabaron de ingresar anteriormente y creo el submenu
        if select == "A":
           while True:
               costs_submenu = int(input('seleccione una opción: \n1- Mano de Obra  \n2- Agua \n3- Mantenimiento \n4- Abono  \n5- Ir atrás: '))
               if costs_submenu == 1:
                   print(f'Los costos para mano de obra son: {mano_de_obra} COP mensuales')
               elif costs_submenu == 2:
                   print(f'Los costos para agua son: {agua} COP mensuales')
               elif costs_submenu == 3:
                   print(f'Los costos para mantenimiento son: {mantenimiento} COP mensuales')
               elif costs_submenu == 4:
                   print(f'Los costos para abono son: {abono} COP mensuales')
               elif costs_submenu == 5:
                   break  # Ir atrás
               else:
                   print("Selección no válida.")  
        #aca creo el otro submenu
        print(" ")
        if select == "B":
            while True:
                production_submenu = int(input('Seleccione una opción: \n1- Valor en Mercado del cultivo \n2- Cantidad Recogida \n3- Ir atrás: '))
                if production_submenu == 1:
                    print(f"El valor en el mercado del cultivo es: {valor_arroba} COP")
                elif production_submenu ==2:
                    print(f'La cantidad recogida fue de {kilos_recolectados} kilos')
                else:
                    break
            
        #calculos pata presentar el informe económico
        costos_totales = mano_de_obra + abono + agua + mantenimiento
        promedio_costos_fijos = costos_totales / 4
        ingresos = valor_arroba * (kilos_recolectados / 12.5)
        ganancia = ingresos - costos_totales
        nuevo_precio_arroba = valor_arroba * 1.37
        ganancia_con_incremento = (nuevo_precio_arroba * (kilos_recolectados / 12.5)) - costos_totales
        costos_disminuidos = costos_totales * 0.95
        produccion_disminuida = kilos_recolectados * 0.63
        ganancia_disminuida = (valor_arroba * (produccion_disminuida / 12.5)) - costos_disminuidos

        # Impresión del informe económico
        print("\nInforme Económico")
        print(f"Costos Totales del Cultivo: {costos_totales} COP")
        print(f"Valor Promedio de Costos Fijos: {promedio_costos_fijos} COP")
        print(f"¿Hubo Ganancia? {'SI' if ganancia > 0 else 'NO'}")
        print(f"Ganancia: {int(ganancia)}")
        print(f"Ganancia con Incremento del 37% en el Precio del Arroz: {ganancia_con_incremento} COP")
        print(f"Ganancia con Disminución del 5% en Costos y 63% en Producción: {ganancia_disminuida} COP")

    elif opcion == 4:
    # Salir del programa
       print("Saliendo de la aplicación.")
       break

    else:
        print("Opción no válida. Por favor, seleccione una opción válida.")
        
        
        
        
        
        