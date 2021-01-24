#Importamos modulo para archivos
from io import open
import pathlib #poder tener el PATH Correcto


#Abrir archivo

#le indico la ruta donde buscar 
#ruta = str(pathlib.Path(__file__).parent) +" /prueba.txt" ---> LE PUEDO INDICAR CON EL PATH LA RUTA 
archivo = open("archivos/prueba.txt", "a+")# ruta - permisos

#Escribir
archivo.write('Hola, soy un texto por medio de python')#Al tener permiso a+ -> escribe al final del archivos

#Cerrar Archivo
archivo.close()
