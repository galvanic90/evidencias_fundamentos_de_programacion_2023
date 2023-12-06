# En esta sección se encuentra la bienvienida al usuario
print(" ")
print("BIENVENIDO A G-SOFT")
print("----------------------")
print("El software de información contable para agricultores")
print(" ")

#En este ciclo se evalua que mientras sea verdadera la opción ingresada por el usuario se ejecutan
#las opciones que hay en el interior del ciclo, como lo son los submenus e información contable
while True:
    print("Seleccione una de las opciones de acuerdo a la información que desea conocer: ")
    opciones = int(input('''
    1 - Horario y gestión del cultivo
    2 - Etapas del cultivo
    3 - Información contable
    4 - Salir
    '''))
#Este condicional evalua que la opción elegida por el usuario sea igual que la opción 1 del menu
#principal, imprime las opciones de cultivos numerados y recibe por consola la opción del usuario.
    if opciones == 1:
        print("Escriba el número correspondiente al nombre del cultivo: ")
        cultivo =int(input('''
        1 - Cultivo 1 (arroz)
        2 - Cultivo 2 (frijol)
        3 - Cultivo 3 (maiz)
        4 - Cultivo 4 (yuca)
        '''))
#Esta serie de condicionales evalua que la opción elegida por el usuario sea igual a una de las 
#opciones del submenu.Además, tras escoger un cultivo, se evalua el cultivo que escogió e imprime
# los días y horarios de Mantenimiento, Regado y Abono del Respectivo Cultivo.
        if cultivo == 1:
            print('''
-Los días y el Horario de Mantenimiento para el cultivo 1 (arroz) son los Lunes y Jueves a las 4:00 pm.
-Los días y el Horario de Regado para el cultivo 1 (arroz) son los Lunes y Jueves a las 4:00 pm.
-Los días y el Horario de Abono para el cultivo 1 (arroz) son los Lunes y Jueves a las 4:00 pm.''')
        if cultivo == 2:
            print('''
-Los días y el Horario de Mantenimiento para el cultivo 2 (frijol) son los Martes y Viernes a las 3:00 pm.
-Los días y el Horario de Regado para el cultivo 2 (frijol) son los Martes y Viernes a las 3:00 pm.
-Los días y el Horario de Abono para el cultivo 2 (frijol) son los Martes y Viernes a las 3:00 pm.''')
        if cultivo == 3:
            print('''
-Los días y el Horario de Mantenimiento para el cultivo 3 (maiz) son los Miercoles y Sábados a las 10:00 am.
-Los días y el Horario de Regado para el cultivo 3 (maiz) son los Miercoles y Sábados a las 10:00 am.
-Los días y el Horario de Abono para el cultivo 3 (maiz) son los Miercoles y Sábados a las 10:00 am.''')
        if cultivo == 4:
            print('''
-Los días y el Horario de Mantenimiento para el cultivo 4 (yuca) son los Lunes y Jueves a las 9:00 am.
-Los días y el Horario de Regado para el cultivo 4 (yuca) son los Lunes y Jueves a las 9:00 am.
-Los días y el Horario de Abono para el cultivo 4 (yuca) son los Lunes y Jueves a las 9:00 am.''')
                              
 #       print("Seleccione una opción de acuerdo a los dias y horarios de cada etapa: ")
 #       gestion = input('''
  #      A - Días y horarios de la etapa de siembra
   #     B - Días y horarios de la etapa de riego
   #     C - Días y horarios de la etapa de abono
    #    D - Ir al menú principal
     #   ''')
        
 #       if gestion == 5:
 #           regresar = input("Deseas volver al menu principal? Ingresa S para regresar o N para continuar ")
 #           if regresar.upper == 'S':
 #               continue      

#Este condicional evalua que la opción elegida por el usuario sea igual que la opción 1 del menu
#principal, imprime las opciones de cultivos numerados y recibe por consola la opción del usuario.
    if opciones == 2:
        print("Escriba el número correspondiente al nombre del cultivo: ")
        cultivo_2 =int(input('''
        1 - Cultivo 1 (arroz)
        2 - Cultivo 2 (frijol)
        3 - Cultivo 3 (maiz)
        4 - Cultivo 4 (yuca)
        '''))
