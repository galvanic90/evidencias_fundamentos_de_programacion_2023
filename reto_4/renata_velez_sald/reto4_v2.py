import math

print("------------------------------------------------------------------" )
print("------------------------------------------------------------------" )
menuprincipal= int(input("Calculadora para realizar operaciones : \n 1 - aritmeticas basicas: \n 2 - aritméticas extendidas: \n 3 - trigonométricas:  \n 4 - estadísticas básicas:   \n Seleccion de la opcion de 1 al 4: "))
print("------------------------------------------------------------------" )

'''
Se importa la libreria math y statics para los calculos de la calculadora

-------------------------------------------------------------------------------------------------------------------------------------------------
-------------------------------------------------------------------------------------------------------------------------------------------------
El menu 1 permite calcular suma, resta, multiplicacion, division, division entera, residuo, potencia num1**num2 y raiz num1**(1/num2)
Este menu tiene dos entradas numerica: num1 y num2  
Luego tiene programada una clase llamada calculdora donde se definen todas las operaciones basicas y extendidas que utilicen dos numeros.
Adicionalmente la division tiene restriccion
----No se puede dividir por cero

-------------------------------------------------------------------------------------------------------------------------------------------------
-------------------------------------------------------------------------------------------------------------------------------------------------
El menu 2 permite calcular logaritmo en base 10, logaritmo, valor absoluto, 1/número, factorial
Este menu tiene una entrada numerica: num1. 
Luego tiene programada una clase llamada calculdora2 donde se definen todas las operaciones. 

Adicionalmente algunas de las funciones tiene restricciones.
----No se puede calcular el logaritmo natural ni base 10 de valores negativos ni de cero.
----No se puede calcular la inversa por division por cero

-------------------------------------------------------------------------------------------------------------------------------------------------
-------------------------------------------------------------------------------------------------------------------------------------------------
El menu 3 permite calcular operaciones trigonometricas en radianes como seno, coseno y tangente
Este menu tiene una entrada numerica: num1. 
Luego tiene programada una clase llamada calculdora3 donde se definen todas las operaciones. 

-------------------------------------------------------------------------------------------------------------------------------------------------
-------------------------------------------------------------------------------------------------------------------------------------------------
El menu 4 permite calcular estadísticas básicas: promedio, media, mediana, moda

Este menu tiene una entrada que permite definir a cuantos numeros se desea calcular  las estadicticas: num_estad. 
Luego tiene un ciclo for que genera el tamano de la lista acorde al numero anterior y permite la entrada de todos los elementos de la lista uno por uno. (un ciclo de n para generar la lista de numeros)
Luego se importa la libreria statistics import mean, median o multimode

'''


if menuprincipal==1:
    #-------------------------------------------------------------------------- 
    print("operaciones aritmeticas basicas y extendidas con 2 numeros como:" )
    print("suma, resta, multiplicacion, division, division entera, residuo, potencia num1**num2 y raiz num1**(1/num2)" )
    num1=int(input("Ingrese el numero 1:   "))
    num2=int(input("Ingrese el numero 2:   "))
    #-------------------------------------------------------------------------- 
    class calculadora():
        # --------------------------------------------------------------
        def suma(self,num1,num2):
            respuesta=num1+num2
            return respuesta
        # --------------------------------------------------------------
        def resta(self,num1,num2):
            respuesta=num1-num2
            return respuesta
        # --------------------------------------------------------------
        def multiplicacion(self,num1,num2):
            respuesta=num1*num2
            return respuesta
        # --------------------------------------------------------------   
        def division(self,num1,num2):
            if num2==0:
                print("No se puede dividir por cero")
            else:
                respuesta=num1/num2
                return respuesta
        # --------------------------------------------------------------   
        def divisionentera(self,num1,num2):
            if num2==0:
                print("No se puede dividir por el numero cero")
            else:
                respuesta=num1//num2
                return respuesta        
        # --------------------------------------------------------------   
        def residuo(self,num1,num2):
            if num2==0:
                print("No se puede dividir por el numero cero")
            else:
                respuesta=num1%num2
                return respuesta        
        # --------------------------------------------------------------
        def potencia(self,num1,num2):
            respuesta=num1**num2
            return respuesta    
        # --------------------------------------------------------------
        def raiz(self,num1,num2):
            if num2<=0:
                print("No se puede calcular raices negativas ni n**(1/0)--- (Se esta calculando n**(1/del numero 1) ")
            else:
                respuesta=num1**(1/num2)
                return respuesta    
        # --------------------------------------------------------------          
    calculadoracientifica=calculadora()  
    #-------------------------------------------------------------------------- 
    print("------------------------------------------------------------------" )
    print("Resultado de la suma es:  " + str(calculadoracientifica.suma(num1,num2)))
    print("------------------------------------------------------------------" )
    print("Resultado de la resta es:  " + str(calculadoracientifica.resta(num1,num2)))
    print("------------------------------------------------------------------" )
    print("Resultado de la multiplicacion es:  " + str(calculadoracientifica.multiplicacion(num1,num2)))
    print("------------------------------------------------------------------" )
    print("Resultado de la division es:  " + str(calculadoracientifica.division(num1,num2)))
    print("------------------------------------------------------------------" )
    print("Resultado de la division entera es:  " + str(calculadoracientifica.divisionentera(num1,num2)))
    print("------------------------------------------------------------------" )
    print("Resultado del residuo de la division es:  " + str(calculadoracientifica.residuo(num1,num2)))
    print("------------------------------------------------------------------" )
    print("Resultado de un numero elevada a una potencia es:  " + str(calculadoracientifica.potencia(num1,num2)))
    print("------------------------------------------------------------------" )
    print("Resultado de un numero elevada a una raiz es :  " + str(calculadoracientifica.raiz(num1,num2)))
    print("------------------------------------------------------------------" )
    #-------------------------------------------------------------------------- 

