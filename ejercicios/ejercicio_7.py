"""
Ejercicio 7.
    -Mostrar todo los numeros impares entre dos valores que usuario pase por consola
"""

rango_uno = int(input("Ingrese el primer valor para mostrar los numeros: "))
rango_dos = int(input("Ingrese el segundo valor para mostrar los numeros: "))

if rango_uno < rango_dos:
    for i in range(rango_uno,rango_dos+1):
        if i%2 != 0:
            print(f'Los numeros impare son:{i}')
else:
    print("El primero valor no puede ser menor que el segundo")
