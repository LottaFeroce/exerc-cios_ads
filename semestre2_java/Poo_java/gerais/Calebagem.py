import math
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



a1 = Aluno("Kleb", 2023001, "aeronautica da boeing")
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

    def __lt__(self, outro): 
        return self.media() < outro.media()

alunos = []
for aluno_cont in range(5):
    print(f"\nAluno {aluno_cont + 1}")
    matricula = input("Matrícula: ")
    nome = input("Nome: ")
    nota1 = float(input("Nota 1: "))
    nota2 = float(input("Nota 2: "))
    nota3 = float(input("Nota 3: "))
    alunos.append(Aluno(matricula, nome, nota1, nota2, nota3))

maior = max(alunos)
menor = min(alunos)

print(f"\nMaior média: {maior.get_nome()} ({maior.media():.2f})")
print(f"Menor média: {menor.get_nome()} ({menor.media():.2f})")

print("\nSituação dos alunos:")
for aluno in alunos:
    situacao = "Aprovado" if aluno.aprovado() else "Reprovado"
    print(f"{aluno.get_nome()} - Média: {aluno.media():.2f} - {situacao}")'''


'''#4
class Numero_complexo:
    def __init__(self, real, imaginario):
        self.real = real
        self.imaginario = imaginario

    def __add__(self, outro):
        return Numero_complexo(self.real + outro.real, self.imaginario + outro.imaginario)

    def __sub__(self, outro):
        return Numero_complexo(self.real - outro.real, self.imaginario - outro.imaginario)

    def __mul__(self, outro):
        real = self.real * outro.real - self.imaginario * outro.imaginario
        imaginario = self.real * outro.imaginario + self.imaginario * outro.real
        return Numero_complexo(real, imaginario)

    def __str__(self):
        return f"{self.real} + {self.imaginario}i"

carga_1 = Numero_complexo(2, 3)
carga_2 = Numero_complexo(1, -4)
print("Soma:", carga_1 + carga_2)
print("Subtração:", carga_1 - carga_2)
print("Produto:", carga_1 * carga_2)'''


'''#5-Crie uma classe para representar um horario (hora, minuto e segundo). Implemente os ´
metodos para fazer as operac¸ ´ oes de incremento (de segundos) no hor ˜ ario e diferenc¸a ´
entre dois horarios.

class Horario:
    def __init__(self, hora=0, minuto=0, segundo=0):
        self.tempo = (hora * 3600 + minuto * 60 + segundo) % 86400
    def __str__(self):
        horas_completas, restos_seg = divmod(self.tempo, 3600)
        minutos_rest, segundos_rest = divmod(restos_seg, 60)
        return f"{horas_completas:02d}:{minutos_rest:02d}:{segundos_rest:02d}"
    def inc(self, segundos):
        self.tempo = (self.tempo + segundos) % 86400
    def diff(self, outro):
        return Horario(0, 0, abs(self.tempo - outro.tempo))


horario_1 = Horario(*map(int, input("Hora, minuto e segundo 1 (separados por espaço): ").split()))
horario_2 = Horario(*map(int, input("Hora, minuto e segundo 2 (separados por espaço): ").split()))

print("Diferença:", horario_1.diff(horario_2))

horario_1.inc(int(input("Segundos para adicionar: ")))
print("Novo horário:", horario_1)
'''

'''
#6
class Vetor:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def soma(self, outro):
        return Vetor(self.x + outro.x, self.y + outro.y, self.z + outro.z)

    def subtracao(self, outro):
        return Vetor(self.x - outro.x, self.y - outro.y, self.z - outro.z)

    def produto_escalar(self, outro):
        return self.x * outro.x + self.y * outro.y + self.z * outro.z

    def produto_vetorial(self, outro):
        x = self.y * outro.z - self.z * outro.y
        y = self.z * outro.x - self.x * outro.z
        z = self.x * outro.y - self.y * outro.x
        return Vetor(x, y, z)

    def modulo(self):
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)

    def __str__(self):
        return f"({self.x}, {self.y}, {self.z})"



Vetor_1 = Vetor(1, 2, 3)
Vetor_2 = Vetor(3, -1, 2)

print("Soma:", Vetor_1.soma(Vetor_2))
print("Subtração:", Vetor_1.subtracao(Vetor_2))
print("Produto escalar:", Vetor_1.produto_escalar(Vetor_2))
print("Produto vetorial:", Vetor_1.produto_vetorial(Vetor_2))
print("Módulo de Vetor_1:", Vetor_1.modulo())

#7
class Carro:
    def __init__(self, marca, ano, preco):
        self.marca = marca
        self.ano = ano
        self.preco = preco

    def mostrar_preco(self):
        print(f"Preço do {self.marca}: R${self.preco:.2f}")

    def mostrar_dados(self):
        print(f"Marca: {self.marca} | Ano: {self.ano} | Preço: R${self.preco:.2f}")


carros = []
for i in range(5):
    print(f"\nCarro {i+1}:")
    marca = input("Marca: ")
    ano = int(input("Ano: "))
    preco = float(input("Preço: "))
    carros.append(Carro(marca, ano, preco))

p = float(input("\nDigite um valor limite de preço: "))

print(f"\nCarros com preço menor que R${p:.2f}:")
for carro in carros:
    if carro.preco < p:
        carro.mostrar_dados()
#8
class Conta_corrente:
    def __init__(self, numero, nome, saldo=0):
        self.numero = numero
        self.nome = nome
        self.saldo = saldo

    def alterar_nome(self, novo_nome):
        self.nome = novo_nome

    def deposito(self, valor):
        self.saldo += valor

    def saque(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
        else:
            print("Saldo insuficiente")

    def mostrar_conta(self):
        print(f"Conta: {self.numero} | Nome: {self.nome} | Saldo: R${self.saldo:.2f}")

carro_1 = Conta_corrente(1234, "Celéb", 500)
carro_1.mostrar_conta()
carro_1.deposito(200)
carro_1.saque(100)
carro_1.mostrar_conta()

#9
class Racional:
    def __init__(self, p, q):
        if q == 0:
            raise ValueError("O denominador não pode ser zero.")
        self.p = p
        self.q = q

    def inverter_sinal(self):
        return Racional(-self.p, self.q)

    def somar(self, outro):
        return Racional(self.p * outro.q + outro.p * self.q, self.q * outro.q)

    def subtrair(self, outro):
        return Racional(self.p * outro.q - outro.p * self.q, self.q * outro.q)

    def produto(self, outro):
        return Racional(self.p * outro.p, self.q * outro.q)

    def quociente(self, outro):
        return Racional(self.p * outro.q, self.q * outro.p)

    def __str__(self):
        return f"{self.p}/{self.q}"

Resultado_1 = Racional(1, 2)
Resultado_2 = Racional(3, 4)
print("Soma:", Resultado_1.somar(Resultado_2))
print("Subtração:", Resultado_1.subtrair(Resultado_2))
print("Produto:", Resultado_1.produto(Resultado_2))
print("Quociente:", Resultado_1.quociente(Resultado_2))
print("Inverter sinal de Resultado_1:", Resultado_1.inverter_sinal())

'''