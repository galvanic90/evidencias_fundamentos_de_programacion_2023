#Reto_3

#Integrantes:
#Deissy_Cancino_Joya
#CC.1098730569
#Correo: deissycancino@gmail.com

#Bairon_Gomez_Peñuela
#CC.1007961775
#Correo:znoriab@gmail.com

#PRIMER PUNTO DEL RETO
#Opciones numeradas (1. Horario de gestion / 2. Etapas del cultivo / 3. Información Contable / 4. Salir)
#Horario de gestión de cultivo - opciones de cultivo y recibir opción (imprimir días y horarios de mantenimiento, regado y abono)
#Etapas del cultivo - imprimir opciones de cultivo numerados (imprimir etapas del cultivo) vegetativa reproductiva y maduración
#Info contable - parte 2 del reto
#Salir - break

#SEGUNDO PUNTO DEL RETO
#cultivo de arroz (siembra y recolección 5 meses)
#Ingresa el usuario los costos variables (medicamentos e imprevistos), costos fijos (mano de obra, abono, agua y mantenimiento) y el precio actual de la arroba de arroz y la cantidad de kg recolectados.
#Debemos definir el ingreso de las variables mes a mes (meses fijos), definir funcion para hacer un ciclo mensual.
#Definir el informe económico con:
 #a. Costos totales del cultivo por mes (sumar el input de cada mes para los costos totales)
 #b. Costos totales de mano de obra (sumar el input de todos los meses de los costos de mdo)
 #c. Meses en los cuales no hubo gastos (un if dentro de un bucle, si el input del mes = "" or 0, mostrar el mes)
 #d. Meses en los cuales el gasto fue menor a 100.000 (otro if en un bucle, si gasto>100.000, no mostrar el mes)
 #e. Meses en los cuales el costo total del mes fue mayor al gasto total del mes. (un if que evalúe ambos input)
 #f. Muestre el valor promedio de costos Fijos y costos variables. (definir una función de promedio)
 #g. ¿Hubo ganancia? SI o NO. Si hubo ¿cuánto dinero fue la ganancia? ((ingresos - (gastos + costos))
 #h. Si el precio del kilo de arroz se incrementa en un 37% de su valor actual. ¿Cuál sería la ganancia obtenida?
 #i. Costos y gastos se disminuyen 5% y la cantidad de arrobas producidas 63%, ¿cuál seria la ganancia?

