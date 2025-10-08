class Filme:
    def __init__(self, nome, duracao):
        self.nome = nome
        self.duracao = duracao

    def play(self):
        print(f"\nDando play no filme: {self.nome}")


class Acao(Filme):
    def __init__(self, nome, duracao, explosoes):
        super().__init__(nome, duracao)
        self.explosoes = explosoes

    def explodir(self):
        print(f"{self.nome} teve {self.explosoes} explosões")


class Drama(Filme):
    def __init__(self, nome, duracao, lagrimas):
        super().__init__(nome, duracao)
        self.lagrimas = lagrimas

    def chorar(self):
        print(f"Prepare os lenços... {self.nome} causou {self.lagrimas} lágrimas")


class Suspense(Filme):
    def __init__(self, nome, duracao, nivel_tensao):
        super().__init__(nome, duracao)
        self.nivel_tensao = nivel_tensao

    def assustar(self):
        print(f"{self.nome} está com nível de tensão {self.nivel_tensao}/10\n")

filme1 = Acao("Caesar King: Rainha de Calydon", 130, 15)
filme2 = Drama("Marley e Eu", 120, 20)
filme3 = Suspense("O Chamado", 110, 11)

filme1.play()
filme1.explodir()

filme2.play()
filme2.chorar()

filme3.play()
filme3.assustar()

class Pessoa:
    def __init__(self, matricula, nome, idade):
        self.matricula = matricula
        self.nome = nome
        self.idade = idade


class Aluno(Pessoa):
    def __init__(self, matricula, nome, idade, notas):
        super().__init__(matricula, nome, idade)
        self.notas = notas
        self.media = 0

    def calcular_media(self):
        self.media = sum(self.notas) / len(self.notas)
        return self.media

    def estudar(self):
        print(f"{self.nome} está estudando para melhorar suas notas")


class Professor(Pessoa):
    def __init__(self, matricula, nome, idade, formacao, disciplina, carga_horaria, salario):
        super().__init__(matricula, nome, idade)
        self.formacao = formacao
        self.disciplina = disciplina
        self.carga_horaria = carga_horaria
        self.salario = salario

    def lecionar(self):
        print(f"Professora {self.nome} está lecionando {self.disciplina}")

aluno1 = Aluno("A001", "Kuroko", 18, [8, 7, 9, 10])
prof1 = Professor("P001", "Yariko", 35, "Engenharia", "POO\n", 40, 5000)

print(aluno1.nome, "tem média:", aluno1.calcular_media(),"")
aluno1.estudar()

prof1.lecionar()

class PessoaBase:
    def __init__(self, nome, telefone, email, endereco):
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.endereco = endereco

    def negociar(self):
        print(f"{self.nome} está negociando um contrato")


class PessoaFisica(PessoaBase):
    def __init__(self, nome, telefone, email, endereco, cpf):
        super().__init__(nome, telefone, email, endereco)
        self.cpf = cpf

    def assinar_contrato(self):
        print(f"Pessoa Física {self.nome} assinou o contrato")


class PessoaJuridica(PessoaBase):
    def __init__(self, nome, telefone, email, endereco, cnpj):
        super().__init__(nome, telefone, email, endereco)
        self.cnpj = cnpj

    def emitir_nota(self):
        print(f"Empresa {self.nome} emitiu uma nota fiscal\n")

pf = PessoaFisica("Yuruko", "991231-4331", "yuru@email.com", "Rua oppaidesu, 10", "123.456.789-00")
pj = PessoaJuridica("TechCorp", "94002-8922", "contato@techcorp.com", "Av. Central, 1000", "12.345.678/0001-99")

pf.negociar()
pf.assinar_contrato()

pj.negociar()
pj.emitir_nota()

class Ingresso:
    def __init__(self, preco, setor):
        self.preco = preco
        self.setor = setor

    def alterar_preco(self, novo_preco):
        self.preco = novo_preco

    def mostrar_setor(self):
        print(f"Setor: {self.setor}")


class IngressoVIP(Ingresso):
    def __init__(self, preco, setor, camarote, open_bar, open_food, estacionamento):
        super().__init__(preco, setor)
        self.camarote = camarote
        self.open_bar = open_bar
        self.open_food = open_food
        self.estacionamento = estacionamento

    def pegar_bebida(self):
        if self.open_bar:
            print("Bebida liberada")
        else:
            print("Esse ingresso não dá direito a open bar")

    def acessar_camarote(self):
        if self.camarote:
            print("Acesso ao camarote liberado\n")
        else:
            print("Acesso ao camarote negado")

