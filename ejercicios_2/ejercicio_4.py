"""
Ejercicio 4. 
    -Crear un scrip que tenga 4 variables: una lista, un string, un entero y un booleano
    y que imprama un mensaje segun el tipo de dato de cada variable.
    -Usar funciones 
"""
def indicarTipo(tipo):
    resultado = None

    if tipo  == list:
        resultado = 'LISTA'
    elif tipo == int:
        resultado = 'ENTERO'
    elif tipo == str:
        resultado = 'STRING'
    elif tipo == bool:
        resultado = 'BOOLEANO'

    return resultado


def comprobarTipo(dato,tipo):
    comprobacion = isinstance(dato, tipo)

    if  comprobacion:
        resultado = f'Este dato es de tipo {indicarTipo(tipo)}'
    else:
        resultado = None
    

    return  resultado


mis_datos = ['Gabriel', 'Maldonado', 21]
texto = 'Agunte programacion'
anio = 2021
verdadero = True

print(comprobarTipo(mis_datos,list))
print(comprobarTipo(texto,str))
print(comprobarTipo(anio,int))
print(comprobarTipo(verdadero,bool))

