import mysql.connector

class Database:
    def __init__(self, banco="aula_venda") -> None:
        self.banco = banco
        self.host = "localhost"
        self.user = "root"
        self.password = "" 
    
    def connect(self):
        self.conn = mysql.connector.connect(
            host=self.host,
            database=self.banco,
            user=self.user,
            password=self.password
        )

        if self.conn.is_connected():
            self.cursor = self.conn.cursor()
            print("Conectado ao MySQL")
        else:
            print("Erro ao conectar ao MySQL.")