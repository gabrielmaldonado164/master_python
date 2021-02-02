import sqlite3
"""
Conexion y creacion de una tabla 
"""
#Conexion a la base de datos
conexion = sqlite3.connect('pruebas.db')

#Crear cursor -> nos permite recorrer y procesar las consultas para luego poder ejecutarla
cursor = conexion.cursor()

#Crear tabla -> con execute ejeuctamos la peticion de un cursor
cursor.execute("""CREATE TABLE IF NOT EXISTS productos(
id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, 
titulo VARCHAR(25), 
descripcion TEXT, 
precio int(255)
)""") 

#Guardar cambios que se realizan en la bd
conexion.commit()
 


"""
 Insertar y listar datos
"""
#Insertamos datos a nuestra tabla
cursor.execute('INSERT INTO productos VALUES(null, "pantalon", "pantalones de jeans", 2555)')
conexion.commit()#guardamos los cambios

#----------------------------------------------------------------------------------------------------------------------------
# """
# Eliminar datos
# """
cursor.execute('DELETE FROM productos')
conexion.commit()
#--------------------------------------------------------------------------------------------------------------------------

#multiples ingreso de datos
datos_ingresar = [ #genera una lista con tuplas para pasra a una solo consulta
    ('Telefono','piola',50),
    ('computadora','god',122),
    ('impresora','buenardo',122),
]

cursor.executemany("INSERT INTO productos VALUES(null,?,?,?)",datos_ingresar)#executemany() -> para varias consultas, los signos de interrogacion es para psar las lista de tuplas
conexion.commit()

#----------------------------------------------------------------------------------------------------------------------------------
"""update"""
cursor.execute('UPDATE productos SET precio=326  WHERE precio=122')#actualizo los precios de los que valen 122 por 326
conexion.commit()

#Listar datos
cursor.execute('SELECT * FROM productos')
productos = cursor.fetchall()#nos muestra todo los datos de la base
print(productos)


#recorro los datos para mostrarlo uno por uno
for i in productos:
    print(i)

#Listar solo un dato
producto = cursor.fetchone()#no saca solo el primer registro que tenga la consulta
print(producto)


#Cerrar conexion(siempre)
conexion.close()