import funciones
import usuarios
import  os

#4/2/2021 -> Hace lo basico, proximamente realizar  mejores validaciones y hacerlo mas interactivo
#8/2/2021 -> se maneja bien con la base, hay que verificar las validaciones y hacerlo interactivo

def main():
    while True:
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
                user.actualizar_usuario()
            except Exception as e:
                print(f'Error: {e}')
        elif menu == 4:
            try:
                user = usuarios.Usuario()
                user.eliminar_usuario()
            except Exception as e:
                print(f'Error: {e}')  
        elif menu == 5:
            print('Hasta luego!')
            exit()
            



if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("\n")
        exit()
 