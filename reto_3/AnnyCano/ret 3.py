print("============================================")
print("BIENVENIDO A LA APLICACION DE CULTIVOS")
print("============================================")
menu_principal=""

while True:
    print("=========================================================")
    print("Seleccione una opcion:")
    menu_principal=input('''
    1) DATOS DEL CULTIVO 
    2) HORARIO Y GESTION DEL CULTIVO
    3) ETAPAS DEL CULTIVO
    4) INFORMACION CONTABLE
    5) SALIR
    ''')
    if menu_principal=="1":
        print("Usted selecciono DATOS DEL CULTIVO")
        while True:
            NOM_CULT=input("1) NOMBRE DEL CULTIVO: ")         
            DH_MANT=input("2) DIAS Y HORARIO DE MANTENIMIENTO: ")
            DH_REG=input("3) DIAS Y HORARIO DE REGADO: ")
            DH_ABO=input("4) DIAS Y HORARIO DE ABONO: ")
            VAR_CULT=input("5) VARIABLES PARA CADA ETAPA DE CULTIVO: ")
            def informacion():
                print("==================================================")
                print("Su cultivo es:"+NOM_CULT)
                print("Los dias y hora es mantenimiento son:"+DH_MANT)
                print("Los dias y hora es regado son:"+DH_REG)
                print("Los dias y hora es abono son:"+DH_ABO)
                print("Tiene alguna variable para cada etapa de cultivo?:"+VAR_CULT)
            

            informacion()
            break
    
    elif menu_principal=="2":
        print("Usted selecciono HORARIO Y GESTION DEL CULTIVO")
        while True:
            submenu_HORARIO_GESTION_CULTIVO=input('''
            1) DIAS Y HORARIO DE CULTIVO
            2) DIAS Y HORARIO DE ABONO
            3) DIAS Y HORARIO DE RIEGO
            4) IR AL MENU PRINCIPAL
            ''')
            if submenu_HORARIO_GESTION_CULTIVO=="1":
                input("Ingrese los dias y horarios de cultivo:")

            elif submenu_HORARIO_GESTION_CULTIVO=="2":
                input("Ingrese los dias y horarios de abonar:")

            elif submenu_HORARIO_GESTION_CULTIVO=="3":
                input("Ingrese los dias y horarios de riego:")

            elif submenu_HORARIO_GESTION_CULTIVO=="4":
                input("Desea volver al menu principal?")
                break
            
            else:
                 print("Vuelva a seleccionar alguna de las opciones")
                 continue
        
    elif menu_principal=="3":
        print("Usted selecciono ETAPAS DEL CULTIVO")
        while True:
            submenu_ETAPAS_DEL_CULTIVO=input('''
            1) SIEMBRA
            2) CRECIMIENTO
            3) COSECHA
            4) IR AL MENU PRINCIPAL
            ''')
            if submenu_ETAPAS_DEL_CULTIVO=="1":
                print("Usted selecciono SIEMBRA")

            elif submenu_ETAPAS_DEL_CULTIVO=="2":
                print("Usted selecciono CRECIMIENTO")

            elif submenu_ETAPAS_DEL_CULTIVO=="3":
                print("Usted selecciono COSECHA")

            elif submenu_HORARIO_GESTION_CULTIVO=="4":
                input("Desea volver al menu principal?")
                break

            else:
                print("Vuelva a seleccionar alguna de las opciones")
                continue
                    

    elif menu_principal=="4":
        print("Usted selecciono INFORMACION CONTABLE")
        while True:
            sub_INF_CONT=input('''
            1) COSTOS
            2) PRODUCCION
            ''')
            if sub_INF_CONT=="1":
                while True:
                    sub_costo_fijo=input('''
                    1) MANO DE OBRA
                    2) AGUA
                    3) MANTENIMIENTO
                    4) ABONO
                    5) IR ATRAS
                    ''')
                    
            elif sub_INF_CONT=="2":
                 sub_INF_PROD=input('''
                 1) VALOR EN MERCADO DEL CULTIVO
                 2) CANTIDAD RECOGIDA
                 3) IR ATRAS
                 ''')
                
            else:
                print("Vuelva a seleccionar alguna de las opciones")
                continue
                
                break
        

    elif menu_principal=="5":
        print("Usted selecciono SALIR")
        break
    
    else:
        print("Vuelva a seleccionar alguna de las opciones")
        continue
        

