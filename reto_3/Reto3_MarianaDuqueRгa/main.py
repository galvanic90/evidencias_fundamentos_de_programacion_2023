mensaje_bienvenida = '''
BIENVENIDO A CULTI-SOFT
---------------------------
El software de información contable para agricultores
'''

seleccion = 'Seleccione una de estas opciones'

menu_principal = '''
1- DATOS DEL CULTIVO
2- HORARIO Y GESTIÓN DEL CULTIVO
3- ETAPAS DEL CULTIVO
4- INFORMACIÓN CONTABLE
5- SALIR
'''

menu_horario_gestion_cultivo = '''
A- DÍAS Y HORARIOS DE CULTIVO
B- DÍAS Y HORARIOS DE ABONO
C- DÍAS Y HORARIOS DE RIEGO
D- IR AL MENÚ PRINCIPAL
'''

menu_etapas_cultivo = '''
1- SIEMBRA
2- CRECIMIENTO
3- COSECHA
'''

menu_informacion_contable = '''
A- COSTOS
B- PRODUCCIÓN
'''

submenu_costos = '''
1- MANO DE OBRA
2- AGUA
3- MANTENIMIENTO
4- ABONO
5- IR ATRÁS
'''

submenu_produccion = '''
A- VALOR EN MERCADO DEL CULTIVO
B- CANTIDAD RECOGIDA
C- IR ATRÁS
'''

# Variables para almacenar datos del cultivo y costos
datos_cultivo = {
    "Nombre del Cultivo": "",
    "Días y Horarios de Cultivo": "",
    "Días y Horarios de Abono": "",
    "Días y Horarios de Riego": "",
}

costos = {
    "Mano de Obra": 0.0,
    "Agua": 0.0,
    "Mantenimiento": 0.0,
    "Abono": 0.0,
}

# Función para mostrar el menú principal
def mostrar_menu_principal():
    print(mensaje_bienvenida)
    cerrar = False

    while not cerrar:
        print(seleccion)
        opcion_menu_principal = input(menu_principal)

        if opcion_menu_principal == '1':
            regresar = mostrar_menu_datos_cultivo()
            if regresar:
                continue
        elif opcion_menu_principal == '2':
            regresar = mostrar_menu_horario_gestion_cultivo()
            if regresar:
                continue
        elif opcion_menu_principal == '3':
            mostrar_menu_etapas_cultivo()
        elif opcion_menu_principal == '4':
            regresar = mostrar_menu_informacion_contable()
            if regresar:
                continue
        elif opcion_menu_principal == '5':
            print("Gracias por usar Culti-Soft. ¡Hasta luego!")
            cerrar = True

# Función para preguntar si desea volver al menú principal
def preguntar_regresar():
    respuesta = input('¿Desea volver al menú principal? (S/N): ')
    return respuesta.upper() == 'S'

# Función para mostrar el menú de datos del cultivo
def mostrar_menu_datos_cultivo():
    global regresar
    datos_cultivo['Nombre del Cultivo'] = input('Ingrese el nombre del cultivo: ')
    regresar = preguntar_regresar()
    return regresar

# Función para mostrar el menú de horario y gestión del cultivo
def mostrar_menu_horario_gestion_cultivo():
    global regresar
    print(seleccion)
    opcion_horario = input(menu_horario_gestion_cultivo)
    if opcion_horario == 'A':
        datos_cultivo["Días y Horarios de Cultivo"] = input('Ingrese los días y horarios de cultivo: ')
        mostrar_menu_horario_gestion_cultivo()
    elif opcion_horario == 'B':
        datos_cultivo["Días y Horarios de Abono"] = input('Ingrese los días y horarios de abono: ')
        mostrar_menu_horario_gestion_cultivo()
    elif opcion_horario == 'C':
        datos_cultivo["Días y Horarios de Riego"] = input('Ingrese los días y horarios de riego: ')
       
        # Imprimir las respuestas
        print(f'Nombre del cultivo: {datos_cultivo["Nombre del Cultivo"]}')
        print(f'Días y Horarios de Cultivo: {datos_cultivo["Días y Horarios de Cultivo"]}')
        print(f'Días y Horarios de Abono: {datos_cultivo["Días y Horarios de Abono"]}')
        print(f'Días y Horarios de Riego: {datos_cultivo["Días y Horarios de Riego"]}')
        mostrar_menu_horario_gestion_cultivo()
    elif opcion_horario == 'D':
        regresar = preguntar_regresar()
    else:
        print("Opción no válida.")      
    return regresar
   

# Función para mostrar el menú de etapas del cultivo
def mostrar_menu_etapas_cultivo():
    global regresar
    print(menu_etapas_cultivo)
    opcion_etapas_cultivo = input("Seleccione una etapa del cultivo: ")
    if opcion_etapas_cultivo == '1':
        etapa_seleccionada = "SIEMBRA"
        print("Etapa de Siembra")
    elif opcion_etapas_cultivo == '2':
        etapa_seleccionada = "CRECIMIENTO"
        print("Etapa de Crecimiento")
    elif opcion_etapas_cultivo == '3':
        etapa_seleccionada = "COSECHA"
        print("Etapa de Cosecha")
    elif opcion_etapas_cultivo == '4':
        regresar = preguntar_regresar()
    else:
        print("Opción no válida.")
    return regresar


