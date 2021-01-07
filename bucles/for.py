#Bucle for

resultado = 0

for i in range(0,10):
    print(f'voy por el numero {i}')
    resultado += i #sumo los numeros de la iteracion

print(f'El resultado de la itereaciones es de: {resultado}')

#Ejemplo tabla

numero_usuario = int(input("Ingrese numero de la tabla: "))

for numero_tabla in range(1,11):
    if numero_usuario < 1:
        print("Solo se puede realizar con numero negativos en estos momentos.")
        break
    else:
        print(f'{numero_usuario} x {numero_tabla} = {numero_usuario*numero_tabla}')