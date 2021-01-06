"""
Si se cumple una condicion, se ejecuta ciertas instrucciones
En caso se que no, se ejecuta otras instrucciones

if condicon;
    instrucciones
else:
    intrucciones

"""


# Ejemplo 1
print("################### EJEMPLO 1 ###################")

color = input("Cual pienza que es mi color favorito?: ")

if color == 'azul':
    print("Correcto, el color es el AZUL")
else:
    print("Incorrecto, vuelva a intentarlo")

# Ejemplo 2
print("\n################### EJEMPLO 2 ###################")

edad = int(input("Ingrese su edad: "))

if edad >= 18:
    print("Perfecto, eres mayor de edad")
else:
    print("Lo sentimos, todavia eres menor de edad y no puedo hablar con vos")


# Ejemplo 3 (if anidados)
print("\n################### EJEMPLO 3 ###################")

nombre = "Gabriel Maldonado"
edad = 21
continente = "America"
pais = "Argentina"

if edad >= 18:
    print(f'{nombre} es mayor de edad')

    if continente != "America":
        print("El usuario no es de america")
    else:
        print(f"El usuario es del continente americano y vive en {pais}")
else:
    print(f'{nombre} es menor de edad' )


# Ejemplo 4 (elif)
print("\n################### EJEMPLO 4 ###################")

dia = int(input("Ingrese el numero del dia de la semana: "))

if dia == 1:
    print("Es lunes")
elif dia == 2:
    print("Es martes")
elif dia == 3:
    print("Es miercoles")
elif dia == 4:
    print("Es jueves")
elif dia == 5:
    print("Es viernes")
else:
    print("Es finde de semana")


# Ejemplo 5 (operadores logicos)
print("\n################### EJEMPLO 5 ###################")

edad_trabajo = int(input("Cuanto años tienes para trabajar?: "))

if edad_trabajo >= 18 and edad_trabajo < 65:
    print("Perfecto, puede trabajar de manera correcta")
else: 
    print("Lo sentimos, lamentablemente con esa edad no puede trabajar")