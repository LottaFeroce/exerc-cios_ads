class Pessoa:
    def __init__(self, nome, idade, endereco):
        self.nome = nome
        self.idade = idade
        self.endereco = endereco

    def mostrar_nome(self):
        return self.nome

    def alterar_idade(self, nova_idade):
        if nova_idade >= 0:
            self.idade = nova_idade
            return True
        return False

    def imprimir_endereco(self):
        return self.endereco
    
jo = Pessoa("Jose", 49, "Sicilia")
jo.alterar_idade(50)
print(jo.mostrar_nome())                
print(jo.idade)                
print(jo.imprimir_endereco())  


class Livro:
    def __init__(self, nome, autor, editora, paginas):
        self.nome = nome
        self.autor = autor
        self.editora = editora
        self.paginas = paginas

    def alterar_editora(self, nova_editora):
        self.editora = nova_editora

    def listar_qtde_paginas(self):
        return self.paginas
lvro = Livro("Moby dyck","Ahab","Le'Fishmaels",6900)
print(lvro.listar_qtde_paginas())


class Aluno:
    def __init__(self, nome, ra, notas):
        self.nome = nome
        self.ra = ra
        self.notas = notas

    def calcular_media(self):
        if len(self.notas) == 0:
            return 0
        return sum(self.notas) / len(self.notas)

    def mostrar_situacao(self):
        media = self.calcular_media()
        if media >= 7:
            return f"APROVADO (média = {media:.2f})"
        elif media >= 5:
            return f"EXAME (média = {media:.2f})"
        else:
            return f"REPROVADO (média = {media:.2f})"

aluno1 = Aluno("Carlos", "RA12345", [8.0, 7.0, 9.0, 6.0])

print(aluno1.nome)
print(aluno1.calcular_media())
print(aluno1.mostrar_situacao())


class ContaCorrente:
    def __init__(self, nome, cpf, numero, saldo=0):
        self.nome = nome
        self.cpf = cpf
        self.numero = numero
        self.saldo = saldo

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            return True
        return False

    def sacar(self, valor):
        if valor > 0 and valor <= self.saldo and self.saldo > 0:
            self.saldo -= valor
            return True
        return False

    def imprimir_saldo(self):
        return self.saldo

conta1 = ContaCorrente("Beatriz", "123.456.789-00", "0001", 500)

conta1.depositar(250)
print(conta1.imprimir_saldo())
conta1.sacar(100)
print(conta1.imprimir_saldo())


class Funcionario:
    def __init__(self, nome, sobrenome, horas_trabalhadas, valor_hora):
        self.nome = nome
        self.sobrenome = sobrenome
        self.horas_trabalhadas = horas_trabalhadas
        self.valor_hora = valor_hora

    def nome_completo(self):
        return f"{self.nome} {self.sobrenome}"

    def calcular_salario(self):
        return self.horas_trabalhadas * self.valor_hora

    def incrementar_horas(self, horas):
        if horas > 0:
            self.horas_trabalhadas += horas
            return True
        return False

func1 = Funcionario("João", "Silva", 160, 25)
print(func1.nome_completo())
print(func1.calcular_salario())
func1.incrementar_horas(8)
print(func1.horas_trabalhadas)

import math 
class Circulo:
    def __init__(self, raio):
        self.raio = raio

    def imprimir_raio(self):
        return self.raio

    def calcular_area(self):
        return math.pi * (self.raio ** 2)

    def calcular_circunferencia(self):
        return 2 * math.pi * self.raio

circulo1 = Circulo(3)
print("Raio:", circulo1.imprimir_raio())
print("Área:", circulo1.calcular_area())
print("Circunferência:", circulo1.calcular_circunferencia())

from datetime import date


class Agenda:
    def __init__(self, dia, mes, ano, anotacao=""):
        self.dia = dia
        self.mes = mes
        self.ano = ano
        self.anotacao = anotacao

    def validar_data(self):
        try:
            date(self.ano, self.mes, self.dia)
            return True
        except ValueError:
            return False

    def anotar_tarefa(self, texto):
        self.anotacao = texto

    def mostrar_anotacao(self):
        return self.anotacao
    
