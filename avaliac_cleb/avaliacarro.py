from flask import Flask, request, jsonify
import mysql.connector

app = Flask(__name__)

def conectar():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="carroleb"
    )

@app.route("/clientes", methods=["GET"])
def listar_clientes():

    conexao = conectar()
    cursor = conexao.cursor(dictionary=True)
    cursor.execute("SELECT * FROM clientes")
    dados = cursor.fetchall()
    cursor.close()
    conexao.close()
    return jsonify(dados)


@app.route("/clientes", methods=["POST"])
def criar_cliente():

    dados = request.get_json()
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute(
        """
        INSERT INTO clientes(nome_cliente, contato)
        VALUES(%s, %s)
        """,
        (
            dados["nome_cliente"],
            dados["contato"]
        )
    )

    conexao.commit()
    cursor.close()
    conexao.close()
    return jsonify({
        "mensagem": "Cliente criado com sucesso"
    }), 201

@app.route("/veiculos", methods=["GET"])
def listar_veiculos():

    conexao = conectar()
    cursor = conexao.cursor(dictionary=True)
    cursor.execute("SELECT * FROM veiculos")
    dados = cursor.fetchall()
    cursor.close()
    conexao.close()
    return jsonify(dados)


@app.route("/veiculos", methods=["POST"])
def criar_veiculo():

    dados = request.get_json()
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute(
        """
        INSERT INTO veiculos
        (
            nome_veiculo,
            modelo,
            valor,
            disponibilidade
        )
        VALUES (%s, %s, %s, %s)
        """,
        (
            dados["nome_veiculo"],
            dados["modelo"],
            dados["valor"],
            "disponivel"
        )
    )

    conexao.commit()
    cursor.close()
    conexao.close()
    return jsonify({
        "mensagem": "Veículo cadastrado"
    }), 201

@app.route("/reservas", methods=["GET"])
def listar_reservas():
    conexao = conectar()
    cursor = conexao.cursor(dictionary=True)
    cursor.execute("""
        SELECT *
        FROM reservas
    """)
    dados = cursor.fetchall()
    cursor.close()
    conexao.close()
    return jsonify(dados)

@app.route("/reservas", methods=["POST"])
def criar_reserva():
    dados = request.get_json()
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute(
        """
        INSERT INTO reservas
        (
            data_reserva,
            clientes_id,
            veiculos_id
        )
        VALUES (%s, %s, %s)
        """,
        (
            dados["data_reserva"],
            dados["clientes_id"],
            dados["veiculos_id"]
        )
    )
    conexao.commit()
    cursor.close()
    conexao.close()
    return jsonify({
        "mensagem": "Reserva criada com sucesso"
    }), 201

@app.route("/reservas/<int:id>", methods=["PUT"])
def cancelar_reserva(id):
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute(
        """
        UPDATE reservas
        SET status_reserva = 'cancelada'
        WHERE id_reserva = %s
        """,
        (id,)
    )
    conexao.commit()
    cursor.close()
    conexao.close()
    return jsonify({
        "mensagem": "Reserva cancelada"
    })

if __name__ == "__main__":
    app.run(debug=True)