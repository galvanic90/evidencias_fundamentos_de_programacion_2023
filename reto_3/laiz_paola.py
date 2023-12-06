#Variables inicializadas. Necesarias ya que puede darse que en el flujo no se le asigne valor.

mes1_mano_obra = 0
mes1_agua = 0
mes1_mtto = 0
mes1_abono = 0
mes1_valor_cultivo = 0
mes1_cantidad = 0
mes1_medicamentos=0
mes1_imprevistos=0

mes2_mano_obra = 0
mes2_agua = 0
mes2_mtto = 0
mes2_abono = 0
mes2_valor_cultivo = 0
mes2_cantidad = 0
mes2_medicamentos=0
mes2_imprevistos=0

mes3_mano_obra = 0
mes3_agua = 0
mes3_mtto = 0
mes3_abono = 0
mes3_valor_cultivo = 0
mes3_cantidad = 0
mes3_medicamentos=0
mes3_imprevistos=0

mes4_mano_obra = 0
mes4_agua = 0
mes4_mtto = 0
mes4_abono = 0
mes4_valor_cultivo = 0
mes4_cantidad = 0
mes4_medicamentos=0
mes4_imprevistos=0

mes5_mano_obra = 0
mes5_agua = 0
mes5_mtto = 0
mes5_abono = 0
mes5_valor_cultivo = 0
mes5_cantidad = 0
mes5_medicamentos=0
mes5_imprevistos=0

mes1_costos_contadores = 0
mes2_costos_contadores = 0
mes3_costos_contadores = 0
mes4_costos_contadores = 0
mes5_costos_contadores = 0

mes1_contador1 = 0
mes1_contador2 = 0
mes1_contador3 = 0
mes1_contador4 = 0

mes2_contador1 = 0
mes2_contador2 = 0
mes2_contador3 = 0
mes2_contador4 = 0

mes3_contador1 = 0
mes3_contador2 = 0
mes3_contador3 = 0
mes3_contador4 = 0

mes4_contador1 = 0
mes4_contador2 = 0
mes4_contador3 = 0
mes4_contador4 = 0

mes5_contador1 = 0
mes5_contador2 = 0
mes5_contador3 = 0
mes5_contador4 = 0

mes1_total_costos = 0
mes2_total_costos = 0
mes3_total_costos = 0
mes4_total_costos = 0
mes5_total_costos = 0

mes1_total_gastos= 0
mes2_total_gastos= 0
mes3_total_gastos= 0
mes4_total_gastos= 0
mes5_total_gastos= 0

mes1_total_prod= 0
mes2_total_prod= 0
mes3_total_prod= 0
mes4_total_prod= 0
mes5_total_prod= 0

mes1_gastos_contadores= 0
mes2_gastos_contadores= 0
mes3_gastos_contadores= 0
mes4_gastos_contadores= 0
mes5_gastos_contadores= 0

mes1_costos_contadores= 0
mes2_costos_contadores= 0
mes3_costos_contadores= 0
mes4_costos_contadores= 0
mes5_costos_contadores= 0

mes1_costos_prom =  0
mes2_costos_prom =  0
mes3_costos_prom =  0
mes4_costos_prom =  0
mes5_costos_prom =  0

mes1_promedio_fijos= 0
mes2_promedio_fijos= 0
mes3_promedio_fijos= 0
mes4_promedio_fijos= 0
mes5_promedio_fijos= 0

#Variables horarios de gestión de Cultivo

gestion_arroz=('''
Mantenimiento: Días: Lunes y Miércoles - Hora: 4:00 pm.
Riego: Días: Martes y Jueves - Hora: 2:00 pm.
Abono: Días: Viernes - Hora: 7:00 am.
''')
gestion_maiz=('''
Mantenimiento: Lunes y Jueves - Hora: 2:00 pm.
Riego: Martes y Viernes - Hora: 10:00 am.
Abono: Miércoles y Lunes - Hora: 7:00 am.
''')
gestion_quinua=('''
Mantenimiento: Miércoles y Jueves - Hora: 8:00 am.
Riego: Miércoles y Viernes - Hora: 11:00 am
Abono: Lunes y Martes - Hora: 3:00 pm
''')
gestion_avena=('''
Mantenimiento: Lunes y Viernes - Hora: 10:00 am
Riego: Martes y Viernes - Hora: 2:00 pm
Abono: Miércoles y Lunes - Hora: 7:00 am
''')

#Etapas del cultivo

