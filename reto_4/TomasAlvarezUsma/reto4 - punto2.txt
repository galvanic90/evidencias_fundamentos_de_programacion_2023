# -*- coding: utf-8 -*-
"""
@author: TOMAS ALVAREZ
cc:1193130489
"""
import math

# Funciones de operaciones aritméticas básicas
def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: División por cero"

# Funciones de operaciones aritméticas extendidas
def division_entera(a, b):
    if b != 0:
        return a // b
    else:
        return "Error: División por cero"

def residuo(a, b):
    if b != 0:
        return a % b
    else:
        return "Error: División por cero"

def potencia(a, n):
    return a ** n

def raiz_n(a, n):
    if a >= 0:
        return a ** (1/n)
    else:
        return "Error: Raíz de número negativo"

def logaritmo_base_10(a):
    return math.log10(a)

def logaritmo(a, base):
    if a > 0 and base > 0 and base != 1:
        return math.log(a, base)
    else:
        return "Error: Argumentos no válidos"

def valor_absoluto(a):
    return abs(a)

def inverso(a):
    if a != 0:
        return 1 / a
    else:
        return "Error: Inverso de cero"

def factorial(n):
    if n >= 0:
        return math.factorial(n)
    else:
        return "Error: Factorial de número negativo"

# Funciones de operaciones trigonométricas
def seno(x):
    return math.sin(x)

def tangente(x):
    return math.tan(x)

# Funciones de operaciones estadísticas básicas
def promedio(lista):
    if len(lista) > 0:
        return sum(lista) / len(lista)
    else:
        return "Error: Lista vacía"

def mediana(lista):
    if len(lista) > 0:
        sorted_lista = sorted(lista)
        middle = len(sorted_lista) // 2
        if len(sorted_lista) % 2 == 0:
            return (sorted_lista[middle - 1] + sorted_lista[middle]) / 2
        else:
            return sorted_lista[middle]
    else:
        return "Error: Lista vacía"

def moda(lista):
    if len(lista) > 0:
        counts = {}
        for item in lista:
            if item in counts:
                counts[item] += 1
            else:
                counts[item] = 1
        max_count = max(counts.values())
        mode = [item for item, count in counts.items() if count == max_count]
        return mode
    else:
        return "Error: Lista vacía"

# Función principal de la calculadora
def calculadora_cientifica():
    while True:
        # Menú principal
        print("Calculadora Científica")
        print("1. Operaciones aritméticas básicas")
        print("2. Operaciones aritméticas extendidas")
        print("3. Operaciones trigonométricas")
        print("4. Operaciones estadísticas básicas")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            # Submenú para operaciones aritméticas básicas
            print("Operaciones aritméticas básicas:")
            print("1. Suma")
            print("2. Resta")
            print("3. Multiplicación")
            print("4. División")
            operacion = input("Seleccione una operación (1/2/3/4): ")
            if operacion in ["1", "2", "3", "4"]:
                num1 = float(input("Ingrese el primer número: "))
                num2 = float(input("Ingrese el segundo número: "))
                if operacion == "1":
                    resultado = suma(num1, num2)
                elif operacion == "2":
                    resultado = resta(num1, num2)
                elif operacion == "3":
                    resultado = multiplicacion(num1, num2)
                elif operacion == "4":
                    resultado = division(num1, num2)
                print("Resultado:", resultado)
            else:
                print("Opción no válida.")

        elif opcion == "2":
            # Submenú para operaciones aritméticas extendidas
            print("Operaciones aritméticas extendidas:")
            print("1. División Entera")
            print("2. Residuo")
            print("3. Exponenciación")
            print("4. Raíz")
            print("5. Logaritmo en base 10")
            print("6. Logaritmo")
            print("7. Valor Absoluto")
            print("8. Inverso")
            print("9. Factorial")
            operacion = input("Seleccione una operación (1/2/3/4/5/6/7/8/9): ")
            if operacion in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
                if operacion in ["1", "2", "3", "4"]:
                    num1 = float(input("Ingrese el primer número: "))
                    num2 = float(input("Ingrese el segundo número: "))
                else:
                    num1 = float(input("Ingrese un número: "))
                if operacion == "1":
                    resultado = division_entera(num1, num2)
                elif operacion == "2":
                    resultado = residuo(num1, num2)
                elif operacion == "3":
                    resultado = potencia(num1, num2)
                elif operacion == "4":
                    n = float(input("Ingrese el valor de n para la raíz: "))
                    resultado = raiz_n(num1, n)
                elif operacion == "5":
                    resultado = logaritmo_base_10(num1)
                elif operacion == "6":
                    base = float(input("Ingrese la base del logaritmo: "))
                    resultado = logaritmo(num1, base)
                elif operacion == "7":
                    resultado = valor_absoluto(num1)
                elif operacion == "8":
                    resultado = inverso(num1)
                elif operacion == "9":
                    resultado = factorial(int(num1))
                print("Resultado:", resultado)
            else:
                print("Opción no válida.")

        elif opcion == "3":
            # Submenú para operaciones trigonométricas
            print("Operaciones trigonométricas:")
            print("1. Seno")
            print("2. Tangente")
            operacion = input("Seleccione una operación (1/2): ")
            if operacion in ["1", "2"]:
                angulo = float(input("Ingrese el valor del ángulo en radianes: "))
                if operacion == "1":
                    resultado = seno(angulo)
                elif operacion == "2":
                    resultado = tangente(angulo)
                print("Resultado:", resultado)
            else:
                print("Opción no válida.")

        elif opcion == "4":
            # Submenú para operaciones estadísticas básicas
            print("Operaciones estadísticas básicas:")
            print("1. Promedio")
            print("2. Mediana")
            print("3. Moda")
            operacion = input("Seleccione una operación (1/2/3): ")
            if operacion in ["1", "2", "3"]:
                data = input("Ingrese los números separados por espacios: ").split()
                numeros = [float(x) for x in data]
                if operacion == "1":
                    resultado = promedio(numeros)
                elif operacion == "2":
                    resultado = mediana(numeros)
                elif operacion == "3":
                    resultado = moda(numeros)
                print("Resultado:", resultado)
            else:
                print("Opción no válida.")

        elif opcion == "5":
            print("¡Hasta luego!")
            break

        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    calculadora_cientifica()
