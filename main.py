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
            "id": aluno[0],
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


@app.route("/atualizar", methods=["POST"])
def atualizar():
    dados = request.form
    
    id = dados["id"]
    nome = dados["nome"]
    idade = dados["idade"]

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("UPDATE alunos SET nome=%s, idade=%s WHERE id=%s", (nome, idade, id))

    conexao.commit()

    cursor.close()
    conexao.close()

    return redirect("/")


@app.route("/deletar/<int:id>")
def delete_aluno(id):

    conexao = conectar()
    cursor = conexao.cursor()

    sql = "DELETE FROM alunos WHERE id=%s"

    cursor.execute(sql, (id,))

    conexao.commit()

    cursor.close()
    conexao.close()

    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)