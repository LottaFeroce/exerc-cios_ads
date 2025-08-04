import mysql.connector
from datetime import datetime

conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='1234',
    database='seu_jao'
)
cursor = conexao.cursor(dictionary=True)

comissoes = {
    'PIX': 0.05,
    'Dinheiro': 0.05,
    'Cartão Débito': 0.03,
    'Cartão Crédito': 0.03
}

def consultar_produto(codigo_barras):
    query = "SELECT * FROM produtos WHERE codigo_barras = %s AND ativo = 1"
    cursor.execute(query, (codigo_barras,))
    return cursor.fetchone()

def registrar_venda():
    try:
        cliente_id = int(input("ID do Cliente: "))
        vendedor_id = int(input("ID do Vendedor: "))
        forma_pagamento = input("Forma de Pagamento (PIX, Dinheiro, Cartão Débito, Cartão Crédito): ")

        itens = {}
        while True:
            codigo = input("Código de Barras do Produto (ou 'fim' para encerrar): ")
            if codigo.lower() == 'fim':
                break
            quantidade = float(input("Quantidade: "))
            itens[codigo] = quantidade

        total = 0
        detalhes = []

        for codigo, quantidade in itens.items():
            produto = consultar_produto(codigo)
            if not produto or produto['estoque_atual'] < quantidade:
                print(f"Produto '{codigo}' não encontrado ou estoque insuficiente.")
                return
            subtotal = float(produto['preco_venda']) * quantidade
            total += subtotal
            detalhes.append((produto, quantidade, subtotal))

        cursor.execute("""
            INSERT INTO vendas (cliente_id, vendedor_id, valor_total, forma_pagamento)
            VALUES (%s, %s, %s, %s)
        """, (cliente_id, vendedor_id, total, forma_pagamento))
        venda_id = cursor.lastrowid

        for produto, quantidade, subtotal in detalhes:
            cursor.execute("""
                INSERT INTO itens_venda (venda_id, produto_id, quantidade, preco_unitario, subtotal)
                VALUES (%s, %s, %s, %s, %s)
            """, (venda_id, produto['id'], quantidade, produto['preco_venda'], subtotal))

            novo_estoque = float(produto['estoque_atual']) - quantidade
            cursor.execute("UPDATE produtos SET estoque_atual = %s WHERE id = %s", (novo_estoque, produto['id']))

        porcentagem = comissoes.get(forma_pagamento, 0)
        valor_comissao = total * porcentagem
        cursor.execute("""
            INSERT INTO comissoes (venda_id, vendedor_id, valor_comissao, data_calculo)
            VALUES (%s, %s, %s, %s)
        """, (venda_id, vendedor_id, valor_comissao, datetime.now().date()))
        conexao.commit()
        print(f"\nVenda registrada com sucesso! Total: R${total:.2f} | Comissão: R${valor_comissao:.2f}")
    except Exception as e:
        print("Erro ao registrar venda:", e)

def relatorio_vendas():
    print("\nRELATÓRIO DE VENDAS")
    cursor.execute("""
        SELECT v.id, v.data_venda, c.nome AS cliente, v.valor_total, v.forma_pagamento
        FROM vendas v
        JOIN clientes c ON v.cliente_id = c.id
    """)
    vendas = cursor.fetchall()
    for venda in vendas:
        print(f"\nVenda #{venda['id']} - {venda['data_venda']} - Cliente: {venda['cliente']}")
        print(f"Total: R${venda['valor_total']:.2f} | Forma de pagamento: {venda['forma_pagamento']}")
        cursor.execute("""
            SELECT p.descricao, i.quantidade, i.preco_unitario
            FROM itens_venda i
            JOIN produtos p ON i.produto_id = p.id
            WHERE i.venda_id = %s
        """, (venda['id'],))
        itens = cursor.fetchall()
        for item in itens:
            print(f"  - {item['quantidade']}x {item['descricao']} (R${item['preco_unitario']:.2f})")

def relatorio_por_funcionario():
    print("\nRELATÓRIO DE VENDAS POR FUNCIONÁRIO")
    cursor.execute("""
        SELECT v.id, v.data_venda, ven.nome AS vendedor, c.nome AS cliente, v.valor_total, v.forma_pagamento
        FROM vendas v
        JOIN vendedores ven ON v.vendedor_id = ven.id
        JOIN clientes c ON v.cliente_id = c.id
        ORDER BY ven.nome, v.data_venda
    """)
    vendas = cursor.fetchall()

    if not vendas:
        print("Nenhuma venda registrada ainda.")
        return

    for venda in vendas:
        print(f"\nVenda #{venda['id']} - {venda['data_venda']} - Vendedor: {venda['vendedor']}")
        print(f"Cliente: {venda['cliente']} | Total: R${venda['valor_total']:.2f} | Forma: {venda['forma_pagamento']}")
        cursor.execute("""
            SELECT p.descricao, i.quantidade, i.preco_unitario
            FROM itens_venda i
            JOIN produtos p ON i.produto_id = p.id
            WHERE i.venda_id = %s
        """, (venda['id'],))
        itens = cursor.fetchall()
        for item in itens:
            print(f"  - {item['quantidade']}x {item['descricao']} (R${item['preco_unitario']:.2f})")

