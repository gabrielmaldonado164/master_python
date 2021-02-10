#-*- coding: utf-8 -*-
try:
    import funciones
    import usuarios
    import  os
    import sys
except Exception as e:
    print(e)
    exit()

LIMPIAR = "clear " if sys.platform.startswith("linux") else "cls"
#4/2/2021 -> Hace lo basico, proximamente realizar  mejores validaciones y hacerlo mas interactivo
#8/2/2021 -> se maneja bien con la base, hay que verificar las validaciones y hacerlo interactivo

def main():
    while True:
        menu = funciones.menu_principal()
        if menu == 1:
            try:
                #os.system(LIMPIAR)
                user = usuarios.Usuario()
                user.listar_usuarios()
                input('para continuar presione enter...')
            except Exception as e:
                print(f'Error: {e}')    
        elif menu == 2:
            try:
                usuarios.Usuario().crear_registro()
                #os.system(LIMPIAR)
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
            conexion = bd.Database().conectar()
            conexion.close()
            exit()
            



if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("\n")
        print('Interrupcion del programa.')
        exit()
 