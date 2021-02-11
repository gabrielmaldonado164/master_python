#-*- coding: utf-8 -*-
import re
import hashlib
import bd
import string



"""
ALEX: 04/02/2021 17:12
    Gabi, ojo con los nombres de las funciones. Por convencion, Python el nombramiento de las funciones
    debera de ser SIN camelcase. Es decir, NO menuPrincipal <= MAL | menu_principal <= BIEN.
"""

def menu_principal():
    while True:
        try:
            print("\n\t\t    ----- Menu Principal -----\n")
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
            print("Lo siento, no es un dato correcto, por favor ingrese un numero positivo.")
            continue
    return opcion

def menu_modificaciones():
    while True:
        try:
            print("\n\t\t      ----- Menu de modificaciones -----\n")
            print("1) Modificar nombre")
            print("2) Modificar apellido")
            print("3) Modificar email")
            print("4) Salir\n")
            opcion = int(input('Ingrese una opcion correspondiente: '))

            if opcion < 1 or opcion > 4:
                print("Opcion incorrecta, por favor ingrese una opcion del menu...")
                print("---------------------------------------------------------\n")
            else:
                break
        except Exception as e:
            print(f'Lo siento, no es un dato correcto, por favor ingrese un numero del menu')
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
    
    nuevo = string.split()
    aprobed = None
    for i in nuevo:
        if i.isalpha() and i != '':
            aprobed = True
        else:
            aprobed = False
            break
    return aprobed



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
    return dato.capitalize()


def validar_email(email):
    expresion = "^[a-zA-Z0-9.!#$%&'+/=?^_`{|}~-]+@[a-zA-Z0-9.-]+(?:\.[a-zA-Z0-9-]+)$"

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
            print('Lo siento, debe ingresar un numero\n')
    return numero

def get_password(text): 
    password = input(text)
    cifrado = hashlib.sha256(password.encode('utf-8'))

    return cifrado.hexdigest()



def pedir_datos():
    nombre =  get_string('Ingrese su nombre: ')
    apellido = get_string('Ingrese su apellido: ')
    email = get_email('Ingrese su email: ')
    password = get_password('Ingrese su contraseña: ')#tengo que hacer una funcion especifico para la pass distinto al string
    # Podes hacer una funcion extra para el password, en la cual encripte la contraseña. Hay una libreria que es import base64
    # conexion = bd.Database().conectar()
    # listado =  conexion.listar_usuarios()
    # if buscar_email(listado,email):
    #     email = get_email('Ingrese su email: ')
    #     continue
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
    print('\t\t----- Listado de  Usuarios en base  ----- \n')
    for datos in usuarios:
        print(
            'ID: {0} \nNombre:{1} \nApellido:{2} \nEmail:{3} \nPassword:{4} \nFecha de Creacion:{5}\n'.format(
                datos['id'],datos['nombre'],datos['apellido'],datos['email'],datos['password'],datos['fecha']
            )
        )
        # viejo -> print(f'ID:{datos["id"]} |  Nombre:{datos["nombre"]}  ----   Apellido:{datos["apellido"]}    ----     Email:{datos["email"]}      ----      Password:{datos["password"]}     ----    Fecha de Creacion:{datos["fecha"]}\n')
    

def buscar_usuario(usuarios,id):
    for match in usuarios:
        if match['id'] == id:
            return True
            break

def buscar_email(usuarios,email):
    for match in usuarios:
        if match['email'] in email.values():
            return True 
            break        

def switch(opcion):
    final = {'none': None}
    while True:
        if opcion == 1:
            dato = {'nombre':get_string('Ingrese nombre nuevo: ')}#lo que se me ocurrio por el momento 8/2/2021      
        elif opcion == 2:
            dato = {'apellido':get_string('Ingrese apellido: ')}
        elif opcion == 3:
            dato = {'email':get_email('Ingrese email nuevo: ')}
        elif opcion == 4:
            final = {'false':False}
            break
        while  True:
            confirmarcion = get_string('Desea confirmar el cambio(s/n)')
            if confirmarcion.lower() == 's':
                final = dato 
                break
                #print('Cambio realizado correctamente.')
            elif  confirmarcion.lower() == 'n':
                print('El cambio no se realizo.')
                break
            else:
                print('Letra invalida.')
                continue
        break
    return final

def prueba():
    dato = str(input('Ingrese nombre: '))
    nuevo = dato.split()
    aprobed = None
    for i in nuevo:
        if i.isalpha() and i != '':
            aprobed = True
        else:
            aprobed = False
            break
    return aprobed
