#creamos una funcion para poder restar varios numeros
def resta(valores):
    
    resultado= valores[0] 
    for i in range (1,len(valores)):
        resultado -= valores[i]
    return resultado
    

#creamos una funcion para calcular el inverso
def inv_mod(num1,num2):
 
    for x in range(1,num2):
        if((num1%num2)*(x%num2) % num2==1):
            return x

   
#creamos una funcion para hayar el factorial      
def factorial(n): 
    if n==0 or n==1:
       resultado=1
    elif n>1:
       resultado=n*factorial(n-1)
    return resultado


#creamos una funcion para encontrar la cotangente
def cotangente (n):
   import math
   c = math.radians(n)
   cot= ((math.cos(c))/(math.sin(c)))
   return cot  
   #La función math.radians() convierte la medida del ángulo de sexagesimal a radianes.


def menu(): #funcion para llamar el menu sin tener que ecribirlo nueva/

 print('''
*** Calculadora P & L***

    Operaciones Básicas
 1  Suma
 2  Resta
 3  Multiplicacion
 4  Division
    
	Operaciones Extendidas
 5  División entera
 6  Residuo
 7  Exponenciación
 8  Raíz n
 9  Logaritmo en base 10
10  Logaritmo
11  Valor absoluto
12  Inverso Modular
13  Factorial

    Operaciones Trigonometricas
14  Seno
15  Coseno
16  Tangente
17  Cotangente

    Operaciones Estadísticas
18  Promedio
19  Media
20  Mediana
21  Moda

 0  Salir


''')


