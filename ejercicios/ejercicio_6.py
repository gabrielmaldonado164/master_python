"""
Ejercicio 6.
    -Mostrar toda las tablas del 1 al 10 y que cada titulo tenga el numero de la tabla que va a mostrar
"""

#for anidado
for i in range(1,11):
    print("##############################")
    print(f'#### Tabla del {i} ##########')
    print("##############################")

    for j in range(1,11):
        print(f'{i} x {j} = {i * j}')