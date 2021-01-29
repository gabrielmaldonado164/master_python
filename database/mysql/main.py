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
cursor.execute("""
CREATE TABLE IF NOT EXISTS productos(
    id INTEGER PRIMARY KEY AUTO_INCREMENT NOT NULL,
    titulo VARCHAR(25),
    descripcion TEXT,
    precio int(255)
);
""") 

conexion.commit()#guardar los cambios