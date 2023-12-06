# Clase para definir un cultivo
class Cultivo():
  def __init__(self, id, nombre, dias_horarios_mantenimiento, dias_horarios_regado, dias_horarios_abono, etapa, costo_mano_obra = 0, costo_abono = 0, costo_agua = 0, costo_mantenimiento = 0, valor_arroba = 0, cantidad_K_recolectados = 0):
    self.id = id
    self.nombre = nombre
    self.dias_horarios_mantenimiento = dias_horarios_mantenimiento
    self.dias_horarios_regado = dias_horarios_regado
    self.dias_horarios_abono = dias_horarios_abono
    self.etapa = etapa
    self.costo_mano_obra = costo_mano_obra
    self.costo_abono = costo_abono
    self.costo_agua = costo_agua
    self.costo_mantenimiento = costo_mantenimiento
    self.valor_arroba = valor_arroba
    self.cantidad_K_recolectados = cantidad_K_recolectados
# Creacion de cultivos
cultivo_papa = Cultivo("1", "Papa", "Lunes y jueves de 3:00pm a 4:00pm", "Miercoles y viernes de 3:00am a 4:00am", "Sabado de 10:00am a 11:00am","Siembra")
cultivo_tomate = Cultivo("2", "Tomate", "Lunes y jueves de 5:00pm a 7:00pm", "Miercoles y viernes de 6:00am a 10:00am", "Sabado de 12:00am a 05:00am","Cosecha")
cultivo_arroz = Cultivo("3", "Arroz", "Martes y Viernes de 5:00pm a 7:00pm", "Lunes y Martes de 6:00am a 10:00am", "Domingo de 12:00am a 05:00am","Crecimiento")
cultivo_fresa = Cultivo("4", "Fresa", "Martes y Viernes de 5:00pm a 7:00pm", "Lunes y Martes de 6:00am a 10:00am", "Domingo de 12:00am a 05:00am","Crecimiento")

# Lista con los diferentes cultivos
lista_cultivos = [cultivo_papa, cultivo_tomate, cultivo_arroz, cultivo_fresa]

# Lista con las etapas del Cultivo
lista_etapas = ["Siembra", "Crecimiento", "Cosecha"]

# Mientras la bandera sea true el flujo principal se ejecutara
bandera_principal = True
# Este metodo mostrara el menu principal, capturara la informacion ingresada por el usuario y la retornara
def mostrar_menu_principal():
  print (f"---------------------------------------------- \n"
         f"Hola, ¡Bienvenido a HuertaSoftware! somos su aliado en Gestión de Cultivos. ¿Qué quieres hacer hoy? Elija una de las siguientes opciones: \n"
                  "1. Horarios de Gestión de Cultivo \n"
                  "2. Etapas del Cultivo \n"
                  "3. Información Contable \n"
                  "4. Salir")
  return input("")
# Este metodo mostrara la lista de cultivos y capturara la informacion ingresada por el usuario y la retornara
def mostrar_lista_cultivos():
  print ("Elija un cultivo:")
  for cultivo in lista_cultivos:
    print (f"{cultivo.id}. {cultivo.nombre}")
  return input("")

# Este metodo mostrara los dias y horarios de un cultivo
def mostrar_dias_horarios(cultivo_id):
  for cultivo in lista_cultivos:
    if cultivo.id == cultivo_id:
      print (f"El cultivo {cultivo.nombre} tiene los siguientes dias y horarios: \n"
            f"Mantenimiento: {cultivo.dias_horarios_mantenimiento} \n"
            f"Regado: {cultivo.dias_horarios_regado} \n"
            f"Abono: {cultivo.dias_horarios_abono}")

# Este método mostrará las posibles etapas para un cultivo
def mostrar_etapas_cultivo():
  print(f"Elija una etapa de cultivo para consultar:")
  numero_iteracion = 1
  for etapa in lista_etapas:
    print(f"{numero_iteracion}. {etapa}")
    numero_iteracion = numero_iteracion + 1
  etapa_elegida = int(input(""))
  return lista_etapas[etapa_elegida - 1]

