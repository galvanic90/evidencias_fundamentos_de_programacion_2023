# -*- coding: utf-8 -*-
"""Untitled19.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1mhouojfJ85kL4G22V6nuBPYwYcl9sGjO
"""

import numpy as np

# Paso 1: Crear un objeto ndarray con números enteros entre 64 y 1024
objeto_enteros = np.arange(64, 1025)

# Paso 2: Redimensionar a una matriz cuadrada (1024 x 1024)
matriz_bidimensional_cuadrada = objeto_enteros.reshape(32,32)


# Paso 3: Crear una columna de datos aleatorios de 30 observaciones con nombres y cédulas aleatorias
nombres = ['Andres', 'Maria', 'Manuel', 'Daniel', 'Sarah', 'Cristian', 'Violetta', 'Lucia', 'Jackson', 'Jose']
nombres_aleatorios = np.random.choice(nombres, size=30)
cedulas_aleatorias = np.random.randint(1000000, 9999999, size=30)

# Paso 4: Concatenar un nuevo vector con observaciones de nombres y cédulas
nombres_cedulas = np.column_stack((nombres_aleatorios, cedulas_aleatorias))

# Paso 5: Encontrar la posición del número más grande en las cédulas
posicion_maximo_cedula = np.argmax(cedulas_aleatorias)

# Mostrar resultados
print("Matriz Cuadrada:")
#print(matriz_bidimensional_cuadrada)
print("\nNombres y Cédulas Aleatorias:")
print(nombres_cedulas)
print(f"\nLa posición del número más grande de las cédulas es: {posicion_maximo_cedula}")

import numpy as np