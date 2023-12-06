# -*- coding: utf-8 -*-
"""
Created on Sun Sep 10 18:14:28 2023

@author: Brahi
"""
#Importamos las librerias que nos van a proporcionar funciones matemáticas, trigonométricas y estadísticas para realizar operaciones matemáticas avanzadas
import math
import statistics 

# Definimos las funciones para las operaciones aritméticas básicas
def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b == 0:
        return "Error: División por cero"
    return a / b

# Definimos las funciones para las operaciones aritméticas extendidas
def division_entera(a, b):
    if b == 0:
        return "Error: División por cero"
    return a // b

def residuo(a, b):
    if b == 0:
        return "Error: División por cero"
    return a % b

def exponente(a, n):
    return a ** n

def raiz_n(a, n):
    if n == 0:
        return "Error: Exponente de raíz cero"
    return a ** (1/n)

def logaritmo_base10(a):
    return math.log10(a)

def logaritmo(a, base):
    return math.log(a, base)

def valor_absoluto(a):
    return abs(a)

def inverso(a):
    if a == 0:
        return "Error: Inverso de cero"
    return 1 / a

def factorial(a):
    if a < 0:
        return "Error: Factorial de número negativo"
    if a == 0:
        return 1
    return math.factorial(a)

# Definimos las funciones para las operaciones trigonométricas
def seno(x):
    return math.sin(x)

def tangente(x):
    return math.tan(x)

# Definimos las funciones para las operaciones estadísticas básicas
def promedio(numbers):
    return sum(numbers) / len(numbers)

def media(numbers):
    numbers.sort()
    middle = len(numbers) // 2
    if len(numbers) % 2 == 0:
        return (numbers[middle - 1] + numbers[middle]) / 2
    else:
        return numbers[middle]

def mediana(numbers):
    numbers.sort()
    middle = len(numbers) // 2
    return numbers[middle]

def moda(numbers):
    from collections import Counter
    counts = Counter(numbers)
    max_count = max(counts.values())
    return [num for num, count in counts.items() if count == max_count]

