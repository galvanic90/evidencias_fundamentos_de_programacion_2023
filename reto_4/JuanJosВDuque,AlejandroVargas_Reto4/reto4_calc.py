import math #Se importa la librer.a math, para operaciones matem.ticas

#A continuaci.n se definen las opciones para el men. principal de la calculadora
def menu_principal():
    print("Calculadora Cient.fica")
    print("1. Operaciones Aritm.ticas")
    print("2. Operaciones Aritm.ticas Extendidas")
    print("3. Operaciones Trigonom.tricas")
    print("4. Operaciones Estad.sticas")
    print("5. Salir")

#Se definen a continuaci.n las operaciones aritm.ticas: Suma, resta, multiplicaci.n y divisi.n
def operaciones_aritmeticas():
    print("Operaciones Aritm.ticas B.sicas")
    a = float(input("Ingrese el primer n.mero: "))
    b = float(input("Ingrese el segundo n.mero: "))
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicaci.n")
    print("4. Divisi.n")
    opcion = int(input("Seleccione una operaci.n (1,2,3 o 4): "))
    if opcion == 1:
        resultado = a + b  #Resultado de la suma
    elif opcion == 2:
        resultado = a - b  #Resultado de la resta
    elif opcion == 3:
        resultado = a * b  #Resultado de la multiplicaci.n
    elif opcion == 4:
        if b != 0:
            resultado = a / b  #Resultado de la divisi.n
        else:
            resultado = "Error: divisi.n por cero" #Se arroja un string en el caso de que se tenga divisi.n por cero
    else:
        resultado = "Opci.n inv.lida"   #Se arroja un string, si el usuario no ingresa una de las opciones correctas
    print("Resultado:", resultado)

#Se define a continuaci.n las opoeraciones aritm.ticas extendidas
def operaciones_aritmeticas_extendidas():
    print("Operaciones Aritm.ticas Extendidas")
    numero = float(input("Ingrese un n.mero: "))
    print("1. Divisi.n Entera")
    print("2. Residuo")
    print("3. Exponenciaci.n")
    print("4. Ra.z cuadrada")
    print("5. Logaritmo en base 10")
    print("6. Logaritmo natural")
    print("7. Valor absoluto")
    print("8. Inverso")
    print("9. Factorial")
    opcion = int(input("Seleccione una operaci.n (1,2,3,4,5,6,7,8 o 9): "))
    if opcion == 1:
        divisor = float(input("Ingrese el divisor: "))
        resultado = numero // divisor  #Resultado de la divisi.n entera
    elif opcion == 2:
        divisor = float(input("Ingrese el divisor: "))
        resultado = numero % divisor  #Resultado del residuo de la divisi.n
    elif opcion == 3:
        exponente = float(input("Ingrese el exponente: "))
        resultado = numero ** exponente #Resultado de la operaci.n de exponenciaci.n
    elif opcion == 4:
        resultado = math.sqrt(numero)  #Resultado de raiz cuadrada
    elif opcion == 5:
        resultado = math.log10(numero)  #Resultado de logaritmo en base 10
    elif opcion == 6:
        resultado = math.log(numero)   #Resultado de logaritmo neperiano
    elif opcion == 7:
        resultado = abs(numero)     #Resultado de valor absoluto
    elif opcion == 8:
        if numero != 0:
            resultado = 1 / numero  #Resultado del inverso
        else:
            resultado = "Error: divisi.n por cero" #String de divisi.n por cero
    elif opcion == 9:
        resultado = math.factorial(int(numero))
    else:
        resultado = "Opci.n inv.lida"
    print("Resultado:", resultado)

#Operaciones trigonom.tricas
def operaciones_trigonometricas():
    print("Operaciones Trigonom.tricas")
    angulo = float(input("Ingrese el .ngulo en grados: "))
    radianes = math.radians(angulo)
    print("1. Seno")
    print("2. Tangente")
    opcion = int(input("Seleccione una operaci.n (1/2): "))
    if opcion == 1:
        resultado = math.sin(radianes)
    elif opcion == 2:
        resultado = math.tan(radianes)
    else:
        resultado = "Opci.n inv.lida"
    print("Resultado:", resultado)

#Operaciones estad.sticas 
def operaciones_estadisticas():
    print("Operaciones Estad.sticas B.sicas")
    n = int(input("Ingrese la cantidad de n.meros: "))
    numeros = []
    for i in range(n):
        numero = float(input(f"Ingrese el n.mero {i + 1}: "))
        numeros.append(numero)
    print("1. Promedio")
    print("2. Mediana")
    print("3. Moda")
    opcion = int(input("Seleccione una operaci.n (1/2/3): "))
    if opcion == 1:
        promedio = sum(numeros) / n
        resultado = promedio
    elif opcion == 2:
        numeros.sort()
        if n % 2 == 0:
            mediana = (numeros[n // 2 - 1] + numeros[n // 2]) / 2
        else:
            mediana = numeros[n // 2]
        resultado = mediana
    elif opcion == 3:
        from collections import Counter
        conteo = Counter(numeros)
        moda = [numero for numero, frecuencia in conteo.items() if frecuencia == max(conteo.values())]
        resultado = moda
    else:
        resultado = "Opci.n inv.lida"
    print("Resultado:", resultado)

#A continuaci.n se presenta un ciclo para mostrar el men. principal reiterativamente
while True:
    menu_principal()
    opcion_principal = int(input("Seleccione una opci.n (1,2,3,4 o 5): "))
    
    if opcion_principal == 1:
        operaciones_aritmeticas()
    elif opcion_principal == 2:
        operaciones_aritmeticas_extendidas()
    elif opcion_principal == 3:
        operaciones_trigonometricas()
    elif opcion_principal == 4:
        operaciones_estadisticas()
    elif opcion_principal == 5:
        print("Fin de la calculadora")
        break
    else:
        print("Opci.n inv.lida. Por favor, seleccione una opci.n v.lida.")
