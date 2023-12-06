# -*- coding: utf-8 -*-
"""
Created on Sun Sep 10 16:07:19 2023

@author: erika
"""

while (True):   
    """ Bloque de funciones aritmeticas basicas"""         
    def sumar(elementos):
           suma=0
           for i in elementos:
               suma=suma+i
           return print(suma)
           False # -*-Con esta linea vuelve al menu ppal cada que hace una operacion -*-
       
    def multiplicar(elementos):
          
           mult = 1
           for i in elementos:
               mult = mult*i
           return print(mult)
           False# -*-Con esta linea vuelve al menu ppal cada que hace una operacion -*-
    def restar(a,b):
           return print(f'El resultado de tu resta es {a-b}')
           False# -*-Con esta linea vuelve al menu ppal cada que hace una operacion -*-
       
    def dividir(a,b):
           return print(f'El resultado de tu division es: {a/b}')
           False# -*-Con esta linea vuelve al menu ppal cada que hace una operacion -*-
           
    """ Bloque de operaciones aritmetocas extendidas"""
    def div_ent (a,b):
           resultado = int(a/b)
           return print(f'El resultado de tu division es: ' + str(resultado))
           False
    def residuo(a,b):
           residuo= a%b
           return print(residuo)
           False# -*-Con esta linea vuelve al menu ppal cada que hace una operacion -*-
       
    def exponente(a,b):  
           exp=pow(a, b)
           return print(exp) 
           False# -*-Con esta linea vuelve al menu ppal cada que hace una operacion -*-
       
    def raiz (a,b):
           raiz=pow(a,(1/b))
           return print(raiz)
           False# -*-Con esta linea vuelve al menu ppal cada que hace una operacion -*-
    def absoluto(a):
           va=abs(a)
           return print(va)
           False# -*-Con esta linea vuelve al menu ppal cada que hace una operacion -*-
       
    def inverso(a):
           inv=1/a
           return print(inv)
           False# -*-Con esta linea vuelve al menu ppal cada que hace una operacion -*-
    def factorial(a):
          if a==0 or a==1:
                   resultado=1
          elif a>1:
                   resultado=a*factorial(a-1)
          return print(resultado) 
          False# -*-Con esta linea vuelve al menu ppal cada que hace una operacion -*-
          
    """Bloque de operaciones estadisticas"""
    def promedio(elementos):
           
           for i in elementos:
               promedio=sumar(elementos)/len(elementos)
           return print(promedio)
           False# -*-Con esta linea vuelve al menu ppal cada que hace una operacion -*-
       
    def mediana (elementos):
           
           elementos.sort()
           longitud = len(elementos)
           mitad = int(longitud / 2)
           # Si la longitud es par, promediar elementos centrales
           if longitud % 2 == 0:
               mediana = (elementos[mitad - 1]+elementos[mitad]) / 2
           else:
               # Si no, es la del centro
               mediana = elementos[mitad]
           return print(mediana)
           False# -*-Con esta linea vuelve al menu ppal cada que hace una operacion -*-
           
    def moda(elementos):
           valores = {valor:elementos.count(valor) for valor in set(elementos)}
           maximo = max(valores.values())
           modas = {k:v for k, v  in valores.items() if v == maximo}
           
           if len(modas) == 1:
               print(f"La moda es {list(modas)[0]}, con {maximo} ocurrencias")
           else:
               print("Las modas son: ")
               for k in modas.keys():
                   print(f"Moda {k}, con {maximo} ocurrencias")
                        
           False# -*-Con esta linea vuelve al menu ppal cada que hace una operacion -*-
    def main (opcion):
         
         if opcion == '1':
             sumar(elementos)
         elif opcion == '2':
             restar(a,b)
         elif opcion == '3':
             multiplicar(elementos)
         elif opcion == '4':
             dividir(a,b)
         elif opcion == '5':
             div_ent(a,b)
         elif opcion == '6':
             residuo(a,b)
         elif opcion == '7':
             exponente(a,b)
         elif opcion == '8':
             raiz(a,b)
         elif opcion == '9':
             absoluto(a)
         elif opcion =='a':
             inverso(a)
         elif opcion =='b':
             factorial(a)
         elif opcion =='c':
             promedio(elementos)
         elif opcion =='d':
             mediana(elementos)
         elif opcion =='e':
             moda(elementos)
         else:
             print('ERROR: Ingresaste una opcion incorrecta')
         return
         
    if __name__ == "__main__":
    
      # -*-Menu para escoger las operaciones a realizar -*-     
    
             opcion = input(''''Bienvenido a su calculadora
                            Elija la operacion que dese realizar 
                        1. Operaciones aritmeticas basicas
                            Sumar -------------------->  1
                            Restar ------------------->  2
                            Multiplicar -------------->  3
                            Dividir ------------------>  4
                        2. Operaciones aritmeticas extendidas
                            Division entera ---------->  5
                            Residuo ------------------>  6
                            Exponenciacion ----------->  7
                            Raiz --------------------->  8
                            Valor absoluto ----------->  9
                            Inverso (1/N) ------------>  a
                            Factorial ---------------->  b
                        3. Operaciones estadisticas basicas
                            Promedio ----------------->  c
                            Mediana ------------------>  d
                            Moda --------------------->  e''')
             opcion = opcion.lower()
         
             if opcion =='1'or opcion =='3' or opcion =='c'or opcion =='d' or opcion =='e' :
    
                 x = int(input('Cuantos elementos deseas ingresar: '))
        
                 elementos = []
                 for i in range(x):
                     X=int(input(f'Ingresa tu {i+1} numero: '))
                     elementos.append(X)
                 print(elementos)
                 main(opcion)
                 
             elif opcion =='2'or opcion =='4' or opcion =='5'or opcion =='6' or opcion =='7'or opcion =='8':
                 a = float(input('Ingresa tu primer numero: '))
                 b = float(input('Ingresa tu segundo numero: '))
                 main(opcion)
             elif opcion =='9'or opcion =='a' or opcion =='b'or opcion =='c' or opcion =='d'or opcion =='e':
                 y=float(input('Ingresa un numero: '))
                 main(opcion)
             else:
                 print('ERROR: Ingresaste una opcion incorrecta')
                     
    
            
       
    
    
