import math


def mostrar_menu_principal():
    print("\n1. Horario de Gestión de Cultivo")
    print("2. Etapas del Cultivo")
    print("3. Información Contable")
    print("4. Salir")
    print("5. Calculadora Científica")
    return input("Ingrese la opción deseada: ")


def gestion_cultivo(cultivos):
    while True:
        print("\nCultivos disponibles:")
        for idx, cultivo in enumerate(cultivos, start=1):
            print(f"{idx}. {cultivo}")

        eleccion = input("\nSeleccione el número del cultivo o 0 para regresar: ")

        if eleccion == "0":
            break

        try:
            eleccion = int(eleccion)
            cultivo_seleccionado = list(cultivos.keys())[eleccion - 1]
            mostrar_horario_cultivo(cultivo_seleccionado, cultivos)
        except (ValueError, IndexError):
            print("\nSelección inválida. Intente de nuevo.")


def mostrar_horario_cultivo(cultivo, cultivos):
    print(f"\nHorarios para {cultivo}:")
    print(f"Mantenimiento: {cultivos[cultivo]['mantenimiento']}")
    print(f"Regado: {cultivos[cultivo]['regado']}")
    print(f"Abono: {cultivos[cultivo]['abono']}")


def etapa_cultivo():
    etapas = ["Siembra", "Crecimiento", "Cosecha"]
    print("\nEtapas del Cultivo:")
    for idx, etapa in enumerate(etapas, start=1):
        print(f"{idx}. {etapa}")

    try:
        eleccion = int(input("\nSeleccione la etapa deseada: "))
        etapa_seleccionada = etapas[eleccion - 1]
        print(f"\nEtapa seleccionada: {etapa_seleccionada}")
    except (ValueError, IndexError):
        print("\nSelección inválida. Intente de nuevo.")


def informacion_contable():
    costos = {
        'mano_de_obra': 0,
        'abono': 0,
        'agua': 0,
        'mantenimiento': 0
    }

    while True:
        print("\n1. Costos")
        print("2. Producción")
        print("3. Informe Económico")
        print("4. Regresar")
        eleccion = input("Seleccione una opción: ")

        if eleccion == "1":
            costos = gestion_costos(costos)
        elif eleccion == "2":
            valor_arroba, kilos_recolectados = gestion_produccion()
        elif eleccion == "3":
            informe_economico(costos, valor_arroba, kilos_recolectados)
        elif eleccion == "4":
            break


def gestion_costos(costos):
    while True:
        print("\n1. Mano de obra")
        print("2. Abono")
        print("3. Agua")
        print("4. Mantenimiento")
        print("5. Ir atrás")
        eleccion = input("Seleccione una opción: ")

        if eleccion == "1":
            costos['mano_de_obra'] = float(input("Ingrese el costo de mano de obra: "))
        elif eleccion == "2":
            costos['abono'] = float(input("Ingrese el costo del abono: "))
        elif eleccion == "3":
            costos['agua'] = float(input("Ingrese el costo del agua: "))
        elif eleccion == "4":
            costos['mantenimiento'] = float(input("Ingrese el costo de mantenimiento: "))
        elif eleccion == "5":
            return costos


def gestion_produccion():
    valor_arroba = float(input("\nIngrese el valor de la arroba de arroz (12.5 kilos): "))
    kilos_recolectados = float(input("Ingrese la cantidad de kilos recolectados: "))
    return valor_arroba, kilos_recolectados


def informe_economico(costos, valor_arroba, kilos_recolectados):
    total_costos = sum(costos.values())
    valor_promedio_costos = total_costos / len(costos)
    ganancia = kilos_recolectados * (valor_arroba / 12.5) - total_costos

    print("\nInforme Económico:")
    print(f"Costos totales: {total_costos}")
    print(f"Valor promedio de costos: {valor_promedio_costos}")
    if ganancia > 0:
        print(f"Ganancia: Sí, {ganancia}")
    else:
        print("Ganancia: No")



