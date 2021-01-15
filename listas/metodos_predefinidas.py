#Metodos para las listas


cantantes = ['The weeknd','Adam levine', 'Post malone', 'Ed Sheeran']
numeros = [1, 2, 4, 8, 5, 9]

#Agregar elemento
cantantes.append('Justin Bieber')
cantantes.insert(1, 'Zayn')#inster tiene dos argumentos: indice - elemento
print(cantantes)

print("\n****************** Ordenar numeros *****************")
#ordernar
print(numeros)
numeros.sort()
print(numeros)

print("\n************** Eliminar elemento *********************")
#Eliminar elemento
cantantes.pop(2)#lo elimino indicando el index
cantantes.remove('Zayn')#lo elimino indicando el valor
print(cantantes)


print("\n*************** Reverso, dar vuelta la lista ********************")
#Reverso
print(numeros)
numeros.reverse()
print(numeros)

print("\n*************** Verificar si un elemento se encuentra en algun lugar (true -false) ********************")
#Buscar elemento con una respuesta boolean
print('Zayn' in cantantes)# verifico si ese elemento esta dentro de la lista


print("\n************* Contar cuanto elementos se tiene **********************")
#Contar elementos
print(cantantes)
print(len(cantantes))#cuento cuantos elementos hay en el array

print("\n************* Verificar se buscando se repite algun valor**********************")
#Saber cuantas veces esta un elemento dentro de la lista
print(numeros.count(8))


print("\n************** Saber indice de el dato que le pasamos(tiene que estar de igual manera tipeado *********************")
#Saber indice de algun elemento de la lista
print(cantantes.index('Justin Bieber'))


print("\n************** Unir dos listas y tener sus propios metodos, datos, etc *********************")
#Unir listas
numeros.extend(cantantes)
print(numeros)






 


