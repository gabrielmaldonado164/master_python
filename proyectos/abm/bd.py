#-*- coding: utf-8 -*-
import pymysql

class Database():
    conexion = None
    def conectar(self):
        base = 'CREATE DATABASE IF NOT EXISTS gabrielh_abm'
        try:
            self.conexion = pymysql.connect(host='ca8.toservers.com',
                            user='gabrielh_admin',
                            password='gabi42020715',
                            database='gabrielh_abm',
                            cursorclass=pymysql.cursors.DictCursor)

            return self.conexion 
        except Exception as e:
            print(f'Lo siento, hubo un error en la conexion: {e}')

    
    