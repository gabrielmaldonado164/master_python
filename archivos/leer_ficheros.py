#Importamos modulo para archivos
from io import open
import pathlib #poder tener el PATH Correcto

#Abrir archivos
#ruta = str(pathlib.Path(__file__).parent) +" /prueba.txt" ---> LE PUEDO INDICAR CON EL PATH LA RUTA 
archivo = open("archivos/prueba.txt", "r")# ruta - permisos

#Leer contenido
# contenido = archivo.read()
# print(contenido)

#Leer contenido y guardarlo en una lista
lista = archivo.readlines() #leer cada linea 
archivo.close()
print(lista)

#Mostrar linea por linea
for frase in lista:
    print('-)' + frase.upper())

#Convertir una frase en elementos de una lista, sirve para colocar algun tipo de simbolo en cada finalizacion de cada palabra

for frase in lista:
    lista_frase  = frase.split()
    print(lista_frase)