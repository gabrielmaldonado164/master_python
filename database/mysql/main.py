import pymysql


conexion = pymysql.connect(host='ca8.toservers.com',
                            user='gabrielh_admin',
                            passwd='gabi42020715',
                            db='gabrielh_test',
                            cursorclass=pymysql.cursors.DictCursor) #<- un cursor que devuelve resultados como diccionarios

cursor = conexion.cursor()

#crear database
cursor.execute('CREATE DATABASE IF NOT EXISTS gabrielh_test')
#crear tabla
table = cursor.execute("""
CREATE TABLE IF NOT EXISTS productos(
    id INTEGER PRIMARY KEY AUTO_INCREMENT NOT NULL,
    titulo VARCHAR(55) NOT NULL,
    descripcion TEXT,
    precio int(255)
);
""") 

conexion.commit()#guardar los cambios

cursor.execute('SHOW TABLES')

for i in cursor:
    print(table)

"""
Insertar datos
"""
# cursor.execute('INSERT INTO productos VALUES(null, "pantalon", "pantalones de jeans", 2555)')
# conexion.commit()#guardamos los cambios


#multiples ingreso de datos
datos_ingresar = [ #genera una lista con tuplas para pasra a una solo consulta
    ('Telefono','piola',50),
    ('computadora','god',122),
    ('impresora','buenardo',122),
]

#cursor.executemany("INSERT INTO productos VALUES(null,%s,%s,%s)",datos_ingresar)#executemany() -> para varias consultas, los signos de interrogacion es para psar las lista de tuplas
conexion.commit()


"""
Listar datos de la tabla
"""
#Listar datos
cursor.execute('SELECT * FROM productos WHERE precio <= 200') #ejecuta para mostrar datos con el WHERE indicando la condicion en especifico
productos = cursor.fetchall()#nos muestra todo los datos de la base

#recorro los datos para mostrarlo de manera limpia
for i in productos:
    print(i)


"""
Eliminar datos de la tabla
"""

#cursor.execute('DELETE FROM productos WHERE titulo = "pantalon"') #eliminamos datos indicando con el WHERE, ya que si no lo indicamos nos elimina toda la base completa
#conexion.commit()

print(cursor.rowcount, "borrados!!")#nos indica cuantas filas fueron eliminados

"""
Actualizar datos
"""

cursor.execute("UPDATE productos SET titulo='xiaomi' WHERE titulo='telefono'")#actualizo los precios de los que valen 122 por 326
conexion.commit()
print(cursor.rowcount, "actualizado!!")



