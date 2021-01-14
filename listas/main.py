"""
LISTAS(arrays)
- Son colecciones o conjuntos de datos/valores, bajo un unico nombre
- Para acceder a esos valores podemos usar un indice numerico
- Una variable que guarde un conjunto de valores
"""

#variable
pelicula = 'Avenger'


print("###################### Array ########################")
#lista
peliculas = ['Avenger', 'Iron man', 'Hulk']
print(peliculas)

print("###################### Array ########################")
#otra maneras de generar listas
cantantes = list(('rauw alejandro' , 'wisin y yandel', 'eminem'))
print(cantantes)


print("\n###################### Array con range ########################")
#con rango

year = list(range(2020,2035))
print(year)


print("\n######################  Mostrar Array indicando su index ########################")
#Ingresar por indices
print(peliculas[1])
print(cantantes[0:2])


print("\n###################### Agregar elementos a un Array  ########################") 
#agregar un elemento a una lista, se agrega a 'spiderman'

peliculas.append("spiderman")
print(peliculas)


print("\n###################### Recorrer elementos de un Array con bucles  ########################")
#recorrer listas con bucles

nueva_peliculas = ''
while nueva_peliculas != 'parar':
    nueva_peliculas = input('Ingrese peliculas nuevas a la lista: ')

    if nueva_peliculas != 'parar':
        peliculas.append(nueva_peliculas)

for i in peliculas:
    print(f'{peliculas.index(i)+1}. {i}')

