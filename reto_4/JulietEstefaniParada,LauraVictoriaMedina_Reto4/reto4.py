# -*- coding: utf-8 -*-
"""Reto4.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1bf_aI6pJ4cZbXgweZdvshtL2fVuLJsAT
"""

import math
import statistics
#funcion que imprime el menu principal de la calculadora
def Menu():
  print("\nCALCULADORA CIENTIFICA \n ¿QUE OPERACIÓN DESEA REALIZAR? "
    "\n 1.ARITMÉTICAS  \n 2.ARITMÉTICAS EXTENDIDAS \n 3.TRIGONOMÉTRICAS  \n 4.ESTADÍSTICAS BÁSICAS \n 5.SALIR")
#funcion que imprime el SubMenu de las OPERACIONES ARITMÉTICAS
def SubMenuOPA():
  print("\nOPERACIONES ARITMÉTICAS \n ¿QUE OPERACIÓN DESEA REALIZAR? "
    "\n 1.SUMA \n 2.RESTA \n 3.MULTIPLICACIÓN \n 4.DIVISIÓN \n 5.IR ATRÁS")
#Funcion que realiza la suma de dos paramtros que debe ingresar el usuario
def Suma(num1,num2):
  print("El total de la Suma es: ", num1 + num2)

def Resta(num1,num2):
  print("El total de la Resta es: ", num1 - num2)

def Multi(num1,num2):
  print("El total de la Multiplicación es: ", num1 * num2)

def Divi(num1,num2):
  print("El total de la División es: ", num1 / num2)

def SubMenuOPAE():
  print("\nOPERACIONES ARITMÉTICAS EXTENDIDAS \n ¿QUE OPERACIÓN DESEA REALIZAR? "
    "\n 1.DIVISIÓN ENTERA \n 2.RESIDUO \n 3.EXPONENCIA \n 4.RAÍZ CUADRADA "
    "\n 5.LOGARITMO EN BASE 10 \n 6.LOGARITMO \n 7.VALOR ABSOLUTO "
    "\n 8.(1)/NÚMERO \n 9.FACTORIAL \n 10.IR ATRÁS")

