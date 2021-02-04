import funciones
import usuarios


def main():
    menu = funciones.menuPrincipal()
    if menu == 1:
        try:
            user = usuarios.Usuario()
            listado = user.listarUsuarios()
            if len(listado) > 1:
                funciones.mostrarUsuarios(listado)  
            else:
                print('Lo sentimos, no hay usuarios registrados')
        except Exception as e:
            print(f'Error: {e}')    
    elif menu == 2:
        try:
            usuarios.Usuario().crearRegistro()
        except Exception as e:
            print(f'Error: {e}')
    elif menu == 3:
        pass
    elif menu == 4:
        try:
            user = usuarios.Usuario()
            listado = user.listarUsuarios()
            if len(listado) > 1:
                funciones.mostrarUsuarios(listado)
                user.eliminarUsuario()   
            else:
                print('Lo sentimos, no hay usuarios registrados en el sistema')
        except Exception as e:
            print(f'Error: {e}')  




main()
 