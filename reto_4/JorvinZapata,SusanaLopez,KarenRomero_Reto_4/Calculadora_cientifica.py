# -*- coding: utf-8 -*-
"""
Created on Sun Sep 10 18:23:31 2023

@author: JorvinZ
"""
''' En este ejercicio de la calculadora científica se trató de realizar todas 
las funciones primero, desde las más básicas hasta las más complejas para 
posteriormente, mediante un menu, pedirle al usuario que tipo de cálculo 
quería realizar y que ingresara los valores para dicho cálculo'''

import math

def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b == 0:
        return "Error: no se puede dividir por cero"
    return a / b

def division_entera(a, b):
    if b == 0:
        return "Error: no se puede dividir por cero"
    return a // b

def residuo(a, b):
    if b == 0:
        return "Error: no se puede dividir por cero"
    return a % b

def exponente(a, n):
    return a ** n

def raiz_n(a, n):
    if a < 0 and n % 2 == 0:
        return "Error: raíz de número negativo con exponente par"
    return a ** (1 / n)

def logaritmo_base_10(a):
    return math.log10(a)

def logaritmo(a, base):
    return math.log(a, base)

def valor_absoluto(a):
    return abs(a)

def inverso(a):
    if a == 0:
        return "Error: inverso de cero"
    return 1 / a

def factorial(a):
    if a < 0:
        return "Error:  no existe factorial de número negativo"
    if a == 0:
        return 1
    return a * factorial(a - 1)

def seno(x):
    return math.sin(x)

def tangente(x):
    return math.tan(x)

def promedio(lista):
    return sum(lista) / len(lista)