# Submenú para la Calculadora
def calculadora_cientifica():
    while True:
        print("\n1. Operaciones Aritméticas Básicas")
        print("2. Operaciones Aritméticas Extendidas")
        print("3. Operaciones Trigonométricas")
        print("4. Operaciones Estadísticas Básicas")
        print("5. Regresar al Menú Principal")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            operaciones_basicas()
        elif opcion == "2":
            operaciones_extendidas()
        elif opcion == "3":
            operaciones_trigonometricas()
        elif opcion == "4":
            operaciones_estadisticas()
        elif opcion == "5":
            return

def operaciones_basicas():
    a = float(input("\nIngrese el primer número: "))
    b = float(input("Ingrese el segundo número: "))

    print("\nResultados:")
    print(f"Suma: {a + b}")
    print(f"Resta: {a - b}")
    print(f"Multiplicación: {a * b}")
    if b != 0:
        print(f"División: {a / b}")
    else:
        print("División: No es posible dividir por cero")

def operaciones_extendidas():
    a = float(input("\nIngrese el número: "))
    n = float(input("Ingrese el valor de n para raíz y exponenciación: "))

    print("\nResultados:")
    print(f"División entera de {a} por {n}: {a // n}")
    print(f"Residuo de {a} por {n}: {a % n}")
    print(f"Exponenciación: {a ** n}")
    print(f"Raíz {n} de {a}: {math.pow(a, 1/n)}")
    print(f"Logaritmo en base 10: {math.log10(a)}")
    print(f"Logaritmo natural: {math.log(a)}")
    print(f"Valor absoluto: {abs(a)}")
    print(f"1/{a}: {1/a}")
    print(f"Factorial: {math.factorial(int(a))}")

def operaciones_trigonometricas():
    x = float(input("\nIngrese el valor de x (en grados): "))
    radian = math.radians(x)

    print("\nResultados:")
    print(f"Seno({x}): {math.sin(radian)}")
    print(f"Tangente({x}): {math.tan(radian)}")

def operaciones_estadisticas():
    datos = list(map(float, input("\nIngrese los números separados por comas: ").split(",")))

    print("\nResultados:")
    print(f"Promedio: {sum(datos) / len(datos)}")
    print(f"Media: {sum(datos) / len(datos)}")
    print(f"Mediana: {sorted(datos)[len(datos) // 2]}")
    moda = max(datos, key=datos.count)
    print(f"Moda: {moda}")


    while True:
        print("\n1. Operaciones Aritméticas Básicas")
        print("2. Operaciones Aritméticas Avanzadas")
        print("3. Trigonometría")
        print("4. Regresar al Menú Principal")
        opc = input("Elige la opción deseada: ")

        if opc == "1":
            pass  # Aquí va la lógica de las operaciones aritméticas básicas
        elif opc == "2":
            pass  # Aquí va la lógica de las operaciones aritméticas avanzadas
        elif opc == "3":
            pass  # Aquí va la lógica de trigonometría
        elif opc == "4":
            break


def main():
    cultivos = {
        'Arroz': {
            'mantenimiento': 'Lunes, Jueves 4:00 pm',
            'regado': 'Lunes, Jueves 5:00 pm',
            'abono': 'Martes, Viernes 6:00 pm'
        }
    }

    while True:
        opcion = mostrar_menu_principal()

        if opcion == "1":
            gestion_cultivo(cultivos)
        elif opcion == "2":
            etapa_cultivo()
        elif opcion == "3":
            informacion_contable()
        elif opcion == "4":
            print("Gracias por usar la aplicación.")
            break
        elif opcion == "5":
            calculadora_cientifica()
        else:
            print("\nOpción no reconocida. Intente de nuevo.")


if __name__ == "__main__":
    print("¡Bienvenido a la aplicación de gestión de cultivos!")
    main()
