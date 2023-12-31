# -*- coding: utf-8 -*-
"""RetoV.2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1RFANAm8X0QJxpqOnPBa_1i8RsJhULyxL
"""



# Este es el menú cuando la persona usa la aplicación que permita administrar las notas de un grupo de estudiantes.
def menu():
  print('''\nSelecciona una opción de acuerdo a la información que desea conocer\n
    1. Agregar: Elija esta opción si desea ingresar los datos de los estudiantes
    2. Buscar: Elija esta opción si desea ingresar la identificación del estudiante para verificar si el estudiante existe e imprimir la información de este
    3. Modificar: Elija esta opción si desea buscar el estudiante con la identificación y modificar las notas
    4. Cancelación de materia: Elija esta opción si desea buscar el estudiante con la identificación y cancelarle la materia al estudiante
    5. Resultado por estudiante: Elija esta opción si desea buscar el estudiante con la identificación y saber el desempeño académico
    6. Informe del grupo
    7. Salir
    ''')

#Inicialización de las variables
datos = {}
while True:
    menu()
    print(" ")
    opciones = int(input("Inserta un numero valor >> "))

#Sección 1:Agregar datos de los estudiantes
# Se desarrolla una estructura de datos en la cual se puedan almacenar los siguientes datos de un estudiante.
    if opciones == 1:
      identificacion = input('\n Ingrese la identificación del alumno:')
      nombre = input('\n Ingrese el nombre del alumno:')
      correo = input('\n Ingrese el correo electrónico del alumno:')
      telefono=input('\n Ingrese el número de telefono del alumno:')
      fecha=(input('\n Ingrese la fecha de nacimiento, formato año mes dia sin espacios ni caracteres especiales:'))
      nota1=float(input('\n Ingrese la nota número 1 del alumno:'))
      nota2=float(input('\n Ingrese la nota número 2 del alumno:'))
      nota3=float(input('\n Ingrese la nota número 3 del alumno:'))
      nota4=float(input('\n Ingrese la nota número 4 del alumno:'))
      datos[identificacion] = {
            'nombre': nombre,
            'correo': correo,
            'telefono': telefono,
            'fecha': fecha,
            'nota1': nota1,
            'nota2': nota2,
            'nota3': nota3,
            'nota4': nota4
      }

#Sección 2:Buscar datos del estudiante.
    if opciones == 2:
      identificacion = input('\n Ingrese la identificación del alumno:')
      if identificacion in datos:
        print("La identificación del alumno es: ", identificacion)
        for clave, valor in datos[identificacion].items():
                print(clave.title() + ':', valor)
      else:
            print('No existe el cliente con la identificación', identificacion)

#Sección 3:Modificar datos del estudiante.
    if opciones == 3:
      identificacion = input('\n Ingrese la identificación del alumno:')
      if identificacion in datos:
        print("La identificación del alumno es: ", identificacion)
        for ident in datos:
         for info in datos[ident]:
           if info == 'nota1':
             datos[ident][info] = input('Ingrese la nueva nota 1 del alumno:')
           if info == 'nota2':
            datos[ident][info] = input('Ingrese la nueva nota 2 del alumno:')
           if info == 'nota3':
            datos[ident][info] = input('Ingrese la nueva nota 3 del alumno:')
           if info == 'nota4':
            datos[ident][info] = input('Ingrese la nueva nota 4 del alumno:')

#Sección 4:Cancelación de materia.
    if opciones == 4:
      identificacion = input('\n Ingrese la identificación del alumno:')
      if identificacion in datos:
        del datos[identificacion]
      else:
            print('No existe el cliente con la identificación', identificacion)
#Sección 5:Resultados del estudiante.
    if opciones == 5:
      identificacion = input('\n Ingrese la identificación del alumno:')
      if identificacion in datos:
            print('Identificación:', identificacion)
            nota_1 = datos[identificacion].get("nota1")
            nota_2 = datos[identificacion].get("nota2")
            nota_3 = datos[identificacion].get("nota3")
            nota_4 = datos[identificacion].get("nota4")
            nota_final = (nota_1 + nota_2 + nota_3 + nota_4) / 4
            print("La nota final del alumno con identificación", identificacion, "es: ", nota_final)
            if nota_final < 3:
              print("El estudiante perdió el curso")
            elif nota_final >=3:
              print("El estudiante aprobó el curso")
      else:
            print('No existe el cliente con la identificación', identificacion)

#Sección 6:Informe del grupo. (Se intentó)
    #if opciones == 6:'''
    #for key, value in datos.items():
  #nota_individual = (value['Nota1'] + value['Nota2'] + value['Nota3'] + value['Nota4'] / 4)
  #notas[key] = {'nota final':nota_individual}
#print(notas)
#for key, value in notas.items():
 # if value and 'nota final' in value.keys():
        # Adding value of nota final to promedio
  #      promedio += value['nota final'] / value['nota final']
#print(promedio)




#Sección 7: Salir y finalizar la ejecución de la aplicación.
    if opciones == 7:
      break