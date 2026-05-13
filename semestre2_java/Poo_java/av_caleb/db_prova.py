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
@app.route("/turmas", methods=["POST"])
def post_turma():
    dados = request.json
    nome = dados["Nome_turma"]
    semestre = dados["Semestre"]
    conexao = conectar()
    cursor = conexao.cursor()
    sql = """
    INSERT INTO Turmas
    (Nome_turma, Semestre)
    VALUES (%s, %s)
    """
    cursor.execute(sql, (nome, semestre))
    conexao.commit()
    cursor.close()
    conexao.close()
    return jsonify({
        "mensagem": "Turma cadastrada com sucesso"
    })
@app.route("/turmas/<int:ID_turma>", methods=["DELETE"])
def delete_turma(ID_turma):
    conexao = conectar()
    cursor = conexao.cursor()
    sql = "DELETE FROM Turmas WHERE ID_turma = %s"
    cursor.execute(sql, (ID_turma,))
    conexao.commit()
    cursor.close()
    conexao.close()
    return jsonify({
        "mensagem": "Turma removida com sucesso"
    })
@app.route("/avaliacoes", methods=["POST"])
def post_avaliacao():
    dados = request.json
    peso = dados["Peso"]
    turma = dados["Turmas_ID_turma"]
    conexao = conectar()
    cursor = conexao.cursor()
    sql = """
    INSERT INTO Avaliacoes
    (Peso, Turmas_ID_turma)
    VALUES (%s, %s)
    """
    cursor.execute(sql, (peso, turma))
    conexao.commit()
    cursor.close()
    conexao.close()
    return jsonify({
        "mensagem": "Avaliação cadastrada com sucesso"
    })
@app.route("/avaliacoes/<int:ID_avaliacoes>", methods=["DELETE"])
def delete_avaliacao(ID_avaliacoes):
    conexao = conectar()
    cursor = conexao.cursor()
    sql = "DELETE FROM Avaliacoes WHERE ID_avaliacoes = %s"
    cursor.execute(sql, (ID_avaliacoes,))
    conexao.commit()
    cursor.close()
    conexao.close()
    return jsonify({
        "mensagem": "Avaliação removida com sucesso"
    })
@app.route("/notas", methods=["GET"])
def get_notas():
    conexao = conectar()
    cursor = conexao.cursor()
    sql = """
    SELECT
        n.ID_nota,
        a.Nome_aluno,
        n.Nota,
        av.ID_avaliacoes
    FROM Notas n
    JOIN Alunos a
        ON n.Alunos_ID_aluno = a.ID_aluno
    JOIN Avaliacoes av
        ON n.Avaliacoes_ID_avaliacoes = av.ID_avaliacoes
    """
    cursor.execute(sql)
    dados = cursor.fetchall()
    notas = []
    for nota in dados:
        notas.append({
            "ID_nota": nota[0],
            "Nome_aluno": nota[1],
            "Nota": nota[2],
            "ID_avaliacao": nota[3]
        })
    cursor.close()
    conexao.close()
    return jsonify(notas)
@app.route("/notas", methods=["POST"])
def post_nota():
    dados = request.json
    nota = dados["Nota"]
    avaliacao = dados["Avaliacoes_ID_avaliacoes"]
    aluno = dados["Alunos_ID_aluno"]
    conexao = conectar()
    cursor = conexao.cursor()
    sql = """
    INSERT INTO Notas
    (Nota, Avaliacoes_ID_avaliacoes, Alunos_ID_aluno)
    VALUES (%s, %s, %s)
    """
    cursor.execute(sql, (nota, avaliacao, aluno))
    conexao.commit()
    cursor.close()
    conexao.close()
    return jsonify({
        "mensagem": "Nota lançada com sucesso"
    })
@app.route("/notas/<int:ID_nota>", methods=["PUT"])
def put_nota(ID_nota):
    dados = request.json
    nota = dados["Nota"]
    conexao = conectar()
    cursor = conexao.cursor()
    sql = """
    UPDATE Notas
    SET Nota = %s
    WHERE ID_nota = %s
    """
    cursor.execute(sql, (nota, ID_nota))
    conexao.commit()
    cursor.close()
    conexao.close()
    return jsonify({
        "mensagem": "Nota atualizada com sucesso"
    })
@app.route("/notas/<int:ID_nota>", methods=["DELETE"])
def delete_nota(ID_nota):
    conexao = conectar()
    cursor = conexao.cursor()
    sql = "DELETE FROM Notas WHERE ID_nota = %s"
    cursor.execute(sql, (ID_nota,))
    conexao.commit()
    cursor.close()
    conexao.close()
    return jsonify({
        "mensagem": "Nota removida com sucesso"
    })
@app.route("/medias", methods=["GET"])
def get_medias():
    conexao = conectar()
    cursor = conexao.cursor()
    sql = """
    SELECT
        a.Nome_aluno,
        t.Nome_turma,
        AVG(n.Nota) AS Media_Final
    FROM Notas n
    JOIN Alunos a
        ON n.Alunos_ID_aluno = a.ID_aluno
    JOIN Turmas t
        ON a.Turmas_ID_turma = t.ID_turma
    GROUP BY a.ID_aluno
    """
    cursor.execute(sql)
    dados = cursor.fetchall()
    medias = []
    for media in dados:
        medias.append({
            "Nome_aluno": media[0],
            "Nome_turma": media[1],
            "Media_Final": float(media[2])
        })
    cursor.close()
    conexao.close()
    return jsonify(medias)
if __name__ == "__main__":
    app.run(debug=True)