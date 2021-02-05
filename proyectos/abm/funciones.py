import re
import bd


"""
ALEX: 04/02/2021 17:12
    Gabi, ojo con los nombres de las funciones. Por convencion, Python el nombramiento de las funciones
    debera de ser SIN camelcase. Es decir, NO menuPrincipal <= MAL | menu_principal <= BIEN.
"""

def menu_principal():
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
                print("Opcion incorrecta, por favor ingrese una opcion del menu...")
                print("---------------------------------------------------------\n")
            else:
                break     
        except Exception as e: # Podes tambien generalizar la excepcion mediante lo siguiente 
        #except Exception as NombreDeLaVariableDondeGuardaElError:
            print("Lo siento, no es un dato correcto, por favor ingrese un numero positivo")
            continue
    return opcion


def validar_string(string):
    """
    Esto quizas lo traes de C, pero https://i.ytimg.com/vi/x1Xp3Qy7c8k/hqdefault.jpg.  <= IMPORTANTE
    Aca con que ya el string sea var = "" ya es suficiente. Si queres que te salga seguro el string, simplemente con hacer que
    el mismo sea str(var) ya te lo convierte a string. Olvidate del resto. 
    El isalpha si bien esta bueno, te limita a solamente tener caracteres alfabeticos. Pero que pasa si es una contraseña...
    U otra cosa.
    """
    # viejo -- 
    # string.strip()
    # if len(string) > 1 and  string.isalpha():
    #     return True   
    # else:
    #    return False
    if string.isalpha() and (string != ""):
        return True
    else:
        return False


def get_string(text):
    """
    Estan buenas las validaciones que haces. Para este caso, resulta ser bastante util. Pero dependera tambien a quien vaya dirigido
    la aplicacion pueda o no tener numeros, por ahi tenes un contacto con el mismo nombre. Que pasa si tenes Gabriel Galvan y Gabriel Maldonado. 
    Se te repiten? O es indiferente eso?
    """
    flag = False
    while not flag:
        dato = input(text)
        if validar_string(dato):
            flag = True
        else:
            print('Lo siento, no es un nombre valido, recuerde no puede contener numeros ni caracteres especiales y tiene que ser mas de 1 caracter')
    return dato


def validar_email(email):
    expresion = "(^[a-zA-Z0-9.!#$%&'+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)$)"

    #if re.search(expresion, email) is not None -> viejo
    if re.search(expresion, email):
        """
        el is not None tambien se puede resumir en if re.search(expresion, email): porque el None es un False en una validacion.
        """
        return True
    else:
        return False


def get_email(text):
    flag = False
    while not flag:
        email = input(text)
        if validar_email(email):
            flag = True
        else:
            print('Lo siento, no es un correo valido.') 
    return email

# def validarNumero(numero):
#     if int(numero): 
#         return True
#     else:
#         return False


def get_numero(text):
    flag = False
    while not flag:
        try:
            numero = int(input(text))
            """
            el validar numero se puede hacer de otra manera, sin la necesidad de tantas lineas de codigo... 
            """
            #if numero > 1 and validarNumero(numero): -> viejo
            if type(numero) is int and numero >= 1:
                flag = True
            else:
                print('Lo siento, debe ser un numero positivo')
        except ValueError:
            print('Lo siento, debe ingresar un numero')
    return numero


def pedir_datos():
    nombre =  get_string('Ingrese su nombre: ')
    apellido = get_string('Ingrese su apellido: ')
    email = get_email('Ingrese su email: ')
    password = input('Ingrese su clave: ')#tengo que hacer una funcion especifico para la pass distinto al string
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

    
def mostrar_usuarios(usuarios):
    print('-----  Usuarios  ----- ')
    for datos in usuarios:
        print(
            'ID: {0} \nNombre:{1} \nApellido:{2} \nEmail:{3} \nPassword:{4} \nFecha de Creacion:{5}\n'.format(
                datos['id'],datos['nombre'],datos['apellido'],datos['email'],datos['password'],datos['fecha']
            )
        )
        # viejo -> print(f'ID:{datos["id"]} |  Nombre:{datos["nombre"]}  ----   Apellido:{datos["apellido"]}    ----     Email:{datos["email"]}      ----      Password:{datos["password"]}     ----    Fecha de Creacion:{datos["fecha"]}\n')
    

def buscar_usuario(id,usuarios):
    for match in usuarios:
        if id == match['id']:
            return True
            break
        else:
            return False

