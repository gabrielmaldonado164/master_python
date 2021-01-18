"""

    Diccionario:
    Un tipo de dato que almacena un conjunto de datos
    En formato CLAVE - VALOR
    Es parecido a un array asociativo o un objeto JSON
"""

datos = {
    'nombre': 'Gabriel',
    'apellido': 'Maldonado',
    'web':'maheca.tk'
}

print(datos)
print("\n******************************************************")
print(datos['web'])#muestra el valor de la  key pasado explixitamente 
print("\n******************************************************")
print(datos.keys())
print("\n******************************************************")
print(datos.values())