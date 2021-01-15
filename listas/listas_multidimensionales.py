#Listas multidimensionales

print("*************** Listada de contactos ****************")

contactos = [
    [
        "Chino",
        "chino@gmail.com"
    ],
    [
        "Uli",
        "uli@gmail.com"
    ],

    [
        "kevin",
        "kevin@gmail.com"
    ]
]


#recorro los dos arrays

for contacto in contactos:#primera dimension
    print("\n")
    for elemento in contacto:#segunda dimension
        print(elemento)