def calculadora(): #creando la funcion calculadora
    
    menu() #funcion creada anteriormente
    opc = input('Dime: ¿Que operación quieres hacer?: ')
    print('')    
    
    while True:
              
        if opc == '1':
            valores=[] #creamos una lista llamada valores que será ingresada por teclado
            print('Ingresa los valores uno a uno y 0 para finalizar')
            num=int(input('Ingresa valor:'))
            while num != 0:
                valores.append(num)  #append para añadir elementos a la lista
                num=int(input('Ingresa valor:'))
          
            print('Los valores que ingresaste fueron:',(valores))
            print('La Suma de estos valores es:', (sum(valores)))
            print('')
            menu()
            opc = input('Dime: ¿Que operación quieres hacer?: ')
         
        elif opc == '2':
            valores=[] #creamos una lista llamada valores que será ingresada por teclado
            print('Ingresa los valores uno a uno y 0 para finalizar')
            num=int(input('Ingresa valor:'))
            while num != 0:
                valores.append(num)  #append para añadir elementos a la lista
                num=int(input('Ingresa valor:'))
            
            print('Los valores que ingresaste fueron:',(valores))
                
            print('La RESTA de estos números es: ', resta(valores))
            print('') #imprimimos un renglon vacio por estetica
            menu()
            opc = input('Dime: ¿Que operación quieres hacer?: ')
   
        elif opc == '3':
            num1 = float(input('Ingrese Número uno: '))
            num2 = float(input('Ingrese Número dos: '))
            print ('La MULTIPLICACIÓN de estos dos números es: ', num1*num2)
            print('')
            menu()
            opc = input('Dime: ¿Que operación quieres hacer?: ')
   
        elif opc == '4':
            num1 = float(input('Ingrese Dividendo: '))
            num2 = float(input('Ingrese Divisor: ')) 
            if num2 !=0:
                print ('La DIVISIÓN entre estos dos números es: ', num1/num2)
            else:
                print ('Oh Oh, no podemos DIVIDIR por 0')
             
            print('')
            menu()
            opc = input('Dime: ¿Que operación quieres hacer?: ')
                     
        elif opc == '5':
            num1 = float(input('Ingrese Dividendo: '))
            num2 = float(input('Ingrese Divisor: ')) 
            if num2 !=0:
               print ('La DIVISIÓN ENTERA entre estos dos números es: ', num1//num2)
            else:
               print ('Oh Oh, no podemos DIVIDIR por 0')
            
            print('')
            menu()
            opc = input('Dime: ¿Que operación quieres hacer?: ')    
            
        elif opc == '6':
            num1 = float(input('Ingrese Dividendo: '))
            num2 = float(input('Ingrese Divisor: ')) 
            print ('El RESIDUO de la DIVISIÓN entre estos dos números es: ', num1%num2)
            print('')
            menu()
            opc = input('Dime: ¿Que operación quieres hacer?: ')

        elif opc == '7':
            num1 = float(input('Ingrese Numero: '))
            num2 = float(input('Exponenciado a: ')) 
            print ('El calculo de estos EXPONENTES es: ', num1**num2)
            print('')
            menu()
            opc = input('Dime: ¿Que operación quieres hacer?: ')            
                 
        elif opc == '8': # El punto . después de 1 y 2 o 3 o 4 o 5 son para forzar que sean tratados como flotantes
            num1 = float(input('Ingrese Numero: '))
            num2 = float(input('¿Que raíz quieres sacar?: ')) 
            if num2 == 2: 
                print ('La RAIZ CUADRADA de este número es: ', num1**(1./2.))
            elif num2 == 3:
                print ('La RAIZ CUBICA de este número es: ', num1**(1./3.))
            elif num2 == 4:
                print ('La RAIZ CUARTA de este número es: ', num1**(1./4.))
            elif num2 == 5:
                print ('La RAIZ QUINTA de este número es: ', num1**(1./5.))
            else:
                print('Por el momento solo puedes sacar Raiz cuadrada, cubica, cuarta y quinta')
                print('No puedo ayudarte con esta operación')
            print('')
            menu()
            opc = input('Dime: ¿Que operación quieres hacer?: ')
          
        elif opc == '9':
            num1 = float(input('Ingrese Numero: '))
            num2 = 10 
            import math #importamos libreria math
            respuesta= math.log(num1,num2)
            print ('El logaritmo base 10 de', num1, 'es', respuesta)
            print('')
            menu()
            opc = input('Dime: ¿Que operación quieres hacer?: ')            
                  
        elif opc == '10':
             num1 = float(input('Ingrese Numero: '))
             num2 = int(input('Ingrese Numero Base: '))
             import math
             respuesta= math.log(num1,num2)
             print ('El logaritmo base', num2, 'de', num1, 'es', respuesta)
             print('')
             menu()
             opc = input('Dime: ¿Que operación quieres hacer?: ')   
         
        elif opc == '11': # valor absoluto de un número es su distancia desde cero en una recta numérica
             num1 = float(input('Ingrese Numero: '))
             print ('El valor absoluto de', num1, 'es', abs(num1))
             print('')
             menu()
             opc = input('Dime: ¿Que operación quieres hacer?: ') 
             
        elif opc == '12': # el inverso de un # es otro # que multiplicado por el primero de 1
             num1 = int(input('Ingrese el Numero: '))
             num2 = int(input('Ingrese el Modulo: '))
             print ('El inverso multiplicativo modular es', inv_mod(num1,num2))
             print('')
             menu()
             opc = input('Dime: ¿Que operación quieres hacer?: ') 
                         
        elif opc == '13':#factorial de un número es el resultado de multiplicar ese número por todos los números que existen desde él hasta el
             num1 = int(input('Ingrese Numero: '))
             print('El facctorial de', num1,'es', factorial(num1))        
             print('')
             menu()
             opc = input('Dime: ¿Que operación quieres hacer?: ') 
                
        elif opc == '14':
             num1 = int(input('Ingrese un Valor para el angulo: '))
             import math
             print ('El Seno de un ángulo de', num1, 'es', math.sin(num1), 'radianes')
             print('')
             menu()
             opc = input('Dime: ¿Que operación quieres hacer?: ')   
              
        elif opc == '15':
             num1 = int(input('Ingrese un Valor para el angulo: '))
             import math
             print ('El Coseno de un angulo de', num1, 'es', math.cos(num1), 'radianes')
             print('')
             menu()
             opc = input('Dime: ¿Que operación quieres hacer?: ')   
                      
        elif opc == '16':
             num1 = int(input('Ingrese un Valor para el angulo: '))
             import math
             print ('La Tangente de', num1, 'es', math.tan(num1), 'radianes')
             print('')
             menu()
             opc = input('Dime: ¿Que operación quieres hacer?: ')    
                
        elif opc == '17': 
             num1 = int(input('Ingrese un Valor para el angulo: '))
             print ('La Cotangente de un angulo de', num1, 'es', cotangente(num1), 'radianes')
             print('')
             menu()
             opc = input('Dime: ¿Que operación quieres hacer?: ')    
           
        elif opc == '18': 
            valores=[] #creamos una lista llamada valores que será ingresada por teclado
            print('Ingresa los valores uno a uno y 0 para finalizar')
            num=int(input('Ingresa valor:'))
            from statistics import mean # otra forma de importar funciones
            while num != 0:             #importamos la función mean para calcular promedio
                valores.append(num)
                num=int(input('Ingresa valor:'))
          
            print('Los valores que ingresaste fueron:',(valores))
            print('El Promedio de estos valores es:', (mean(valores)))
            print('')
            menu()
            opc = input('Dime: ¿Que operación quieres hacer?: ')       
           
        elif opc == '19':
            valores=[] #creamos una lista llamada valores que será ingresada por teclado
            print('Ingresa los valores uno a uno y 0 para finalizar')
            num=int(input('Ingresa valor:'))
            from statistics import harmonic_mean #importamos la función harmonic_mean para calcular media
            while num != 0:
                valores.append(num)
                num=int(input('Ingresa valor:'))
          
            print('Los valores que ingresaste fueron:',(valores))
            print('La Media de estos valores es:', (harmonic_mean(valores)))
            print('')
            menu()
            opc = input('Dime: ¿Que operación quieres hacer?: ')  
      
        elif opc == '20':
            valores=[] #creamos una lista llamada valores que será ingresada por teclado
            print('Ingresa los valores uno a uno y 0 para finalizar')
            num=int(input('Ingresa valor:'))
            from statistics import median #importamos la función median para calcular mediana
            while num != 0:
                valores.append(num)
                num=int(input('Ingresa valor:'))
          
            print('Los valores que ingresaste fueron:',(valores))
            print('La Mediana de estos valores es:', (median(valores)))
            print('')
            menu()
            opc = input('Dime: ¿Que operación quieres hacer?: ') 
     
        elif opc == '21':
            valores=[] #creamos una lista llamada valores que será ingresada por teclado
            print('Ingresa los valores uno a uno y 0 para finalizar')
            num=int(input('Ingresa valor:'))
            from statistics import mode #importamos la función mode para calcular moda
            while num != 0:
                valores.append(num)
                num=int(input('Ingresa valor:'))
          
            print('Los valores que ingresaste fueron:',(valores))
            print('La Moda de estos valores es:', (mode(valores)))
            print('')
            menu()
            opc = input('Dime: ¿Que operación quieres hacer?: ') 
          
        elif opc == '0':
            print('Fué un placer, hasta la próxima')
            
            break
                       
        
calculadora()
         
