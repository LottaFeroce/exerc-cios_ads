'''class Pessoa:   #1
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
a1.alterar_curso("Programação Agil")'''

'''3-Crie uma classe representando os alunos de um determinado curso. A classe deve
conter os atributos matr´ıcula do aluno, nome, nota da primeira prova, nota da segunda
prova e nota da terceira prova. Crie metodos para acessar o nome e a m ´ edia do aluno. ´
(a) Permita ao usuario entrar com os dados de 5 alunos. ´
(b) Encontre o aluno com maior media geral. ´
(c) Encontre o aluno com menor media geral ´
(d) Para cada aluno diga se ele foi aprovado ou reprovado, considerando o valor 6 para
aprovac¸ao'''
'''class Aluno:
    def __init__(self, matricula, nome, nota1, nota2, nota3):
        self.matricula = matricula
        self.nome = nome
        self.nota1 = nota1
        self.nota2 = nota2
        self.nota3 = nota3

    def media(self):
        return (self.nota1 + self.nota2 + self.nota3) / 3

    def get_nome(self):
        return self.nome

    def aprovado(self):
        return self.media() >= 6

    def __mediana__(self, outro):  
        return self.media() < outro.media()

alunos = []
for aluno_cont in range(5):
    print(f"\n Aluno {aluno_cont+1} ")
    matricula = input("Matrícula: ")
    nome = input("Nome: ")
    nota1 = float(input("Nota 1: "))
    nota2 = float(input("Nota 2: "))
    nota3 = float(input("Nota 3: "))
    alunos.append(Aluno(matricula, nome, nota1, nota2, nota3))

maior = max(alunos)  
menor = min(alunos)

print(f"\nMaior média: {maior.get_nome()} ({maior.media():.2f})")
print(f"Menor média: {menor.get_nome()} ({menor.media():.2f})")'''



"""#5-Crie uma classe para representar um horario (hora, minuto e segundo). Implemente os ´
metodos para fazer as operac¸ ´ oes de incremento (de segundos) no hor ˜ ario e diferenc¸a ´
entre dois horarios."""

class Horario:
    def __init__(self, hora=0, minuto=0, segundo=0):
        self.segundos_totais = (hora * 3600 + minuto * 60 + segundo) % 86400

    def __str__(self):
        horas, resto = divmod(self.segundos_totais, 3600)
        minutos, segundos = divmod(resto, 60)
        return f"{horas:02d}:{minutos:02d}:{segundos:02d}"

    def incrementar(self, segundos):
        self.segundos_totais = (self.segundos_totais + segundos) % 86400

    def diferenca(self, outro):
        diff = abs(self.segundos_totais - outro.segundos_totais)
        return Horario(0, 0, diff)

    @classmethod
    def from_input(cls):
        hora = int(input("Hora: "))
        minuto = int(input("Minuto: "))
        segundo = int(input("Segundo: "))
        return cls(hora, minuto, segundo)



print("Digite o primeiro horário:")
horario_1 = Horario.from_input()

print("\nDigite o segundo horário:")
horario_2 = Horario.from_input()

print(f"\nHorário 1: {horario_1}")
print(f"Horário 2: {horario_2}")

print(f"Diferença: {horario_1.diferenca(horario_2)}")

seg = int(input("\nQuantos segundos deseja adicionar ao primeiro horário? "))
horario_1.incrementar(seg)
print(f"Novo horário 1 após incremento: {horario_1}")
