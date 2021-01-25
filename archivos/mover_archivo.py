#Importamos modulo para archivos
from io import open
import pathlib #poder tener el PATH Correcto
import shutil #poder copiar, mover y elimimar archivos


#Mover archivo
ruta_original = "archivos/prueba_copiado.txt"
ruta_nueva = "../archivos"
shutil.move(ruta_original,ruta_nueva)#le indicdo las ruta original y la nueva para poder mover el archivo