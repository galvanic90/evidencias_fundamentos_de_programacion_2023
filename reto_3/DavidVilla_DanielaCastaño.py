from re import I
from ast import While

i=0
while True:
    i+=1
    print('''     ------Bienvenido la calculadora contable de sus cultivo.------


   ------A continuación se le presentaran las siguientes opciones para conocer el estudio contable de sus cultivos.------
    ''')

    exec(f"Nombre{i}=input('Ingrese Nombre del cultivo {i}: ')")
    exec(f"Mantenimiento{i}=input('Días y Horario de Mantenimiento {i} (Ej. Lunes, Jueves 4:00 pm) : ')")
    exec(f"Regado{i}=input('Días y Horario de Regado {i} (Ej. Lunes, Jueves 4:00 pm): ')")
    exec(f"Abono{i}=input('Días y Horario de Abono  {i} (Ej. Lunes, Jueves 4:00 pm) : ')")
    exec(f"Etapas{i}=input('Variables para cada ETAPA del Cultivo y sus intervalos {i} (Ingrese el numero correspondiente 1.SIEMBRA 2.CRECIMIENTO 3.COSECHA): ')")
    Finalizar=input("Si desea finalizar el ingreso de información ingrese '1', de lo contrario ingrese '0': ")
    if Finalizar=='1':
      n=i+1
      break




while True:

  print("""
  Seleccione un cultivo a validar""")
  i=int(1)
  for i in range(1,n):
    exec(f"print('{i}. Nombre cultivo {i}: {globals()[f'Nombre{i}']}')")

  i=input("")

  Menu=input('''
  Seleccione una opción:

  1. Horario de Gestión de Cultivo: si se elige esta opción, se deben imprimir las opciones de cultivos numerados y recibir por consola la opción del usuario.
  Tras escoger un cultivo, se debe evaluar el cultivo que escogió e imprimir los días y horarios de Mantenimiento, Regado y Abono del Respectivo Cultivo.

  2. Etapas del Cultivo: si se elige esta opción, se deben imprimir las opciones de cultivos numerados y recibir por consola la opción del usuario.
  Tras escoger un cultivo, se debe evaluar el cultivo que escogió e imprimir todas las Etapas del Respectivo Cultivo.

  3. Información Contable:  Aquí se desarrolla el punto 2 del reto.

  4. Salir: si se elige esta opción, simplemente se debe finalizar la ejecución de la aplicación.

  ''')

  if Menu=='1':
    print(globals()[f'Nombre{i}'])
    print(globals()[f'Mantenimiento{i}'])
    print(globals()[f'Regado{i}'])
    print(globals()[f'Abono{i}'])
  elif Menu=='2':
    print(globals()[f'Nombre{i}'])
    if (globals()[f'Etapas{i}'])=='1':
      print("SIEMBRA")
    elif (globals()[f'Etapas{i}'])=='2':
      print("CRECIMIENTO")
    elif (globals()[f'Etapas{i}'])=='3':
      print("COSECHA")
  elif Menu=='3':

    while True:
      Punto2=input('''
      1- Costos
      2- Producción
      3- Calcular resultados
      ''')
      if Punto2=='1':
          manoobra=int(input("Ingrese el valor pagado a los trabajadores: "))
          abono=int(input("Ingrese el valor pagado por el abono aplicado al cultivo: "))
          agua=int(input("Ingrese el valor pagado por el agua del riego (que no proviene del riego directo por la lluvia): "))
          mantenimiento=int(input('ingrese el valor pagado por mantenimiento de los equipos, herramientas y elementos que requieren cultivo: '))
      elif Punto2=='2':
          valormercado=int(input("Ingrese el valor del cultivo por arroba (12.5 kilos) de arroz: "))
          cantidadrecogida=int(input("Ingrese  la cantidad arrobas recogidas: "))
      elif Punto2=='3':
          Total=manoobra+abono+agua+mantenimiento
          Promedio=(manoobra+abono+agua+mantenimiento)/4
          Utilidades=valormercado*cantidadrecogida
          print("Los costos totales del cultivo fueron de: ", Total)
          print("El valor promedio de los costos fijos es de: ", Promedio)
          if Utilidades>Total:
            print("Se obtuvo una ganancia de: ", Utilidades-Total)
          else:
            print("Se obtuvo una pérdida de: ", Utilidades-Total)
          print("Si el precio aumenta un 37% la ganancia obtenida sería de: ", round(Utilidades*1.037,0))
          print("Si los costos y gastos disminuyen en un 5% y la cantidad de producida en un 63%, la ganancia sería de: ", (valormercado*cantidadrecogida*1.63-(Total*0.95)))
          print("Se ha finalizado la aplicación")
          break
  else:
    print("Se ha finalizado la aplicación")
    break


