class funcionario:
    def __init__(self,nome,login,senha):
        self.nome = nome
        self.login = login
        self.senha = senha
    
    def logon(self):
        print(f"{self.nome} Logou com sucesso")

    def alterar_senha(self,nova_senha):
        self.senha = nova_senha
        return True
    
class Gerente(funcionario):
    def __init__(self, nome, login, senha,setor):
        super().__init__(nome, login, senha)
        self.setor = setor
    
    def logon(self):
        confirm = input ("Digite o token: ")
        if confirm:
            print(f"Gerente {self.nome} logado com sucesso, no setor {self.setor}")

luan = Gerente("Luan Victor","Daegon@gmail.com","1211","Vendas")


colab = funcionario("Eliandrick","lalilulilou@gmail.com","00123")
colab = funcionario("Felizardo","ungalossado@yahoo.com","0451")

colab.logon()