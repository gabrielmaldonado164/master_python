import bd
#Podes tambien hacer lo siguiente
# from bd import Database
import funciones

class Usuario:
    conexion = bd.Database().conectar()
    # y con esto guardar conexion
    # conexion = Database().conectar()

    # Tambien podes SI QUERES, instancias como variable global el cursor
    # cursor = conexion.cursor()

    def crearRegistro(self):
        if self.conexion.open:
            try:
                datos = funciones.pedirDatos()
                cursor = self.conexion.cursor()
                #entonces te queda self.cursor para ya tirar executes a lo loco.
                sql = 'INSERT INTO usuarios (nombre, apellido, email, password) VALUES (%s, %s, %s, %s)'
                cursor.execute(sql,(datos['nombre'], datos['apellido'],datos['email'],datos['password']))
                self.conexion.commit()
                print('Registrado correctamente! ')
            except Exception as e:
                print(f'Error: {e}')
            finally:
                self.conexion.close()
        else:
            print('Al parecer hay  problemas de conexion')
    
    def listarUsuarios(self):
        if self.conexion.open:
            try:
                cursor = self.conexion.cursor()
                #entonces te queda self.cursor para ya tirar executes a lo loco.
                cursor.execute('SELECT * FROM usuarios')
                resultados = cursor.fetchall() 
                return resultados
            except Exception as e:
                print('Error use: {e}')
            finally:
                self.conexion.close()
        else:
            pass
    
    def eliminarUsuario(self):
        if self.conexion.open:
            try:
                print('hola')
                ids = funciones.getNumero('Ingrese ID del usuario a eliminar: ')
                usuarios = self.listarUsuarios()
                if funciones.buscarUsuario(ids,usuarios):
                    cursor = self.conexion.cursor()
                    #entonces te queda self.cursor para ya tirar executes a lo loco.
                    cursor.execute('DELETE FROM usuarios WHERE id = {0}', format(ids)) # ojo aca que no estas formateando correctamente
                    # cursor.execute('DELETE FROM usuarios WHERE id = {0}'.format(ids)) - por lo menos yo lo haria asi. 
                    self.conexion.commit()
                else:
                    print('Lo sentimos no hay un usuarios con ese ID')
            except Exception as e:
                print(f'Error: {e}')
        else:
            pass






