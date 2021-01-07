"""
    BUCLE WHILE
Estructura de contro que itera o repite la ejecucion de una serie de instrucciones de tantas veces como sea  necesarion, haste que deje de cumplirse la condicion

WHile condicion
    bloque de instrucciones
    actualizar el contador
"""

contador = 1

while contador <= 100:
    print(f'Estoy en el numero: {contador}')
    contador += 1

#ejemplo con coma seperador

mostrar = str(0)
contador = 1

while contador <= 100:
    mostrar = mostrar + ", " + str(contador)
    contador += 1

print(mostrar)


#ejemplo tabla

contador = 1

numero_usuario = int(input("Ingresar numero de tabla: "))

while contador <= 10:
    if numero_usuario < 1:
        print("Solo se puede realizar con numero negativos en estos momentos.")
        break
    else:
        print(f'{numero_usuario} x {numero_tabla} = {numero_usuario*numero_tabla}')