ingresso1 = Ingresso(150, "Pista")
vip1 = IngressoVIP(500, "Camarote", True, True, True, True)

ingresso1.mostrar_setor()
vip1.mostrar_setor()
vip1.pegar_bebida()
vip1.acessar_camarote()

class Passagem:
    def __init__(self, preco, assento):
        self.preco = preco
        self.assento = assento

    def alterar_preco(self, novo_preco):
        self.preco = novo_preco

    def escolher_assento(self, novo_assento):
        self.assento = novo_assento


class PassagemAviao(Passagem):
    def __init__(self, preco, assento, portao_embarque, checkin):
        super().__init__(preco, assento)
        self.portao_embarque = portao_embarque
        self.checkin = checkin

    def decolar(self):
        print("O avião está decolando\n")


class PassagemBus(Passagem):
    def __init__(self, preco, assento, placa, leito):
        super().__init__(preco, assento)
        self.placa = placa
        self.leito = leito

    def abastecer(self):
        print(f"O ônibus de placa {self.placa} está sendo abastecido")

bus = PassagemBus(120, "Poltrona 10", "ABC-1234", True)
aviao = PassagemAviao(800, "12A", "Portão 5", True)

bus.abastecer()
aviao.decolar()

class FuncionarioBase:
    def __init__(self, nome, matricula, salario):
        self.nome = nome
        self.matricula = matricula
        self.salario = salario
        self.pontos = []

    def bater_ponto(self):
        self.pontos.append(True)
        print(f"{self.nome} bateu ponto hoje")


class Vendedor(FuncionarioBase):
    def __init__(self, nome, matricula, salario, comissao):
        super().__init__(nome, matricula, salario)
        self.comissao = comissao

    def bater_meta(self):
        print(f"{self.nome} bateu a meta e recebeu comissão de R${self.comissao:.2f}")


class Gerente(FuncionarioBase):
    def __init__(self, nome, matricula, salario, senha):
        super().__init__(nome, matricula, salario)
        self.senha = senha

    def autenticar(self):
        print(f"Gerente {self.nome} autenticado com sucesso\n")

vendedor1 = Vendedor("Yariko", "V123", 2000, 500)
gerente1 = Gerente("Marina", "G001", 8000, "1234")

vendedor1.bater_ponto()
vendedor1.bater_meta()

gerente1.bater_ponto()
gerente1.autenticar()

class Brinquedo:
    def __init__(self, nome, cor, tamanho, preco):
        self.nome = nome
        self.cor = cor
        self.tamanho = tamanho
        self.preco = preco

    def brincar(self):
        print(f"Brincando com {self.nome}")


class BuzzLightyear(Brinquedo):
    def brincar(self):
        print(f"Ao infinito e além({self.nome})")


class Woody(Brinquedo):
    def brincar(self):
        print(f"Há uma bota na loja da cobra({self.nome})")


class Rex(Brinquedo):
    def brincar(self):
        print(f"{self.nome} O homem galinha caiu na grelha do KFC")


class Jessie(Brinquedo):
    def brincar(self):
        print(f"{self.nome} está fazendo Skotnitsa")


class Slinky(Brinquedo):
    def brincar(self):
        print(f"{self.nome} está se esticando e voltando\n")

brinquedos = [
    BuzzLightyear("Buzz Lightyear", "Branco", "Médio", 120),
    Woody("Woody", "Marrom", "Médio", 100),
    Rex("Rex", "Verde", "Grande", 80),
    Jessie("Jessie", "Vermelha", "Pequena", 90),
    Slinky("Slinky", "Cinza", "Pequeno", 70)
]
for b in brinquedos:
    b.brincar()


class Imovel:
    def __init__(self, inscricao_municipal, valor_aluguel, iptu):
        self.inscricao_municipal = inscricao_municipal
        self.valor_aluguel = valor_aluguel
        self.iptu = iptu

    def obter_parcela_iptu(self):
        return self.iptu / 12

    def set_valor_aluguel(self, novo_valor):
        self.valor_aluguel = novo_valor


class Casa(Imovel):
    def __init__(self, inscricao_municipal, valor_aluguel, iptu, piscina, churrasqueira):
        super().__init__(inscricao_municipal, valor_aluguel, iptu)
        self.piscina = piscina
        self.churrasqueira = churrasqueira


