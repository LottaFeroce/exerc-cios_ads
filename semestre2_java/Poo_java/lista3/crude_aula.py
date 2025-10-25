import mysql.connector
class Database:
    def __init__(self,banco = "perkele") -> None:
        self.banco = banco

    def connect(self):
        self.conn = mysql.connector.connect(host='10.0.2.15',database='perkele',user='root',password='1234')
        if self.conn.is_connected():
            self.cursor = self.conn.cursor()
            db_info = self.conn.get_server_info()
            print("Conectad com sucesso")
        else:
            print("Erro")
db = Database()
db.connect()
