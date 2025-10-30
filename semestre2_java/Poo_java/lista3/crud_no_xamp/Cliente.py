from Database import Database

class Cliente:
    def __init__(self,nome=None,cpf=None,fone=None,cidade=None):
        self.nome = nome
        self.cpf = cpf
        self.fone = fone
        self.cidade = cidade
        self.db = Database()


    def cadastrar(self):
        self.db = Database()
        tupla = (self.nome,self.cpf,self.fone,self.cidade)
        resultado = self.db.insert(tupla)
        return resultado

    def buscar(self):
        self.db = Database()
        dados = self.db.select()
        return dados()

    

cliente1 = Cliente()
cliente1.db.connect()