#-------------------------------------------------------------------------- 
#--Variables vacias
'''
Las variables del program se dejan vacias para poder crear una lista y mostrar al usuario que datos se tienen y cuales faltan a medida que introduzaca los datos
'''

#--------------------------------------------------------------------------  
nom_cultivo=[]
#--------------------------------------------------------------------------  
dia_mantenimiento=[]
horario_mantenimiento=[]
#--------------------------------------------------------------------------  
dia_regado=[]
hora_regado=[]
#--------------------------------------------------------------------------  
dia_abono=[]
hora_abono=[]
#--------------------------------------------------------------------------  
etapa=[]
fase=[]
Intervalo_inicial=[]
Intervalo_final=[]



print("Software par informacible para cultivos agricolas")
print("--------------------------------------------------")

#-------------------------------------------------------------------------- 
#--Menu principal 
'''
En la opcion 1 se permite ingresar informacion nueva por cultivo
En esta opcion se encuentran las siguientes opciones dentro del submenu 1
Nombre de cultivo, dia y horario de mantenimiento, dia y hora de regado, dia y hora de abono, etapa de cultivo, fase de cultivo e intervalo 

en la opcion 2 se permite imprimnir los datos del cultivo segun lo que se introduzca en la opcion 1, los datos se almacen en listas , en caso de que el usuario le falten datos el sistema mostra el espacio vacio 
'''