# Función para mostrar el menú de información contable
def mostrar_menu_informacion_contable():
    global regresar
    print(menu_informacion_contable)
    opcion_contable = input("Seleccione una opción: ")
    if opcion_contable == 'A':
        mostrar_menu_costos()
    elif opcion_contable == 'B':
        mostrar_menu_produccion()
    else:
        regresar = preguntar_regresar()
    return regresar

# Función para mostrar el menú de costos
def mostrar_menu_costos():
    global regresar
    print(submenu_costos)
    opcion_costos = input("Seleccione un costo a ingresar: ")
    if opcion_costos == '1':
        costos["Mano de Obra"] = float(input('Ingrese el valor de Mano de Obra: $'))
        mostrar_menu_costos()
    elif opcion_costos == '2':
        costos["Agua"] = float(input('Ingrese el valor de Agua: $'))
        mostrar_menu_costos()
    elif opcion_costos == '3':
        costos["Mantenimiento"] = float(input('Ingrese el valor de Mantenimiento: $'))
        mostrar_menu_costos()
    elif opcion_costos == '4':
        costos["Abono"] = float(input('Ingrese el valor de Abono: $'))
        mostrar_menu_costos()
    elif opcion_costos == '5':
        regresar = preguntar_regresar()
    else:
        print("Opción no válida.")
    return regresar

# Función para mostrar el menú de producción
def mostrar_menu_produccion(valor_mercado=0.0, cantidad_recolectada=0.0):
    global regresar
    print(submenu_produccion)
    opcion_produccion = input("Seleccione una opción: ")

    if opcion_produccion == 'A':
        valor_mercado = float(input('Ingrese el valor en mercado del cultivo por arroba: $'))
        mostrar_menu_produccion(valor_mercado, cantidad_recolectada)
    elif opcion_produccion == 'B':
        cantidad_recolectada = float(input('Ingrese la cantidad recolectada en kilos: '))
        mostrar_informe_economico(valor_mercado, cantidad_recolectada)  # Llamar a la función de informe económico
        mostrar_menu_produccion(valor_mercado, cantidad_recolectada)  # Continuar mostrando el menú
    elif opcion_produccion == 'C':
        regresar = preguntar_regresar()
    else:
        print("Opción no válida.")

    return regresar

# Función para mostrar el informe económico
def mostrar_informe_economico(valor_mercado, cantidad_recolectada):
    # a. Costos totales del cultivo
    costos_totales = costos["Mano de Obra"] + costos["Agua"] + costos["Mantenimiento"] + costos["Abono"]

    # b. Valor promedio de costos fijos
    valor_promedio_costos_fijos = costos_totales / 4  # 4 tipos de costos fijos

    # c. ¿Hubo ganancia?
    ingresos = valor_mercado * (cantidad_recolectada / 12.5)  # Ingresos por la cosecha
    ganancia = ingresos - costos_totales  # Ganancia es ingresos menos costos totales
    hubo_ganancia = "SÍ" if ganancia > 0 else "NO"

    # d. Ganancia con incremento del 37% en el precio del arroz
    incremento_precio_arroz = 0.37  # 37%
    nuevo_valor_mercado_arroba = valor_mercado * (1 + incremento_precio_arroz)
    ingresos_con_incremento = nuevo_valor_mercado_arroba * (cantidad_recolectada / 12.5)
    ganancia_con_incremento = ingresos_con_incremento - costos_totales
    hubo_gananciad = "SÍ" if ganancia_con_incremento > 0 else "NO"

    # e. Ganancia con disminución del 5% en costos y 63% en cantidad de arrobas producidas
    disminucion_costos = 0.05  # 5%
    disminucion_arrobas_producidas = 0.63  # 63%
    nuevos_costos_totales = costos_totales * (1 - disminucion_costos)
    nueva_cantidad_recolectada = cantidad_recolectada * (1 - disminucion_arrobas_producidas)
    nuevos_ingresos = valor_mercado * (nueva_cantidad_recolectada / 12.5)
    ganancia_con_disminucion = nuevos_ingresos - nuevos_costos_totales
    hubo_gananciae = "SÍ" if ganancia_con_disminucion > 0 else "NO"

    # Mostrar el informe económico
    print("\nINFORME ECONÓMICO")
    print("------------------------------")

    
    print(f"a. Costos totales del cultivo: ${costos_totales:.2f}")
    print(f"b. Valor promedio de costos fijos: ${valor_promedio_costos_fijos:.2f}")
    print(f"c. ¿Hubo ganancia? {hubo_ganancia} ({ganancia:.2f} pesos)")
    print(f"d. Ganancia con incremento del 37% en el precio del arroz: ${ganancia_con_incremento:.2f} ¿Hubo ganancia? {hubo_gananciad}")

    print(f"e. Ganancia con disminución del 5% en costos y 63% en cantidad de arrobas producidas: ${ganancia_con_disminucion:.2f} ¿Hubo ganancia? {hubo_gananciae}")



if __name__ == '__main__':
    mostrar_menu_principal()

