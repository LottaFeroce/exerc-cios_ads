import random
class Aluno:
    def __init__(self,nome,matricula):
        self.nome = nome
        self.matricula = matricula

class Universidade:
    def __init__(self,nome):
        self.nome = nome
        self.alunos = []

    def adicionar_alunos(self, aluno:object):
        self.alunos.append(aluno)

    def listar_alunos(self):
        for item in self.alunos:
            print(f"|Nome: {item.nome}| Matricula: {item.matricula}|")

aluno1 = Aluno("Carliel","31723647")
aluno2 = Aluno("Joker","104938")
aluno3 = Aluno("Nome","Matri<ula")
aluno4 = Aluno("Skrimblo","2222")
fac = Universidade("Senanscquer")
fac.adicionar_alunos(aluno1)
fac.adicionar_alunos(aluno2)
fac.adicionar_alunos(aluno3)

fac.adicionar_alunos(aluno4)
print(len(fac.alunos))

fac.listar_alunos()


class Motor:
    def __init__(self,pot,comb):
        self.chassi = random.randrange(0,10000)
        self.potencia = pot
        self.combustivel = comb

    def get_combustivel(self):
        return self.combustivel

class Carro:
    def __init__(self,potencia_motor,combustivel,modelo):
        self.modelo = modelo
        self.motor = Motor(potencia_motor,combustivel)

carro = Carro("Fusca",121,"Gasolina")
print(f"O {carro.modelo} possui o motor: {carro.motor.potencia} cilindradas")
print(f"O {carro.modelo} deve usar {carro.motor.get_combustivel}")