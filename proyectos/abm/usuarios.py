import bd
import funciones

class Usuario:
    def crearRegistro(self):
        conexion = bd.Database().conectar()
        if conexion.open:
            try:
                datos = funciones.pedirDatos()
                cursor = conexion.cursor()
                cursor.executemany('INSERT INTO usuarios (nombre, apellido, email, password,fecha) VALUES (%s,%s,%s,%s,20)',datos[0],datos[1],datos[2],datos[3])
                conexion.commit()
                print('Ingresado')
            except Exception as e:
                print(f'Error{e}')

                
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      