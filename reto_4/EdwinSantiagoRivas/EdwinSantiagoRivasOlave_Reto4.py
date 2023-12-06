# Operaciones aritmeticas básicas

def sumar(x, y):
    return x + y

def restar(x, y):
    return x - y

def multiplicar(x, y):
    return x * y

def dividir(x, y):
    if y != 0:
        return x / y
    else:
        return('Error. No se puede dividir por 0')

# Operaciones aritméticas extendidas

def div_entera(x, y):
    if y != 0:
        return x // y
    else:
        return('Error. No se puede dividir por 0')

def residuo(x, y):
    if y != 0:
        return x % y
    else:
        return('Error. No se puede dividir por 0')

def exponenciacion(x, y):
    return x ** y

def raiz_cuadrada(x, n):

    if n == 0:
        return 1
    elif n > 0:
        return x ** (1 / n)
    else:
        return('Error. El índice debe ser mayor que 0')

def logaritmo_10(a):
    if a > 0:
                # a = Número a calcular
        y = 0   # y = Logaritmo base 10

        if a >= 10:
            a /= 10
            y += 1
            return a

def fraccion(x):
    if x != 0:
        resultado = 1 / x
        return resultado
    else:
        return("Error. No se puede calcular 1/número de 0.")

def factorial(n):
    if n == 1:
        return n
    elif n < 0:
        return('Error. Solo se calculan números enteros-no negativos')
    else:
        return n * factorial(n-1)

def logaritmo(a, b):
    # a = antilogaritmo, b = base, c = logaritmo
    c = 0
    if a >= b:
        a /= b
        c += 1
        return c
# Operaciones estadísticas
def media(lista):
    media = sum(lista) / len(lista)
    return media

