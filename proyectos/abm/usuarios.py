import bd
import funciones

class Usuario:
    conexion = bd.Database().conectar()
    def crearRegistro(self):
        if self.conexion.open:
            try:
                datos = funciones.pedirDatos()
                cursor = self.conexion.cursor()
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
                    cursor.execute('DELETE FROM usuarios WHERE id = {0}', format(ids))
                    self.conexion.commit()
                else:
                    print('Lo sentimos no hay un usuarios con ese ID')
            except Exception as e:
                print(f'Error: {e}')
        else:
            pass






