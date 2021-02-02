import pymysql

class BaseDatos:
    def __init__(self):
        try:
            self.conexion = pymysql.connect(host='ca8.toservers.com',
                            user='gabrielh_admin',
                            passwd='gabi42020715',
                            db='gabrielh_test',
                            port=3306,
                            cursorclass=pymysql.cursors.DictCursor)
            self.cursor = self.conexion.cursor()
        except Exception as e:
            print(f'Error al intentar la conexion {e}')
        
    def close(self):
        self.conexion.close()
    

        