def mediana(lista):

    # Calcular longitud de la lista
    longitud = len(lista)

    ordenar_lista = sorted(lista)  # sorted es una función que ordena una lista
    if longitud % 2 == 0:
        # Si la longitud es par, la mediana es el promedio de los dos números del medio
        mitad1 = ordenar_lista[longitud // 2 - 1]
        mitad2 = ordenar_lista[longitud // 2]
        mediana = (mitad1 + mitad2) / 2
    else:
        # Si la longitud es impar, la mediana es el número del medio
        mediana = ordenar_lista[longitud // 2]
    return mediana

# Moda con libreria
from statistics import mode  # Fue complejo hallar la moda con código por paso asi que toco usar la libreria statistics xD

# Operaciones trigonométricas
import math   # 'import math'para hallar seno, coseno

def calculadora_cientifica():
    print('''Calculadora científica encendida(on)\n
    1. Operaciones aritméticas básicas
    2. Operaciones aritméticas extendidas
    3. Operaciones estadísticas
    4. Operaciones trigonométricas
    5. Apagar calculadora   
    ''')

    # Se define el tipo de operación básica como submenú
    def operacion_basica():
        print('''
        1. Suma
        2. Resta
        3. Multiplicación
        4. División
        5. Volver
        ''')

        elegir_operacion = input('Elige la operacion: ')

        if elegir_operacion == '5':
            return calculadora_cientifica()     # Me devuelve al menú principal
        
        # Para cada operación se le define la misma entrada de datos ya que todos ellos se calculan tipos int y float
        primer_valor = float(input('Digite el 1er número: '))
        segundo_valor = float(input('Digite el 2do número: '))

        if elegir_operacion == '1':
            resultado = sumar(primer_valor, segundo_valor)
        elif elegir_operacion == '2':
            resultado = restar(primer_valor, segundo_valor)
        elif elegir_operacion == '3':
            resultado = multiplicar(primer_valor, segundo_valor)
        elif elegir_operacion == '4':
            resultado = dividir(primer_valor, segundo_valor)

        print(f'El resultado de la operación es igual: {resultado}')

    # Se define el tipo de operación extendida como submenú
    def operacion_extendida():
        print('''
        1. División entera
        2. Residuo
        3. Exponenciación a la n de número
        4. Raíz n de un número
        5. Logaritmo en base 10
        6. Valor absoluto
        7. 1/número
        8. Factorial
        9. Logaritmo
        10. Volver
        ''')
        elegir_operacion = input('Elige la operacion: ')

        # cada condicional tiene su input ya que cada operacion se calcula con diferentes valores entre int y float
        if elegir_operacion == '1':
            primer_valor = float(input('Digite el número dividiendo: '))
            segundo_valor = float(input('Digite el número divisor: '))
            resultado = div_entera(primer_valor, segundo_valor)
            print(f'El resultado de la operación es igual: {resultado}')

        elif elegir_operacion == '2':
            primer_valor = float(input('Digite el número dividiendo: '))
            segundo_valor = float(input('Digite el número divisor: '))
            resultado = residuo(primer_valor, segundo_valor)
            print(f'El resultado de la operación es igual: {resultado}')

        elif elegir_operacion == '3':
            primer_valor = int(input('Digite el número base(a): '))
            segundo_valor = int(input('Digite el número exponente(n): '))
            resultado = exponenciacion(primer_valor, segundo_valor)
            print(f'El resultado de la operación es igual: {resultado}')

        elif elegir_operacion == '4':
            primer_valor = float(input('Digite el número radical de la raíz √: '))
            segundo_valor = int(input('Digite el índice de la raíz (Ej: 2 para la raíz cuadrada): '))
            resultado = raiz_cuadrada(primer_valor, segundo_valor)
            print(f'El resultado de la operación es igual: {resultado}')

        elif elegir_operacion == '5':
            primer_valor = int(input('Logaritmo en base 10 de: '))
            if primer_valor <= 0:
                print('El numero debe de ser mayor que 0')
            else:
                resultado = logaritmo_10(primer_valor)
                print(f'El logaritmo en base 10 de {primer_valor} es: {resultado}')

        elif elegir_operacion == '6':
            primer_valor = int(input('Digite el número: '))
            resultado = abs(primer_valor)
            print(f'El valor absoluto de {primer_valor} es {resultado}')

        elif elegir_operacion == '7':
            primer_valor = int(input('Digite el número 1/: '))
            resultado = fraccion(primer_valor)
            print(f'El valor fraccionario de 1/{primer_valor} es: {resultado}')

        elif elegir_operacion == '8':
            primer_valor = int(input('Digite el número a calcular el factorial: '))
            resultado = factorial(primer_valor)
            print(f'El factorial de {primer_valor} es: {resultado}')

        elif elegir_operacion == '9':
            primer_valor = int(input('Digite el número del logaritmo: '))
            segundo_valor = int(input('Digite la base del logaritmo: '))
            if primer_valor <= 0 or segundo_valor <= 0:
                print('Ambos números deben ser mayores que 0')
            else:
                resultado = logaritmo(primer_valor, segundo_valor)
                print(f'El logaritmo en base {primer_valor} de {segundo_valor} es (≈): {resultado}')
        elif elegir_operacion == '10':
            return calculadora_cientifica()     # Me devuelve al menú principal

    # Se define el tipo de operación estadística como submenú
    def operacion_estadistica():
        print('''
        1. Media
        2. Mediana
        3. Moda
        4. Volver
        ''')
        elegir_operacion = input('Elige la operacion: ')

        if elegir_operacion == '4':
            return calculadora_cientifica()     # Me devuelve al menú principal

        # Se ingresa un máximo de 7 números para hallar media. mediana, moda
        primer_valor = int(input('Digite el 1er número: '))
        segundo_valor = int(input('Digite el 2do número: '))
        tercer_valor = int(input('Digite el 3er número: '))
        cuarto_valor = int(input('Digite el 4to número: '))
        quinto_valor = int(input('Digite el 5to número: '))
        sexto_valor = int(input('Digite el 6to número: '))
        septimo_valor = int(input('Digite el 7mo número: '))

        numeros = [primer_valor, segundo_valor, tercer_valor, cuarto_valor, quinto_valor, sexto_valor, septimo_valor]

        if elegir_operacion == '1':
            resultado = media(numeros)
            print(f'La media es: {resultado}')
        elif elegir_operacion == '2':
            resultado = mediana(numeros)
            print(f'La mediana es: {resultado}')
        elif elegir_operacion == '3':
            resultado = mode(numeros)
            print(f"La moda es: {resultado}")
        
    # Se define el tipo de operación trigonométrica como submenú
    def operacion_trigonometrica():

        print('''
        1. Seno
        2. Coseno
        3. Volver
        ''')
        elegir_operacion = input('Elige la operacion: ')

        if elegir_operacion == '1':
            x = int(input('Ingrese el valor para hallar seno: '))
            print(f'Seno de {x} es: {math.sin(x)}')

        elif elegir_operacion == '2':
            x = int(input('Ingrese el valor para hallar coseno: '))
            print(f'Coseno de {x} es: {math.cos(x)}')
        elif elegir_operacion == '3':
            return calculadora_cientifica()     # Me devuelve al menú principal

# Elegir el tipo de operación básica, extentida, estadística, trigonométrica

    elegir_tipo_operacion = input('Ingresa el dígito del tipo de opereación a realizar: ')

    if elegir_tipo_operacion  == '1':
        operacion_basica()
    elif elegir_tipo_operacion  == '2':
        operacion_extendida()
    elif elegir_tipo_operacion  == '3':
        operacion_estadistica()
    elif elegir_tipo_operacion  == '4':
        operacion_trigonometrica()
    elif elegir_tipo_operacion == '5':
        print('Calculadora científica apagada(off)')

calculadora_cientifica()