# Este método mostrará el cultivo que se encuentra en la etapa seleccionada
def mostrar_cultivo_etapa(etapa):
  for cultivo in lista_cultivos:
    if etapa == cultivo.etapa:
      print(f"El cultivo {cultivo.nombre} se encuentra en la etapa {cultivo.etapa}")

# Este método mostrará la información contable que debe ingresar el usuario únicamente para el cultivo de arroz
def mostrar_informacion_contable(cultivo_id):
  for cultivo in lista_cultivos:
    if "arroz" in cultivo.nombre.lower() and cultivo_id == cultivo.id:
      print("Ingrese la siguiente información: \n")
      cultivo.costo_mano_obra = int(input("ingrese el costo de la Mano de Obra: "))
      cultivo.costo_abono = int(input("ingrese el costo del Abono: "))
      cultivo.costo_agua = int(input("ingrese el costo del Agua: "))
      cultivo.costo_mantenimiento = int(input("ingrese el costo del Mantenimiento: "))
      cultivo.valor_arroba = int(input("ingrese el valor del Arroba: "))
      cultivo.cantidad_K_recolectados = int(input("ingrese la cantidad de Kilos Recolectados: "))

      # Informe económico
      costos_totales = cultivo.costo_mano_obra + cultivo.costo_abono + cultivo.costo_agua + cultivo.costo_mantenimiento
      lista_costos_fijos = [cultivo.costo_mano_obra, cultivo.costo_abono, cultivo.costo_agua, cultivo.costo_mantenimiento]
      promedio_costos_fijos = sum(lista_costos_fijos)/len(lista_costos_fijos)
      cantidad_arrobas_recolectadas = cultivo.cantidad_K_recolectados / 12.5
      valor_total_arrobas_recolectadas = cantidad_arrobas_recolectadas * cultivo.valor_arroba
      ganancia = valor_total_arrobas_recolectadas - costos_totales
      incremento_valor_arroba = valor_total_arrobas_recolectadas * 1.37
      costos_reducidos = costos_totales - (costos_totales*0.05)
      cantidad_arrobas_reducidas = cantidad_arrobas_recolectadas - (cantidad_arrobas_recolectadas*0.63)
      valor_cantidad_reducida = cantidad_arrobas_reducidas * cultivo.valor_arroba
      ganancia_reducida = valor_cantidad_reducida - costos_reducidos 


      print(f"Sus costos totales son de {costos_totales}")
      print(f"Su promedio de costos fijos es de {promedio_costos_fijos}")
      # Esta función permite identificar si hubo o no ganancia. Numeral c
      if ganancia > 0:
        print(f"¡felicidades! Se está haciendo millonario. Su ganancia es de {ganancia}")
      else:
        print(f"Lo siento. En el momento no hay ganancia. Su balance final es de {ganancia}")
      
       # Esta función muestra el incremento del arroz en un 37%. Numeral d
      print(f"Suponiendo que el valor del kilo del arroz incrementa un 37%, su balance final sería de {incremento_valor_arroba}")

       # Si los costos y gastos se disminuyen en un 5% y la cantidad de arrobas producidas en un 63%
      print(f"Suponiendo que los costos y gastos se disminuyen en un 5% y la cantidad de arrobas producidas en un 63%. Sus costos serían de {costos_reducidos} y su cantidad sería {cantidad_arrobas_reducidas} con un balance final de {ganancia_reducida}")
    




    elif cultivo_id == cultivo.id:
      print(f"No hay información disponible del cultivo {cultivo.nombre}")


# Flujo principal de la aplicacion
while bandera_principal:
  entrada_usuario = mostrar_menu_principal()
# Flujo para entrada "Horarios de Gestión de Cultivo"
  if entrada_usuario == "1":
    cultivo_elegido = mostrar_lista_cultivos()
    mostrar_dias_horarios(cultivo_elegido)
# Flujo para entrada "Etapas del Cultivo"
  elif entrada_usuario == "2":
    etapa_elegida = mostrar_etapas_cultivo()
    mostrar_cultivo_etapa(etapa_elegida)
# Flujo para entrada "Información Contable"
  elif entrada_usuario == "3":
    cultivo_elegido = mostrar_lista_cultivos()
    mostrar_informacion_contable(cultivo_elegido)
  elif entrada_usuario == "4":
    print ("El usuario ha salido del sistema")
    bandera_principal = False