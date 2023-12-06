import math
from statistics import StatisticsError


# Función para mostrar el menú principal
def mostrar_menu_principal():
    print("Calculadora Científica")
    print("1. Operaciones aritméticas básicas")
    print("2. Operaciones aritméticas extendidas")
    print("3. Operaciones trigonométricas")
    print("4. Operaciones estadísticas básicas")
    print("5. Salir")


# Función para realizar operaciones aritméticas básicas
def operaciones_aritmeticas():
    print("Operaciones Aritméticas Básicas")
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))

    print("Seleccione la operación:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")

    opcion = int(input("Opción: "))

    if opcion == 1:
        resultado = num1 + num2
    elif opcion == 2:
        resultado = num1 - num2
    elif opcion == 3:
        resultado = num1 * num2
    elif opcion == 4:
        if num2 == 0:
            print("Error: No se puede dividir entre cero.")
            return
        resultado = num1 / num2
    else:
        print("Opción no válida")
        return

    print("Resultado: ", resultado)


# Función para realizar operaciones aritméticas extendidas
def operaciones_extendidas():
    print("Operaciones Aritméticas Extendidas")
    num = float(input("Ingrese un número: "))

    print("Seleccione la operación:")
    print("1. División Entera")
    print("2. Residuo")
    print("3. Exponenciación")
    print("4. Raíz cuadrada")
    print("5. Raíz cúbica")
    print("6. Logaritmo en base 10")
    print("7. Logaritmo natural")
    print("8. Valor absoluto")
    print("9. Inverso (1/número)")
    print("10. Factorial")

    opcion = int(input("Opción: "))

    if opcion == 1:
        divisor = float(input("Ingrese el divisor: "))
        resultado = num // divisor
    elif opcion == 2:
        divisor = float(input("Ingrese el divisor: "))
        resultado = num % divisor
    elif opcion == 3:
        exponente = float(input("Ingrese el exponente: "))
        resultado = num ** exponente
    elif opcion == 4:
        resultado = math.sqrt(num)
    elif opcion == 5:
        resultado = num ** (1 / 3)
    elif opcion == 6:
        resultado = math.log10(num)
    elif opcion == 7:
        resultado = math.log(num)
    elif opcion == 8:
        resultado = abs(num)
    elif opcion == 9:
        if num == 0:
            print("Error: No se puede calcular el inverso de cero.")
            return
        resultado = 1 / num
    elif opcion == 10:
        resultado = math.factorial(int(num))
    else:
        print("Opción no válida")
        return

    print("Resultado: ", resultado)


# Función para realizar operaciones trigonométricas
def operaciones_trigonometricas():
    print("Operaciones Trigonométricas")
    angulo = float(input("Ingrese el valor del ángulo en grados: "))

    print("Seleccione la operación:")
    print("1. Seno")
    print("2. Tangente")

    opcion = int(input("Opción: "))

    if opcion == 1:
        resultado = math.sin(math.radians(angulo))
    elif opcion == 2:
        resultado = math.tan(math.radians(angulo))
    else:
        print("Opción no válida")
        return

    print("Resultado: ", resultado)


# Función para realizar operaciones estadísticas básicas
def operaciones_estadisticas():
    print("Operaciones Estadísticas Básicas")
    numeros = input("Ingrese una lista de números separados por espacios: ").split()
    numeros = [float(num) for num in numeros]

    print("Seleccione la operación:")
    print("1. Promedio")
    print("2. Media")
    print("3. Mediana")
    print("4. Moda")

    opcion = int(input("Opción: "))

    if opcion == 1:
        resultado = sum(numeros) / len(numeros)
    elif opcion == 2:
        resultado = math.fsum(numeros) / len(numeros)
    elif opcion == 3:
        numeros.sort()
        if len(numeros) % 2 == 0:
            mid1 = len(numeros) // 2
            mid2 = mid1 - 1
            resultado = (numeros[mid1] + numeros[mid2]) / 2
        else:
            resultado = numeros[len(numeros) // 2]
    elif opcion == 4:
        from statistics import mode
        try:
            resultado = mode(numeros)
        except StatisticsError:
            resultado = "No hay moda"
    else:
        print("Opción no válida")
        return

    print("Resultado: ", resultado)


# Programa principal
while True:
    mostrar_menu_principal()
    opcion_principal = int(input("Seleccione una opción (1-5): "))

    if opcion_principal == 1:
        operaciones_aritmeticas()
    elif opcion_principal == 2:
        operaciones_extendidas()
    elif opcion_principal == 3:
        operaciones_trigonometricas()
    elif opcion_principal == 4:
        operaciones_estadisticas()
    elif opcion_principal == 5:
        print("Gracias por usar la calculadora científica. ¡Hasta luego!")
        break
    else:
        print("Opción no válida")
