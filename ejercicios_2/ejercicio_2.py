"""
Ejercicio 2. Escribir un programa que añada valores a una lista mientras su longitud
sea menor a 120 y luego mostrar la Lista
PLUS: Usar while y for
"""

valores = []

for elemento in range(0,120):
    valores.append(f'Elemento: {elemento}')
    print(f'Mostrando elemento: {elemento}')

print(valores)


#CON WHILE

# datos = []
# x = 0

# while x < 120:
#     datos.append(f'Elementos: {x}')
#     print(f'Mostrando el elemento:{x}')
#     x += 1
