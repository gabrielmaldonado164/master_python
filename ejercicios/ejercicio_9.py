"""
Ejercicio 9.
    -Peridr al usuario numeros indefinidamente, hasta que coloque 111 y se termine el programa
"""



contador = 0
while contador < 100:
    numero = int(input("Introduce un numero: "))

    if numero == 111:
        break
    else:
        print(f'Ingreso el numero {numero}')
    
    contador += 1