#Definidas las funciones (RETO 2)
def informacion_contable():
    meses = int(input("¿Cuántos meses se demoró su cultivo?: "))
    meses = (meses + 1)
    def entrada(valor_entrada):
      valor_entrada = valor_entrada
      if (valor_entrada==""):
        valor_entrada = float(0)
      else:
        valor_entrada = float(valor_entrada)
      return valor_entrada
    def ingreso_gastos_mes(mes):
      med = input(f"Ingrese los gastos en medicamentos para el mes {mes}: ")
      med = entrada (med)
      imp = input(f"Ingrese los gastos en imprevistos para el mes {mes}: ")
      imp = entrada(imp)
      return med, imp

    def ingreso_costos_mes(mes):
      mdo = input(f"Ingrese los costos de mano de obra para el mes {mes}: ")
      mdo = entrada (mdo)
      abono = input(f"Ingrese los costos de abono para el mes {mes}: ")
      abono = entrada(abono)
      agua = input(f"Ingrese los costos de agua para el mes {mes}: ")
      agua = entrada(agua)
      mant = input(f"Ingrese los costos de mantenimiento para el mes {mes}: ")
      mant = entrada (mant)
      return mdo, abono, agua, mant

    def calcular_gastos_totales(gastos_totales):
      return sum(gastos_totales)

    def calcular_costos_totales(costos_totales):
      return sum(costos_totales)
    def calcular_promedio(costos_totales):
      return sum(costos_totales) / len(costos_totales)

    def ganancia(p_arroba, q_kilos, gastos_totales, costos_totales):
      ingresos = (p_arroba / 12.50) * q_kilos
      ganancia = ingresos - (gastos_totales + costos_totales)
      return ganancia

    def ganancia_aumentoprecio(p_arroba, q_kilos, p_aumento, gastos_totales, costos_totales):
      ingresos = ((p_arroba / 12.50) * (1 + p_aumento)) * q_kilos
      ganancia_nueva = ingresos - (gastos_totales + costos_totales)
      return ganancia_nueva

    def ganancia_dismgastos(p_arroba, q_kilos, p_dis, p_dis_arrobas, gastos_totales, costos_totales):
      ingresos = (p_arroba) * ((q_kilos/12.50) * (1 - p_dis_arrobas))
      ganancia_nueva2 = ingresos - ((gastos_totales * (1 - p_dis)) + (costos_totales * (1 - p_dis)))
      return ganancia_nueva2

    gastos_totales = [] #se hace una lista de todos los gastos
    costos_totales = [] #se hace una lista de todos los costos
    costos_mdo_total = [] #se hace una lista de todos los costos de mdobra

    for mes in range(1, meses): #el mes 1 es la posición 0
        med, imp = ingreso_gastos_mes(mes)
        mdo, abono, agua, mant = ingreso_costos_mes(mes)

        gastos_mes_total = med + imp
        costos_mes_total = mdo + abono + agua + mant

        costos_mdo_total.append(mdo) #se suma todos los mdo de todos los meses en la lista.
        gastos_totales.append(gastos_mes_total) #con la suma anterior de med e imp, suma todos los meses en la lista.
        costos_totales.append(costos_mes_total) #con la suma anterior de mod + abono + agua + mant, suma todos los meses en la lista.

    p_arroba = float(input("Ingrese el valor de la arroba (12.5kg) de arroz hoy: "))
    q_kilos = float(input("Ingrese la cantidad de kilos recolectados: "))
    print("""
------------ Informe Económico ------------

Gastos y costos mensuales:""")
    for mes in range(1, meses):
        print("Mes",mes,": ")
        print("Gastos Totales: $",(gastos_totales[mes - 1])) #Como el mes 1 es la posición 0, debemos restarle 1 para que encuentre la posición correcta
        print("Costos Totales: $",(costos_totales[mes - 1])) #Como el mes 1 es la posición 0, debemos restarle 1 para que encuentre la posición correcta
    print("""
--- Suma de Costos de Mano de Obra:""", sum(costos_mdo_total))

    print("""
--- Meses sin gastos:""")
    for mes in range(1, meses):
        if gastos_totales[mes - 1] == 0:
            print(f"Mes {mes}")

    print("""
--- Meses con gasto menor a $100.000:""")
    for mes in range(1, meses):
        if gastos_totales[mes - 1] < 100000:
            print(f"Mes {mes}")

    print("""
---Meses en los que el costo total fue mayor al gasto total:""")
    for mes in range(1, meses):
        if costos_totales[mes - 1] > gastos_totales[mes - 1]:
            print(f"Mes {mes}")

    print("""
--- Promedio de Costos Fijos:""", round(calcular_promedio(costos_totales),2))
    print("""
--- Promedio de Costos Variables:""", round(calcular_promedio(gastos_totales),2))

    ganancia_total = round((ganancia(p_arroba, q_kilos, sum(gastos_totales), sum(costos_totales))),2)
    if ganancia_total > 0:
        print("""
--- Hubo ganancia: Sí""")
        print(f"""
- Ganancia total: ${ganancia_total}""")
    else:
        print("""
--- Hubo ganancia: No""")
        print(f"""
- Pérdida total: ${ganancia_total}""")

    p_aumento = 0.37
    num_aumento = int(p_aumento*100)
    ganancia_aumentada = round(ganancia_aumentoprecio(p_arroba, q_kilos, p_aumento, sum(gastos_totales), sum(costos_totales)),2)
    print(f"""
--- Ganancia con aumento del precio del kilo de arroz en {num_aumento}%: ${ganancia_aumentada}""")

    p_dis = 0.05
    num_dis = int(p_dis*100)
    p_dis_arrobas = 0.63
    num_dis_arrobas = int(p_dis_arrobas*100)
    ganancia_disminuida = round(ganancia_dismgastos(p_arroba, q_kilos, p_dis, p_dis_arrobas, sum(gastos_totales), sum(costos_totales)),2)
    print(f"""
--- Ganancia con disminución de gastos y costos en {num_dis}% y disminución en producción de {num_dis_arrobas}% de arrobas: ${ganancia_disminuida}""")

