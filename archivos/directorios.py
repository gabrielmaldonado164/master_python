import  os
import  shutil

#Crear directorio
if not os.path.isdir("./archivos/mi_carpeta"):#verifico si ya existe o no
    os.mkdir("./archivos/mi_carpeta")#creo la carpeta
else:
    print("El directorio ya existe")

#Copiar
ruta_original = "./archivos/mi_carpeta"
ruta_nueva = "./archivos/mi_carpeta_2"
shutil.copytree(ruta_original,ruta_nueva)#copio el directorio argumentando la ruta y la ruta donde va a ser copiado

#Eliminar
#os.rmdir("./archivos/mi_carpeta_2")

#Listar archivos de los directorios
print("Contenido de las carpetas")

contenido  = os.listdir("./archivos/mi_carpeta")#lo lista como lista

#recorro la lista donde guarde el contenido con el metodo os.listdir() para visualizar los datos uno abajo del otro
for fichero in contenido:
    print(f'Fichero:{fichero}')