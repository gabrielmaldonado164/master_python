"""
Una variables es un contenedor de informacion que dentro guardara un dato, 
se pueden crear muchas variables y que cada una tenga un dato distinto
"""

#crear variable y asignarle valor
texto = "Que lindo dia"
entero = 25
decimal = 2.50

#muestrar los datos
print(texto)
print(entero)
print(decimal)

print("#######################")

#3 maneras de concatenar
nombre = "Gabriel"
apellido = "Maldonado"
edad = "21"

#toda las maneras son validas
print(nombre + " " + apellido + " tiene " + edad)
print(f'{nombre} {apellido} tiene {edad}')
print("{} {} tiene {}".format(nombre, apellido, edad))

