#Capturar excepciones y manejar errores en codigo, susceptible a fallos/errores


#try - excepet (mas utilizado)

try:#intento de realizar el codigo
    nombre = input("Ingrese su nombre: ")

    if len(nombre) > 1:
        nombre_usuario = f'Su nombre es {nombre}'
    
    print(nombre_usuario)
except:#capturo el error y le trabajo, en este caso le damos un mensaje de error
    print("Ha ocurrido un error inesperado, por favor verificar de colocar caracteres y str")
else:#en caso funcionar el try, genero el else
    print("Todo ha funcionado de manera correcta")
finally:#se ejecuta si o si, ya que es el final de la iteracion
    print("Fin de la iteracion con el try")

print("--------------------------------------------")

#Manejo de multiples excepciones

"""
    Lo que hago es detectar/capturar cada error y dar un mensajer o realizar una cierta tarea indicada
"""
try:
    numero = int(input("Ingrese un numero: "))
    print(f'La raiz cuadrada es  {numero*numero}')
except ValueError:
    print("Ingrese un numero valido por favor")
except TypeError:
    print("No se puede sumar dos STRING")