etapa1_arroz=('La etapa de SIEMBRA del cultivo de Arroz es de 55 a 60 días')
etapa2_arroz=('La etapa de CRECIMIENTO del cultivo de Arroz es de 55 a 60 días')
etapa3_arroz=('La etapa de COSECHA del cultivo de Arroz es de 55 a 60 días')
etapa1_maiz=('La etapa de SIEMBRA del cultivo de Maíz es de 55 a 60 días')
etapa2_maiz=('La etapa de CRECIMIENTO del cultivo de Maíz es de 55 a 60 días')
etapa3_maiz=('La etapa de COSECHA del cultivo de Maíz es de 55 a 60 días')
etapa1_quinua=('La etapa de SIEMBRA del cultivo de Quinua es de 55 a 60 días')
etapa2_quinua=('La etapa de CRECIMIENTO del cultivo de Quinua es de 55 a 60 días')
etapa3_quinua=('La etapa de COSECHA del cultivo de Quinua es de 55 a 60 días')
etapa1_avena=('La etapa de SIEMBRA del cultivo de Avena es de 55 a 60 días')
etapa2_avena=('La etapa de CRECIMIENTO del cultivo de Avena es de 55 a 60 días')
etapa3_avena=('La etapa de COSECHA del cultivo de Avena es de 55 a 60 días')

#Desarrollo código

#Menú para escoger tipo de cultivo

tipo_cultivo=input("""ECOHUERTA LAIZ & PAO

      Actualmente contamos el siguiente programa el cual le permitirá llevar a cabo la gestión de recolección y mantenimiento de los siguientes cultivos: Arroz, Maiz, Quinua y Avena

      Por favor ingrese el nombre del tipo de cultivo:

      1. Arroz
      2. Maiz
      3. Quinua
      4. Avena
      5. Salir
      """)

#Menú principal

opciones=input(""" Ahora, por favor ingrese la siguiente opción la cual desee obtener más información:

      1. Horario de Gestión de Cultivo
      2. Etapas del cultivo
      3. Información contable
      4. Seleccionar otro tipo de cultivo
      5. Salir
      """)

