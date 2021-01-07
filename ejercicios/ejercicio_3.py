"""
Ejercicio 3.
    -Realizar un programa que muestre los cuadrados de los primeros 60 numeros naturales

"""

#for
for i in range(1,61):
    resultado = i * i
    print(f'El cuadrado de {i} es {resultado}')

#while
print("----------------------------------------------")
contador = 1

while contador <= 60:
    resultado = contador * contador
    print(f'El cuadrado de {contador} es {resultado}')
    contador += 1