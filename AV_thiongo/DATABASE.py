import mysql.connector

class Database:
    def __init__(self, banco="loja_online") -> None:
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

    def insert(self, query, values):
        self.connect()
        try:
            self.cursor.execute(query, values)
            self.conn.commit()
            return True
        except Exception as e:
            print("Erro INSERT:", e)
        finally:
            self.close_connection()

    def select(self, query):
        self.connect()
        try:
            self.cursor.execute(query)
            return self.cursor.fetchall()
        except Exception as e:
            print("Erro SELECT:", e)
        finally:
            self.close_connection()

    def select_by_id(self, query, id):
        self.connect()
        try:
            self.cursor.execute(query, (id,))
            return self.cursor.fetchone()
        except Exception as e:
            print("Erro SELECT ID:", e)
        finally:
            self.close_connection()

    def update(self, query, values):
        self.connect()
        try:
            self.cursor.execute(query, values)
            self.conn.commit()
            return True
        except Exception as e:
            print("Erro UPDATE:", e)
        finally:
            self.close_connection()

    def delete(self, query, id):
        self.connect()
        try:
            self.cursor.execute(query, (id,))
            self.conn.commit()
            return True
        except Exception as e:
            print("Erro DELETE:", e)
        finally:
            self.close_connection()

    def close_connection(self):
        if self.conn.is_connected():
            self.cursor.close()
            self.conn.close()
            print("Conexão encerrada")
