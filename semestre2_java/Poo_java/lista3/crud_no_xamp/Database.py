import mysql.connector

class Database:
    def __init__(self, banco = "mechnik") -> None:
        self.banco = banco
        self.host= 'localhost'#pode estar conectado a um IP ("localhost" é quando está na máquina)
        self.user = 'root'

    def connect(self):
        self.conn = mysql.connector.connect(host = self.host, database=self.banco,user=self.user,password='')
        if self.conn.is_connected():
            self.cursor = self.conn.cursor()
            db_info = self.conn.get_server_info()
            print("Conectado com sucesso")
        else:
            print("Erro")

    def insert_cliente(self, tupla):
        self.connect()
        try:
            self.cursor.execute('INSERT INTO cliente (nome,cpf,fone,cidade) VALUES (%s,%s,%s,%s)',tupla)
            self.conn.commit()
            return True
        except Exception as err:
            print(err)

        finally:
            self.close_connection()

    def insert_carro(self, tupla):
        self.connect()
        try:
            self.cursor.execute('INSERT INTO carro (marca,modelo) VALUES (%s,%s)',tupla)
            self.conn.commit()
            return True
        except Exception as err:
            print(err)

        finally:
            self.close_connection()

    def close_connection(self):
        if self.conn.is_connected():
            self.cursor.close()
            self.conn.close()
            print("Conexão encerrada")

if __name__ == "__main__":
    db = Database()
    db.connect()


