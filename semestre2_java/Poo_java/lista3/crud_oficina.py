import mysql.connector
def conectar():
    return mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='oficina'
    )



def criar_funcionario(nome, cargo, salario):
    con = conectar()
    cursor = con.cursor()
    cursor.execute(
        "INSERT INTO funcionarios (nome, cargo, salario) VALUES (%s, %s, %s)",
        (nome, cargo, salario)
    )
    con.commit()
    con.close()
    print("Funcionário adicionado com sucesso")


def listar_funcionarios():
    con = conectar()
    cursor = con.cursor()
    cursor.execute("SELECT * FROM funcionarios")
    funcionarios = cursor.fetchall()
    if not funcionarios:
        print("Nenhum funcionário cadastrado.")
    else:
        for (id_func, nome, cargo, salario) in funcionarios:
            print(f"{id_func} - {nome} | {cargo} | R${salario}")
    con.close()


def atualizar_funcionario(id_funcionario, novo_nome, novo_cargo, novo_salario):
    con = conectar()
    cursor = con.cursor()
    cursor.execute(
        "UPDATE funcionarios SET nome=%s, cargo=%s, salario=%s WHERE id_funcionario=%s",
        (novo_nome, novo_cargo, novo_salario, id_funcionario)
    )
    con.commit()
    con.close()
    print("Funcionário atualizado")


def deletar_funcionario(id_funcionario):
    con = conectar()
    cursor = con.cursor()
    cursor.execute(
        "DELETE FROM funcionarios WHERE id_funcionario=%s",
        (id_funcionario,)
    )
    con.commit()
    con.close()
    print("Funcionário removido")



def criar_proprietario(nome, telefone):
    con = conectar()
    cursor = con.cursor()
    cursor.execute(
        "INSERT INTO proprietarios (nome, telefone) VALUES (%s, %s)",
        (nome, telefone)
    )
    con.commit()
    con.close()
    print("Proprietário cadastrado com sucesso")


def listar_proprietarios():
    con = conectar()
    cursor = con.cursor()
    cursor.execute("SELECT * FROM proprietarios")
    proprietarios = cursor.fetchall()
    if not proprietarios:
        print("Nenhum proprietário cadastrado.")
    else:
        for (id_prop, nome, telefone) in proprietarios:
            print(f"{id_prop} - {nome} | {telefone}")
    con.close()


def atualizar_proprietario(id_proprietario, novo_nome, novo_telefone):
    con = conectar()
    cursor = con.cursor()
    cursor.execute(
        "UPDATE proprietarios SET nome=%s, telefone=%s WHERE id_proprietario=%s",
        (novo_nome, novo_telefone, id_proprietario)
    )
    con.commit()
    con.close()
    print("Proprietário atualizado com sucesso")


def deletar_proprietario(id_proprietario):
    con = conectar()
    cursor = con.cursor()
    cursor.execute(
        "DELETE FROM proprietarios WHERE id_proprietario=%s",
        (id_proprietario,)
    )
    con.commit()
    con.close()
    print("Proprietário removido com sucesso")



def criar_carro(modelo, placa, id_proprietario):
    con = conectar()
    cursor = con.cursor()
    cursor.execute(
        "INSERT INTO carros (modelo, placa, id_proprietario) VALUES (%s, %s, %s)",
        (modelo, placa, id_proprietario)
    )
    con.commit()
    con.close()
    print("Carro cadastrado com sucesso")


def listar_carros():
    con = conectar()
    cursor = con.cursor()
    consulta = """
    SELECT c.id_carro, c.modelo, c.placa, p.nome
    FROM carros c
    JOIN proprietarios p ON c.id_proprietario = p.id_proprietario
    """
    cursor.execute(consulta)
    carros = cursor.fetchall()
    if not carros:
        print("Nenhum carro cadastrado.")
    else:
        for (id_carro, modelo, placa, proprietario) in carros:
            print(f"{id_carro} - {modelo} ({placa}) | Dono: {proprietario}")
    con.close()


