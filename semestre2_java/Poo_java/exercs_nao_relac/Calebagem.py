class Pessoa:
    def __init__(self, nome, idade, endereco):
        self.__nome = nome
        self.__idade = idade
        self.__endereco = endereco

    def mostrar_endereco(self):
        print(f"Endereço de {self.nome}: {self.__endereco}")

    def alterar_endereco(self, novo_endereco):
        self.endereco = novo_endereco
        print(f"Endereço de {self.nome} alterado para: {self.__endereco}")



p1 = Pessoa("Celéb", 22, "Rua do Senac, 123")
p1.mostrar_endereco()
p1.alterar_endereco("Avenida Varsil, 456")


class Aluno:
    def __init__(self, nome, matricula, curso):
        self.__nome = nome
        self.__matricula = matricula
        self.__curso = curso

    def mostrar_curso(self):
        print(f"O aluno {self.nome} faz {self.curso}")

    def alterar_curso(self, novo_curso):
        self.curso = novo_curso
        print(f"O aluno {self.nome} trocou para {self.curso}")



a1 = Aluno("Kleb", 2023001, "Engenheiro do havai")
a1.mostrar_curso()
a1.alterar_curso("Programação Agil")

