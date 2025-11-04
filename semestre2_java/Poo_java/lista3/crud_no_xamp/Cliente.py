from Database import Database

class Cliente:
    def __init__(self,nome=None,cpf=None,fone=None,cidade=None):
        self.nome = nome
        self.cpf = cpf
        self.fone = fone
        self.cidade = cidade

    def cadastrar(self): #### NA CLASSE OS MÉTODOS ESCRITO EM PORTUGUES
        self.db = Database()
        tupla = (self.nome,self.cpf,self.fone,self.cidade)
        result = self.db.insert(tupla)        
        return result
    
    def buscar(self):
        self.db = Database()
        cliente = self.db.select()
        return cliente
    
    def buscar_por_id(self,id):
        self.db = Database()
        cliente = self.db.select_by_id(id)
        return cliente

    def atualizar(self,tupla):
        self.db = Database()
        cliente = self.db.update(tupla)
        return cliente
 
    def excluir(self,id):
        self.db = Database()
        result = self.db.delete(id)
        return result
    


cli = Cliente()
clientes = cli.buscar()

for item in clientes:
    print(item)

id_atualizar = int(input("Digite o ID do cliente que deseja atualizar: "))
cli_atualizar = cli.buscar_por_id(id_atualizar)
cli_atualizar = list(cli_atualizar)

cli_atualizar[1] = input("Digite o novo nome")
cli_atualizar[2] = input("Digite o novo cpf")
cli_atualizar[3] = input("Digite o novo fone")
cli_atualizar[4] = input("Digite o novo cidade")

print(cli_atualizar)