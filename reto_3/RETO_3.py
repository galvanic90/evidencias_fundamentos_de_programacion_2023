# Definición de datos de cultivos
cultivos = [
    {
        "nombre": "Tomate",
        "mantenimiento": "Lunes, Jueves 4:00 pm",
        "regado": "Martes, Viernes 5:00 pm",
        "abono": "Miércoles, Sábado 6:00 pm",
        "etapas": ["Siembra", "Crecimiento", "Floración", "Maduración", "Cosecha"]
    },
    {
        "nombre": "Maíz",
        "mantenimiento": "Lunes, Miércoles 3:00 pm",
        "regado": "Martes, Jueves 4:00 pm",
        "abono": "Miércoles, Viernes 5:00 pm",
        "etapas": ["Siembra", "Crecimiento", "Floración", "Maduración", "Cosecha"]
    },
    {
        "nombre": "Lechuga",
        "mantenimiento": "Lunes, Miércoles 2:00 pm",
        "regado": "Martes, Jueves 3:00 pm",
        "abono": "Miércoles, Viernes 4:00 pm",
        "etapas": ["Siembra", "Crecimiento", "Cosecha"]
    }
]

# Función para mostrar el menú principal
def mostrar_menu_principal():
    print("\nMenú Principal:")
    print("1. Horario de Gestión de Cultivo")
    print("2. Etapas del Cultivo")
    print("3. Información Contable")
    print("4. Salir")

# Función para mostrar el submenú de costos
def mostrar_submenu_costos():
    print("\nSubmenú de Costos:")
    print("1. Mano de obra")
    print("2. Abono")
    print("3. Agua")
    print("4. Mantenimiento")

# Función para calcular costos totales
def calcular_costos(mano_obra, abono, agua, mantenimiento):
    return mano_obra + abono + agua + mantenimiento

# Función para calcular la ganancia
def calcular_ganancia(precio_arroba, cantidad_kilos_recolectados, costos_totales):
    ingresos = precio_arroba * (cantidad_kilos_recolectados / 12.5) # Transforma kilos a arrobas
    ganancia = ingresos - costos_totales
    return ganancia

# Función principal
def main():
    print("Bienvenido a la Aplicación de Gestión de Cultivos")

    while True:
        mostrar_menu_principal()
        opcion = input("Seleccione una opción (1/2/3/4): ")

        if opcion == "1":
            print("\nLista de cultivos:")
            for i, cultivo in enumerate(cultivos, start=1):
                print(f"{i}. {cultivo['nombre']}")

            seleccion = int(input("Seleccione un cultivo: "))
            cultivo_seleccionado = cultivos[seleccion - 1]
            print(f"\nHorario de Mantenimiento: {cultivo_seleccionado['mantenimiento']}")
            print(f"Horario de Regado: {cultivo_seleccionado['regado']}")
            print(f"Horario de Abono: {cultivo_seleccionado['abono']}")

        elif opcion == "2":
            print("\nEtapas del Cultivo:")
            for etapa in cultivo_seleccionado["etapas"]:
                print(etapa)

        elif opcion == "3":
            print("\nInformación Contable:")
            mano_obra = float(input("Costo de Mano de Obra: "))
            abono = float(input("Costo de Abono: "))
            agua = float(input("Costo de Agua: "))
            mantenimiento = float(input("Costo de Mantenimiento: "))

            costos_totales = calcular_costos(mano_obra, abono, agua, mantenimiento)
            print(f"\nCostos Totales del Cultivo: ${costos_totales:.2f}")

            precio_arroba = float(input("Precio de la Arroba de Arroz: "))
            cantidad_kilos_recolectados = float(input("Cantidad de Kilos Recolectados: "))
            ganancia = calcular_ganancia(precio_arroba, cantidad_kilos_recolectados, costos_totales)

            if ganancia >= 0:
                print(f"¿Hubo ganancia? Sí")
                print(f"Ganancia: ${ganancia:.2f}")
            else:
                print(f"¿Hubo ganancia? No")

            precio_arroba_incrementado = precio_arroba * 1.37
            ganancia_incrementada = calcular_ganancia(precio_arroba_incrementado, cantidad_kilos_recolectados, costos_totales)
            print(f"Ganancia con incremento del 37% en el precio: ${ganancia_incrementada:.2f}")

            costos_disminuidos = costos_totales * 0.95
            produccion_disminuida = cantidad_kilos_recolectados * 0.63
            ganancia_disminuida = calcular_ganancia(precio_arroba, produccion_disminuida, costos_disminuidos)
            print(f"Ganancia con costos y producción disminuidos: ${ganancia_disminuida:.2f}")

        elif opcion == "4":
            print("Gracias por usar la aplicación. ¡Hasta luego!")
            break

        else:
            print("Opción no válida. Por favor, elija una opción válida.")

if __name__ == "__main__":
    main()
