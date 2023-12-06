#uso de la biblioteca de matemáticas
import math

#función suma
def suma(a, b):
    return a + b

#función resta
def resta(a, b):
    return a - b

#función multiplicación
def multiplicacion(a, b):
    return a * b

#función división
def division(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: División entre cero"

#función división entera
def division_entera(a, b):
    return a // b

#función residuo
def residuo(a, b):
    return a % b

#función exponente
def exponente(a, n):
    return a ** n

#función raiz
def raiz_n(a, n):
    if a >= 0:
        return a ** (1/n)
    else:
        return "Error: No se puede calcular la raíz de un número negativo"

#función logaritmo con base 10
def log_base_10(a):
    return math.log10(a)

#función logritmo con cualquier base
def logaritmo(a, base):
    return math.log(a, base)

#función valor absoluto
def valor_absoluto(a):
    return abs(a)

#función inverso
def inverso(a):
    if a != 0:
        return 1 / a
    else:
        return "Error: No se puede calcular el inverso de cero"

#función factorial
def factorial(a):
    if a >= 0:
        return math.factorial(a)
    else:
        return "Error: No se puede calcular el factorial de un número negativo"

#función seno
def seno(x):
    return math.sin(x)

#función tangente
def tangente(x):
    return math.tan(x)

#función promedio
def promedio(numbers):
    return sum(numbers) / len(numbers)

#función media
def media(numbers):
    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)
    if n % 2 == 0:
        mid1 = sorted_numbers[n // 2 - 1]
        mid2 = sorted_numbers[n // 2]
        return (mid1 + mid2) / 2
    else:
        return sorted_numbers[n // 2]

#función mediana
def mediana(numbers):
    return statistics.median(numbers)

#función moda
def moda(numbers):
    return statistics.mode(numbers)

#implementación de menú
opcion = int(input("Ingrese la operación que desea realizar:\n"
                   "1. División entera\n"
                   "2. Residuo\n"
                   "3. Exponente\n"
                   "4. Raíz n\n"
                   "5. Logaritmo en base 10\n"
                   "6. Logaritmo\n"
                   "7. Valor absoluto\n"
                   "8. Inverso\n"
                   "9. Factorial\n"
                   "10. Seno\n"
                   "11. Tangente\n"
                   "12. Promedio\n"
                   "13. Media\n"
                   "14. Mediana\n"
                   "15. Moda\n"))

#impresión de valores según selección
if opcion == 1:
    print("División entera:", division_entera(num1, num2))
elif opcion == 2:
    print("Residuo:", residuo(num1, num2))
elif opcion == 3:
    n = int(input("Ingrese el exponente: "))
    print("Exponente:", exponente(num1, n))
elif opcion == 4:
    n = int(input("Ingrese el valor de n para la raíz n: "))
    print("Raíz n:", raiz_n(num1, n))
elif opcion == 5:
    print("Logaritmo en base 10:", log_base_10(num1))
elif opcion == 6:
    base = float(input("Ingrese la base del logaritmo: "))
    print("Logaritmo:", logaritmo(num1, base))
elif opcion == 7:
    print("Valor absoluto:", valor_absoluto(num1))
elif opcion == 8:
    print("Inverso:", inverso(num1))
elif opcion == 9:
    print("Factorial:", factorial(int(num1)))
elif opcion == 10:
    print("Seno:", seno(num1))
elif opcion == 11:
    print("Tangente:", tangente(num1))
elif opcion == 12:
    num_count = int(input("Ingrese la cantidad de números para calcular el promedio: "))
    numbers = []
    for _ in range(num_count):
        number = float(input("Ingrese un número: "))
        numbers.append(number)
    print("Promedio:", promedio(numbers))
elif opcion == 13:
    num_count = int(input("Ingrese la cantidad de números para calcular la media: "))
    numbers = []
    for _ in range(num_count):
        number = float(input("Ingrese un número: "))
        numbers.append(number)
    print("Media:", media(numbers))
elif opcion == 14:
    num_count = int(input("Ingrese la cantidad de números para calcular la mediana: "))
    numbers = []
    for _ in range(num_count):
        number = float(input("Ingrese un número: "))
        numbers.append(number)
    print("Mediana:", mediana(numbers))
elif opcion == 15:
    num_count = int(input("Ingrese la cantidad de números para calcular la moda: "))
    numbers = []
    for _ in range(num_count):
        number = float(input("Ingrese un número: "))
        numbers.append(number)
    print("Moda:", moda(numbers))
else:
    print("Opción no válida")