# Empezamos a realizar el Menú principal, el cuál va consistir de un ciclo While 
while True:
    print("\nBienvenidos a tú Calculadora Científica")
    print("Menú de tareas a realizar:")
    print("1. Operaciones Aritméticas")
    print("2. Operaciones Trigonométricas")
    print("3. Operaciones Estadísticas")
    print("4. Salir")
    choice = input("Seleccione una opción: ")

    if choice == "1":
        # Submenú para operaciones aritméticas
        print("\nOperaciones Aritméticas")
        print("1. Suma")
        print("2. Resta")
        print("3. Multiplicación")
        print("4. División")
        print("5. División Entera")
        print("6. Residuo")
        print("7. Exponenciación")
        print("8. Raíz n")
        print("9. Logaritmo en base 10")
        print("10. Logaritmo")
        print("11. Valor Absoluto")
        print("12. Inverso")
        print("13. Factorial")
        operation = input("Seleccione la operación a realizar: ")
        # Entrada de datos utilizando un control de flujo
        if operation == "1":
            a = float(input("Ingrese el primer número: "))
            b = float(input("Ingrese el segundo número: "))
            result = suma(a, b)
            print("El resultado de la suma es:", result)
            
        elif operation == "2":
            a = float(input("Ingrese el primer número: "))
            b = float(input("Ingrese el segundo número: "))
            result = resta(a, b)
            print("El resultado de la resta es:", result)
        elif operation == "3":
            a = float(input("Ingrese el primer número: "))
            b = float(input("Ingrese el segundo número: "))
            result = multiplicacion(a, b)
            print("El resultado de la multiplicación es:", result)
        elif operation == "4":
            a = float(input("Ingrese el primer número: "))
            b = float(input("Ingrese el segundo número: "))
            result = division(a, b)
            print("El resultado de la división es:", result)
        elif operation == "5":
            a = float(input("Ingrese el primer número: "))
            b = float(input("Ingrese el segundo número: "))
            result = division_entera(a, b)
            print("EL resultado de la división entera es:", result)
        elif operation == "6":
            a = float(input("Ingrese el primer número: "))
            b = float(input("Ingrese el segundo número: "))
            result = residuo(a, b)
            print("El resultado del residuo es:", result)
        elif operation == "7":
            a = float(input("Ingrese la base: "))
            n = float(input("Ingrese el exponente: "))
            result = exponente(a, n)
            print("El resultado del exponente es:", result)
        elif operation == "8":
            a = float(input("Ingrese el número: "))
            n = float(input("Ingrese el valor de n: "))
            result = raiz_n(a, n)
            print("El resultado de la raíz es:", result)
        elif operation == "9":
            a = float(input("Ingrese el número: "))
            result = logaritmo_base10(a)
            print("El Resultado del logaritmo base 10 es:", result)
        elif operation == "10":
            a = float(input("Ingrese el número: "))
            base = float(input("Ingrese la base del logaritmo: "))
            result = logaritmo(a, base)
            print("El resultado del logaritmo es:", result)
        elif operation == "11":
            a = float(input("Ingrese el número: "))
            result = valor_absoluto(a)
            print("El resultado del valor abosluto es:", result)
        elif operation == "12":
            a = float(input("Ingrese el número: "))
            result = inverso(a)
            print("EL resultado del inverso es:", result)
        elif operation == "13":
            a = int(input("Ingrese un número entero: "))
            result = factorial(a)
            print("El resultado del factorial es:", result)
        else:
            print("Operación no válida, ingrese un número válido.")
            
    elif choice == "2":
        # Submenú para operaciones trigonométricas
        print("\nOperaciones Trigonométricas")
        print("1. Seno")
        print("2. Tangente")
        operation = input("Seleccione la operación trigonométrica a realizar: ")
        # Entrada de datos utilizando un control de flujo
        if operation == "1":
            x = float(input("Ingrese el valor de x en radianes: "))
            result = seno(x)
            print("Resultado:", result)
        elif operation == "2":
            x = float(input("Ingrese el valor de x en radianes: "))
            result = tangente(x)
            print("Resultado:", result)
        else:
            print("Operación no válida, ingrese un número válido.")

    elif choice == "3":
        # Submenú para operaciones estadísticas
        print("\nOperaciones Estadísticas")
        print("1. Promedio")
        print("2. Media")
        print("3. Mediana")
        print("4. Moda")
        operation = input("Seleccione la operación estadística a realizar: ")
        # Entrada de datos utilizando un control de flujo
        if operation == "1":
            numbers = [float(x) for x in input("Ingrese una lista de números separados por espacios: ").split()]
            result = promedio(numbers)
            print("Resultado (Promedio):", result)
        elif operation == "2":
            numbers = [float(x) for x in input("Ingrese una lista de números separados por espacios: ").split()]
            result = statistics.mean(numbers)  # Utiliza statistics.mean para calcular la media
            print("Resultado (Media):", result)
        elif operation == "3":
            numbers = [float(x) for x in input("Ingrese una lista de números separados por espacios: ").split()]
            result = statistics.median(numbers)  # Utiliza statistics.median para calcular la mediana
            print("Resultado (Mediana):", result)
        elif operation == "4":
            numbers = [float(x) for x in input("Ingrese una lista de números separados por espacios: ").split()]
            result = statistics.mode(numbers)  # Utiliza statistics.mode para calcular la moda
            print("Resultado (Moda):", result)
        else:
            print("Operación no válida, Ingrese un número válido.")


# Submenú para terminar el codígo
    elif choice == "4":
        print("Muchas gracias por utilizar Tú Calculadora, hasta luego.")
        break
    else:
        print("Opción no válida. Por favor, seleccione una opción válida.")
        
