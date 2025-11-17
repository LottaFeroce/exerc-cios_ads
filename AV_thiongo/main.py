from DATABASE import Database
from cliente import Cliente
from produto import Produto
from vendedor import Vendedor
from venda import Venda
from carrinho import Carrinho_item

def menu():
    db = Database()

    while True:
        print("\n           Sauvojen tuntija")
        print("§" * 40)
        print("1 - Cadastrar Cliente")
        print("2 - Listar Clientes")
        print("3 - Excluir Cliente")
        print("4 - Atualizar Cliente")
        print("5 - Cadastrar Produto")
        print("6 - Listar Produtos")
        print("7 - Adicionar ao Carrinho")
        print("8 - Finalizar Compra")
        print("9 - Listar Vendas")
        print("0 - Sair")

        opcao = input("Escolha: ")

###################### CLIENTE ################
        if opcao == '1':
            cli = Cliente()
            cli.nome = input("Nome: ")
            cli.cpf = input("CPF: ")
            cli.email = input("Email: ")
            cli.senha = input("Senha: ")

            db.insert("""
                INSERT INTO cliente (nome, cpf, email, senha)
                VALUES (%s, %s, %s, %s)
            """, (cli.nome, cli.cpf, cli.email, cli.senha))

            print("Cliente cadastrado com sucesso")

        elif opcao == '2':
            result = db.select("SELECT * FROM cliente")
            for busca_cli in result:
                print(f"ID: {busca_cli[0]} | Nome: {busca_cli[1]} | CPF: {busca_cli[2]} | Email: {busca_cli[3]}")

        elif opcao == '3':
            result = db.select("SELECT * FROM cliente")
            for busca_cli in result:
                print(f"ID: {busca_cli[0]} - {busca_cli[1]}")

            id_cli = int(input("ID para excluir: "))
            db.delete("DELETE FROM cliente WHERE cliente_id=%s", id_cli)
            print("Cliente excluído")

        elif opcao == '4':
            result = db.select("SELECT * FROM cliente")
            for busca_cli in result:
                print(f"ID: {busca_cli[0]} - {busca_cli[1]}")

            id_cli = int(input("ID para atualizar: "))
            cliente = db.select_by_id("SELECT * FROM cliente WHERE cliente_id=%s", id_cli)

            nome = input(f"Novo nome ({cliente[1]}): ") or cliente[1]
            cpf = input(f"Novo CPF ({cliente[2]}): ") or cliente[2]
            email = input(f"Novo Email ({cliente[3]}): ") or cliente[3]
            senha = input("Nova senha: ") or cliente[4]

            db.update("""
                UPDATE cliente
                SET nome=%s, cpf=%s, email=%s, senha=%s
                WHERE cliente_id=%s
            """, (nome, cpf, email, senha, id_cli))

            print("Cliente atualizado")

######################## PRODUTO ################
        elif opcao == '5':
            prod = Produto()
            prod.nome = input("Nome do produto: ")
            prod.valor = float(input("Valor: "))
            prod.descricao = input("Descrição: ")
            prod.quantidade = int(input("Quantidade: "))

            db.insert("""
                INSERT INTO produto (nome, valor, descricao, quantidade)
                VALUES (%s, %s, %s, %s)
            """, (prod.nome, prod.valor, prod.descricao, prod.quantidade))

            print("Produto cadastrado")

        elif opcao == '6':
            produtos = db.select("SELECT * FROM produto")
            for busca_prod in produtos:
                print(f"ID: {busca_prod[0]} | {busca_prod[1]} | R$ {busca_prod[2]} | Estoque: {busca_prod[4]}")

######################## CARRINHO #################
        elif opcao == '7':
            id_cli = int(input("ID Cliente: "))
            id_prod = int(input("ID Produto: "))
            qtd = int(input("Quantidade: "))

            produto = db.select_by_id("SELECT * FROM produto WHERE produto_id=%s", id_prod)

            if produto:
                valor = produto[2]
                db.insert("""
                    INSERT INTO carrinho (cliente_id, produto_id, quantidade, valor)
                    VALUES (%s, %s, %s, %s)
                """, (id_cli, id_prod, qtd, valor))

                print("Item adicionado ao carrinho")
            else:
                print("Produto não encontrado")

####################### FINALIZAR COMPRA ################
        elif opcao == '8':
            id_cli = int(input("ID Cliente: "))

            itens = db.select(f"SELECT * FROM carrinho WHERE cliente_id={id_cli}")

            if len(itens) == 0:
                print("Carrinho vazio")
                continue

            total = 0
            total_qtd = 0

            for item in itens:
                total += item[4] * item[3]
                total_qtd += item[3]

            db.insert("""
                INSERT INTO venda (cliente_id, valor, quantidade)
                VALUES (%s, %s, %s)
            """, (id_cli, total, total_qtd))

            db.delete("DELETE FROM carrinho WHERE cliente_id=%s", id_cli)

            print(f"Compra finalizada Total: R$ {total}")

######################## LISTAR VENDAS #################
        elif opcao == '9':
            vendas = db.select("SELECT * FROM venda")
            for busca_vend in vendas:
                print(f"ID: {busca_vend[0]} | Cliente: {busca_vend[1]} | Total: {busca_vend[2]} | Itens: {busca_vend[3]}")

        elif opcao == '0':
            print("Saindo.")
            break

        else:
            print("Opção inválida")


if __name__ == "__main__":
    menu()