while True:                #Este ciclo va a evaluar las diferentes opciones (dependiendo la que escoga del menú principal) para el tipo de cultivo elegido en un principio.
    if opciones =='4':     #Esta opción me permite escoger otro tipo de cultivo al seleccionado en un principio.

      tipo_cultivo=input(""" Por favor ingrese el nombre del tipo de cultivo:

      1. Arroz
      2. Maiz
      3. Quinua
      4. Avena
      5. Salir
      """)

      opciones=input(""" Ahora, por favor ingrese la siguiente opción la cual desee obtener más información:

      1. Horario de Gestión de Cultivo
      2. Etapas del cultivo
      3. Información contable
      4. Seleccionar otro tipo de cultivo
      5. Salir
      """)

    else:
      if opciones =='1':          #Esta condición me permite obtener la información de gestión de cultivo
        
        gestion_cultivo=input("""Seleccione una de estas opciones:
        1. Días y horarios de mantenimiento/abono/riego   
        2. Menú principal

        """) #Este es un submenú 

        if gestion_cultivo== '1' and tipo_cultivo == '1':
          print('Los días y horarios del gestión del cultivo de Arroz son'+ gestion_arroz )
        elif gestion_cultivo== '1' and tipo_cultivo == '2':
          print('Los días y horarios del gestión del cultivo de Maiz son'+ gestion_maiz )
        elif gestion_cultivo== '1' and tipo_cultivo == '3':
          print('Los días y horarios del gestión del cultivo de Quinua son'+ gestion_quinua )
        elif gestion_cultivo== '1' and tipo_cultivo == '4':
          print('Los días y horarios del gestión del cultivo de Avena son'+ gestion_avena )
        elif gestion_cultivo== '2':

          opciones=input(""" Ahora, por favor ingrese la siguiente opción la cual desee obtener más información:

          AVISO: La información contable sólo esta disponible para el cultivo: ARROZ

          1. Horario de Gestión de Cultivo
          2. Etapas del cultivo
          3. Información contable
          4. Seleccionar otro tipo de cultivo
          5. Salir
          """) # Aquí regreso al menú principal

      elif opciones =='2':     #Esta condición me permite obtener la información de las etapas del cultivo

        etapa_cultivo=input("""Seleccione una de estas opciones:
            1. Siembra
            2. Crecimiento
            3. Cosecha
            4. Menú principal
            """) #Este es un submenú 

        if etapa_cultivo == '1' and tipo_cultivo == '1':
          print(etapa1_arroz)
        elif etapa_cultivo == '1' and tipo_cultivo == '2':
          print(etapa1_maiz)
        elif etapa_cultivo == '1' and tipo_cultivo == '3':
          print(etapa1_quinua)
        elif etapa_cultivo == '1' and tipo_cultivo == '4':
          print(etapa1_avena)
        elif etapa_cultivo == '2' and tipo_cultivo == '1':
          print(etapa2_arroz)
        elif etapa_cultivo == '2' and tipo_cultivo == '2':
          print(etapa2_maiz)
        elif etapa_cultivo == '2' and tipo_cultivo == '3':
          print(etapa2_quinua)
        elif etapa_cultivo == '2' and tipo_cultivo == '4':
          print(etapa2_avena)
        elif etapa_cultivo == '3' and tipo_cultivo == '1':
          print(etapa3_arroz)
        elif etapa_cultivo == '3' and tipo_cultivo == '2':
          print(etapa3_maiz)
        elif etapa_cultivo == '3' and tipo_cultivo == '3':
          print(etapa3_quinua)
        elif etapa_cultivo == '3' and tipo_cultivo == '4':
          print(etapa3_avena)
        elif etapa_cultivo == '4':

          opciones=input(""" Ahora, por favor ingrese la siguiente opción la cual desee obtener más información:
          1. Horario de Gestión de Cultivo
          2. Etapas del cultivo
          3. Información contable
          4. Seleccionar otro tipo de cultivo
          5. Salir
          """) # Aquí regreso al menú principal

      elif opciones =='3': # Esta condición me permite obtener el informe contable
 
        info_contable=input("""Por favor seleccionar la opción:

        El cultivo de arroz tiene un tiempo de cosecha de 5 meses. Ingresar los costos y gastos de cada mes para obtener información contable:

        1. Gastos
        2. Costos
        3. Producción
        4. Informe económico
        5. Menú principal
 
        """) #Este es un submenú 

        while True:               #Este ciclo va a evaluar las diferentes opciones en orden a medida que se va escogiendo las ocpiones (primero opción 1, opción 2..,) para el tipo de cultivo elegido en un principio.

          if info_contable == '5':
            print('Gracias por utilizar nuestra aplicación.')
            break

          else:

              if info_contable =='1':         #Esta condición me permite ingresar el valor de los gastos para los 5 meses de Cosecha

                mes1_medicamentos=int(input('''

                ***GASTOS***

                Ingresar el valor pagado por concepto de medicamentos del mes 1:'''))
                if mes1_medicamentos == 0 :
                  mes1_medicamentos=int(input('No ingresór valor. Ingresar el valor pagado por concepto de medicamentos del mes 1:'))
                  mes1_gastos_contador1= 0
                else:
                  mes1_gastos_contador1=1

                mes2_medicamentos=int(input('Ingresar el valor pagado por concepto de medicamentos del mes 2:'))
                if mes2_medicamentos == 0 :
                  mes2_medicamentos=int(input('No ingresór valor. Ingresar el valor pagado por concepto de medicamentos del mes 2:'))
                  mes2_gastos_contador1=0
                else:
                  mes2_gastos_contador1=1

                mes3_medicamentos=int(input('Ingresar el valor pagado por concepto de medicamentos del mes 3:'))
                if mes3_medicamentos == 0 :
                  mes3_medicamentos=int(input('No ingresó valor. Ingresar valor en mercado del cultivo del mes 3:'))
                  mes3_gastos_contador1= 0
                else:
                  mes3_gastos_contador1= 1

                mes4_medicamentos=int(input('Ingresar el valor pagado por concepto de medicamentos del mes 4:'))
                if mes4_medicamentos == 0:
                  mes4_medicamentos=int(input('No ingresó valor. Ingresar valor en mercado del cultivo del mes 4:'))
                  mes4_gastos_contador1= 0
                else:
                  mes4_gastos_contador1= 1

                mes5_medicamentos=int(input('Ingresar el valor pagado por concepto de medicamentos del mes 5:'))
                if mes5_medicamentos == 0:
                  mes5_medicamentos=int(input('No ingresó valor. Ingresar valor en mercado del cultivo del mes 5:'))
                  mes5_prod_contador1=0
                else:
                  mes5_prod_contador1=1

                mes1_imprevistos=int(input('Ingresar el valor pagado por concepto de imprevistos del mes 1:'))
                if mes1_imprevistos == 0:
                  mes1_imprevistos=int(input('No ingresó valor.Ingresar el valor pagado por concepto de imprevistos del mes 1:'))
                  mes1_gastos_contador2=0
                else:
                  mes1_gastos_contador2=1

                mes2_imprevistos=int(input('Ingresar el valor pagado por concepto de imprevistos del mes 2:'))
                if mes2_imprevistos == 0:
                  mes2_imprevistos=int(input('No ingresó valor.Ingresar el valor pagado por concepto de imprevistos el mes 2:'))
                  mes2_gastos_contador2=0
                else:
                  mes2_gastos_contador2=1

                mes3_imprevistos=int(input('Ingresar el valor pagado por concepto de imprevistos el mes 3:'))
                if mes3_imprevistos == 0:
                  mes3_imprevistos=int(input('No ingresó valor.Ingresar el valor pagado por concepto de imprevistos el mes 3:'))
                  mes3_gastos_contador2=0
                else:
                  mes3_gastos_contador2=1

                mes4_imprevistos=int(input('Ingresar el valor pagado por concepto de imprevistos el mes 4:'))
                if mes4_imprevistos == 0:
                  mes4_imprevistos=int(input('No ingresó valor.Ingresar el valor pagado por concepto de imprevistos el mes 4:'))
                  mes4_gastos_contador2=0
                else:
                  mes4_gastos_contador2=1

                mes5_imprevistos=int(input('Ingresar el valor pagado por concepto de imprevistos el mes 5:'))
                if mes5_imprevistos == 0:
                  mes5_imprevistos=int(input('No ingresó valor.Ingresar el valor pagado por concepto de imprevistos el mes 5:'))
                  mes5_gastos_contador2=0
                else:
                  mes5_gastos_contador2=1

                  print(''' Ahora, ingrese los GASTOS:
                  ''')

                break

              elif info_contable == '2':  #Esta condición me permite ingresar el valor de los costos fijos para los 5 meses de Cosecha

                  mes1_mano_obra=int(input('''

                  **** COSTOS FIJOS ****

                  *MANO DE OBRA

                  Ingresar costo concepto MANO DE OBRA el mes 1: '''))

                  if mes1_mano_obra != 0:
                    mes1_contador1=1
                  else:
                    mes1_contador1=0
                    mes1_mano_obra=int(input('No ingresó valor. Ingresar costo concepto MANO DE OBRA el mes 1:'))

                  mes2_mano_obra=int(input('Ingresar valor pagado a los trabajadores el mes 2:'))
                  if mes2_mano_obra != 0:
                    mes2_contador1=1
                  else:
                    mes2_contador1=0
                    mes2_mano_obra=int(input('No ingresó valor. Ingresar costo concepto MANO DE OBRA el mes 2:'))

                  mes3_mano_obra=int(input('Ingresar valor pagado a los trabajadores el mes 3:'))
                  if mes3_mano_obra != 0:
                    mes3_contador1=1
                  else:
                    mes3_contador1=0
                    mes3_mano_obra=int(input('No ingresó valor. Ingresar costo concepto MANO DE OBRA el mes 3:'))

                  mes4_mano_obra=int(input('Ingresar costo concepto MANO DE OBRA el mes 4:'))
                  if mes4_mano_obra != 0:
                    mes4_contador1=1
                  else:
                    mes4_contador1=0
                    mes4_mano_obra=int(input('No ingresó valor. Ingresar costo concepto MANO DE OBRA el mes 4:'))

                  mes5_mano_obra=int(input('Ingresar costo concepto MANO DE OBRA el mes 5:'))
                  if mes5_mano_obra != 0:
                    mes5_contador1=1
                  else:
                    mes5_contador1=0
                    mes5_mano_obra=int(input('No ingresó valor. Ingresar costo concepto MANO DE OBRA el mes 5:'))

                  mes1_agua=int(input('''

                  *AGUA

                  Ingresar costo concepto AGUA el mes 1:'''))
                  if mes1_agua != 0:
                    mes1_contador2=1
                  else:
                    mes1_contador2=0
                    mes1_agua=int(input('No ingresó valor. Ingresar costo concepto AGUA el mes 1:'))

                  mes2_agua=int(input('Ingresar costo concepto AGUA el mes 2:'))
                  if mes2_agua != 0:
                    mes2_contador2=1
                  else:
                    mes2_contador2=0
                    mes2_agua=int(input('No ingresó valor. Ingresar costo concepto AGUA el mes 2:'))

                  mes3_agua=int(input('Ingresar costo concepto AGUA el mes 3:'))
                  if mes3_agua != 0:
                    mes3_contador2=1
                  else:
                    mes3_contador2=0
                    mes3_agua=int(input('No ingresó valor. Ingresar costo concepto AGUA el mes 3:'))

                  mes4_agua=int(input('Ingresar costo concepto AGUA el mes 4:'))
                  if mes4_agua != 0:
                    mes4_contador2=1
                  else:
                    mes4_contador2=0
                    mes4_agua=int(input('No ingresó valor. Ingresar costo concepto AGUA el mes 4:'))

                  mes5_agua=int(input('Ingresar costo concepto AGUA el mes 5:'))
                  if mes5_agua != 0:
                    mes5_contador2=1
                  else:
                    mes5_contador2=0
                    mes5_agua=int(input('No ingresó valor. Ingresar costo concepto AGUA el mes 5:'))

                  mes1_mtto=int(input('''

                  *MANTENIMIENTO

                  Ingresar costo concpeto MANTENIMIENTO de los equipos, herramientas y elementos en el mes 1: '''))
                  if mes1_mtto != 0:
                    mes1_contador3=1
                  else:
                    mes1_contador3=0
                    mes1_mtto=int(input('No ingresó valor. Ingresar costo concpeto MANTENIMIENTO de los equipos, herramientas y elementos en el mes 1:'))

                  mes2_mtto=int(input('Ingresar costo concpeto MANTENIMIENTO de los equipos, herramientas y elementos en el mes 2:'))
                  if mes2_mtto != 0:
                    mes2_contador3=1
                  else:
                    mes2_contador3=0
                    mes2_mtto=int(input('No ingresó valor. Ingresar costo concpeto MANTENIMIENTO de los equipos, herramientas y elementos en el mes 2:'))

                  mes3_mtto=int(input('Ingresar costo concpeto MANTENIMIENTO de los equipos, herramientas y elementos en el mes 3:'))
                  if mes3_mtto != 0:
                    mes3_contador3=1
                  else:
                    mes3_contador3=0
                    mes3_mtto=int(input('No ingresó valor. Ingresar costo concpeto MANTENIMIENTO de los equipos, herramientas y elementos en el mes 3:'))

                  mes4_mtto=int(input('Ingresar costo concpeto MANTENIMIENTO de los equipos, herramientas y elementos en el mes 4:'))
                  if mes4_mtto != 0:
                    mes4_contador3=1
                  else:
                    mes4_contador3=0
                    mes4_mtto=int(input('No ingresó valor. Ingresar costo concpeto MANTENIMIENTO de los equipos, herramientas y elementos en el mes 1:'))

                  mes5_mtto=int(input('Ingresar costo concpeto MANTENIMIENTO de los equipos, herramientas y elementos en el mes 5:'))
                  if mes5_mtto != 0:
                    mes5_contador3=1
                  else:
                    mes5_contador3=0
                    mes5_mtto=int(input('No ingresó valor. Ingresar costo concpeto MANTENIMIENTO de los equipos, herramientas y elementos en el mes 5: '))

                  mes1_abono=int(input('''

                  *ABONO

                  Ingresar valor pagado por el abono aplicado al cultivo el mes 1: '''))
                  if mes1_abono != 0:
                    mes1_contador4=1
                  else:
                    mes1_contador4=0
                    mes1_abono=int(input('No ingresó valor. Ingresar valor pagado por el abono aplicado al cultivo el mes 1:'))

                  mes2_abono=int(input('Ingresar valor pagado por el abono aplicado al cultivo el mes 2:'))
                  if mes2_abono != 0:
                    mes2_contador4=1
                  else:
                    mes2_contador4=0
                    mes2_abono=int(input('Ingresar valor pagado por el abono aplicado al cultivo el mes 2:'))

                  mes3_abono=int(input('Ingresar valor pagado por el abono aplicado al cultivo el mes 3:'))
                  if mes3_abono != 0:
                    mes3_contador4=1
                  else:
                    mes3_contador4=0
                    mes3_abono=int(input('Ingresar valor pagado por el abono aplicado al cultivo el mes 1:'))

                  mes4_abono=int(input('Ingresar valor pagado por el abono aplicado al cultivo el mes 4:'))
                  if mes3_abono != 0:
                    mes4_contador4=1
                  else:
                    mes3_contador4=0
                    mes3_abono=int(input('Ingresar valor pagado por el abono aplicado al cultivo el mes 4:'))

                  mes5_abono=int(input('Ingresar valor pagado por el abono aplicado al cultivo el mes 5:'))
                  if mes5_abono != 0:
                    mes5_contador4=1
                  else:
                    mes5_contador4=0
                    mes5_abono=int(input('Ingresar valor pagado por el abono aplicado al cultivo el mes 5:'))
                    print('''
                    Ahora, ingrese la PRODUCCIÓN:
                    ''')

                  break

              elif info_contable == '3':  #Esta condición me permite ingresar los valores de producción para los 5 meses de Cosecha

                    mes1_valor_cultivo=int(input('''

                    **** PRODUCCIÓN ****

                    Ingresar valor en mercado del cultivo el mes 1: '''))
                    if mes1_valor_cultivo == 0:
                      mes1_valor_cultivo=int(input('No ingresó valor. Ingresar valor en mercado del cultivo el mes 1:'))
                      mes1_prod_contador1=0
                    else:
                      mes1_prod_contador1=1

                    mes2_valor_cultivo=int(input('Ingresar valor en mercado del cultivo el mes 2:'))
                    if mes2_valor_cultivo == 0:
                      mes2_valor_cultivo=int(input('No ingresó valor. Ingresar valor en mercado del cultivo el mes 2:'))
                      mes2_prod_contador1=0
                    else:
                      mes2_prod_contador1=1

                    mes3_valor_cultivo=int(input('Ingresar valor en mercado del cultivo el mes 3:'))
                    if mes3_valor_cultivo == 0:
                        mes3_valor_cultivo=int(input('No ingresó valor. Ingresar valor en mercado del cultivo el mes 3:'))
                        mes3_prod_contador1=0
                    else:
                        mes3_prod_contador1=1

                    mes4_valor_cultivo=int(input('Ingresar valor en mercado del cultivo el mes 4:'))
                    if mes4_valor_cultivo == 0:
                      mes4_valor_cultivo=int(input('No ingresó valor. Ingresar valor en mercado del cultivo el mes 4:'))
                      mes4_prod_contador1=0
                    else:
                      mes4_prod_contador1=1

                    mes5_valor_cultivo=int(input('Ingresar valor en mercado del cultivo el mes 5:'))
                    if mes5_valor_cultivo == 0:
                      mes5_valor_cultivo=int(input('No ingresó valor. Ingresar valor en mercado del cultivo el mes 5:'))
                      mes5_prod_contador1=0
                    else:
                      mes5_prod_contador1=1

                    mes1_cantidad=int(input('Ingresar cantidad recogida el mes 1:'))
                    if mes1_cantidad == 0:
                      mes1_cantidad=int(input('No ingresó valor. Ingresar cantidad recogida el mes 1:'))
                      mes1_prod_contador2=0
                    else:
                      mes1_prod_contador2=1

                    mes2_cantidad=int(input('Ingresar cantidad recogida el mes 2:'))
                    if mes2_cantidad == 0:
                      mes2_cantidad=int(input('No ingresó valor. Ingresar cantidad recogida el mes 2:'))
                      mes2_prod_contador2=0
                    else:
                      mes2_prod_contador2=1

                    mes3_cantidad=int(input('Ingresar cantidad recogida el mes 3:'))
                    if mes3_cantidad == 0:
                      mes3_cantidad=int(input('No ingresó valor. Ingresar cantidad recogida el mes 3:'))
                      mes3_prod_contador2=0
                    else:
                      mes3_prod_contador2=1

                    mes4_cantidad=int(input('Ingresar cantidad recogida el mes 4:'))
                    if mes4_cantidad == 0:
                      mes4_cantidad=int(input('No ingresó valor. Ingresar cantidad recogida el mes 4:'))
                      mes4_prod_contador2=0
                    else:
                      mes4_prod_contador2=1

                    mes5_cantidad=int(input('Ingresar cantidad recogida el mes 5:'))
                    if mes5_cantidad == 0:
                      mes5_cantidad=int(input('No ingresó valor. Ingresar cantidad recogida el mes 5:'))
                      mes5_prod_contador2=0
                    else:
                      mes5_prod_contador2=1
                      break


              elif info_contable == '4': #Esta condición me permite imprimir la información que se va a visualizar en el informe contable

              #Cálculos costos totales cultivo mes
                mes1_total_costos= mes1_mano_obra + mes1_agua + mes1_mtto + mes1_abono
                mes2_total_costos= mes2_mano_obra + mes2_agua + mes2_mtto + mes1_abono
                mes3_total_costos= mes3_mano_obra + mes3_agua + mes3_mtto + mes1_abono
                mes4_total_costos= mes4_mano_obra + mes4_agua + mes4_mtto + mes1_abono
                mes5_total_costos= mes5_mano_obra + mes5_agua + mes5_mtto + mes1_abono

              #Cálculos gastos totales cultivo mes
                mes1_total_gastos= mes1_medicamentos + mes1_imprevistos
                mes2_total_gastos= mes2_medicamentos + mes2_imprevistos
                mes3_total_gastos= mes3_medicamentos + mes3_imprevistos
                mes4_total_gastos= mes4_medicamentos + mes4_imprevistos
                mes5_total_gastos= mes5_medicamentos + mes5_imprevistos

              #Cálculos valor producción totales cultivo mes
                mes1_total_prod= mes1_valor_cultivo * mes1_cantidad
                mes2_total_prod= mes2_valor_cultivo * mes2_cantidad
                mes3_total_prod= mes3_valor_cultivo * mes3_cantidad
                mes4_total_prod= mes4_valor_cultivo * mes4_cantidad
                mes5_total_prod= mes5_valor_cultivo * mes5_cantidad

              #Contadores gastos para sacar promedio
                mes1_gastos_contadores= mes1_gastos_contador1 + mes1_gastos_contador2
                mes2_gastos_contadores= mes1_gastos_contador1 + mes2_gastos_contador2
                mes3_gastos_contadores= mes1_gastos_contador1 + mes3_gastos_contador2
                mes4_gastos_contadores= mes1_gastos_contador1 + mes4_gastos_contador2
                mes5_gastos_contadores= mes1_gastos_contador1 + mes5_gastos_contador2

              #Contadores costos para sacar promedio
                mes1_costos_contadores= mes1_contador1 + mes1_contador2 + mes1_contador3 + mes1_contador4
                mes2_costos_contadores= mes2_contador1 + mes2_contador2 + mes2_contador3 + mes2_contador4
                mes3_costos_contadores= mes3_contador1 + mes3_contador2 + mes3_contador3 + mes3_contador4
                mes4_costos_contadores= mes4_contador1 + mes4_contador2 + mes4_contador3 + mes4_contador4
                mes5_costos_contadores= mes5_contador1 + mes5_contador2 + mes5_contador3 + mes5_contador4

              #Costos promedios/mes
                mes1_costos_prom =  mes1_total_costos/mes1_costos_contadores
                mes2_costos_prom =  mes2_total_costos/mes2_costos_contadores
                mes3_costos_prom =  mes3_total_costos/mes3_costos_contadores
                mes4_costos_prom =  mes4_total_costos/mes4_costos_contadores
                mes5_costos_prom =  mes5_total_costos/mes5_costos_contadores

              #Gastos promedios/mes
                mes1_promedio_fijos= mes1_total_gastos/mes1_gastos_contadores
                mes2_promedio_fijos= mes2_total_gastos/mes2_gastos_contadores
                mes3_promedio_fijos= mes3_total_gastos/mes3_gastos_contadores
                mes4_promedio_fijos= mes4_total_gastos/mes4_gastos_contadores
                mes5_promedio_fijos= mes5_total_gastos/mes5_gastos_contadores

             #Punto a - Información contable

                print ('''

                *** INFORME CONTABLE***

                ''')

                print ('''

                a. Costos totales por mes:

                ''')


                print(' Los costos totales del mes 1 son' , mes1_total_costos)
                print(' Los costos totales del mes 2 son' , mes2_total_costos)
                print(' Los costos totales del mes 3 son' , mes3_total_costos)
                print(' Los costos totales del mes 4 son' , mes4_total_costos)
                print(' Los costos totales del mes 5 son' , mes5_total_costos)

              #Punto b - Costos totales mano de obra

                costo_total_mo= mes1_mano_obra + mes2_mano_obra + mes3_mano_obra + mes4_mano_obra + mes5_mano_obra


                print ('''

                b. Costos Mano de Obra:

                ''')
                print(' Los costos totales de la Mano de Obra son: ' , costo_total_mo)

              #Punto c - Calculos no gastos

                print ('''

                c. Gastos:

                ''')

                if mes1_total_gastos == 0:
                  print('En el mes 1 no hubo gastos')
                
                if mes2_total_gastos == 0:
                  print('En el mes 2 no hubo gastos')

                if mes3_total_gastos == 0:
                  print('En el mes 3 no hubo gastos')

                if mes4_total_gastos == 0:
                  print('En el mes 4 no hubo gastos')

                if mes5_total_gastos == 0:
                  print('En el mes 5 no hubo gastos')


              #Punto d - Gastos < 100.000

                print('''

                d. Gastos < 100.000

                ''')
                

                if mes1_total_gastos < 100000:
                  print('En el mes 1 los gastos no superaron los $100.000')

                if mes2_total_gastos < 100000:
                  print('En el mes 2 los gastos no superaron los $100.000')

                if mes3_total_gastos < 100000:
                  print('En el mes 3 los gastos no superaron los $100.000')

                if mes4_total_gastos < 100000:
                  print('En el mes 4 los gastos no superaron los $100.000')

                if mes5_total_gastos < 100000:
                  print('En el mes 5 los gastos no superaron los $100.000')

              #Punto e.	Meses en los cuales el costo total del mes fue mayor al gasto total del mes

                print('''

                e. Meses en los cuales el costo total del mes fue mayor al gasto total del mes

                ''')

                if mes1_total_costos > mes1_total_gastos
                  print('En el mes 1 el costo total fue mayor al gasto total')

                if mes2_total_costos > mes2_total_gastos
                  print('En el mes 2 el costo total fue mayor al gasto total')

                if mes3_total_costos > mes3_total_gastos
                  print('En el mes 3 el costo total fue mayor al gasto total')

                if mes4_total_costos > mes4_total_gastos
                  print('En el mes 4 el costo total fue mayor al gasto total')

                if mes5_total_costos > mes5_total_gastos
                  print('En el mes 5 el costo total fue mayor al gasto total')
                          
              #Punto f.	Muestre el valor promedio de costos Fijos y costos variables.


                print('''

                e. Meses en los cuales el costo total del mes fue mayor al gasto total del mes

                ''')
                  
                total_costos_fijos= mes1_total_costos + mes2_total_costos + mes3_total_costos + mes4_total_costos + mes5_total_costos
                total_gastos= mes1_total_gastos + mes2_total_gastos + mes3_total_gastos + mes4_total_gastos + mes5_total_gastos

                prom_costos_fijos= (prom_costos_fijos)/5
                prom_gastos= (total_gastos)/5
                print('El promedio de los costos fijos es: ', prom_costos_fijos)
                print('El promedio de los gastos es: ', prom_gastos) 

            # Punto g.	¿Hubo ganancia?  SI o NO.  Si hubo ¿cuánto dinero fue la ganancia? (dinero que queda después de sacar los costos totales y gastos totales del dinero recibido por la venta de la cosecha)

                print('''

                g. Ganancias

                ''')

                total_prod=  mes1_total_prod +  mes2_total_prod +  mes3_total_prod +  mes4_total_prod +  mes5_total_prod
                ganancia = total_prod - total_costos_fijos - total_gastos 

                if ganancia <=0:
                  print('Esta cosecha no tubo ganancia')
                  
                else:
                  print('Esta cosecha tubo ganancia y fue de: $', ganancia)
    
            # h.	Si el precio del kilo de arroz se incrementa en un 37% de su valor actual.  ¿Cuál sería la ganancia obtenida?

                print('''

                h. Ganancias si el valor del cultivo se incrementa en un 37% de su valor actual.

                ''')


                total_prod_incremento= (total_prod * 1.37)
                ganancia_incremento = total_prod_incremento - total_costos_fijos - total_gastos

                if ganancia <=0:
                  print('Esta cosecha no tubo ganancia con el incremento del 37% en el precio de venta.')
                  
                else:
                  print('Con un aumento en el precio de venta del 37% la ganancia fue de: $', ganancia_incremento)


            # i.	Si los costos y gastos se disminuyen en un 5% y la cantidad de arrobas producidas en un 63%, ¿cuál seria  la ganancia?
          
                  print('''

                  i. Ganancias si la cantidad producida disminuye un 63% y el total de costos y gastos un 5%.

                  ''')
                  
                  total_prod_dismin=((-total_prod * 0.63) + total_prod)
                  total_costos_fijos_dism=((-total_costos_fijos * 0.05) + total_costos_fijos)
                  total_gastos_dism=((-total_gastos * 0.05) + total_gastos)

                  ganancia_disminucion= total_prod_dismin - total_costos_fijos - total_gastos_dism
                  
                  print ('Si tuvieramos una disminucion del 63% en la cantidad producida y del 5% en el total de costos y gastos: ') 

                  if ganancia_disminucion <= 0:
                    print('No hubo ganancia') 

                  else:
                    print('La ganancia sería de: $', ganancia_disminucion)

                break

      elif opciones =='4': #Esta condición me permite ingresar otro tipo de cultivo (Funciona como menú principal)

          tipo_cultivo=input("""Por favor ingrese el nombre del tipo de cultivo:

          1. Arroz
          2. Maiz
          3. Quinua
          4. Avena
          5. Salir
          """)

      else:
        print('')