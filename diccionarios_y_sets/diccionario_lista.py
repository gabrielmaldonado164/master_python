"""
Diccionario dentro de una lista y como recorrerlo
"""

personas = [
    {
        'nombre':'Gabriel',
        'email':'gabriel@gmail.com'
    },
    {
        'nombre':'Kevin',
        'email':'kevin@gmail.com'
    },
    {
        'nombre':'Uli',
        'email':'uli@gmail.com'
    }

]


print(personas)
print("\-----------------------------------------------")
print(personas[0]['nombre'])#indicando el index del elemento y la key puedo mostrarlo
print("\-----------------------------------------------")


print("\n Listada de contactos: ")
print("\-----------------------------------------------")

for contacto in personas:
    print(f'Nombre del contacto: {contacto["nombre"]}')
    print(f'Email del contacto: {contacto["email"]}')
    print("\n-----------------------------------------------")
