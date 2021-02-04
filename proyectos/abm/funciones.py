import re
import bd

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

def validarSring(string):
        string.strip()
        if len(string) > 1 and  string.isalpha():
            return True
        else:
            return False

def getString(text):
    flag = False
    while not flag:
        dato = input(text)
        if validarSring(dato):
            flag = True
        else:
            print('Lo siento, no es un nombre valido, recuerde no puede contener numeos ni caracteres especiales y tiene que ser mas de 1 caracter')
    return dato

def validarEmail(email):
    expresion = "(^[a-zA-Z0-9.!#$%&'+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)$)"

    if re.search(expresion, email) is not None:
        return True
    else:
        return False

def getEmail(text):
    flag = False
    while not flag:
        email = input(text)
        if validarEmail(email):
            flag = True
        else:
            print('Lo siento, no es un correo valido.') 

    return email

def validarNumero(numero):
    if int(numero):
        return True
    else:
        return False

def getNumero(text):
    flag = False
    while not flag:
        try:
            numero = input(text)
            if numero > 1 and validarNumero(numero):
                flag = True
            else:
                print('Lo siento, debe ser un numero positivo')
        except ValueError:
            print('Lo siento, debe ingresar un numero')
    return numero


def pedirDatos():
    nombre =  getString('Ingrese su nombre: ')
    apellido = getString('Ingrese su apellido: ')
    email = getEmail('Ingrese su email: ')
    password = input('Ingrese su clave: ')

    datos = {
        'nombre':nombre,
        'apellido':apellido,
        'email':email,
        'password':password
    }

    return datos

    
def mostrarUsuarios(usuarios):
    for datos in usuarios:
        print('-----  Usuarios  ----- ')
        print(f'ID:{datos["id"]} |  Nombre:{datos["nombre"]}  ----   Apellido:{datos["apellido"]}    ----     Email:{datos["email"]}      ----      Password:{datos["password"]}     ----    Fecha de Creacion:{datos["fecha"]}\n')


def buscarUsuario(id,usuarios):
    for match in usuarios:
        if id == match["id"]:
            return True
            break
        else:
            return False





 


















