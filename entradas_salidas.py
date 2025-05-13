import os

# Entrada de datos del usuario
print ("\n *** Entrada de datos del usuario ***")

nombre = input("Ingresa tu nombre: ")
edad = input("Ingresa tu edad: ")

print("Hola, " + nombre + "!")
print("Tienes " + edad + " años.")

# Convertir a entero un string
print ("\n *** Convertir a entero un string ***")
edad = int(input("Ingresa tu edad: "))

if edad >= 18:
    print("Eres mayor de edad.")
else:
    print("Eres menor de edad.")
    
# Salida de datos con formateo de cadenás
print ("\n *** Salida de datos con formateo de cadenás ***")
nombre = "Juan"
edad = 25
print(f"Hola, mi nombre es {nombre} y tengo {edad} años.")

# Lectura de archivos
print ("\n *** Lectura de archivos ***")
ruta = os.path.join(os.path.dirname(__file__), "datos.txt")
archivo = open(ruta, "r")
contenido = archivo.read()
print(contenido)
archivo.close()

# Escritura de archivos
print ("\n *** Escritura de archivos ***")
archivo = open(ruta, "w")
archivo.write("Hola, mundo!")
archivo.close()

# Uso de With
print ("\n *** Uso de With ***")
with open(ruta, "r") as archivo:
    contenido = archivo.read()
    print(contenido)