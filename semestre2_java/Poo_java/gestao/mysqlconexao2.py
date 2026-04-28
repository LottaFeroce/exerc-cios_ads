import mysql.connector
def conectar():
    conexao = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "aula_connect"
    )
    return conexao

def get_alunos():
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM alunos")
    dados = cursor.fetchall()
    for aluno in dados:
        print(f"ID: {aluno[0]} | Nome: {aluno[1]} | Idade: {aluno[2]}")

    cursor.close()
    conexao.close()