def DiviEnt(num1,num2):
  print("El total de la División Entera es: ", num1 // num2)

def Residuo(num1,num2):
  print("El Residuo de la division es: ", num1 % num2)

def Expo(num1,num2):
  print("El exponente del numero " + str(num1) + " es: ", num1 ** num2)

def Raiz(num1):
  print("La raiz cuadrada del numero " + str(num1) + " es: ",(num1 **(0.5)))

def LogaDi(num1):
  num2 = 10
  resul = math.log(num1,num2)
  print("El Logaritmo en base 10 del numero " + str(num1) + " es: " + str(resul))

def Loga(num1,num2):
  resul = math.log(num1,num2)
  print("El Logaritmo en base " + str(num2) + " del numero " + str(num1) + " es: " + str(resul))

def ValAbs(num1):
 result  = abs(num1)
 print("El valor Absoluto del numero " + str(num1) + " es: ", result )

def unoDiv(num1):
 result = 1 /num1
 print("La division de 1 entre el numero " + str(num1) + " es: ", result )

#funcion para hallar el factorial de un numero ingresado
def Fact(num1):
  #declaro un variable para igualarla al numero ingresadp y convertirlo a un int
 num = int(num1)
 #declaro una variable = 1
 factorial = 1
 #ciclo for para recorrer el numero ingresado
 for i in range(1,num+1):
    #variable para hallar el valor de i= numero de veces del for * factorial
    factorial = i*factorial
    #impresion para visualizar el resultado del numero ingresado y el factorial
 print("El factorial del numero " + str(num) + " es: "+str(factorial))

def SubMenuOPTR():
  print("\nOPERACIONES TRIGONOMÉTRICAS \n ¿QUE OPERACIÓN DESEA REALIZAR? "
    "\n 1.SENO(X) \n 2.TANGENTE(X) \n 3.COSENO(X) \n 4.IR ATRÁS")

def Seno(num1):
  result = math.sin(num1)
  print("El Seno del numero " + str(num1) + " es: "+str(result))

def Tan(num1):
  result = math.tan(num1)
  print("El Tangente del numero " + str(num1) + " es: "+str(result))

#funcion que realiza la operacion del seno del numero digitado por el usuario
def Cos(num1):
  #se declara una variable para obtener el resultado del coseno del numero ingresado utilizando la libreria math
  result = math.cos(num1)
  #imprimimos el valor digitado y luego resultado
  print("El Coseno del numero " + str(num1) + " es: "+str(result))

def SubMenuOPEB():
  print("\nOPERACIONES ESTADÍSTICAS BÁSICAS \n ¿QUE OPERACIÓN DESEA REALIZAR? "
    "\n 1.PROMEDIO \n 2.MEDIA \n 3.MEDIANA \n 4.MODA \n 5.IR ATRÁS")

def Prom(canti):
  #declaramos variables que se van a utilizar para opreaciones
  conta = 0
  suma = 0
  #ciclo for para recorrer las veces de la cantidad de numeros obtenidos
  for i in range(canti):
   #input para pedir numero
   canti = int(input("Ingrese el valor "))
   #contador para sumar los valores ingresados por el usuario
   suma += canti
   #contador para sumar las veces que se ingresa un numero ("valor")
   conta +=1
   #operacion para hallar el promedio
   result = suma / conta
   #impresion para mostar la suma de los valores obtenido y el promedio total
  print("La suma de los numeros ingresados es de: " + str(suma) +
      " y su promedio es: " +str(result))

#funcion para hallar la media de los numeros digitados por el usuario
def Media(canti):
  #creacion de una lista para guardar los numeros ingresados
  data = []
  #ciclo for para recorrer el numero de las cantidades
  for i in range(canti):
   #variable que se encarga de pedir los valores
   canti = int(input("Ingrese el valor "))
   #sentencia para ingresar a la lista (data) los valores con la sentencia (append)
   data.append(canti)
   #variable que opera la media de los valores obtenidos en la lista
   result = statistics.mean(data)
   #impresion que me muestra los resultados de la Media
  print("La Media de los numeros ingresados es de: " +str(result))


def Mediana(canti):
  data = []
  for i in range(canti):
   canti = int(input("Ingrese el valor "))
   data.append(canti)
   result = statistics.median(data)
  print("La Mediana de los numeros ingresados es de: " +str(result))

def Moda(canti):
  data = []
  for i in range(canti):
   canti = int(input("Ingrese el valor "))
   data.append(canti)
   result = statistics.mode(data)
  print("La Moda de los numeros ingresados es de: " +str(result))


while True:
 Menu()
 OpM = input('Ingrese una opcion del Menu Principal :')
 if OpM == "1":
  SubMenuOPA()
  opa = int(input('Ingrese la opcion que desea del SubMenu OPERACIONES ARITMÉTICAS :'))
  while opa >0 and opa <5:
   num1 = float(input("Ingrese un numero: "))
   if opa == 1:
    num2 = float(input("Ingrese un numero: "))
    Suma(num1,num2)
    opInser = input("\nDesea realizar una nueva SUMA \n 1.SI \n 2.NO \n Rta: ")
    if opInser == "2":
     break
   elif opa == 2:
    num2 = float(input("Ingrese un numero: "))
    Resta(num1,num2)
    opInser = input("\nDesea realizar una nueva RESTA \n 1.SI \n 2.NO \n Rta: ")
    if opInser == "2":
     break
   elif opa == 3:
    num2 = float(input("Ingrese un numero: "))
    Multi(num1,num2)
    opInser = input("\nDesea realizar una nueva MULTIPLICACIÓN \n 1.SI \n 2.NO \n Rta: ")
    if opInser == "2":
     break
   elif opa == 4:
    num2 = float(input("Ingrese un numero: "))
    Divi(num1,num2)
    opInser = input("\nDesea realizar una nueva DIVISIÓN \n 1.SI \n 2.NO \n Rta: ")
    if opInser == "2":
     break
   elif opa == 5:
    break
 elif OpM == "2":
  SubMenuOPAE()
  opa = int(input('Ingrese la opcion que desea del SubMenu OPERACIONES ARITMÉTICAS EXTENDIDAS :'))
  while opa >0 and opa<10:
   num1 = float(input("Ingrese un numero: "))
   if opa == 1:
    num2 = float(input("Ingrese un numero: "))
    DiviEnt(num1,num2)
    opInser = input("\nDesea realizar una nueva DIVISIÓN ENTERA \n 1.SI \n 2.NO \n Rta: ")
    if opInser == "2":
     break
   elif opa == 2:
    num2 = float(input("Ingrese un numero: "))
    Residuo(num1,num2)
    opInser = input("\nDesea hallar otro RESIDUO \n 1.SI \n 2.NO \n Rta: ")
    if opInser == "2":
     break
   elif opa == 3:
    num2 = float(input("Ingrese el numero exponencial: "))
    Expo(num1,num2)
    opInser = input("\nDesea hallar otra EXPONENCIA \n 1.SI \n 2.NO \n Rta: ")
    if opInser == "2":
     break
   elif opa == 4:
    Raiz(num1)
    opInser = input("\nDesea hallar RAÍZ \n 1.SI \n 2.NO \n Rta: ")
    if opInser == "2":
     break
   elif opa == 5:
    LogaDi(num1)
    opInser = input("\nDesea hallar otro LOGARITMO BASE 10 \n 1.SI \n 2.NO \n Rta: ")
    if opInser == "2":
     break
   elif opa == 6:
    num2 = float(input("Ingrese numero del logaritmo: "))
    Loga(num1,num2)
    opInser = input("\nDesea hallar otro LOGARITMO \n 1.SI \n 2.NO \n Rta: ")
    if opInser == "2":
     break
   elif opa == 7:
    ValAbs(num1,num2)
    opInser = input("\nDesea hallar otro VALOR ABSOLUTO \n 1.SI \n 2.NO \n Rta: ")
    if opInser == "2":
     break
   elif opa == 8:
    unoDiv(num1)
    opInser = input("\nDesea dividir otro numero en 1\n 1.SI \n 2.NO \n Rta: ")
    if opInser == "2":
     break
   elif opa == 9:
    Fact(num1)
    opInser = input("\nDesea sacar el Factorial de otro numero 1\n 1.SI \n 2.NO \n Rta: ")
    if opInser == "2":
     break
   elif opa == 10:
    break
 elif OpM =="3":
  SubMenuOPTR()
  opa = int(input('Ingrese la opcion que desea del SubMenu OPERACIONES TRIGONOMÉTRICAS :'))
  while opa >0 and opa<4:
   num1 = float(input("Ingrese un numero: "))
   if opa == 1:
    #utilizamos la funcion Seno
    Seno(num1)
    opInser = input("\nDesea realizar otra operacion con SENO(X)\n 1.SI \n 2.NO \n Rta: ")
    if opInser == "2":
     break
   elif opa == 2:
    #utilizamos la funcion tangente
    Tan(num1)
    opInser = input("\nDesea realizar otra operacion con TANGENTE(X)\n 1.SI \n 2.NO \n Rta: ")
    if opInser == "2":
     break
   elif opa == 3:
    Cos(num1)
    opInser = input("\nDesea realizar otra operacion con COSENO(X)\n 1.SI \n 2.NO \n Rta: ")
    if opInser == "2":
     break
   elif opa == 4:
    break
 elif OpM =="4":
  SubMenuOPEB()
  opa = int(input('Ingrese la opcion que desea del SubMenu OPERACIONES ESTADÍSTICAS BÁSICAS :'))
  while opa >0 and opa<5:
   canti = int(input("Cuantos numeros desea ingresar: "))
   if opa == 1:
    Prom(canti)
    opInser = input("\nDesea realizar otra operacion para PROMEDIO \n 1.SI \n 2.NO \n Rta: ")
    if opInser == "2":
     break
   elif opa == 2:
    Media(canti)
    opInser = input("\nDesea realizar otra operacion para MEDIA\n 1.SI \n 2.NO \n Rta: ")
    if opInser == "2":
     break
   elif opa == 3:
    Mediana(canti)
    opInser = input("\nDesea realizar otra operacion para MEDIANA\n 1.SI \n 2.NO \n Rta: ")
    if opInser == "2":
     break
   elif opa == 4:
    Moda(canti)
    opInser = input("\nDesea realizar otra operacion para MODA\n 1.SI \n 2.NO \n Rta: ")
    if opInser == "2":
     break
   elif opa == 5:
    break
 elif OpM =="5":
  print("\nFin del Programa")
  break
 else: print("\nOpción Incorrecta")