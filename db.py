import mysql.connector
import sqlite3

class Connectdb:
    def __init__(self, dbname):
        self.user = 'admin'
        self.password = 'LLETWGFLCOJZCUQC'
        self.host = 'sl-eu-gb-p03.dblayer.com'
        self.port = 17795
        self.conn = mysql.connector.connect(
            user=self.user,
            password=self.password,
            host=self.host,
            port=self.port,
            database=dbname
            )
        self.cursor = self.conn.cursor()
    
    def select(self, stmt, data):
        self.cursor.execute(stmt, data)
        return self.cursor.fetchall()

    def change(self, stmt, data):
        self.cursor.execute(stmt, data)
        self.conn.commit()
        return True, "Query OK, "+str(self.cursor.rowcount)+" rows affected!"

class Connectlite:
    def __init__(self, dbname):
        self.conn = sqlite3.connect(dbname+'.db')
        self.cursor = self.conn.cursor()

    def select(self, stmt, data):
        self.cursor.execute(stmt, data)
        return self.cursor.fetchall()

    def change(self, stmt, data):
        self.cursor.execute(stmt, data)
        self.conn.commit()
        return True, "Query OK, "+str(self.cursor.rowcount)+" rows affected!"