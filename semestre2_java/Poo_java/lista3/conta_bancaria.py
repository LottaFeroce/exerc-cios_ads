class Pessoa:
    def __init__(self, nome):
        self.nome = nome

class Conta(Pessoa):
    def __init__(self, nome, numero, agencia, senha):
        super().__init__(nome)
        self.numero = numero
        self.agencia = agencia
        self.saldo = 0.0
        self.extrato = []
        self.__senha = senha

    def autenticar(self, agencia, numero, senha):
        return self.agencia == agencia and self.numero == numero and self.__senha == senha

    def depositar(self, agencia, numero, valor):
        if self.agencia == agencia and self.numero == numero and valor > 0:
            self.saldo += valor
            self.extrato.append(f"Depósito: +R${valor:.2f}")
            return True
        return False

    def sacar(self, agencia, numero, senha, valor):
        if self.autenticar(agencia, numero, senha) and valor > 0 and self.saldo >= valor:
            self.saldo -= valor
            self.extrato.append(f"Saque: -R${valor:.2f}")
            return True
        return False

    def consultar_saldo(self, agencia, numero, senha):
        if self.autenticar(agencia, numero, senha):
            return self.saldo
        return None

    def consultar_extrato(self, agencia, numero, senha):
        if self.autenticar(agencia, numero, senha):
            return self.extrato
        return None


contas = []

def encontrar_conta(agencia, numero):
    for c in contas:
        if c.agencia == agencia and c.numero == numero:
            return c
    return None


while True:
    print("\n=== SISTEMA BANCÁRIO ===")
    print("1. Cadastrar conta")
    print("2. Consultar saldo")
    print("3. Consultar extrato")
    print("4. Sacar dinheiro")
    print("5. Depositar dinheiro")
    print("6. Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nome = input("Nome: ")
        agencia = input("Agência: ")
        numero = input("Número da conta: ")
        senha = input("Senha: ")
        if encontrar_conta(agencia, numero) is None:
            conta = Conta(nome, numero, agencia, senha)
            contas.append(conta)
            print("Conta criada com sucesso")
        else:
            print("Conta já existente.")

    elif opcao == "2":
        agencia = input("Agência: ")
        numero = input("Conta: ")
        senha = input("Senha: ")
        conta = encontrar_conta(agencia, numero)
        if conta:
            saldo = conta.consultar_saldo(agencia, numero, senha)
            if saldo is not None:
                print(f"Saldo: R${saldo:.2f}")
            else:
                print("Autenticação falhou.")
        else:
            print("Conta não encontrada.")

    elif opcao == "3":
        agencia = input("Agência: ")
        numero = input("Conta: ")
        senha = input("Senha: ")
        conta = encontrar_conta(agencia, numero)
        if conta:
            extrato = conta.consultar_extrato(agencia, numero, senha)
            if extrato is not None:
                if extrato:
                    print("Extrato:")
                    for mov in extrato:
                        print(" -", mov)
                else:
                    print("Nenhuma movimentação registrada.")
            else:
                print("Autenticação falhou.")
        else:
            print("Conta não encontrada.")

    elif opcao == "4":
        agencia = input("Agência: ")
        numero = input("Conta: ")
        senha = input("Senha: ")
        valor = float(input("Valor do saque: "))
        conta = encontrar_conta(agencia, numero)
        if conta and conta.sacar(agencia, numero, senha, valor):
            print("Saque realizado com sucesso")
        else:
            print("Falha ao realizar saque.")

    elif opcao == "5":
        agencia = input("Agência: ")
        numero = input("Conta: ")
        valor = float(input("Valor do depósito: "))
        conta = encontrar_conta(agencia, numero)
        if conta and conta.depositar(agencia, numero, valor):
            print("Depósito realizado com sucesso")
        else:
            print("Falha ao realizar depósito.")

    elif opcao == "6":
        print("Encerrando o sistema.")
        break

    else:
        print("Opção inválida.")
