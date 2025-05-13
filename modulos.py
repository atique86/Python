import math
import random
import datetime
from math import sqrt

resultado = math.sqrt(25)
print(f"Raíz cuadrada de 25: {resultado}")  # Imprime 5.0

resultado = sqrt(81)
print(f"Raíz cuadrada de 81: {resultado}")  # Imprime 81.0

numero_aleatorio = random.randint(1, 10)
print(f"Número aleatorio entre 1 y 10: {numero_aleatorio}")  # Imprime un número entero aleatorio entre 1 y 10

fecha_actual = datetime.datetime.now()
print(f"Fecha actual: {fecha_actual}")  # Imprime la fecha y hora actual


# Importación de modulos propios
import mi_modulo

mi_modulo.saludar("Juan")  # Imprime "Hola, Juan!"
resultado = mi_modulo.calcular_suma(5, 3)
print(resultado)  # Imprime 8

import operaciones
import utilidades

resultado = operaciones.sumar(5, 3)
utilidades.imprimir_mensaje(f"El resultado de la suma es: {resultado}")

nombre = utilidades.obtener_nombre_usuario()
utilidades.imprimir_mensaje(f"Hola, {nombre}!")