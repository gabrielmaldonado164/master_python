
def menuPrincipal():
    while True:
        try:
            print("----- Menu Principal -----")
            print("1) Listar usuarios")
            print("2) Registrar usuario")
            print("3) Actualizar usuario")
            print("4) Eliminar usuario")
            print("5) Salir\n")
            opcion = int(input('Ingrese una opcion correspondiente: '))

            if opcion < 1 or opcion > 5:
                print("Opcion incorrecta, por favor ingrese una opcion del menu")
                print("---------------------------------------------------------\n")
            else:
                break     
        except ValueError:
            print("Lo siento, no es un dato correcto, por favor ingrese un numero positivo")
            continue
    
    return opcion





