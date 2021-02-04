import re
import bd


"""
ALEX: 04/02/2021 17:12
    Gabi, ojo con los nombres de las funciones. Por convencion, Python el nombramiento de las funciones
    debera de ser SIN camelcase. Es decir, NO menuPrincipal <= MAL | menu_principal <= BIEN.
"""


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
        except ValueError: # Podes tambien generalizar la excepcion mediante lo siguiente 
        #except Exception as NombreDeLaVariableDondeGuardaElError:
            print("Lo siento, no es un dato correcto, por favor ingrese un numero positivo")
            continue
    
    return opcion


def validarSring(string):
    """
    Esto quizas lo traes de C, pero https://i.ytimg.com/vi/x1Xp3Qy7c8k/hqdefault.jpg.  <= IMPORTANTE
    Aca con que ya el string sea var = "" ya es suficiente. Si queres que te salga seguro el string, simplemente con hacer que
    el mismo sea str(var) ya te lo convierte a string. Olvidate del resto. 
    El isalpha si bien esta bueno, te limita a solamente tener caracteres alfabeticos. Pero que pasa si es una contraseña...
    U otra cosa.
    """
        string.strip()
        if len(string) > 1 and  string.isalpha():
            return True
        else:
            return False


def getString(text):
    """
    Estan buenas las validaciones que haces. Para este caso, resulta ser bastante util. Pero dependera tambien a quien vaya dirigido
    la aplicacion pueda o no tener numeros, por ahi tenes un contacto con el mismo nombre. Que pasa si tenes Gabriel Galvan y Gabriel Maldonado. 
    Se te repiten? O es indiferente eso?
    """
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
        """
        el is not None tambien se puede resumir en if re.search(expresion, email): porque el None es un False en una validacion.
        """
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
            """
            el validar numero se puede hacer de otra manera, sin la necesidad de tantas lineas de codigo... 
            """
            if numero > 1 and validarNumero(numero):
            # if type(numero) is int and numero > 1:    -- con esto te resumis 5 o 6 lineas de codigo.
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
    # Podes hacer una funcion extra para el password, en la cual encripte la contraseña. Hay una libreria que es import base64
    """
        import base64

        data = "abc123!?$*&()'-=@~"

        # Standard Base64 Encoding
        encodedBytes = base64.b64encode(data.encode("utf-8"))
        encodedStr = str(encodedBytes, "utf-8")

        print(encodedStr)
        # Output
        YWJjMTIzIT8kKiYoKSctPUB+
    """

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
        """
        trata de hacer mas... compacto el codigo, no lo alargues tanto. Por eso me gusta mas el format jajajaaj
        """
        """
        print(
            'ID: {0} \nNombre:{1} \nApellido:{2} \nEmail:{3} \nPassword:{4} \nFecha de Creacion:{5}\n'.format(
                datos['id'],datos['nombre'],datos['apellido'],datos['email'],datos['password'],datos['fecha']
            )
        )
        """

def buscarUsuario(id,usuarios):
    for match in usuarios:
        if id == match["id"]:
            return True
            break
        else:
            return False





 


















