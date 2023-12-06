# -*- coding: utf-8 -*-
"""Reto 5. Entregable

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1p5RUPBevQfhyPD7fjHu0dP7JV97SKueD
"""

# ----- Reto 5: Calificaciones de Estudiantes ------
import statistics
alumnos=[]
notas_grupo=[]



# Menucillos

print("Bienvenido a tu gestor de calificaciones")

while True:
  print('''Digite la opción que desea ejecutar:
  1. Añadir alumno
  2. Buscar alumno
  3. Modificar notas
  4. Borrar alumno
  5. Informe alumno
  6. Informe grupo
  7. Salir de la aplicación
   ''')
  c = int(input())
  if c == 7:
    print("Gracias por usar este aplicativo")
    break

  elif c == 1:
    n = int(input("¿Cuántos alumnos va a ingresar?: "))
    for i in range(n):
      id=input("Identificación alumno " + str(i+1) + ": ")
      nombre=input("Nombre del alumno " + str(i+1) + ": ")
      correo=input("Correo del alumno " + str(i+1) + ": ")
      tel=input("Teléfono del alumno " + str(i+1) + ": ")
      fechanac=input("Ingrese fecha de nacimiento DD/MM/AAAA del alumno " + str(i+1) + ": ")
      notas = [int(i) for i in input('Ingrese las 4 notas del alumno ' + str(i+1) + ": ").split()]
      alumnos.append(
          {'id':id,'nombre': nombre, 'correo': correo, 'tel': tel, 'fechanac': fechanac, 'notas': notas}
      )
      notas_grupo.append(notas)
      consolidado_notas_grupo=[]
      for m in range(len(notas_grupo)):
       for s in range (len(notas_grupo[m])):
        consolidado_notas_grupo.append(notas_grupo[m][s])
    for a in alumnos:
      print("-------------------")
      print("\t Identificación: ", a['id'])
      print("\t Nombre: ", a['nombre'])
      print("\t Correo eletrónico: ", a['correo'])
      print("\t Teléfono: ", a['tel'])
      print("\t Fecha de nacimiento: ", a['fechanac'])
      print("\t Notas: ", a['notas'])

  elif c == 2:
    alumno=input("Digita la identificación del alumno: ")
    for a in alumnos:
      if alumno == a['id']:
        print("\t Identificación: ", a['id'])
        print("\t Nombre: ", a['nombre'])
        print("\t Correo eletrónico: ", a['correo'])
        print("\t Teléfono: ", a['tel'])
        print("\t Fecha de nacimiento: ", a['fechanac'])
        print("\t Notas: ", a['notas'])
      else:
        "El alumno no existe"

  elif c == 3:
    alumno=input("Digita la identificación del alumno: ")
    for a in alumnos:
      if alumno == a['id']:
        nuevas_notas = [int(i) for i in input('Ingrese las 4 notas actualizadas del alumno').split()]
        a.update({'notas': nuevas_notas})
        print("\t Identificación: ", a['id'])
        print("\t Nombre: ", a['nombre'])
        print("\t Correo eletrónico: ", a['correo'])
        print("\t Teléfono: ", a['tel'])
        print("\t Fecha de nacimiento: ", a['fechanac'])
        print("\t Notas: ", a['notas'])
      else:
        "El alumno no existe"

  elif c == 4:
    alumno=input("Digita la identificación del alumno que de sea aliminar: ")
    for a in alumnos:
      if alumno == a['id']:
        alumnos.remove(a)
        print("El alumno con id", alumno, "ha sido eliminado")

      else:
        "El alumno no existe"

  elif c == 5:
    alumno=input("Digita la identificación del alumno: ")

    # generar todo el codigo para el punto 5
    print("--- Informe académico por estudiante ---")
    promedio_grupo= sum(consolidado_notas_grupo)/(4*n)
    print("la nota promedio del grupo es", promedio_grupo)

    for a in alumnos:



     if alumno == a['id']:

       suma_notas = sum(a['notas'])
       numero_notas = len(a['notas'])
       promedio = suma_notas/numero_notas
       #promedio_grupo+=[] #def varidable, crear un diccionario independiente con el promedio de notas de todos los estudiantes
       print("La nota final del estudiante ", a['nombre'], "es ",promedio)
       if promedio > promedio_grupo:
        print("La nota final del estudiante", a['nombre'], "estuvo por encima de la media")
       elif promedio < promedio_grupo:
        print("La nota final del estudiante", a['nombre'], "estuvo por debajo de la media")
       else:
        print("La nota final del estudiante", a['nombre'], "fue igual a la media")
       if promedio >= 3:
        print("El estudiante", a['nombre'], "aprobó el curso")
       else:
        print("El estudiante", a['nombre'], "reprobó el curso")

       if promedio == 5.0:
        print("El estudiante", a['nombre'], "está en el quintil 5")
       elif promedio >= 4.0 and promedio <= 4.9:
        print(f"El alumno ", a['nombre'], "está en el percentil 4")
       elif promedio >=3.0 and promedio <= 3.9:
        print(f"El alumno ", a['nombre'], "está en el percentil 3")
       elif promedio >=2.0 and promedio <= 2.9:
        print(f"El alumno ", a['nombre'], "está en el percentil 2")
       else:
        print(f"El alumno ", a['nombre'], "está en el percentil 1")

  elif c == 6:
    print("--- Nota final por estudiante ---")
    for a in alumnos:
      name = a['nombre']
      suma_todos = sum(a['notas'])
      total_datos = len(a['notas'])
      promedio = suma_todos/total_datos
      print(f"El alumno", name, "ha sacado de nota final ",promedio)

    print("--- Nota promedio del grupo ---")
    total_notas=[]
    otro=[]
    for a in alumnos:
      total_notas.append(a['notas'])
    for sublista in total_notas:
      otro.append(sum(sublista) / len(sublista))
    suma_de_notas = sum(otro)
    conteo = len(otro)
    prom = suma_de_notas/conteo
    print(f"La nota promedio del grupo fue ", prom)

    print("--- Estudiantes por encima, iguales o debajo del promedio ---")
    for a in alumnos:
      name = a['nombre']
      suma_todos = sum(a['notas'])
      total_datos = len(a['notas'])
      promedio = suma_todos/total_datos

      if promedio>=prom:
        print(f"El alumno ", name," está por encima del promedio grupal")
      elif promedio == prom:
        print(f"El alumno ", name, " está igual al promedio grupal")
      elif promedio <= prom:
        print(f"El alumno ", name," está por debajo de promedio grupal")
      else:
        print("No se puede calcular el promedio")

    print("--- Número de estudiantes ganadores y perdedores ---")
    min = 3.0
    for a in alumnos:
      name = a['nombre']
      suma_todos = sum(a['notas'])
      total_datos = len(a['notas'])
      promedio = suma_todos/total_datos

      if promedio >= min:
        print(f"El alumno ", name, " ganó el curso")
      else:
        print(f"El alumno ", name, " perdió el curso")

    print("--- Porcentaje de ganadores y perdedores ---")
    ganan = []
    for a in alumnos:
      name = a['nombre']
      suma_todos = sum(a['notas'])
      total_datos = len(a['notas'])
      promedio = suma_todos/total_datos

      if promedio >= min:
        ganan.append(promedio)
        contar = len(ganan)
        total_alum = len(a['nombre'])-1
        win_rate = float((contar/total_alum)*100)
        print(f"El ", win_rate,"% de los alumnos ganó")
      elif promedio <= min:
        lose_rate = 100-win_rate
        print(f"El ", lose_rate,"% de los alumnos perdió")
      else:
        print("No se puede calcular el porcentaje de ganadores y perdedores")

    print("--- Distribución de estudiantes por percentil ---")

    from decorator import dispatch_on
    consolidado_notas_grupo=otro
    consolidado_notas_grupo.sort()

    from collections import Counter
    dic_frec= Counter(consolidado_notas_grupo)
    notas_abs=[]
    frec_abs=[]
    notas_abs.append
    frec_abs.append
    notas_abs= dic_frec.keys()
    frec_abs=list(dic_frec.values())
    frec_acum = [sum(frec_abs[0:j+1])
          for j in range(0, len(frec_abs), 1)]
    dic_percentil={'notas_abs': notas_abs, 'frec_abs': frec_abs, "frec_acum": frec_acum}
    k= int(input("ingrese el percentil entre 1 y 99: "))
    P=(k*len(consolidado_notas_grupo))/100
    print(P)
    if P<frec_acum[0]:
        res = list(dic_frec.keys())[0]
        print("El", k,"% de lo estudiantes obtuvo una nota menor o igual a " + str(res))
    for i in frec_acum:
        if P== i:
         res = list(dic_frec.keys())[frec_acum.index(P)]
         print("El", k,"% de lo estudiantes obtuvo una nota menor o igual a " + str(res))

    print("--- Moda ---")
    flat_list = []
    for item in total_notas:
      flat_list += item
    print(statistics.mode(flat_list))

    print("--- Mediana ---")
    flat_list.sort()
    print(statistics.median(flat_list))

    print("--- Desviación estándar ---")
    print(statistics.pstdev(flat_list))

  else:
    print("Esta opción no está en el menú, elige una correcta")