#Importamos modulo para archivos
from io import open
import pathlib #poder tener el PATH Correcto
import os

#Veo en que ruta me encuentro
#os.path.abspath("./") -> nos saca la ruta absoluta de donde me encuentro
print(os.path.abspath("./"))#le puedo indicar dentro la ruta de donde queremos que ingrese a partir de la ruta absoluta que nos de
print("----------------------------------------")


#Hago una verificacion para ver si el archivo existe con el metodo de ISFILE()
if os.path.isfile(os.path.abspath("./archivos") + "/prueba.txt"):
    print("El archivo existe")
else:
    print("El archivo no existe")