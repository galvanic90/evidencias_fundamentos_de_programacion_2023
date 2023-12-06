opcion = 0 
#Menú principal de calculadora
while opcion != 12:
  print("""
  Indique la operación a realizar:

  0 Agregar o cambiar números
  1 Suma
  2 Resta
  3 Multiplicación
  4 División
  5 Valor absoluto
  6 División entera y residuo
  7 Potencia
  8 Raíz cuadrada
  9 Trigonometría (Seno, Coseno, Tangente)
  10 Estadistica (Promedio, media, mediana, moda)
  11 Terminar
        """)
  #Ingresar opción de operación por usuario
  opcion = int(input())
  
  #Ingresar valores
  if opcion == 0:
    numero1 = int(input("Introduzca el primer digito: "))
    numero2 = int(input("Introduzca el segundo digito: "))
  
  #Sumar dos números
  elif opcion == 1:
    print("")
    print("Resultado: ", numero1," + ", numero2," = ", numero1+numero2)
  
  #Restar dos números
  elif opcion == 2:
    print("")
    print("Resultado: ", numero1," - ", numero2," = ", numero1-numero2)
  
  #Multiplicar dos números
  elif opcion == 3:
    print("")
    print("Resultado: ", numero1," * ", numero2," = ", numero1*numero2)
  
  #Dividir dos números
  elif opcion == 4:
    print("")
    print("Resultado: ", numero1," / ", numero2," = ", float(numero1/numero2))
  
  #Calcular valor absoluto de cada número
  elif opcion == 5:
    if numero1 <= 0:
      print(" Valor absoluto de ", numero1, " = ", numero1*-1)
    else: print ("Valor absoluto de", numero1, " = ", numero1)
    if numero2 <= 0:
        print("Valor absoluto de", numero2, " = ", numero2*-1)
    else: print ("Valor absoluto de", numero2, " = ", numero2)
  
  #División de dos números con su valor entero y residuo
  elif opcion == 6:
    print("")
    print("Resultado: Primer dígito es el valor entero y el segundo el residuo", divmod(numero1,numero2))
  
  #Operación exponente con dos número
  elif opcion == 7:
    if numero1 <= 0:
      print("Resultado: ", numero1**numero2)
    if numero1 > 0:
      print("Resultado: ", numero1**numero2)     
    if numero2 <= 0:
      print("Resultado: ", 1/numero1**numero2)
  
  #Raíz cuadrada de dos números
  elif opcion == 8:
    print("")
    print("Raíz número 1: ", " = ", numero1**(1/2))
    print("Raíz número 2: ", " = ", numero2**(1/2))
  
  #Introducir valores para calcular seno, coseno y tangente utilizando grados
  elif opcion == 9:
    import math
    numero1 = int(input("Introduzca los grados: "))
    print("")
    print("Seno de ", numero1," = ", math.sin(numero1))
    print("Coseno de ", numero1," = ", math.cos(numero1))
    print("Tangente de ", numero1," = ", math.tan(numero1))
  
  #Agregar cadena de valores para calcular valores estadísticos, se utiliza statistics función 
  elif opcion == 10:
    import statistics
    from statistics import mean
    from statistics import median, multimode

    datos = []

    valores = int(input("Indique el número de valores a ingresar: "))

    for i in range(valores):
        valor = float(input("Ingrese el valor: "))
        datos.append(valor)

    print(datos)
      #Ordenar los datos
    datos.sort()
    print(datos)
      #Mediada, media y moda
    print("Mediana")
    print(statistics.median(datos))
    print("Media")
    print(mean(datos))
    print("Moda")
    print(multimode(datos))

