# -*- coding: utf-8 -*-
"""Reto_3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1UiZEKOdhWeIWbcOuGxtQ1TwBNHUyQpN6
"""

nombreCultivo = "Cultivo de Arroz"
horarioMantenimiento = "Lunes, Jueves 4:00 pm"
horarioRegado = "Lunes, Jueves 4:00 pm"
horarioAbono = "Lunes, Jueves 4:00 pm"
# Variables Costos
mano_obra = int(input("Valor pagado a los trabajadores: " ))
agua = int(input("Valor pagado por el agua de riego: "))
mantenimiento = int(input("Valor pagado por mantenimiento de los equipos, herramientas y otros elementos: "))
abono = int(input("Valor del abono aplicado al cultivo: "))
# Variables Producción
valor_arroba = int (input("Valor de la arroba (12.5 kilos) de arroz: "))
cantidad = int(input("Cantidad de kilos recolectados: "))

#Menú Principal
menu = """
MENÚ PRINCIPAL
Seleccione la opción que requiere:
1. Horario de gestión de cultivo
2. Etapas del cultivo
3. Información contable
4. Salir
"""
print (menu)
opcion = input("Opción: ")
print ('-'*50)

# Opción N°1 relacionado a la infomación del cultivo como (Horario de gestión de cultivo)
if opcion == '1':
  print ("Datos del cultivo: ", nombreCultivo)
  print ("Horario de Mantenimiento: ", horarioMantenimiento)
  print ("Horario de Regado: ", horarioRegado)
  print ("Horario de Abono: ", horarioAbono)

# Opción N°2 Las Etapas del cultivo
elif opcion == '2':

  # Submenú de Etapas del Cultivo
  print ("""
  MENÚ ETAPAS DEL CULTIVO
  Seleccione la etapa del cultivo:
  1- Siembra
  2- Crecimiento
  3- Cosecha
  4- Regresar a Menú Principal
  5- Salir
  """)
  etapaCultivo = input("Etapa: ")
  print ('-'*50)
  # Opción Siembra
  if etapaCultivo == '1':
    print ("Su etapa de cultivo es Siembra")
  # Opción Crecimiento
  elif etapaCultivo == '2':
      print ("Su etapa de cultivo es Crecimiento")
  # Opción Cosecha
  elif etapaCultivo == '3':
    print ("Su etapa de cultivo es Cosecha")
  # Opción Regresar
  elif etapaCultivo == '4':
    print (menu)
  # Opción Salir
  elif etapaCultivo == '5':
    exit ()
  else:
    print ("Ingrese una opción válida")

# Opción N°3 Información Contable
elif opcion == '3':
  # Submenú de Información Contable
  submenu_info_contable = """
  MENÚ INFORMACIÓN CONTABLE
  Seleccione la información contable que requiere diligenciar:
  A- Costos
  B- Producción
  C- Informe Financiero
  D- Regresar a Menú Principal
  E- Salir
  """
  print (submenu_info_contable)
  infoContable = input("Opción: ")
  print ('-'*50)

  # Opción de Costos
  if infoContable == 'A':
    # Submenú de Costos
    print ("""
    MENÚ DE COSTOS
    Seleccione el costo a diligenciar:
    1- Mano de Obra
    2- Agua
    3- Mantenimiento
    4- Abono
    5- Ir Atrás
    6- Salir
    """)
    costo = input("opción: ")
    print ('-'*50)
    if costo == '1':
      print ("Valor pagado a los trabajadores ", mano_obra)
    elif costo == '2':
      print ("Valor pagado por el agua de riego ", agua)
    elif costo == '3':
      print ("Valor pagado por mantenimiento de los equipos, herramientas y otros elementos", mantenimiento)
    elif costo == '4':
      print ("Valor del abono aplicado al cultivo", abono)
    elif costo == '5':
      print (submenu_info_contable)
    elif costo == '6':
      exit()
    else:
      print ("Ingrese una opción valida")

  # Opción Producción
  elif infoContable == 'B':
     print ("""
    MENÚ DE PRODUCCIÓN
    Seleccione la producción a diligenciar:
    A- Valor en Mercado del Cultivo
    B- Cantidad Recogida
    C- Ir Atrás
    D- Salir
    """)
     productividad = input("Opción: ")
     print ('-'*50)
     if productividad == 'A':
      print ("Valor de la arroba (12.5 kilos) de arroz ", valor_arroba)
     elif productividad == 'B':
      print ("Cantidad de kilos recolectados ", cantidad)
     elif productividad == 'C':
      print (submenu_info_contable)
     elif productividad == 'D':
      exit()
     else:
      print ("Ingrese una opción valida")

  #INFORME FINANCIERO
  elif infoContable == 'C':
    print ("INFORME FINANCIERO")
    print ('-'* 50)

    # Costo Total
    costos_totales = mano_obra + agua + mantenimiento + abono
    print ("El costo total fijo del cultivo es de", costos_totales)
    print ('-'* 20)

    # Valor promedio
    valor_promedio = costos_totales/4
    print ("El valor promedio de los costos fijos es de", valor_promedio)
    print ('-'* 20)

    # Ganancia
    ingresos = valor_arroba * cantidad
    ganancia = ingresos - costos_totales
    if ganancia > 0 :
      print ("Tuvo ganancia de ", ganancia)
      print ('-'* 20)
    else:
      print ("No tuvo ganancia")
      print ('-'* 20)

    # Aumento del valor de la ganacia a 37% x kg
    valor_kilo = valor_arroba / 12.5
    nuevo_valor = valor_kilo + (valor_kilo * 0.37)
    nueva_ganancia = nuevo_valor - costos_totales
    print ("Por el aumento de 37% del valor del kilo, su ganancia es de", nueva_ganancia)
    print ('-'* 20)

    # Disminución de costos al 5%
    nuevo_costoTotal = costos_totales - (costos_totales * 0.05)
    print ("Al bajar el 5% de los costos quedaron en", nuevo_costoTotal)
    # Aumento en cantidad producidas x arroba al 63%
    nuevas_arrobas_producidas = valor_arroba + (valor_arroba * 0.63)
    print ("Las nuevas arrobas producidas son", nuevas_arrobas_producidas)
    # Nueva Ganancia
    nuevos_ingresos = valor_arroba * nuevas_arrobas_producidas
    new_ganancia = nuevo_costoTotal - nuevos_ingresos
    print ("Sus gancias total al disminuir los costos al 5% y aumentar la producción por arroba del 63% es de", new_ganancia)

  elif infoContable == 'D':
    print (menu)
  elif infoContable == 'E':
    exit()
  else:
    print ("Seleccione una opción valida")



# Opción N°4 Salir
elif opcion == '4':
  exit()

else:
  print ("Debes ingresar un número entre el 1 y 4")