def mediana(lista):
    lista.sort()
    n = len(lista)
    if n % 2 == 0: #si el número de elementos es un par
        return (lista[n // 2 - 1] + lista[n // 2]) / 2
    else: #si el número de elementos es impar
        return lista[n // 2]

def moda(lista):
    from collections import Counter
    counts = Counter(lista) #se cuenta cada elemento de la lista y se crea un diccionario de recuento
    max_count = max(counts.values()) #se encuentra el valor máximo dentro de los valores (recuento) de las llaves 
    modas = [] #se crea una lista que contendrá todas las modas
    for num, count in counts.items(): #creamos un ciclo para contar los recuentos, y si hay dos números con el mismo recuento, se agrega a la lista moda
        if count == max_count:
            modas.append(num)
    return modas

# Función principal - Aquí se aplicó el mismo principio que en el reto 3
#así que esta función funciona como la interface de todas las funciones que 
#realizamos anteriormente. 
def main():
    print("Calculadora Científica")
    
    while True:
        print("\nOperaciones disponibles:")
        print("1. Operaciones aritméticas básicas")
        print("2. Operaciones aritméticas extendidas")
        print("3. Operaciones trigonométricas básicas")
        print("4. Operaciones estadísticas básicas")
        print("5. Salir")
        
        opcion = input("Seleccione el número de la opción anteriormente mencionada que desea realizar: ")
        
        #Acá, por medio de condicionales, se presentan la serie de operaciones
        #que el usuario quiere realizar, y se procede a utilizar las funciones que 
        #hicimos anteriormente
        if opcion == "1":          
            print("\nOperaciones aritméticas básicas:")
            #acá se le pide al usuario que ingresé de una vez los dos números 
            #con los que desea realizar la operación para no tener que estar poniendolos
            #nuevamente en cada línea de cada operación
            num1 = float(input("Ingrese un número: "))
            num2 = float(input("Ingrese otro número: "))
            
            print("Seleccione una operación:")
            print("1. Suma")
            print("2. Resta")
            print("3. Multiplicación")
            print("4. División")
            
            #se le pide nuevamente al usuario que escoja una opción de las anteriores
            operacion = int(input("Escriba el número de la operación que desea realizar: "))
            
            #y por medio de condicionales decidimos que operación quiere realizar
            #de las anteriormente mencionadas
            if operacion == 1:
                resultado = suma(num1, num2)
            elif operacion == 2:
                resultado = resta(num1, num2)
            elif operacion == 3:
                resultado = multiplicacion(num1, num2)
            elif operacion == 4:
                resultado = division(num1, num2)
            else:
                resultado = "Operación no válida"
            
            print(f"El resultado de su operación es: {resultado}")
        
        #nuevamente por medio de condicionales se entra a otra sección de operaciones
        elif opcion == "2":
            print("\nOperaciones aritméticas extendidas:")
            
            print("Seleccione una operación:")
            print("a. División entera")
            print("b. Residuo")
            print("c. Exponenciación a la n")
            print("d. Raíz n")
            print("e. Logaritmo en base 10")
            print("f. Logaritmo")
            print("g. Valor absoluto")
            print("h. 1/número")
            print("i. Factorial")
            
            operacion = input("Seleccione la letra de la operación que desea realizar:  ")
            
            if operacion == "a":
                num = float(input("Ingrese un número: "))
                num2 = float(input("Ingrese otro número: "))
                resultado = division_entera(num, num2)
            elif operacion == "b":
                num = float(input("Ingrese un número: "))
                num2 = float(input("Ingrese otro número: "))
                resultado = residuo(num, num2)
            elif operacion == "c":
                num = float(input("Ingrese un número: "))
                n = int(input("Ingrese el exponente n: "))
                resultado = exponente(num, n)
            elif operacion == "d":
                num = float(input("Ingrese un número: "))
                n = int(input("Ingrese el valor de n: "))
                resultado = raiz_n(num, n)
            elif operacion == "e":
                num = float(input("Ingrese un número: "))
                resultado = logaritmo_base_10(num)
            elif operacion == "f":
                num = float(input("Ingrese un número: "))
                base = float(input("Ingrese la base del logaritmo: "))
                resultado = logaritmo(num, base)
            elif operacion == "g":
                num = float(input("Ingrese un número: "))
                resultado = valor_absoluto(num)
            elif operacion == "h":
                num = float(input("Ingrese un número: "))
                resultado = inverso(num)
            elif operacion == "i":
                num = float(input("Ingrese un número: "))
                resultado = factorial(int(num))
            else:
                resultado = "Operación no válida"
            
            print(f"El resultado de su operación es: {resultado}")
        
        elif opcion == "3":
            print("\nOperaciones trigonométricas:")
            angulo = float(input("Ingrese el ángulo en grados: "))
            
            print("Seleccione una operación:")
            print("a. Seno")
            print("b. Tangente")
            
            operacion = input("Seleccione la letra de la operación que desea: ")
            
            if operacion == "a":
                resultado = seno(math.radians(angulo))  # Convertir a radianes
            elif operacion == "b":
                resultado = tangente(math.radians(angulo))  # Convertir a radianes
            else:
                resultado = "Operación no válida"
            
            print(f"El resultado de su operación es: {resultado}")
        
        elif opcion == "4":
            print("\nOperaciones estadísticas básicas:")
            
            print("Seleccione una operación:")
            print("a. Promedio")
            print("b. Mediana")
            print("c. Moda")
            
            operacion = input("Seleccione la letra de la operación que desea: ")
            
            if operacion == "a":
                lista = input("Ingrese los números que desea separados SOLO por espacios: ")
                lista = [float(x) for x in lista.split()]
                #esta línea de código es un poco compleja, pero dado 
                #que debía introducir varios valores, busqué en google la forma. Lo que hace 
                #lista.split() es separar los valores que el usuario ingresó separado por espacios
                #y ponerlos en forma de lista, pero los ingresa como si fueran caracteres
                # y lo que hace el float(x) es convertir esos caracteres a flotantes. 
                #Este código es más eleagante que este que escribiré a continuación y hace lo mismo
                '''   lista = lista.split()
                   lista2 = []
                   for x in lista:
                       lista = float(x)
                       lista2.append(lista)
                   print(lista2)'''
                resultado = promedio(lista)
            elif operacion == "b":
                lista = input("Ingrese los números que desea separados SOLO por espacios: ")
                lista = [float(x) for x in lista.split()]
                resultado = mediana(lista)
            elif operacion == "c":
                lista = input("Ingrese los números que desea separados SOLO por espacios: ")
                lista = [float(x) for x in lista.split()]
                resultado = moda(lista)
            else:
                resultado = "Operación no válida"
            
            print(f"El resultado de su operación es: {resultado}")
        
        elif opcion == "5":
            print("Saliendo de la aplicación.")
            break
        
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    main()
