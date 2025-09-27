class pessoa:
    def __init__(self,nome,email,senha):
        self.nome = nome
        self.email = email
        self.senha = senha
    def detective(self):
        print(f"Olá {self.nome}")

class butcher(pessoa):
    def __init__(self,nome,email,senha,victims):
        super().__init__(nome,email,senha)
        self.victims = victims
    def surprise(self):
        print(f"Surprise motherfucker {self.nome}")

pes1 = pessoa("d","Jamesmemes@gmail.com","suspicion")
pes1.detective()
pes2 = butcher("ing","patrickbateman@gmail.com","00451",32)
pes2.surprise()
