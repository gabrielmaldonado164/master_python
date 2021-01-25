#Importamos modulo para archivos
from io import open
import pathlib #poder tener el PATH Correcto


""" Permisos:
        r -> Leer,abrir un archivos, da error si no existe
        a -> Agregar, abre un archivo para agregarlo, crea el archivo si no existe
        w -> Escribir, abre un archivo para escribir, crea el archivo si no existe
        x -> Crea, crea el archivo indicado, devuelve un error si exixte el archivo
"""

#Abrir archivo

#le indico la ruta donde buscar 
#ruta = str(pathlib.Path(__file__).parent) +" /prueba.txt" ---> LE PUEDO INDICAR CON EL PATH LA RUTA 
archivo = open("archivos/prueba.txt", "a+")# ruta - permisos(tipo A -> crea el archivo si no existe)

#Escribir
archivo.write('Hola, soy un texto por medio de python')#Al tener permiso a+ -> escribe al final del archivos

#Cerrar Archivo
archivo.close()
