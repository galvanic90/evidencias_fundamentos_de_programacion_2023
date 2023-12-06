#--------Calculadora--------#

# Variables iniciadoras

elementos=[]
total = 0

# Operaciones aritméticas básicas

def sumar(list):
  global total
  for n in list:
    total += n
  return total

def restar(list):
  if len(list)==1:
    return list[0]
  else:
    return restar(list[:-1])-list[-1]
    

def multiplicar(list):
  mult = 1 #inicializo en 1 porque multiplicar por cero da cero siempre
  for i in list: #recorro el arreglo, multiplicando los elementos
      mult = mult*i
  return mult

def dividir(num1,num2):
  if(num2==0):
    print("No se puede dividir por 0")
  else:
    return num1/num2

# Operaciones matemáticas extendidas

def div_ent(num1,num2):
  if(num2==0):
    print("No se puede dividir por 0")
  else:
    return num1//num2

def residuo(num1,num2):
  if(num2==0):
    print("No se puede dividir por 0")
  else:
    return num1%num2

def potencia(num1,num2):
  if(num2==0):
    return 1
  else:
    return num1**num2

def radica(num1,num2):
  if(num1==0):
    return 0
  elif(num1 < 0):
    print("No se puede radicar un número negativo")
  elif(num2==2):
    return num1**(1/float(num2))
  elif(num2==3):
    return num1**(1/float(num2))
  elif(num2==4):
    return num1**(1/float(num2))
  elif(num2==5):
    return num1**(1/float(num2))
  else:
    print(f"No se puede calcular la raíz del número {num1}")

def log_diez(num1):
  if(num1==1):
    return 0
  else:
     v = 0.87*((num1-1)/(num1+1))*((((num1-1)/(num1+1))**2)*((1/3)+(1/5)*((num1-1)/(num1+1))**2)+1)
  return v

def logaritmo(num1):
  if(num1==1):
    return 0
  else:
     v = 0.87*(((num1-1)/(num1+1))*((((num1-1)/(num1+1))**2)*((1/3)+(1/5)*((num1-1)/(num1+1))**2)+1))*2.3025
  return v

def valor_abs(num1):
  if num1 >=0:
    return num1
  else:
    return -num1

def fraccion(num1): #inverso
  print(f"1/{num1}")

def factorial(num1):
  if num1 == 1 or num1 == 0:
    return 1
  else:
    return num1 * factorial(num1 - 1)

# Operaciones Trigonométricas
pi = 3.1415926535897932384626433832795028841971

def deg(num1):
    rad = num1 * pi/180
    return rad

def seno(num1):  # Utilizo la expansión de Seno de Taylor
    k = 0
    seno = 0
    while num1 >= pi:
        num1 -= pi
    if pi > num1 > pi / 2:
        num1x = pi - num1
    while k < 15:
        seno += (-1)**k * num1**(2*k + 1) / factorial(2*k + 1)
        k += 1
    return seno

def coseno(num1):
  coseno = (1-(seno(num1)**2))**0.5
  return coseno

def tangente(num1):
  tangente = seno(num1)/coseno(num1)
  return tangente

# Operaciones estadísticas básicas

def promedio(list): #Es lo mismo que la media
  return sumar(list)/len(list)

def mediana(list):
  list.sort() # Organizar de menor a mayor los datos
  longitud = len(list) #Determino la cantidad de elementos en el arreglo
  mitad = int(longitud / 2) #Calculo la mitad del arreglo
    # Si la longitud es par, promediar elementos centrales
  if longitud % 2 == 0:
      mediana = (list[mitad - 1]+list[mitad]) / 2
  else:
        # Si no, es la del centro
      mediana = list[mitad]
  return mediana

def moda(list):
  repetidos = 0 #inicializo la variable para identificar los números repetidos
  for i in list: #recorro la lista en busca de elementos repetidos
      n = list.count(i)
      if n > repetidos:
          repetidos = n
  moda = [] #Arreglo donde se guardara el o los valores de mayor frecuencia o repetidos
  for i in list:
      n = list.count(i) # Devuelve el número de veces que x aparece enla lista.
      if n == repetidos and i not in moda:
          moda.append(i)
  if len(moda) != len(list):
      return moda
  else:
      print ('No hay moda')

