import pymysql

class Database():
    conexion = None

    def conectar(self):
        try:
            self.conexion = pymysql.connect(host='ca8.toservers.com',
                            user='gabrielh_admin',
                            passwd='gabi42020715',
                            db='gabrielh_test',
                            cursorclass=pymysql.cursors.DictCursor)
            return self.conexion 
        except Exception as e:
            print(f'Lo sinto, hubo un error en la conexion: {e}')
    
   
db = Database()
db.conectar()