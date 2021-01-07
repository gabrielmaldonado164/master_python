"""
Ejercicio 5.
    -Realizar un programa que muestre todo los nuemeros, entre los que el usuario pase por consola
"""

rango_uno = int(input("Ingrese el primer valor para mostrar los numeros: "))
rango_dos = int(input("Ingrese el segundo valor para mostrar los numeros: "))

if rango_uno < rango_dos:        
    for i in range(rango_uno,rango_dos+1):
        print(f'Los numeros son: {i}')
else:     
    print("El primero valor debe ser menor que el segundo")