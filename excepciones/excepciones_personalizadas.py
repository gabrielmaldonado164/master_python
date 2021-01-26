"""
    Puedeo personalizar un tipo de error, indicando un mensaje por ejemplo
    
    .El keyword RAISE, puede personalizar el mensaje, puedo indicar el tipo de error que tengo y lanzar el mensaje,
    .Los raise pueden estar dentro de try - except en caso de que se de otro tipos de errores ls que no queremos personalizar,
    el mismo para poder capturarlo y poder tratarlo
"""

nombre = input("Ingrese su nombre: ")
edad = int(input("Ingrese su edad: "))

if edad  < 2 or edad > 105:
    raise ValueError("La edad no es correcta") 
elif len(nombre) <= 1:
    raise ValueError("El nombre no es correcto, ingrese + de 1 caracter")
else: 
    print(f'Bienvenido {nombre} con tus {edad} años')
