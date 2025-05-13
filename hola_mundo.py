print ("¡Hola, Mundo!")

división_entera = 14 // 3   # 3
print (división_entera)

# Estructuras Condicionales
print ("\n*** Estructuras Condicionales ***")
calificacion = 85

if calificacion >= 90:
   print ("Excelente")

elif calificacion >= 80:
   print ("Muy bueno")

elif calificacion >= 70:
   print ("Bueno")

else:
   print ("Necesita mejorar")

# Bucles o Loops
print ("\n*** Bucles o Loops ***")

#FOR
print ("\n *** FOR ***")
frutas = ["manzana", "banana", "naranja"]
for fruta in frutas:
    print(fruta)

#WHILE
print ("\n *** WHILE ***")
contador = 0
while contador < 5:
    print(contador)
    contador += 1

# Control de Bucles

#BREAK
print ("\n *** BREAK ***")
contador = 0
while True:
    print(contador)
    contador += 1

    if contador == 5:
        break

#CONTINUE
print ("\n *** CONTINUE ***")
for i in range(10):
    if i % 2 == 0:
        continue
    print(i)

#PASS
print ("\n *** PASS ***")
for i in range(5):
    pass

# Métodos de listas
print ("\n *** Métodos de listas ***")
frutas = ["manzana", "banana", "naranja"]

frutas.append("pera")
print(frutas)  # Imprime ["manzana", "banana", "naranja", "pera"]

frutas.insert(1, "uva")
print(frutas)  # Imprime ["manzana", "uva", "banana", "naranja", "pera"]

frutas.remove("banana")
print(frutas)  # Imprime ["manzana", "uva", "naranja", "pera"]

fruta_eliminada = frutas.pop(2)
print(frutas)  # Imprime ["manzana", "uva", "pera"]
print(fruta_eliminada)  # Imprime "naranja"

frutas.sort()
print(frutas)  # Imprime ["manzana", "pera", "uva"]

frutas.reverse()
print(frutas)  # Imprime ["uva", "pera", "manzana"]

# Listas de compresión
print ("\n*** Listas de compresión ***")
numeros = [1, 2, 3, 4, 5]
cuadrados = [x ** 2 for x in numeros if x % 2 == 0]
print(cuadrados)  # Imprime [4, 16]

# Métodos de tuplas
print ("\n *** Métodos de tuplas ***")
mi_tupla = (1, 2, 3, 2, 4, 2)

print (mi_tupla.index(2))   # Salida: 1
print (mi_tupla.index(2, 2))   #Salida: 3
print (mi_tupla.index(2, 2, 4))   #Salida: 3
print (mi_tupla.count(2))
print (len(mi_tupla))

# Métodos con diccionarios (clave - valor)
print ("\n *** Métodos con diccionarios ***")
persona = {"nombre": "Juan", "edad": 25, "ciudad": "Madrid"}

print(persona.keys())    # Imprime dict_keys(["nombre", "edad", "ciudad"])
print(persona.values())  # Imprime dict_values(["Juan", 25, "Madrid"])
print(persona.items())   # Imprime dict_items([("nombre", "Juan"), ("edad", 25), ("ciudad", "Madrid")])

persona.update({"profesion": "Ingeniero"})
print(persona)  # Imprime {"nombre": "Juan", "edad": 25, "ciudad": "Madrid", "profesion": "Ingeniero"}

# Operaciones con conjuntos
print ("\n *** Operaciones con conjuntos ***")
frutas_conj = {"manzana", "banana", "naranja"}
numeros_conj = set([1, 2, 3, 4, 5])

print (frutas_conj)
print (numeros_conj)

conjunto1 = {1, 2, 3}
conjunto2 = {3, 4, 5}

union = conjunto1 | conjunto2
print(union)  # Imprime {1, 2, 3, 4, 5}

interseccion = conjunto1 & conjunto2
print(interseccion)  # Imprime {3}

diferencia = conjunto1 - conjunto2
print(diferencia)  # Imprime {1, 2}

diferencia_simetrica = conjunto1 ^ conjunto2
print(diferencia_simetrica)  # Imprime {1, 2, 4, 5}

# Métodos con conjuntos
print ("\n  *** Métodos con conjuntos ***")
frutas_met = {"manzana", "banana", "naranja"}

frutas_met.add("pera")
print(frutas_met)  # Imprime {"manzana", "banana", "naranja", "pera"}

frutas_met.remove("banana")
print(frutas_met)  # Imprime {"manzana", "naranja", "pera"}

frutas_met.discard("uva")
print(frutas_met)  # Imprime {"manzana", "naranja", "pera"}

frutas_met.clear()
print(frutas_met)  # Imprime set()