import funciones
import usuarios

#4/2/2021 -> Hace lo basico, proximamente realizar  mejores validaciones y hacerlo mas interactivo

def main():
    menu = funciones.menu_principal()
    if menu == 1:
        try:
            user = usuarios.Usuario()
            user.listar_usuarios()
        except Exception as e:
            print(f'Error: {e}')    
    elif menu == 2:
        try:
            usuarios.Usuario().crear_registro()
        except Exception as e:
            print(f'Error: {e}')
    elif menu == 3:
        try:  
            user = usuarios.Usuario()
            listado = user.listar_usuarios()
            if len(listado) >= 1:
                funciones.mostrar_usuarios(listado)
                user.actualizar_usuario() 
            else:
                print('Lo sentimos, no hay usuarios registrados en el sistema')
        except Exception as e:
            print(f'Error: {e}')
    elif menu == 4:
        try:
            user = usuarios.Usuario()
            listado = user.listar_usuarios()
            if len(listado) >= 1:
                funciones.mostrar_usuarios(listado)
                user.eliminar_usuario()   
            else:
                print('Lo sentimos, no hay usuarios registrados en el sistema')
        except Exception as e:
            print(f'Error: {e}')  




main()
 