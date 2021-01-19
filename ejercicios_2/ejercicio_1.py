"""
Ejercicio 1) Hacer un programa que tenga una lista de  8 numeros enteros 
    -Recorrer la lista y mostrarla(en una funcion)
    -Ordenarla y mostrarla
    -Mostrar su longitud
    -Buscar algun elemento(que el usuario pida por teclado)
"""
#Crear lista
numeros = [1,23,432,5,24,53,78,9]

#Recorrer y mostrar
for elemento in numeros:
    print(elemento)


print("--------------Recorre y mostrar datos--------------------------")
#Generar una funcion y mostrar datos
def  mostrar_lista(lista):
    for i in lista:
        print(f'Los numeros son: {i}')

mostrar_lista(numeros)


#Ordernar y mostrar lista
print("----------------Lista ordenada------------------------")

numeros.sort()#ordena la lista de menor a mayor
print(numeros)

print("----------------Lista ordenada con funcion------------------------")
mostrar_lista(numeros)


#Saber longitud de la lista
print("----------------Longitu de la lista------------------------")
print(len(numeros))


#Buscar un numero en la lista(manera sin manejo de errores)
print("----------------Buscar un numero dentro de la lista------------------------")

dato = int(input("Ingrese un numero para buscar: "))
comprobar = isinstance(dato, int)#instancio y verifico si es un entero el dato

#un bucle para pedir datos hasta que coloque lo pedido
while not comprobar or dato <= 0: 
    dato = int(input("Ingrese un numero para buscar: "))
else:
    print(f'El numero ingresado es el {dato}')    

search = numeros.index(dato)#devuelve un boleano en caso de que encuentre el dato
print(f'El numero buscado en la lista, es el indice: {search}')#muestro el indice donde se encuentra el numero buscado