#Esta serie de condicionales evalua que la opción elegida por el usuario sea igual a una de las 
#opciones del submenu.Además, tras escoger un cultivo, se evalua el cultivo que escogió e imprime
# las etapas del respectivo Cultivo.     
        if cultivo_2 == 1:
            print(""" Las etapas del cultivo 1, de arroz y sus respectivos intervalos son:
Etapa 1 - Fase vegetativa, con una duración de 35 a 50 días.
Etapa 2 - Fase reproductiva, con una duración de 35 a 30 días.
Etapa 3 - Fase de maduración, con una duración de 30 a 35 días.""")
        if cultivo_2 == 2:
            print("""Las etapas del cultivo 2, de frijol y sus respectivos intervalos son:
Etapa 1 - Fase vegetativa, desde el día 32 al día 55 desde la siembra.
Etapa 2 - Fase reproductiva, desde el día 65 al día 89 desde la siembra.
Etapa 3 - Fase de senescencia, desde el día 90 al día 300 desde la siembra.""")
        if cultivo_2 == 3:
            print("""Las etapas del cultivo 3, de maiz y sus respectivos intervalos son:
Etapa 1 - Fase vegetativa, desde el día 5 al día 55 desde la siembra.
Etapa 2 - Fase reproductiva, desde el día 57 al día 112 desde la siembra.""")
        if cultivo_2 == 4:
            print("""Las etapas del cultivo 4, de maiz y sus respectivos intervalos son:
Etapa 1 - Fase crecimiento lento, desde el día 0 al día 60 desde la siembra.
Etapa 2 - Fase de máximo crecimiento, desde el día 60 al día 150 desde la siembra.
Etapa 3 - Fase de senescencia, desde el día 150 al día 300 desde la siembra. """)
#En esta sección del código se muestra el resumen contable de acuerdo a la información ingresada 
#por el usuario, una vez se elija la opción 3 del menú principal
    if opciones == 3:           
        meses = ["Mes 1", "Mes 2", "Mes 3", "Mes 4", "Mes 5"]
        mensual_med = []
        mensual_imp = []
        mensual_mano = []
        mensual_abono = []
        mensual_agua = []
        mensual_mant = []
        costo_total = []
        gasto_total = []
# Este ciclo permite que se almacenen 5 datos y se recorra i en para poder tener la información
#contable detallada por mes
        for i in meses:
          print("Ingrese el gasto mensual en medicamentos correspondiente al mes de ", i)
          mensual_med.append (int(input()))
          print("Ingrese el gasto mensual imprevisto correspondiente al mes de ", i)
          mensual_imp.append (int(input()))
          print("Ingrese el costo mensual en mano de obra correspondiente al mes de ", i)
          mensual_mano.append (int(input()))
          print("Ingrese el costos mensual en abono correspondiente al mes de ", i)
          mensual_abono.append (int(input()))
          print("Ingrese el costo mensual por agua correspondiente al mes de ", i)
          mensual_agua.append (int(input()))
          print("Ingrese el costo mensual en mantenimiento correspondiente al mes de ", i)
          mensual_mant.append (int(input()))
        valor_arroz = int(input("Ingrese el valor de la arroba de arroz: "))
        cant_kilos = int(input("Ingrese la cantidad de kilos recolectados: "))
        print(" ")
        print("----------------------------")
        print("Resumen contable")
        print("----------------------------")
        print(" ")
#Este ciclo permite recorrer la longitud de meses para obtener el costo total, la mano de obra y gasto
        for i in range(len(meses)):
          costo_total.append(mensual_mano[i] + mensual_abono[i] + mensual_agua[i] + mensual_mant[i])
          print("El costo total del cultivo del ", meses[i], "es", costo_total[i])
          gasto_total.append(mensual_med[i] + mensual_imp[i])
#En esta serie de condicionales se evalua cuando el gasto es igual a 0, cuando el gasto es menor a
#100000 y cuando el costo es mayor al gasto.
          if gasto_total[i] == 0:
            print("En el mes de ",meses[i], "no hubo gastos ")
          if gasto_total[i] < 100000:
            print("En el mes de ", meses[i], "el gasto fue menor a 100000 pesos")
          if costo_total[i] > gasto_total[i]:
            print("En el mes de ", meses[i], "el costo total fue mayor al gasto total")
        total_mano = sum(mensual_mano)
        print("El costo total de mano de obra es: ", total_mano)
        costos_fijos = sum(costo_total) / len(costo_total)
        costos_variables = sum(gasto_total) / len(gasto_total)
        print("El valor promedio de los costos fijos es: ",costos_fijos)
        print("El valor promedio de los costos variables es: ",costos_variables)
        ganancia = (valor_arroz*cant_kilos) - sum(gasto_total) - sum(costo_total)
        print("La ganancia fue de", ganancia, "pesos")
        valor_aumentado = valor_arroz + valor_arroz*0.24
        ganancia_dos = (valor_aumentado*cant_kilos) - sum(gasto_total) - sum(costo_total)
        print("Si el precio del kilo de arroz aumenta en un 37%, la ganancia obtenida es: ", ganancia_dos)
        costos_disminuidos = sum (costo_total) - sum(costo_total)*0.05
        gastos_disminuidos = sum (gasto_total) - sum(gasto_total)*0.05
        cantidad_disminuida = cant_kilos - (cant_kilos*0.63)
        ganancia_disminuida = (valor_arroz*cantidad_disminuida) - costos_disminuidos - gastos_disminuidos
        print("Si los costos y gastos se disminuyen en un 5% y la cantidad de arrobas producidas en un 63%, la ganancia es de: ", ganancia_disminuida)
#En esta sección, cuando el usuario ingrese la opción 4 en el menu principal, se rompe el ciclo 
#y la ejecución
    if opciones == 4:
        break        