def relatorio_cadastros():
    print("\nRELATÓRIO DE PESSOAS CADASTRADAS")
    print("\nClientes:")
    cursor.execute("SELECT id, nome, cpf_cnpj, telefone FROM clientes")
    clientes = cursor.fetchall()
    for c in clientes:
        print(f"  ID: {c['id']} | Nome: {c['nome']} | CPF/CNPJ: {c['cpf_cnpj']} | Tel: {c['telefone']}")

    print("\nVendedores:")
    cursor.execute("SELECT id, nome, cpf, telefone FROM vendedores")
    vendedores = cursor.fetchall()
    for v in vendedores:
        print(f"  ID: {v['id']} | Nome: {v['nome']} | CPF: {v['cpf']} | Tel: {v['telefone']}")

def consultar_estoque():
    print("\nESTOQUE ATUAL")
    cursor.execute("SELECT descricao, estoque_atual, preco_venda FROM produtos WHERE ativo = 1")
    produtos = cursor.fetchall()
    for p in produtos:
        print(f"{p['descricao']}: {p['estoque_atual']} unidades | R${p['preco_venda']:.2f}")

def cadastrar_cliente():
    try:
        nome = input("Nome do cliente: ")
        tipo = input("Tipo (PF/PJ): ").upper()
        cpf_cnpj = input("CPF ou CNPJ: ")
        telefone = input("Telefone: ")
        email = input("Email: ")
        endereco = input("Endereço: ")
        cursor.execute("""
            INSERT INTO clientes (nome, tipo, cpf_cnpj, telefone, email, endereco)
            VALUES (%s, %s, %s, %s, %s, %s)
        """, (nome, tipo, cpf_cnpj, telefone, email, endereco))
        conexao.commit()
        print("Cliente cadastrado com sucesso!")
    except Exception as e:
        print("Erro ao cadastrar cliente:", e)

def cadastrar_vendedor():
    try:
        nome = input("Nome do vendedor: ")
        cpf = input("CPF: ")
        telefone = input("Telefone: ")
        email = input("Email: ")
        data_str = input("Data de admissão (DD-MM-YYYY): ")
        data_admissao = datetime.strptime(data_str, "%d-%m-%Y").date()
        cursor.execute("""
            INSERT INTO vendedores (nome, cpf, telefone, email, data_admissao)
            VALUES (%s, %s, %s, %s, %s)
        """, (nome, cpf, telefone, email, data_admissao))
        conexao.commit()
        print("Vendedor cadastrado com sucesso!")
    except Exception as e:
        print("Erro ao cadastrar vendedor:", e)

def cadastrar_produto():
    try:
        codigo_barras = input("Código de Barras: ")
        descricao = input("Descrição: ")
        categoria = input("Categoria (Elétrico, Hidráulico, Ferragens, Material Básico, Outros): ")
        unidade_medida = input("Unidade de Medida (UN, KG, M, M², CX, SC): ")
        preco_custo = float(input("Preço de Custo: "))
        preco_venda = float(input("Preço de Venda: "))
        estoque_atual = float(input("Estoque Atual: "))
        estoque_minimo = float(input("Estoque Mínimo: "))
        estoque_maximo = float(input("Estoque Máximo (ou deixe em branco): ") or 0)
        cursor.execute("""
            INSERT INTO produtos (codigo_barras, descricao, categoria, unidade_medida,
                                  preco_custo, preco_venda, estoque_atual, estoque_minimo, estoque_maximo)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        """, (codigo_barras, descricao, categoria, unidade_medida,
              preco_custo, preco_venda, estoque_atual, estoque_minimo, estoque_maximo))
        conexao.commit()
        print("Produto cadastrado com sucesso!")
    except Exception as e:
        print("Erro ao cadastrar produto:", e)

def menu():
    while True:
        print("\nMENU CRUD — escolha uma opção")
        print("1. Registrar nova venda")
        print("2. Consultar estoque")
        print("3. Relatório de vendas")
        print("4. Cadastrar cliente")
        print("5. Cadastrar vendedor")
        print("6. Cadastrar produto")
        print("7. Ver relatório de cadastros (clientes e vendedores)")
        print("8. Relatório de vendas por funcionário")
        print("9. Sair")
        escolha = input(">> ")
        if escolha == '1':
            registrar_venda()
        elif escolha == '2':
            consultar_estoque()
        elif escolha == '3':
            relatorio_vendas()
        elif escolha == '4':
            cadastrar_cliente()
        elif escolha == '5':
            cadastrar_vendedor()
        elif escolha == '6':
            cadastrar_produto()
        elif escolha == '7':
            relatorio_cadastros()
        elif escolha == '8':
            relatorio_por_funcionario()
        elif escolha == '9':
            print("Encerrando sistema.")
            break
        else:
            print("\nOpção inválida! Tente novamente.")

if __name__ == "__main__":
    menu()
