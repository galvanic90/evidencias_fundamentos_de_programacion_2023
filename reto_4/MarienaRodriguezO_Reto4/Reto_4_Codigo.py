"""
Reto Semana 4
 
Presentado por:
    Mariena Rodriguez Oquendo
    CC. 1085331871
    
"""

###### Definición de Operaciones a realizar ######

### Operaciones aritméticas básicas ###
def suma(x, y):    # Definición de Suma
    return x + y

def resta(x, y):   # Definición de Resta
    return x - y

def multiplicacion(x, y): # Definición de Multiplicación
    return x * y

def division(x, y):       # Definición de División
    if y == 0:
        return 'Error, no se puede dividir por cero'
    return x / y

### Operaciones aritméticas extendidas ###
def division_entera(x, y):  # Definición de División Entera
    if y == 0:
        return "Error: no se puede dividir por cero."
    return x // y

def residuo(x, y):          # Definición de Residuo
    if y == 0:
        return 'Error, no se puede dividir por cero'
    return x % y

def exponente(x, n):        # Definición de Exponenciación
    result = 1
    for _ in range(int(n)):
        result *= x
    return result

def raiz(x, n):             # Definición de Raíz
    if n == 0:
        return 'Error, el índice de la raíz no puede ser cero'
    return x ** (1 / n)

### Operaciones Estadísticas Básicas ###
def calcular_promedio(lista):   # Como calcular el Promedio
    if lista == 0:
        return 'Error: La lista se encuentra vacía'
    total = 0
    for num in lista:
        total += num
    return total / len(lista)

def calcular_mediana(lista):    # Como calcular la Mediana
    lista_m = sorted(lista)
    
    n = len(lista_m)   # Calcular la longitud de la lista
    
    if n % 2 == 1:     # Si la longitud de la lista es impar, devuelve el número del medio
        return lista_m[n // 2]
    else:              # Si la longitud de la lista es par, devuelve el promedio de los dos números del medio
        medio1 = lista_m [n // 2 - 1]
        medio2 = lista_m [n // 2]
        return (medio1 + medio2) / 2

def calcular_moda(lista):       # Como calcular la Moda
    if lista == 0:
        return 'Error, la lista se encuentra vacía'
    contador = {}
    for elemento in lista:
        if elemento in contador:
            contador[elemento] += 1
        else:
            contador[elemento] = 1
    moda = []
    max_frecuencia = 0
    for elemento, frecuencia in contador.items():
        if frecuencia > max_frecuencia:
            moda = [elemento]
            max_frecuencia = frecuencia
        elif frecuencia == max_frecuencia:
            moda.append(elemento)
    if max_frecuencia == 1:
        return 'No se ha encontrado moda en la lista'
    return moda

##########  #############
while True:
    print('Bienvenido a la Calculadora Científica')
    
    opcion = input(''' Elija la operación que desea realizar:
                   1: Suma
                   2: Resta
                   3: Multiplicación
                   4: División
                   5: División Entera
                   6: Residuo
                   7: Exponenciación 
                   8: Raíz
                   9: Promedio o Media
                   10: Mediana
                   11: Moda
                   12: Salir
                   ''')

    if opcion in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']:

        # Operaciones Aritméticas 
        if opcion in ['1', '2', '3', '4', '5', '6', '7', '8']:
            if opcion in ['1', '2', '3', '4', '5', '6']:
                num1 = float(input('Ingrese el primer número: '))
                num2 = float(input('Ingrese el segundo número: '))
                            
                if opcion == '1':
                    print('La suma es de: ', suma(num1, num2))
                elif opcion == '2':
                    print('La resta es de: ', resta(num1, num2))
                elif opcion == '3':
                    print('La multiplicación es de: ', multiplicacion(num1, num2))
                elif opcion == '4':
                    print('La división es de: ', division(num1, num2))
                elif opcion == '5':
                    print('La división entera es de: ', division_entera(num1, num2))
                elif opcion == '6':
                    print('El residuo es de: ', residuo(num1, num2))
            
            if opcion in ['7', '8']:  
                num1 = float(input('Ingrese un número: '))
                if opcion == '7':
                    n = float(input('Ingrese el número correspondiente a el exponente: '))
                    print('La exponenciación es de: ', exponente(num1, n))
                elif opcion == '8':
                    n = float(input('Ingrese el número correspondiente al índice de la raíz: '))
                    print('La raíz es de: ', raiz(num1, n))

        # Operaciones Estadísticas
        elif opcion in ['9', '10', '11']:
            lista = input('Ingrese una lista de números separados por espacio: ').split()
            lista = [float(x) for x in lista]
            
            if opcion == '9':
                print('El promedio es de: ', calcular_promedio(lista))
            elif opcion == '10':
                print('La mediana es de: ', calcular_mediana(lista))
            elif opcion == '11':
                print('La moda es de: ', calcular_moda(lista))
                                
        if opcion == '12':
                print('Esta saliendo de la calculadora científica.')
                break
                
    else:
        print('Opción no válida, seleccione una opción del menú.')
  