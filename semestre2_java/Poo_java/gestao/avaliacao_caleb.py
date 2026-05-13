from flask import Flask, request, jsonify
from db import conectar

app = Flask(__name__)

@app.route("/alunos", methods=["GET"])
def get_alunos():

    conexao = conectar()
    cursor = conexao.cursor()

    sql = """
    SELECT
        ID_aluno,
        Nome_aluno,
        Matricula,
        Turmas_ID_turma
    FROM Alunos
    """

    cursor.execute(sql)

    dados = cursor.fetchall()

    alunos = []

    for aluno in dados:
        alunos.append({
            "ID_aluno": aluno[0],
            "Nome_aluno": aluno[1],
            "Matricula": aluno[2],
            "Turmas_ID_turma": aluno[3]
        })

    cursor.close()
    conexao.close()

    return jsonify(alunos)

@app.route("/alunos", methods=["POST"])
def post_aluno():

    dados = request.json

    nome = dados["Nome_aluno"]
    matricula = dados["Matricula"]
    turma = dados["Turmas_ID_turma"]

    conexao = conectar()
    cursor = conexao.cursor()

    sql = """
    INSERT INTO Alunos
    (Nome_aluno, Matricula, Turmas_ID_turma)
    VALUES (%s, %s, %s)
    """

    cursor.execute(sql, (nome, matricula, turma))

    conexao.commit()

    cursor.close()
    conexao.close()

    return jsonify({
        "mensagem": "Aluno adicionado com sucesso"
    })


@app.route("/alunos/<int:ID_aluno>", methods=["PUT"])
def put_aluno(ID_aluno):

    dados = request.json

    nome = dados["Nome_aluno"]
    matricula = dados["Matricula"]
    turma = dados["Turmas_ID_turma"]

    conexao = conectar()
    cursor = conexao.cursor()

    sql = """
    UPDATE Alunos
    SET
        Nome_aluno = %s,
        Matricula = %s,
        Turmas_ID_turma = %s
    WHERE ID_aluno = %s
    """

    cursor.execute(sql, (nome, matricula, turma, ID_aluno))

    conexao.commit()

    cursor.close()
    conexao.close()

    return jsonify({
        "mensagem": "Aluno atualizado com sucesso"
    })



@app.route("/alunos/<int:ID_aluno>", methods=["DELETE"])
def delete_aluno(ID_aluno):

    conexao = conectar()
    cursor = conexao.cursor()

    sql = "DELETE FROM Alunos WHERE ID_aluno = %s"

    cursor.execute(sql, (ID_aluno,))

    conexao.commit()

    cursor.close()
    conexao.close()

    return jsonify({
        "mensagem": "Aluno removido com sucesso"
    })



if __name__ == "__main__":
    app.run(debug=True)

"""

GET/alunos
POST:{
    "Nome_aluno": "Pedro Henrique",
    "Matricula": "2025010",
    "Turmas_ID_turma": 1
}
PUT:{
    "Nome_aluno": "Pedro Atualizado",
    "Matricula": "2025010",
    "Turmas_ID_turma": 2
}

"""