"""
Ejercicio 10.
    -Pedir 15 notas y verificar cuantos aprobaron y cuantos desaprobaron
"""

contador = 0
aprobados = 0
desaprobados = 0

while contador < 15:
    nota = int(input(f"Ingrese la nota del alumno {contador+1}: "))

    if nota >= 6:
        aprobados += 1
    else:
        desaprobados += 1
    
    contador += 1

print(f'La cantidad de aprobado es de {aprobados} y de desaprobados es {desaprobados}')

