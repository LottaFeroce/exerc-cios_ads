class Pessoa:   #1
    def __init__(self, nome, idade, endereco):
        self.nome = nome
        self.idade = idade
        self.endereco = endereco

    def mostrar_endereco(self):
        print(f"Endereço de {self.nome}: {self.endereco}")

    def alterar_endereco(self, novo_endereco):
        self.endereco = novo_endereco
        print(f"Endereço de {self.nome} alterado para: {self.endereco}")



p1 = Pessoa("Celéb", 22, "Rua do Senac, 123")
p1.mostrar_endereco()
p1.alterar_endereco("Avenida Varsil, 456")


class Aluno:    #2
    def __init__(self, nome, matricula, curso):
        self.nome = nome
        self.matricula = matricula
        self.curso = curso

    def mostrar_curso(self):
        print(f"O aluno {self.nome} faz {self.curso}")

    def alterar_curso(self, novo_curso):
        self.curso = novo_curso
        print(f"O aluno {self.nome} trocou para {self.curso}")



a1 = Aluno("Kleb", 2023001, "Engenheiro do havai")
a1.mostrar_curso()
a1.alterar_curso("Programação Agil")

'''3-Crie uma classe representando os alunos de um determinado curso. A classe deve
conter os atributos matr´ıcula do aluno, nome, nota da primeira prova, nota da segunda
prova e nota da terceira prova. Crie metodos para acessar o nome e a m ´ edia do aluno. ´
(a) Permita ao usuario entrar com os dados de 5 alunos. ´
(b) Encontre o aluno com maior media geral. ´
(c) Encontre o aluno com menor media geral ´
(d) Para cada aluno diga se ele foi aprovado ou reprovado, considerando o valor 6 para
aprovac¸ao'''
class Aluno_representado:
    def __init__(self, matricula, nome, nota_p1, nota_p2, nota_p3):
        self.matricula = matricula
        self.nome = nome
        self.nota_p1 = nota_p1
        self.nota_p2 = nota_p2
        self.nota_p3 = nota_p3

    def inserir_dados(self, nova_matricula, novo_nome, nova_nota_p1, nova_nota_p2, nova_nota_p3):
        self.matricula = nova_matricula
        self.nome = novo_nome
        self.nota_p1 = nova_nota_p1
        self.nota_p2 = nova_nota_p2
        self.nota_p3 = nova_nota_p3

    def media(self):
        """Calcula a média das 3 provas."""
        return (self.nota_p1 + self.nota_p2 + self.nota_p3) / 3

    def situacao(self):
        """Retorna a situação do aluno (aprovado ou reprovado)."""
        return "Aprovado" if self.media() >= 6 else "Reprovado"


# Função para criar e armazenar os dados de 5 alunos
def cadastrar_alunos():
    alunos = []
    for i in range(5):
        matricula = input(f"Digite a matrícula do aluno {i + 1}: ")
        nome = input(f"Digite o nome do aluno {i + 1}: ")
        nota_p1 = float(input(f"Digite a nota da primeira prova do aluno {i + 1}: "))
        nota_p2 = float(input(f"Digite a nota da segunda prova do aluno {i + 1}: "))
        nota_p3 = float(input(f"Digite a nota da terceira prova do aluno {i + 1}: "))
        
        aluno = Aluno_representado(matricula, nome, nota_p1, nota_p2, nota_p3)
        alunos.append(aluno)
    return alunos

def aluno_maior_media(alunos):
    return max(alunos, key=lambda aluno: aluno.media())

def aluno_menor_media(alunos):
    return min(alunos, key=lambda aluno: aluno.media())

def exibir_situacao_alunos(alunos):
    for aluno in alunos:
        print(f"{aluno.nome}: {aluno.situacao()} (Média: {aluno.media():.2f})")

def main():
    alunos = cadastrar_alunos()
    
    maior_media = aluno_maior_media(alunos)
    menor_media = aluno_menor_media(alunos)
    
    print(f"\nAluno com maior média: {maior_media.nome} - Média: {maior_media.media():.2f}")
    print(f"Aluno com menor média: {menor_media.nome} - Média: {menor_media.media():.2f}")
    
    exibir_situacao_alunos(alunos)

if __name__ == "__main__":
    main()