def atualizar_carro(id_carro, novo_modelo, nova_placa, novo_id_proprietario):
    con = conectar()
    cursor = con.cursor()
    cursor.execute(
        "UPDATE carros SET modelo=%s, placa=%s, id_proprietario=%s WHERE id_carro=%s",
        (novo_modelo, nova_placa, novo_id_proprietario, id_carro)
    )
    con.commit()
    con.close()
    print("Carro atualizado com sucesso")


def deletar_carro(id_carro):
    con = conectar()
    cursor = con.cursor()
    cursor.execute(
        "DELETE FROM carros WHERE id_carro=%s",
        (id_carro,)
    )
    con.commit()
    con.close()
    print("Carro removido com sucesso")




def menu_funcionarios():
    while True:
        print("\n--- Menu Funcionários ---")
        print("1 - Adicionar")
        print("2 - Listar")
        print("3 - Atualizar")
        print("4 - Remover")
        print("0 - Voltar")
        opc = input("\nEscolha uma opção: ")

        if opc == '1':
            nome = input("Nome: ")
            cargo = input("Cargo: ")
            salario = float(input("Salário: "))
            criar_funcionario(nome, cargo, salario)
        elif opc == '2':
            listar_funcionarios()
        elif opc == '3':
            idf = int(input("ID do funcionário: "))
            nome = input("Novo nome: ")
            cargo = input("Novo cargo: ")
            salario = float(input("Novo salário: "))
            atualizar_funcionario(idf, nome, cargo, salario)
        elif opc == '4':
            idf = int(input("ID do funcionário: "))
            deletar_funcionario(idf)
        elif opc == '0':
            break
        else:
            print("Opção inválida")


def menu_proprietarios():
    while True:
        print("\n--- Menu Proprietários ---")
        print("1 - Adicionar")
        print("2 - Listar")
        print("3 - Atualizar")
        print("4 - Remover")
        print("0 - Voltar")
        opc = input("\nEscolha uma opção: ")

        if opc == '1':
            nome = input("Nome: ")
            telefone = input("Telefone: ")
            criar_proprietario(nome, telefone)
        elif opc == '2':
            listar_proprietarios()
        elif opc == '3':
            idp = int(input("ID do proprietário: "))
            nome = input("Novo nome: ")
            telefone = input("Novo telefone: ")
            atualizar_proprietario(idp, nome, telefone)
        elif opc == '4':
            idp = int(input("ID do proprietário: "))
            deletar_proprietario(idp)
        elif opc == '0':
            break
        else:
            print("Opção inválida")


def menu_carros():
    while True:
        print("\n--- Menu Carros ---")
        print("1 - Adicionar")
        print("2 - Listar")
        print("3 - Atualizar")
        print("4 - Remover")
        print("0 - Voltar")
        opc = input("\nEscolha uma opção: ")

        if opc == '1':
            modelo = input("Modelo: ")
            placa = input("Placa: ")
            id_prop = int(input("ID do proprietário: "))
            criar_carro(modelo, placa, id_prop)
        elif opc == '2':
            listar_carros()
        elif opc == '3':
            idc = int(input("ID do carro: "))
            modelo = input("Novo modelo: ")
            placa = input("Nova placa: ")
            idp = int(input("Novo ID do proprietário: "))
            atualizar_carro(idc, modelo, placa, idp)
        elif opc == '4':
            idc = int(input("ID do carro: "))
            deletar_carro(idc)
        elif opc == '0':
            break
        else:
            print("Opção inválida")



while True:
    print("\n=== Oficina Beebs ===")
    print("1 - Funcionários")
    print("2 - Proprietários")
    print("3 - Carros")
    print("0 - Sair")

    opcao = input("\nEscolha uma opção: ")

    if opcao == '1':
        menu_funcionarios()
    elif opcao == '2':
        menu_proprietarios()
    elif opcao == '3':
        menu_carros()
    elif opcao == '0':
        print("Encerrando o sistema.")
        break
    else:
        print("Opção inválida, tente novamente")