elif menuprincipal==2:
    #-------------------------------------------------------------------------- 
    print("operaciones extendidas con 1 numero como:" )
    print("logaritmo en base 10, logaritmo, valor absoluto, 1/número, factorial" )
    num1=int(input("Ingrese el numero 1:   "))
    #-------------------------------------------------------------------------- 
    class calculadora2():
        # --------------------------------------------------------------   
        def logaritmo(self,num1):
            if num1<=0:
                print("------------------------------------------------------------------" )
                print("No se puede calcular el logaritmo natural de valores negativos ni de cero.")
                print("------------------------------------------------------------------" )
            else:
                respuesta=math.log(num1)
                return respuesta    
        # -------------------------------------------------------------- 
        def logaritmo10(self,num1):
            if num1<=0:
                print("------------------------------------------------------------------" )
                print("No se puede calcular el logaritmo base 10 de valores negativos ni de cero. ")
                print("------------------------------------------------------------------" )
            else:
                respuesta=math.log10(num1)
                return respuesta   
        # --------------------------------------------------------------                       
        def absoluto(self,num1):
            respuesta=abs(num1)
            return respuesta    
        # -------------------------------------------------------------- 
        def inversa(self,num1):
            if num1==0:
                print("------------------------------------------------------------------" )
                print("No se puede calcular la inversa por division por cero")
                print("------------------------------------------------------------------" )
            else:
                respuesta=1/num1
                return respuesta    
        # --------------------------------------------------------------    
        def factorial(self,num1):
            if num1<=0:
                print("------------------------------------------------------------------" )
                print("No se puede calcular el factorial de valores negativos.")
                print("------------------------------------------------------------------" )
            else:
                respuesta = math.factorial(num1)
                return respuesta          
    calculadoracientifica2=calculadora2()   
    #--------------------------------------------------------------------------
    print("------------------------------------------------------------------" ) 
    print("Resultado del logaritmo natural es:  " + str(calculadoracientifica2.logaritmo(num1)))
    print("------------------------------------------------------------------" )
    print("Resultado del logaritmo base 10 es:  " + str(calculadoracientifica2.logaritmo10(num1)))
    print("------------------------------------------------------------------" )
    print("Resultado del valor asboluto es:  " + str(calculadoracientifica2.absoluto(num1)))
    print("------------------------------------------------------------------" )
    print("Resultado de la inversa es:  " + str(calculadoracientifica2.inversa(num1)))
    print("------------------------------------------------------------------" )
    print("Resultado del factorial es:  " + str(calculadoracientifica2.factorial(num1)))
    print("------------------------------------------------------------------" )
    #-------------------------------------------------------------------------- 
 
elif menuprincipal==3:
    #-------------------------------------------------------------------------- 
    print("operaciones trigonometricas en radianes como:" )
    print("seno, coseno y tangente" )
    num1=int(input("Ingrese el numero 1:   "))
    #-------------------------------------------------------------------------- 
    class calculadora3():
        # --------------------------------------------------------------   
        def trig_seno(self,num1):
            respuesta=math.sin(num1)
            return respuesta  
    # --------------------------------------------------------------   
        def trig_cos(self,num1):
            respuesta=math.cos(num1)
            return respuesta  
    # --------------------------------------------------------------   
        def trig_tan(self,num1):
            respuesta=math.tan(num1)
            return respuesta  


    calculadoracientifica3=calculadora3()   
    #--------------------------------------------------------------------------
    print("------------------------------------------------------------------" )
    print("Resultado del seno en radianes es:  " + str(calculadoracientifica3.trig_seno(num1)))
    print("------------------------------------------------------------------" )
    print("Resultado del coseno en radianes es:  " + str(calculadoracientifica3.trig_cos(num1)))
    print("------------------------------------------------------------------" )
    print("Resultado del tangente en radianes es:  " + str(calculadoracientifica3.trig_cos(num1)))
    print("------------------------------------------------------------------" )
    #-------------------------------------------------------------------------- 
 
elif menuprincipal==4:
    print("estadísticas básicas: promedio, media, mediana, moda" )
    num_estad=int(input("A cuantos numeros desea calcular el promedio o media, mediana o moda:  "))
    lista=[]

    for x in range(num_estad):
        valor=int(input("Ingrese un numero entero:  "))
        lista.append(valor)
    from statistics import mean
    from statistics import median
    from statistics import multimode
    print("La media o promedio de los numeros es:  " + str(mean(lista)))
    print("La mediana de los numeros es:  " + str(median(lista)))
    print("La moda de los numeros es:  " + str(multimode(lista)))

else:
    print("Por favor seleccionar una opcion disponible")