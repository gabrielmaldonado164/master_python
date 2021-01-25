#Importamos modulo para archivos
from io import open
import pathlib #poder tener el PATH Correcto
import shutil #poder copiar, mover y elimimar archivos

#Copiar fichero
ruta_original = "archivos/prueba.txt"
ruta_nueva = "archivos/prueba_copiado.txt"
shutil.copyfile(ruta_original,ruta_nueva)#copiamos el archivo, le indicamos la ruta original y le decimos donde se tiene que copiar