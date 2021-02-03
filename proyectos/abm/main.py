import funciones
import usuarios


def main():
    menu = funciones.menuPrincipal()
    if menu == 2:
        usuarios.Usuario().crearRegistro()

main()
