"""
    SET, es un tipo de dato, para tener un conjunto de valores, pero no tiene un indice ni un orden,
    no puede tener objetos mutables(como listas, diccionarios) dentro del mismo

    Sus elementos propios si pueden ser mutados

    Un SET puede ser convertido en lista y viceversa 
"""

#primera manera de generar un SET

nombres = {"Gabi","Uli","Kevin","Chino"}

print(type(nombres))
print(nombres)

print("******************************************")

apellido = set({"Maldonado","Ahumada","Tomas"})
print(type(apellido))
print(apellido)