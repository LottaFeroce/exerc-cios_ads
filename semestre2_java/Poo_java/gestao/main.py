import mysql.connector
from db import conectar
from flask import Flask, request, jsonify, render_template, redirect

app = Flask(__name__)

@app.route("/")
def home():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("SELECT * FROM alunos")
    alunos = cursor.fetchall()

   #alunos = []

    """for aluno in dados:
        alunos.append({
            "ID_aluno": aluno[0],
            "nome": aluno[1],
            "idade": aluno[2]
        })"""

    cursor.close()
    conexao.close()

    return render_template("aula.html", alunos = alunos)

@app.route("/cadastrar", methods=["POST"])
def cadastrar():
    nome = request.form["nome"]
    idade = request.form["idade"]
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("INSERT INTO alunos (nome, idade) VALUES (%s, %s)",(nome,idade))

    conexao.commit()

    cursor.close()
    conexao.close()

    return redirect("/")


@app.route("/alunos/<int:ID_aluno>", methods=["PUT"])
def put_aluno(ID_aluno):
    dados = request.json

    nome = dados["nome"]
    idade = dados["idade"]

    conexao = conectar()
    cursor = conexao.cursor()

    sql = "UPDATE alunos SET nome=%s, idade=%s WHERE ID_aluno=%s"

    cursor.execute(sql, (nome, idade, ID_aluno))

    conexao.commit()

    cursor.close()
    conexao.close()

    return jsonify({"mensagem": "Aluno atualizado com sucesso"})


@app.route("/alunos/<int:ID_aluno>", methods=["DELETE"])
def delete_aluno(ID_aluno):

    conexao = conectar()
    cursor = conexao.cursor()

    sql = "DELETE FROM alunos WHERE ID_aluno=%s"

    cursor.execute(sql, (ID_aluno,))

    conexao.commit()

    cursor.close()
    conexao.close()

    return jsonify({"mensagem": "Aluno se foi!"})


if __name__ == "__main__":
    app.run(debug=True)