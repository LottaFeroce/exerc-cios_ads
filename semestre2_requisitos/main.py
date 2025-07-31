from datetime import datetime

estoque = {
    'cimento': {'quantidade': 10, 'preco_unitario': 35.00, 'categoria': 'material básico'},
    'tijolo': {'quantidade': 500, 'preco_unitario': 1.50, 'categoria': 'alvenaria'},
    'fio elétrico': {'quantidade': 100, 'preco_unitario': 2.00, 'categoria': 'elétrica'},
}

vendas = []

comissoes = {
    'pix': 0.05,
    'dinheiro': 0.05,
    'cartão': 0.03,
}

def consultar_estoque(produto):
    return estoque.get(produto.lower(), 'Produto não encontrado.')

def registrar_venda(cliente, produtos_vendidos, forma_pagamento):
    total = 0
    detalhes_venda = []

    for item, quantidade in produtos_vendidos.items():
        if item in estoque and estoque[item]['quantidade'] >= quantidade:
            preco = estoque[item]['preco_unitario']
            subtotal = preco * quantidade
            total += subtotal
            estoque[item]['quantidade'] -= quantidade
            detalhes_venda.append({
                'produto': item,
                'quantidade': quantidade,
                'preco_unitario': preco,
                'subtotal': subtotal
            })
        else:
            print(f"Estoque insuficiente para {item} ou item não encontrado.")
            return

    comissao = total * comissoes.get(forma_pagamento.lower(), 0)
    venda = {
        'cliente': cliente,
        'data': datetime.now(),
        'itens': detalhes_venda,
        'forma_pagamento': forma_pagamento,
        'total': total,
        'comissao': comissao
    }
    vendas.append(venda)
    print(f"Venda registrada para {cliente}. Total: R${total:.2f}, Comissão: R${comissao:.2f}")

def relatorio():
    print("\n=== RELATÓRIO DE VENDAS ===")
    for venda in vendas:
        print(f"{venda['data']} - Cliente: {venda['cliente']} - Total: R${venda['total']:.2f} - Forma: {venda['forma_pagamento']}")
        for item in venda['itens']:
            print(f"  - {item['quantidade']}x {item['produto']} (R${item['preco_unitario']:.2f})")
    print("\n=== ESTOQUE ATUAL ===")
    for nome, info in estoque.items():
        print(f"{nome.title()}: {info['quantidade']} unidades, R${info['preco_unitario']:.2f} cada")


if __name__ == "__main__":
    registrar_venda('João', {'cimento': 2, 'tijolo': 50}, 'pix')
    registrar_venda('Maria', {'fio elétrico': 30}, 'dinheiro')
    relatorio()