class Apartamento(Imovel):
    def __init__(self, inscricao_municipal, valor_aluguel, iptu, elevador, andar):
        super().__init__(inscricao_municipal, valor_aluguel, iptu)
        self.elevador = elevador
        self.andar = andar


class Terreno(Imovel):
    def __init__(self, inscricao_municipal, valor_aluguel, iptu, area_m2):
        super().__init__(inscricao_municipal, valor_aluguel, iptu)
        self.area_m2 = area_m2


class Chacara(Imovel):
    def __init__(self, inscricao_municipal, valor_aluguel, iptu, area_de_lazer):
        super().__init__(inscricao_municipal, valor_aluguel, iptu)
        self.area_de_lazer = area_de_lazer

casa1 = Casa("12345", 2500, 1200, True, True)
apt1 = Apartamento("98765", 1800, 800, True, 10)
chacara1 = Chacara("55555", 4000, 2500, True)

print("Casa - IPTU mensal:", casa1.obter_parcela_iptu())
apt1.set_valor_aluguel(1900)
print("Apartamento - novo valor aluguel:", apt1.valor_aluguel)


class Compra:
    def __init__(self, numero, produto, valor):
        self.numero = numero
        self.produto = produto
        self.valor = valor
        self.valor_total = 0

    def calcular_valor_total(self):
        imposto = self.valor * 0.17
        frete = self.valor * 0.05
        self.valor_total = self.valor + imposto + frete
        return self.valor_total


class CompraAvista(Compra):
    def __init__(self, numero, produto, valor, desconto):
        super().__init__(numero, produto, valor)
        self.desconto = desconto

    def calcular_valor_total(self):
        total = super().calcular_valor_total()
        self.valor_total = total - self.desconto
        return self.valor_total


class CompraParcelada(Compra):
    def __init__(self, numero, produto, valor, parcelas):
        super().__init__(numero, produto, valor)
        self.parcelas = parcelas

    def simular_numero_de_parcelas(self):
        valor_por_parcela = self.calcular_valor_total() / self.parcelas
        print(f"{self.parcelas} parcelas de R${valor_por_parcela:.2f}\n")

compra1 = Compra("001", "Notebook", 3000)
print("Valor total compra comum:", compra1.calcular_valor_total())

compra2 = CompraAvista("002", "Celular", 2000, 200)
print("Valor total compra à vista (com desconto):", compra2.calcular_valor_total())

compra3 = CompraParcelada("003", "TV", 2500, 5)
compra3.simular_numero_de_parcelas()

class Transporte:
    def __init__(self, tipo, capacidade):
        self.tipo = tipo
        self.capacidade = capacidade

    def mover(self):
        print(f"O transporte {self.tipo} está em movimento")


class Terrestre(Transporte):
    def __init__(self, tipo, capacidade, rodas):
        super().__init__(tipo, capacidade)
        self.rodas = rodas


class Automovel(Terrestre):
    def __init__(self, tipo, capacidade, rodas, modelo):
        super().__init__(tipo, capacidade, rodas)
        self.modelo = modelo


class Aereo(Transporte):
    def __init__(self, tipo, capacidade, asas):
        super().__init__(tipo, capacidade)
        self.asas = asas


class AviaoMonomotor(Aereo):
    def __init__(self, tipo, capacidade, asas, autonomia):
        super().__init__(tipo, capacidade, asas)
        self.autonomia = autonomia


class AviaoComercial(Aereo):
    def __init__(self, tipo, capacidade, asas, companhia):
        super().__init__(tipo, capacidade, asas)
        self.companhia = companhia


class Aquatico(Transporte):
    def __init__(self, tipo, capacidade, motores):
        super().__init__(tipo, capacidade)
        self.motores = motores


class Lancha(Aquatico):
    def __init__(self, tipo, capacidade, motores, velocidade_max):
        super().__init__(tipo, capacidade, motores)
        self.velocidade_max = velocidade_max


class Navio(Aquatico):
    def __init__(self, tipo, capacidade, motores, tripulacao):
        super().__init__(tipo, capacidade, motores)
        self.tripulacao = tripulacao

carro = Automovel("Carro", 5, 4, "Sedan")
aviao_com = AviaoComercial("Avião", 180, 2, "LATAM")
lancha = Lancha("Lancha", 8, 2, 80)

carro.mover()
aviao_com.mover()
lancha.mover()