#Ejecuta el menú principal en bucle, solo se sale con la opción "4. Salir"
while True:
  #Menú Principal
  print("""
--- Menú Principal.
        Consultas sobre el cultivo:
        1. Horario de gestión de cultivo
        2. Etapas del cultivo
        3. Información contable
        4. Salir""")
  accion=input()
  #SubMenú Horario de gestión
  if(accion=="1"): #se realiza con condicional debido a las opciones en el input y al nuevo menú (condicional anidado)
    print("""
  --- Menú Horario de gestión de cultivo.
          Seleccione el cultivo:
          1. Arroz
          2. Tomate
          3. Cebolla""")
    accion2=input()
  #Impresión de las opciones de gestión
   #Abriremos un condicional de acuerdo a lo que se seleccione en el menú de horario (es un condicional dentro de otro condicional)
    if(accion2=="1"): #Gestión del arroz
      print("""
Seleccionaste gestión del cultivo de arroz:
Mantenimiento: Lunes, miércoles y Viernes a las 4:00 pm.
Regado: Lunes, miércoles y viernes 4:00pm los primeros 15 días. Después, inundar todos los días a las 4:00pm.
Abono: La primera vez con la siembra, 15 días después de la siembra y luego cada 45 días.
""")
    elif(accion2=="2"): #Gestión del tomate
      print("""
Seleccionaste gestión del cultivo de tomate:
Mantenimiento: Entutorado y poda los martes y jueves a las 5:00 pm.
Regado: Lunes, miércoles y viernes 5:00pm.
Abono: Cada 15 días, en la etapa de maduración, todos los lunes a las 4:00pm.
""")
    elif(accion2=="3"): #Gestión de la cebolla
      print("""
Seleccionaste gestión del cultivo de cebolla:
Mantenimiento: Miércoles y Viernes 5:00 pm, utilizar la maleza como acolchado.
Regado: Martes y jueves 5:00pm.
Abono: La primera vez con la siembra, depsués cada 20 días.
""")
    else:#Si se selecciona un valor diferente muestra que la opción es incorrecta
      print("Opción incorrecta")

 #SubMenú Etapas del cultivo
  elif(accion=="2"): #Este es el elif del primer condicional.
    print("""
 --- Menú etapas del cultivo.
          Seleccione el cultivo:
          1. Arroz
          2. Tomate
          3. Cebolla""")
    accion3=input()
    #Impresión de las etapas del cultivo, se realiza con condicional debido a las opciones en el input, condicional dentro de otro condicional.
    if(accion3=="1"): #Etapas del arroz
      print("""
Seleccionaste etapas del arroz:
Etapa 1 - Fase vegetativa: De 50 a 60 días.
Etapa 2 - Fase reproductiva: De 30 a 40 días.
Etapa 3 - Fase de maduración: De 40 a 50 días.
Tiempo total: Entre 120 y 150 días.
""")
    elif(accion3=="2"): #Etapas del tomate
      print("""
Seleccionaste tapas del tomate:
Etapa 1 - Fase inicial: De 25 a 30 días.
Etapa 2 - Fase vegetativa: De 25 a 30 días.
Etapa 3 - Fase reproductiva: De 40 a 50 días.
Etapa 4 - Fase de maduración: De 30 a 50 días.
Tiempo total: Entre 120 y 150 días
""")
    elif(accion3=="3"): #Etapas de la cebolla
      print("""
Seleccionaste etapas de la cebolla:
Etapa 1 - Establecimiento: De 25 a 30 días.
Etapa 2 - Fase vegetativa: De 25 a 30 días.
Etapa 3 - Iniciación de bulbo: De 25 a 30 días.
Etapa 4 - Desarrollo de bulbo: De 40 a 45 días.
Etapa 5 - Maduración: De 10 a 15 días.
Tiempo total: Entre 125 y 160 días
""")
    else: #Si se selecciona un valor diferente muestra que la opción es incorrecta
      print("Opción incorrecta")

  elif(accion=="3"): #Ingresa al menú de contabilidad
    print("""
  ***Esta información será solamente calculada para el cultivo de arroz:""")
    informacion_contable() #Llama la función definida para información contable
  elif(accion=="4"): #Si se selecciona esta opción del menú principal, se sale del programa (break en un bucle)
    break
  else:
    print("Ingrese acción valida")