# Menucillos

print("Bienvenido, ¡Vamos a calcular!")

while True:
  print('''Digite la opción que desea ejecutar:
  1. Suma
  2. Resta
  3. Multiplicación
  4. División
  5. División Entera
  6. Residuo
  7. Exponenciación
  8. Radicación
  9. Logaritmo base 10
  10. Logaritmo
  11. Valor absoluto
  12. Inverso
  13. Factorial
  14. Seno
  15. Coseno
  16. Tangente
  17. Promedio
  18. Mediana
  19. Moda
  20. Salir de la calculadora
   ''')
  c = int(input())
  if c == 20:
    print("Gracias por usar esta calculadora")
    break
  elif c == 1:
    valor=int(input("Ingresar valores a sumar (0 para finalizar):"))
    while valor!=0:
      elementos.append(valor)
      valor=int(input("Ingresar valores a sumar (0 para finalizar):"))
    print(sumar(elementos))
  elif c == 2:
    valor=int(input("Ingresar valores a restar (0 para finalizar):"))
    while valor!=0:
      elementos.append(valor)
      valor=int(input("Ingresar valores a restar (0 para finalizar):"))
    print(restar(elementos))
  elif c == 3:
    valor=int(input("Ingresar valores a multiplicar (0 para finalizar):"))
    while valor!=0:
      elementos.append(valor)
      valor=int(input("Ingresar valores a multiplicar (0 para finalizar):"))
    print(multiplicar(elementos))
  elif c == 4:
    x=int(input("Ingrese el primer número: "))
    y=int(input("Ingrese el segundo número: "))
    print(dividir(x,y))
  elif c == 5:
    x=int(input("Ingrese el primer número: "))
    y=int(input("Ingrese el segundo número: "))
    print(div_ent(x,y))
  elif c == 6:
    x=int(input("Ingrese el primer número: "))
    y=int(input("Ingrese el segundo número: "))
    print(residuo(x,y))
  elif c == 7:
    x=int(input("Ingrese el número que quiere elevar: "))
    y=int(input("Ingrese el exponente: "))
    print(potencia(x,y))
  elif c == 8:
    x=int(input("El número a radicar: "))
    y=int(input("Solo digitar para sacar raiz: 2-3-5-7: "))
    print(radica(x,y))
  elif c == 9:
    x=int(input("Ingrese el número: "))
    print(log_diez(x))
  elif c == 10:
    x=int(input("Ingrese el número: "))
    print(logaritmo(x))
  elif c == 11:
    x=int(input("Ingrese el número: "))
    print(valor_abs(x))
  elif c == 12:
    x=int(input("Ingrese el número: "))
    print(fraccion(x))
  elif c == 13:
    x=int(input("Ingrese el número: "))
    print(factorial(x))
  elif c == 14:
    x=int(input("Ingrese el número: "))
    print(seno(x))
  elif c == 15:
    x=int(input("Ingrese el número: "))
    print(coseno(x))
  elif c == 16:
    x=int(input("Ingrese el número: "))
    print(tangente(x))
  elif c == 17:
    valor=int(input("Ingresar valores a promediar (0 para finalizar):"))
    while valor!=0:
      elementos.append(valor)
      valor=int(input("Ingresar valores a promediar (0 para finalizar):"))
    print(promedio(elementos))
  elif c == 18:
    valor=int(input("Ingresar valores para buscar la mediana (0 para finalizar):"))
    while valor!=0:
      elementos.append(valor)
      valor=int(input("Ingresar valores para buscar la mediana (0 para finalizar):"))
    print(mediana(elementos))
  elif c == 19:
    valor=int(input("Ingresar valores para buscar la moda (0 para finalizar):"))
    while valor!=0:
      elementos.append(valor)
      valor=int(input("Ingresar valores para buscar la moda (0 para finalizar):"))
    print(moda(elementos))
  else:
    print("Ingrese una opción válida")