menuprincipal= int(input("Menu principal: \n 1 - Introduccion de datos nuevos de los cultivos: \n 2 - Horario de Gestión de Cultivo: \n 3 - Información Contable: \n 0 - Salir del programa:    "))
while menuprincipal !=0:
    if menuprincipal==1:
        #-------------------------------------------------------------------------- 
        print("--------------------------------------------------")
        submenu1= int(input("Submenu1: \n 1 - Nombre de cultivo:  \n 2 - Dias y horario de mantenimiento: \n 3 - Dias y horario de regado: \n 4 - Dias y horario de abono: \n 5 - Variables del cultivo: \n 0 - Ir al menu principal:    "))
        print("--------------------------------------------------")
        while submenu1 !=0:
            print("-------------------------------------------------------------------------- ")
            print("-------------------------------------------------------------------------- ")
            print("-------------------------------------------------------------------------- ")
            if submenu1==1:
                nom_cultivo=input('Nombre de cultivo:  ')
            elif submenu1==2:
                dia_mantenimiento=input('Dias de mantenimiento del cultivo (Lunes a Domingo):  ')
                horario_mantenimiento=input('Horario de mantenimiento del cultivo:  ')
            elif submenu1==3:
                dia_regado=input('Dias de regado del cultivo:  ')
                hora_regado=input('Horario de regado del cultivo:  ')
            elif submenu1==4:
                dia_abono=input('Dias de abono del cultivo:  ')
                hora_abono=input('Horario de abono del cultivo:  ')
            elif submenu1==5:
                etapa=input('Etapa del cultivo (Siembra, crecimiento,cosecha,):  ')
                fase=input('Fase del cultivo:  ')
                Intervalo_inicial=input('Dia inicial del intervalo:  ')
                Intervalo_final=input('Dia final del intervalo:  ')
            else:
                print("Por favor seleccionar una opcion disponible")
            print("--------------------------------------------------")
            submenu1= int(input("Submenu1: \n 1 - Nombre de cultivo:  \n 2 - Dias y horario de mantenimiento: \n 3 - Dias y horario de regado: \n 4 - Dias y horario de abono: \n 5 - Variables del cultivo: \n 0 - Ir al menu principal:    "))
            print("-------------------------------------------------------------------------- ")
            print("-------------------------------------------------------------------------- ")
            print("-------------------------------------------------------------------------- ")
        #--------------------------------------------------------------------------  


    elif menuprincipal==2:
 #-------------------------------------------------------------------------- 
        print("-------------------------------------------------------------------------- ")
        print("-------------------------------------------------------------------------- ")
        print("-------------------------------------------------------------------------- ")
        print("Datos del cultivo ingresados por el usuario")
        print("Nombre de cultivo: " ) 
        print(nom_cultivo ) 
        print("Dias de mantenimiento del cultivo (Lunes a Domingo): " ) 
        print(dia_mantenimiento) 
        print("Horario de mantenimiento del cultivo: " ) 
        print(horario_mantenimiento)       
        print("Dias de regado del cultivo: " ) 
        print(dia_regado) 
        print("Horario de regado del cultivo:  " ) 
        print(hora_regado )    
        print("Dias de abono del cultivo: " ) 
        print(dia_abono ) 
        print("Horario de abono del cultivo: " ) 
        print(hora_abono ) 
        print("Etapa del cultivo (Siembra, crecimiento,cosecha,): " ) 
        print(etapa)       
        print("Fase del cultivo: " ) 
        print(fase ) 
        print("Dia inicial del intervalo: " ) 
        print(Intervalo_inicial )  
        print("Dia final del intervalo: " ) 
        print(Intervalo_final ) 
        print("-------------------------------------------------------------------------- ")
        print("-------------------------------------------------------------------------- ")
        print("-------------------------------------------------------------------------- ")


    elif menuprincipal==3:
        print("--------------------------------------------------")
        submenu3= int(input("Submenu2: \n 1 - Costos fijos:  \n 2 - Costos variables: \n 3 - Produccion: \n 4 - Informe economico  \n 0 - Ir al menu principal:    "))
        print("--------------------------------------------------")
        while submenu3 !=0:
            print("-------------------------------------------------------------------------- ")
            print("-------------------------------------------------------------------------- ")
            print("-------------------------------------------------------------------------- ")
            if submenu3==1:
                print("Costos fijos")
                costo_mano_obra=int(input('Costo de mano de obra:  '))
                costo_abono=int(input('Costo de abono:  '))
                costo_agua=int(input('Costo de agua:  '))
                costo_mantenimiento=int(input('Costo de mantenimiento:  '))

            elif submenu3==2:
                print("Costos variables")
                costo_medicamento=int(input('Costo del medicamento:  '))
                costo_imprevistos=int(input('Costo de los imprevistos:  '))

            elif submenu3==3:
                print("Produccion")                
                costo_arroba=int(input('Valor de la arroba de 12.5 Kg:  '))
                cantidad_kg=int(input('cantidad de kilogramos produccidos:  '))

            elif submenu3==4:
                print("Informe economico")                
                meses_de_cultivo=int(input('Meses de cultivo:  '))
                costo_mes_fijo=costo_mano_obra+costo_abono+costo_agua+costo_mantenimiento
                costo_total_fijo=meses_de_cultivo*costo_mes_fijo

                costo_mes_var=costo_medicamento+costo_imprevistos
                costo_total_var=meses_de_cultivo*costo_mes_var

                costo_mes_total=costo_mes_fijo+costo_mes_var
                costo_total=costo_total_fijo+costo_total_var  

                beneficios_ventas=costo_arroba*(cantidad_kg/12.5)
                ganancias=beneficios_ventas-costo_total
                
                print("Costos mensuales fijos")   
                print(costo_mes_fijo)  
                print("Costos totales fijos")  
                print(costo_total_fijo)  
                print("Costos mensuales variables")   
                print(costo_mes_var)  
                print("Costos totales variables")  
                print(costo_total_var)  
                print("Costos total mensual")   
                print(costo_mes_total)  
                print("Costos totales ")  
                print(costo_total)  
                print("utilidades")    
                print(ganancias)  


            else:
                print("Por favor seleccionar una opcion disponible")
            
            print("--------------------------------------------------")
            submenu3= int(input("Submenu2: \n 1 - Costos fijos:  \n 2 - Costos variables: \n 3 - Produccion: \n 4 - Informe economico  \n 0 - Ir al menu principal:    "))
            print("-------------------------------------------------------------------------- ")
            print("-------------------------------------------------------------------------- ")
            print("-------------------------------------------------------------------------- ")
        #--------------------------------------------------------------------------  
    elif menuprincipal==4:
        print("menu4")
    else:
        print("Por favor seleccionar una opcion disponible")
    menuprincipal= int(input("Menu principal: \n 1 - Introduccion de datos de los cultivos: \n 2 - Horario de Gestión de Cultivo: \n 3 - Información Contable: \n 0 - Salir del programa:    "))

