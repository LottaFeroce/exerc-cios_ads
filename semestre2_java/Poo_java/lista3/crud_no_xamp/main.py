from Cliente import Cliente

while True:
    print("SysMechnik")
    print("="*30)
    print("Selecione uma opção")
    option = input ("1-Cadastrar CLiente\n2-Listar Clientes\n3-Excluir\n4-Atualizar\n0-Sair\n")
    

    if option =='0':
        break

    elif option == '1':
        cli = Cliente()
        cli.nome = input("Digite o nome do CLiente: ")
        cli.cpf = input("Digite o CPF: ")
        cli.fone = input("Digite o Telefone: ")
        cli.cidade = input("Digite a Cidade :")
        result = cli.cadastrar()
        if result == True:
            print("Cadastrado com sucesso")

    elif option == '2':
        cli = Cliente()
        result = cli.buscar()
        for cliente in result:
            print(f"ID: {cliente[0]} | NOME: {cliente[1]} | CPF: {cliente[2]} | FONE: {cliente[3]} | CIDADE: {cliente[4]}")
    
    elif option == '3':
        cli = Cliente()
        result = cli.buscar()
        for cliente in result:
            print(f"ID: {cliente[0]} | NOME: {cliente[1]} | CPF: {cliente[2]} | FONE: {cliente[3]} | CIDADE: {cliente[4]}")

        id_excluir = int(input("Digite o ID do cliente que deseja excluir: "))
        result = cli.excluir(id_excluir)
        if result == True:
            print("Excluido(a) com sucesso")
        
    elif option == '4':
        cli = Cliente()
        result = cli.buscar()
        for cliente in result:
            print(f"ID: {cliente[0]} | NOME: {cliente[1]} | CPF: {cliente[2]} | FONE: {cliente[3]} | CIDADE: {cliente[4]}")
        
        id_atualizado = int(input("Digite o ID do cliente que deseja atualizar: "))
        result = list(cli.atualizar(id_atualizado))
        result[1] = input("Digite o Nome: ")
        result[2] = input("Digite o CPF: ")
        result[3] = input("Digite o Fone: ")
        result[4] = input("Digite a Cidade: ")
        atualizacao = cli.atualizar(tuple(result))
        if atualizacao == True:
            print("CLiente atualizado com sucesso.")

            
