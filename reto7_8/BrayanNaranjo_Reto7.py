# -*- coding: utf-8 -*-
"""
Created on Mon Oct  9 20:13:20 2023

@author: Brahi
"""

import numpy as np
import random

# Paso 1: Crear un objeto de tipo ndarray con números enteros entre 64 y 1024
ndarray_num = np.random.randint(64, 1025, 1024)

# Paso 2: Redimensionar a una matriz bidimensional cuadrada
cuadrada_matriz = ndarray_num.reshape(32, 32)

# Paso 3: Crear una columna de datos aleatorios de nombres y cédulas con 30 registros
nombres = ['Andres', 'Maria', 'Manuel', 'Daniel', 'Sarah', 'Cristian', 'Violetta', 'Lucia', 'Jackson', 'Jose']
numeros_cedula = [random.randint(1000000000, 9999999999) for _ in range(30)]
nombres_repetidos = [random.choice(nombres) for _ in range(30)]
datos_aleatorios = np.column_stack((nombres_repetidos, numeros_cedula))

# Paso 4: Concatenar un nuevo vector con las observaciones de nombres y cédulas
vector_concatenado = np.hstack((datos_aleatorios[:, 0], datos_aleatorios[:, 1]))

# Paso 5: Mostrar la posición del número más grande de las cédulas
posicion_max = np.argmax(datos_aleatorios[:, 1])

# Mostrar resultados
print("Paso 1: Ndarray con números enteros entre 64 y 1024:\n", ndarray_num)
print("\nPaso 2: Matriz bidimensional cuadrada:\n", cuadrada_matriz)
print("\nPaso 3: Columna de datos aleatorios con nombres y cédulas:\n", datos_aleatorios)
print("\nPaso 4: Vector concatenado con los nombres y las cédulas:\n", vector_concatenado)
print("\nPaso 5: Posición del número más grande de las cédulas:", posicion_max)
