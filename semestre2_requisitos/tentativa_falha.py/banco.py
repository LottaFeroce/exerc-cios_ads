'''# exemplo de leitura no backend
total_itens = int(request.form["total_itens"])
for i in range(1, total_itens + 1):
    produto = request.form.get(f"produto_{i}")
    quantidade = request.form.get(f"quantidade_{i}")
    preco_unitario = request.form.get(f"preco_unitario_{i}")
    subtotal = request.form.get(f"subtotal_{i}")
    # ... insere no banco com venda_id
from pylance import *
from flask import Flask, request, jsonify
from mysql.connector import connect
from datetime import datetime, timedelta

app = Flask(__name__)

# Conexão
def get_conn():
    return connect(
        host="localhost",
        user="root",
        password="1234",
        database="seu_jao"
    )

@app.route('/registrar_venda', methods=['POST'])
def registrar_venda():
    try:
        data = request.form
        conn = get_conn()
        cursor = conn.cursor()

        cliente_id = data["cliente_id"]
        vendedor_id = data["vendedor_id"]
        valor_total = float(data["valor_total"])
        desconto = float(data.get("desconto", 0))
        forma_pagamento = data["forma_pagamento"]
        status = data.get("status", "Concluída")
        observacoes = data.get("observacoes", "")
        produtos = eval(data["produtos"])  # formato: [{'id': 1, 'qtd': 2, 'preco': 10.0}, ...]

        # 💸 Inserir Venda
        cursor.execute("""
            INSERT INTO vendas (cliente_id, vendedor_id, valor_total, desconto, forma_pagamento, status, observacoes)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """, (cliente_id, vendedor_id, valor_total, desconto, forma_pagamento, status, observacoes))
        venda_id = cursor.lastrowid

        # 📦 Itens da Venda
        for p in produtos:
            subtotal = p['qtd'] * p['preco']
            cursor.execute("""
                INSERT INTO itens_venda (venda_id, produto_id, quantidade, preco_unitario, subtotal)
                VALUES (%s, %s, %s, %s, %s)
            """, (venda_id, p['id'], p['qtd'], p['preco'], subtotal))

        # 📅 Parcelas (se for crediário)
        if forma_pagamento == "Crediário":
            qtd_parcelas = int(data.get("qtd_parcelas", 1))
            data_primeira = datetime.strptime(data.get("primeira_parcela"), "%Y-%m-%d")
            valor_parcela = round(valor_total / qtd_parcelas, 2)

            for i in range(qtd_parcelas):
                vencimento = (data_primeira + timedelta(days=30 * i)).strftime("%Y-%m-%d")
                cursor.execute("""
                    INSERT INTO parcelas_crediario (venda_id, numero_parcela, valor_parcela, data_vencimento)
                    VALUES (%s, %s, %s, %s)
                """, (venda_id, i+1, valor_parcela, vencimento))

        # 💰 Comissão
        valor_comissao = float(data.get("valor_comissao", 0))
        if valor_comissao > 0:
            data_comissao = datetime.now().strftime("%Y-%m-%d")
            cursor.execute("""
                INSERT INTO comissoes (venda_id, vendedor_id, valor_comissao, data_calculo)
                VALUES (%s, %s, %s, %s)
            """, (venda_id, vendedor_id, valor_comissao, data_comissao))

        conn.commit()
        return jsonify({"status": "sucesso", "venda_id": venda_id})

    except Exception as e:
        return jsonify({"status": "erro", "detalhes": str(e)})
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()

if __name__ == '__main__':
    app.run(debug=True)
'''