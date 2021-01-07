"""
Ejercico 8.
    -Sacar el porcetaje de un numero
    -El usuario indica el numero
    -El usuario indica el porcentaje
"""

numero = int(input("Ingrese un numero: "))
numero_porcentaje = int(input(f"Ingrese el porcetaje para sacarle al numero {numero}: "))

porcentaje = (numero * numero_porcentaje) / 100

print(f'El {numero_porcentaje}% de {numero} es {porcentaje}')