agenda1 = Agenda(28, 2, 2024)

print("Data válida?", agenda1.validar_data())
agenda1.anotar_tarefa("Estudar POO com a BB-chan 💜")
print("Anotação:", agenda1.mostrar_anotacao())


class Triangulo:
    def __init__(self, ladoA, ladoB, ladoC):
        self.ladoA = ladoA
        self.ladoB = ladoB
        self.ladoC = ladoC

    def calcular_perimetro(self):
        return self.ladoA + self.ladoB + self.ladoC

    def get_maior_lado(self):
        return max(self.ladoA, self.ladoB, self.ladoC)

    def calcular_area(self):
        p = self.calcular_perimetro() / 2
        s = p * (p - self.ladoA) * (p - self.ladoB) * (p - self.ladoC)
        if s <= 0:
            return 0
        return math.sqrt(s)
tri1 = Triangulo(3, 4, 5)

print("Perímetro:", tri1.calcular_perimetro())
print("Maior lado:", tri1.get_maior_lado())
print("Área:", tri1.calcular_area())


class AlunoAcademia:
    def __init__(self, nome, idade, peso, altura, mensalidade=120):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura
        self.mensalidade = mensalidade

    def calcular_imc(self):
        if self.altura > 0:
            return self.peso / (self.altura ** 2)
        return 0

    def obter_valor_mensalidade(self):
        if self.idade < 18:
            return self.mensalidade * 0.5
        return self.mensalidade

a1 = AlunoAcademia("Lucas", 17, 65, 1.75)

print("IMC:", a1.calcular_imc())
print("Mensalidade:", a1.obter_valor_mensalidade())


class Carro:
    def __init__(self, marca, modelo, cor, ano, valor, nivel=0, consumo=10):
        self.marca = marca
        self.modelo = modelo
        self.cor = cor
        self.ano = ano
        self.valor = valor
        self.nivel = nivel 
        self.consumo = consumo 

    def abastecer(self, litros):
        if litros > 0:
            self.nivel += litros

    def andar(self, distancia_km):
        if distancia_km > 0 and self.consumo > 0:
            litros_necessarios = distancia_km / self.consumo
            if litros_necessarios <= self.nivel:
                self.nivel -= litros_necessarios
                return distancia_km
            else:
                distancia_possivel = self.nivel * self.consumo
                self.nivel = 0
                return distancia_possivel
        return 0

    def verificar_nivel(self):
        return self.nivel

    def calcular_imposto(self):
        return self.valor * 0.035 
carro1 = Carro("Fiat", "Uno", "Vermelho", 2010, 25000, nivel=10, consumo=12)

print("Nível inicial:", carro1.verificar_nivel())
print("Distância percorrida:", carro1.andar(50))
print("Nível após andar:", carro1.verificar_nivel())

carro1.abastecer(20)
print("Novo nível:", carro1.verificar_nivel())
print("IPVA:", carro1.calcular_imposto())


class NotaFiscal:
    def __init__(self, numero, tipo, serie, cnpj, razao_social, data,
                 icms, frete, ipi, valor_produto):
        self.numero = numero
        self.tipo = tipo
        self.serie = serie
        self.cnpj = cnpj
        self.razao_social = razao_social
        self.data = data
        self.icms = icms
        self.frete = frete
        self.ipi = ipi
        self.valor_produto = valor_produto
        self.valor_total = 0

    def obter_numero(self):
        return self.numero

    def obter_data_emissao(self):
        return self.data

    def alterar_razao_social(self, nova_razao):
        self.razao_social = nova_razao

    def calcular_valor_total(self):
        icms_valor = self.icms * self.valor_produto if self.icms <= 1 else self.icms
        ipi_valor = self.ipi * self.valor_produto if self.ipi <= 1 else self.ipi
        self.valor_total = self.valor_produto + self.frete + icms_valor + ipi_valor
        return self.valor_total
