import mysql.connector
from db import conectar
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/alunos", methods = ["GET"])
def get_alunos():
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM alunos")
    dados = cursor.fetchall()
    alunos = []
    for aluno in dados:
        alunos.append({
            "ID_alunos": aluno[0],
            "nome": aluno[1],
            "idade": aluno[2],

        })
    '''for aluno in dados:
        print(f"ID: {aluno[0]} | Nome: {aluno[1]} | Idade: {aluno[2]}")'''
    
    cursor.close()
    conexao.close()

    return jsonify(alunos)
 
@app.route("/alunos/<int:ID_aluno>", methods = ["PUT"])
def put_aluno(ID_aluno):
    dados=request.json
    nome=dados["nome"]
    idade=dados["idade"]

    conexao=conectar()
    cursor=conexao.cursor()

    sql="UPDATE alunos SET nome=%s, idade=%s WHERE ID_aluno=%s"
    cursor.execute(sql, (nome, idade, ID_aluno))
    conexao.commit()
    cursor.close()
    conexao.close()
    return jsonify({"Mensagem": "Aluno atualizado"})

@app.route("/alunos", methods=["POST"])
def post_aluno():
    dados = request.json
    nome = dados["nome"]
    idade = dados["idade"]

    conexao = conectar()
    cursor = conexao.cursor()

    sql = "INSERT INTO alunos(nome, idade) VALUES (%s, %s)"
    cursor.execute(sql, (nome, idade))

    conexao.commit()
    cursor.close()
    conexao.close()

    return jsonify({"Mensagem": "Aluno adicionado com sucesso!"})
curl -X POST http://localhost:5000/alunos \
-H "Content-Type: application/json" \
-d '{
    "nome": "João",
    "idade": 20
}'
    
@app.route("/alunos", methods = ["DELETE"])
def delete_aluno(ID_aluno):
    conexao = conectar()
    cursor = conexao.cursor()

    sql="DELETE FROM alunos WHERE ID_aluno=%s"
    cursor.execute(sql, (ID_aluno))
    conexao.commit()
    cursor.close()
    conexao.close()
    return jsonify({"Mensagem": "Aluno se foi"})



if __name__ == "__main__":
    app.run(debug=True)