#-*- coding: utf-8 -*-
from bd import Database
#Podes tambien hacer lo siguiente
# from bd import Database
import funciones
import os

class Usuario:
    #viejo -> conexion = bd.Database().conectar()
    # y con esto guardar conexion
    try:
        conexion = Database().conectar()
        cursor = conexion.cursor()
    except Exception as e:
        print('xd' + e)
    # Tambien podes SI QUERES, instancias como variable global el cursor
    # cursor = conexion.cursor()

    def crear_registro(self):
        if self.conexion.open:
            try:
                datos = funciones.pedir_datos()  
                #entonces te queda self.cursor para ya tirar executes a lo loco.
                sql = 'INSERT INTO usuarios (nombre, apellido, email, password) VALUES (%s, %s, %s, %s)'
                self.cursor.execute(sql,(datos['nombre'], datos['apellido'],datos['email'],datos['password']))
                self.conexion.commit()
                print('\n\tRegistrado correctamente!!! \n')
            except Exception as e:
                print(f'Error: {e}')
            finally:
                pass
        else:
            print('Al parecer hay  problemas de conexion...')
    
    def listar_usuarios(self):
        if self.conexion.open:
            try:
                self.cursor.execute('SELECT * FROM usuarios ORDER BY id ASC')
                resultados = self.cursor.fetchall() 
                if len(resultados) >= 1:
                    funciones.mostrar_usuarios(resultados)
                    return resultados
                else:
                    print('Lo siento, no hay usuarios registrados en el sistema.\n')
                    return False
            except Exception as e:
                print(f'Error use: {e}')
            finally:
                pass
        else:
            pass
    
    def eliminar_usuario(self):
        if self.conexion.open:
            try:
                listado = self.listar_usuarios()
                if listado != False:
                    ids = funciones.get_numero('Ingrese ID del usuario a eliminar: ')
                    if funciones.buscar_usuario(listado,ids):
                        self.cursor.execute('DELETE FROM usuarios WHERE id = {0}'.format(ids))
                        self.conexion.commit()
                        print('Usuarios eliminado correctamente')
                    else:
                        print('Lo siento, no hay usuarios con ese id, volviendo al menu principal...\n')
                # ids = funciones.get_numero('Ingrese ID del usuario a eliminar: ')
                # usuarios = self.listar_usuarios()
                # if funciones.buscar_usuario(ids,usuarios):
                #     #entonces te queda self.cursor para ya tirar executes a lo loco.
                #     self.cursor.execute('DELETE FROM usuarios WHERE id = {0}'.format(ids)) # ojo aca que no estas formateando correctamente
                #     # cursor.execute('DELETE FROM usuarios WHERE id = {0}'.format(ids)) - por lo menos yo lo haria asi. 
                #     self.conexion.commit()
                #     print('Usuario eliminado correctamente')
                # else:
                #     print('Lo sentimos no hay un usuarios con ese ID')
            except Exception as e:
                print(f'Error: {e}')
        else:
            print('Error en la conexion, verifique si se encuentra conectado\n')
        
    def actualizar_usuario(self):
        if self.conexion.open:
            try:
                listado = self.listar_usuarios()
                if listado != False:
                    ids = funciones.get_numero('Ingrese ID del usuario a actualizar: ')
                    if  funciones.buscar_usuario(listado,ids):
                        while True:
                            menu = funciones.menu_modificaciones()
                            opciones = funciones.switch(menu)
                            print(opciones)
                            if 'nombre' in opciones:
                                self.cursor.execute('UPDATE usuarios SET nombre = "{}" WHERE id = {}'.format(opciones['nombre'],ids))
                                print('Usuario actualizado!!')
                                self.conexion.commit()
                            elif 'apellido' in opciones:
                                self.cursor.execute('UPDATE usuarios SET apellido = "{}" WHERE id = {}'.format(opciones['apellido'],ids))
                                print('Usuario actualizado!!')
                                self.conexion.commit()
                            elif 'email' in opciones:
                                if funciones.buscar_email(listado,opciones):
                                    print('Lo siento, no se puede agregar el email ya que se encuentra registrado en base.\n')
                                else:
                                    self.cursor.execute('UPDATE usuarios SET email = "{}" WHERE id = {}'.format(opciones['email'],ids))
                                    self.conexion.commit()
                            elif opciones.values() == None:
                                continue
                            elif 'false' in opciones:
                                print('Volviendo al menu principal...')
                                #os.system('clear')

                                break
                    else:
                        print('Lo siento, no se encontro un usuario con ese id')               

                # ids = funciones.get_numero('Ingrese ID del usuario a actualizar: ')
                # usuarios = self.listar_usuarios()
                # # self.cursor.execute('UPDATE usuarios SET nombre="pep" WHERE id=7)
                # # self.conexion.commit()
                # if funciones.buscar_usuario(ids,usuarios):
                #     nombre = funciones.get_string('Ingrese nombre nuevo: ')
                #     apellido = funciones.get_string('Ingrese apellido nuevo: ')
                #     email = funciones.get_email('Ingrese email nuevo: ')

                #     sql = 'UPDATE usuarios SET nombre = "{0}", apellido = "{1}", email = "{2}" WHERE id = {3}'
                #     self.cursor.execute(sql.format(nombre,apellido,email,ids))
                #     self.conexion.commit()
                #     print('Correctamente actualizado')
                # else:
                #     print('Lo siento no se encontro un usuario con ese ID')
            except Exception as e:
                print(f'Error del try actualizar:  {e}')
        else:
            print('Error en la conexion, verifique si se encuentra conectado')