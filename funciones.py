# Función saludo
print("\n *** Función saludo *** ")
def saludo():
    print("¡Hola, mundo!")
saludo()  # Imprime "¡Hola, mundo!"

# Función con parametros
print("\n *** Función con parametros ***")
def saludo(nombre):
    print(f"¡Hola, {nombre}!")
saludo("Juan")  # Imprime "¡Hola, Juan!"
saludo("María")  # Imprime "¡Hola, María!"

# Valores retorno
print("\n *** Valores retorno ***")
def suma(a, b):
    return a + b
resultado = suma(3, 4)
print(resultado)  # Imprime 7

# Funciones anónimas (lambda)
print("\n *** Funciones anónimas (lambda) ***")
def cuadrado(x): return x ** 2
print(cuadrado(5))  # Imprime 25

# Alcance de las variables (local vs. global)
print ("\n *** Alcance de las variables (local vs. global) ***")
def funcion():
    variable_local = 10
    print(variable_local)  # Accesible dentro de la función

variable_global = 20
def funcion2():
    print(variable_global)  # Accesible desde cualquier lugar
funcion()  # Imprime 10
funcion2()  # Imprime 20
print(variable_global)  # Imprime 20
#print(variable_local)  # Genera un error, la variable no está definida en este alcance.

# Documentación de funciones (docstrings)
print ("\n Documentación de funciones (docstrings)")
def area_rectangulo(base, altura):
    """
    Calcula el área de un rectángulo.
    Args:
        base (float): La base del rectángulo.
        altura (float): La altura del rectángulo.
    Returns:
        float: El área del rectángulo.
    """
    return base * altura
area = area_rectangulo(5, 3)
print(f"El área del rectángulo es: {area}")

# Funciones con número variable de argumentos
print("\n *** Funciones con número variable de argumentos ***")
def suma_variable(*numeros):
    total = 0
    for numero in numeros:
        total += numero
    return total

print(suma_variable(1, 2, 3))  # Imprime 6
print(suma_variable(4, 5, 6, 7))  # Imprime 22