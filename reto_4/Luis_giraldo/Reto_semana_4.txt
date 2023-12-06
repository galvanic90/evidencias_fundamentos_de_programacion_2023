import math

def menu_principal():
    print("Calculadora Científica")
    print("1. Operaciones Aritméticas")
    print("2. Operaciones Aritméticas Extendidas")
    print("3. Operaciones Trigonométricas")
    print("4. Operaciones Estadísticas")
    print("5. Salir")

def operaciones_aritmeticas():
    print("Operaciones Aritméticas")
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))
    
    print("Resultados:")
    print("Suma:", num1 + num2)
    print("Resta:", num1 - num2)
    print("Multiplicación:", num1 * num2)
    if num2 != 0:
        print("División:", num1 / num2)
    else:
        print("La división por cero no está permitida")

def operaciones_extendidas():
    print("Operaciones Aritméticas Extendidas")
    num = float(input("Ingrese un número: "))
    
    print("Resultados:")
    print("División Entera por 2:", num // 2)
    print("Residuo por 2:", num % 2)
    exponente = int(input("Ingrese el exponente para la potencia: "))
    print("Potencia:", num ** exponente)
    raiz_n = int(input("Ingrese el valor de n para la raíz n: "))
    if raiz_n > 0:
        print(f"Raíz {raiz_n}:", num ** (1 / raiz_n))
    else:
        print("n debe ser mayor que 0")
    print("Logaritmo en base 10:", math.log10(num))
    print("Valor absoluto:", abs(num))
    print("Inverso:", 1 / num)
    print("Factorial:", math.factorial(int(num)))

def operaciones_trigonometricas():
    print("Operaciones Trigonométricas")
    angulo = float(input("Ingrese el valor del ángulo en grados: "))
    
    radianes = math.radians(angulo)
    
    print("Resultados:")
    print("Seno:", math.sin(radianes))
    print("Coseno:", math.cos(radianes))
    print("Tangente:", math.tan(radianes))

def operaciones_estadisticas():
    print("Operaciones Estadísticas")
    num_list = input("Ingrese una lista de números separados por espacios: ").split()
    numeros = [float(x) for x in num_list]
    
    print("Resultados:")
    print("Promedio:", sum(numeros) / len(numeros))
    print("Media:", sorted(numeros)[len(numeros) // 2])
    print("Moda:", max(set(numeros), key=numeros.count))

while True:
    menu_principal()
    opcion = input("Seleccione una opción: ")

    if opcion == '1':
        operaciones_aritmeticas()
    elif opcion == '2':
        operaciones_extendidas()
    elif opcion == '3':
        operaciones_trigonometricas()
    elif opcion == '4':
        operaciones_estadisticas()
    elif opcion == '5':
        print("¡Hasta luego!")
        break
    else:
        print("Opción no válida. Intente de nuevo.")
