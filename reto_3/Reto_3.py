# -*- coding: utf-8 -*-
"""
Created on Tue Sep  5 05:14:51 2023

@author: erika
"""
name_1 =0
horario_1=0
etapa_1=0
cont_1=0
name_2 =0
horario_2=0
etapa_2=0
cont_2=0
name_3 =0
horario_3=0
etapa_3=0
cont_3=0
trab1=0
abono1=0
agua1=0
mante1=0
trab2=0
abono2=0
agua2=0
mante2=0
trab1=0
abono1=0
agua1=0
mante1=0
arroba=0
cant=0
mano_obra=0
ban=0


contador =1
while(contador == 1):
    menu_inicial =int(input('''          
                         
             Bienvenido al software de gestion de cultivos
         

        1. Ingresar los datos de un cultivo
        2. Ver los datos de un cultivo  ''')) 
    
    if(menu_inicial==1):
        menu_ppal=int(input('''            

    Seleccione el cultivo al que quiere ingresarle la informacion
          1. Cultivo 1(debe ser arroz)
          2. Cultivo 2
          3. Cultivo 3
          4. Volver al menu principal 
          '''))
   
    
    
        if(menu_ppal== 1):
            cultivo_1 = input('''Ingrese los datos del cultivo: nombre, horarios de gestion, etapa, informacion contable
    Presione ENTER para continuar''')  
            name_1=input("Ingrese el nombre del cultivo: \n")
            horario_1 = input("Ingrese el horario de gestion del cultivo: \n")
            etapa_1 = input("Ingrese la etapa en la que se encuentra el cultivo: \n")
           
            cont_1 = int(input('''Ingrese la informacion contable del cultivo: 
                                  1. Costos
                                  2. Producción'''))
                                  
            if(cont_1 == 1):
                costos_cultivo1 = int(input('''Ingrese los costos del cultivo 
                1. Mano de obra 
                2. Abono 
                3. Agua 
                4. Mantenimiento de equipos menu principal
                5. Ir al menu principal 
                              '''))
                if(costos_cultivo1==1):
                    mano_obra=input()
                elif(costos_cultivo1==2):
                    abono=input()
                elif(costos_cultivo1==3):
                    agua=input()
                elif(costos_cultivo1==4):
                    mante=input()
                else:
                    contador=1                            
            elif(cont_1==2):
                ban=1
                prod_cultivo1 = int(input('''Ingrese la produccion del cultivo de arroz
                              1: Valor de la arroba de arroz
                              2. Cantidad recogida
                              3. Ir al menu principal 
                              '''))
                if(prod_cultivo1==1):
                    arroba=int(input("Ingrese el valor de la arroba de arroz "))
                                              
                elif(prod_cultivo1==2):
                    cant=int(input("Ingrese la cantidad de arroz recogida "))
                                       
                else:
                    contador=1

            contador=0
            print("los datos ingresados son: \n " + name_1 +"\n" + horario_1 + "\n" + etapa_1 + "\n" + cont_1 + "\n" + "\n" + "\n")
            contador=1
        elif(menu_ppal== 2):
                cultivo_2 = input('''Ingrese los datos del cultivo: nombre, horarios de gestion, etapa, informacion contable
    Presione ENTER para continuar''')  
                name_2=input("Ingrese el nombre del cultivo: \n")
                horario_2 = input("Ingrese el horario de gestion del cultivo: \n")
                etapa_2 = input("Ingrese la etapa en la que se encuentra el cultivo: \n")
                cont_2 =input("Ingrese la informacion contable del cultivo: \n")
                contador=0
                print("los datos ingresados son: \n " + name_2 +"\n" + horario_2 + "\n" + etapa_2 + "\n" + cont_2 + "\n" + "\n" + "\n")
                contador=1
            
            
        elif(menu_ppal== 3):
                    cultivo_3 = input('''Ingrese los datos del cultivo: nombre, horarios de gestion, etapa, informacion contable
    Presione ENTER para continuar''')  
                    name_3=input("Ingrese el nombre del cultivo: \n")
                    horario_3 = input("Ingrese el horario de gestion del cultivo: \n")
                    etapa_3 = input("Ingrese la etapa en la que se encuentra el cultivo: \n")
                    cont_3 =input("Ingrese la informacion contable del cultivo: \n")
                    contador=0
                    print("los datos ingresados son: \n " + name_3 +"\n" + horario_3 + "\n" + etapa_3 + "\n" + cont_3 + "\n" + "\n" + "\n")
                    contador=1
           
        else:
            contador=1
            
    elif(menu_inicial==2):
        infor=int(input("Seleccione el cultivo de el que quiere conocer la informacion \n "))
        if(infor==1):   
            if(name_1 ==0 or  horario_1 ==0 or  etapa_1 ==0 or cont_1 ==0):
                print("***NO HAY DATOS PARA MOSTRAR***")
                contador=1
            else:
                print("1." + name_1)
                
                print("los datos ingresados son: \n " + name_1 +"\n" + horario_1 + "\n" + etapa_1 + "\n" + cont_1 + "\n" + "\n" + "\n")
        elif(infor==2):
            if(name_2 ==0 or  horario_2 ==0 or  etapa_2 ==0 or cont_2 ==0):
                print("***NO HAY DATOS PARA MOSTRAR***")
                contador=1
            else:
                print("2." + name_2)
                print("los datos ingresados son: \n " + name_2 +"\n" + horario_2 + "\n" + etapa_2 + "\n" + cont_2 + "\n" + "\n" + "\n")
        elif(infor==3):
            if(name_3 ==0 or horario_3 ==0 or  etapa_3 == 0 or cont_3 ==0):
                print("***NO HAY DATOS PARA MOSTRAR***")
                contador=1
            else:
                print("3." + name_3)
                print("los datos ingresados son: \n " + name_3 +"\n" + horario_3 + "\n" + etapa_3 + "\n" + cont_3 + "\n" + "\n" + "\n")
        else:
            contador=1
                  
        
      