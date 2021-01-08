"""
FUNCIONES
-Una funcion es un conjunto de instrucciones agrupados bajo un nombre concreto que puede 
reutilizarce invocando a la funciones tantas veces como sea necesario

    def nombre_funcion(parametros):
        instrucciones
"""

#Ejemplo 1

print("######### EJEMPLO 1 ###########")

#Definir funcion

def muestraDeNombres():
    print('Gabi')
    print('Kevin')
    print('Luis')
    print('Chino')
    print('Jessi')
    print('\n')

#Invocar funcion
muestraDeNombres()


#Ejemplo 2, com parametros

print("######### EJEMPLO 2 ###########")

def mostrarDatos(nombre,edad):
    print(f'Tu nombre es:{nombre} y tienes {edad} años')

    if edad >= 18: 
        print("Eres mayor de edad")

nombre = input("Ingrese su nombre: ")
edad = int(input("Ingrese su edad: "))

mostrarDatos(nombre, edad)

#Ejemplo 3

print("######### EJEMPLO 3 ###########")

def tabla(numero):
    print(f'Tabla de multiplicar de {numero}')

    for contador in range(11):
        operacion = numero * contador
        print(f'{numero} x {contador} = {operacion}')
    
    print("\n")

tabla(2)


#Ejemplo 3 bis, en el cual hago tablas del rango que le pase

for numero_tabla  in range(1,11): #al recorrer el mismo va realizando las tabla con el contador
    tabla(numero_tabla)




#Ejemplo 4
print("\n######### EJEMPLO 4 ###########")


def getEmpleado(nombre,dni = None):#el dni lo hago opcional
    print("EMPLEDO")
    print(f'Nombre:{nombre}')
    
    if dni != None:#veo si me paso un dato y lo muestro en todo caso
        print(f'Dni:{dni}')

getEmpleado('Gabriel',145611251) 



#Ejemplo 5
print("\n######### EJEMPLO 5 ###########")

def saludo(nombre):
    saludar = f'Que tengas un buen dia {nombre}'

    return saludar

print(saludo('Gabi'))


#Ejemplo 6, returns
print("\n######### EJEMPLO 6 ###########")

def calculadora(numero_uno, numero_dos):

     suma = numero_uno + numero_dos
     resta = numero_uno - numero_dos
     multiplicacion = numero_uno * numero_dos
     division =numero_uno / numero_dos

     cadena = ""
     cadena += 'Suma: ' + str(suma)
     cadena += '\nResta:' + str(resta)
     cadena += '\nMultiplicacion: ' + str(multiplicacion)
     cadena += '\nDivision: ' + str(division)

     return cadena 


print(calculadora(10,2))




#Ejemeplo 7, funciones dentro de otras
print("\n######### EJEMPLO 7 ###########")

def getNombre(nombre):
    texto = f'El nombre es:{nombre}'
    return texto

def getApellido(apellido):
    texto = f'El apellido es: {apellido}'
    return texto

#esta se encarga de llamar a las otras dos
def mostrarTodo(nombre, apellido):
    texto = getNombre(nombre) + '\n' + getApellido(apellido)
    return texto

print(mostrarTodo('Gabriel','Maldonado'))
