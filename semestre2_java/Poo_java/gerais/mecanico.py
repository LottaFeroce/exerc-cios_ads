class mecanico:
    def __init__(self,nome,matricula,nivel,salario):
        self.nome = nome
        self.matricula = matricula
        self.nivel = nivel
        self.salario = 0

    def passar_orcamento(self):
        print("Seu carro ficou tanto...")

    def realizar_diagnostico(self):
        print(f"{self.nome} Diagnóstico do veiculo")

    def get_salario(self):
        pass


mec1 = mecanico("Carlos","1234","N1")
mec1.passar_orcamento()
mec1.realizar_diagnostico()
sal = mec1.get_salario()
print("Salario: ",sal)


mec2 = mecanico("Jhonan","41335","N2")
mec2.set_salario(9000)
x = mec2.get_salario()
print(f"Salario do {mec2.nome} é {mec2.salario}")

mec1.set_salario(5000)

sal = mec1.get_salario()
print(sal)
