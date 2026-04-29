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

def post_aluno():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("INSERT INTO alunos(nome, idade) VALUES (%s, %s)", (input("Digite o nome do aluno: "),input("Digite a idade do aluno: ")))
    conexao.commit()
    print("Aluno adicionado com sucesso!")

    cursor.close()
    conexao.close()

def put_aluno():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("UPDATE alunos SET nome=%s, idade=%s  WHERE ID_aluno=%s", (input("Altere o nome do aluno: "),int(input("Altere a idade do aluno: ")),int(input("ID do aluno: "))))
    conexao.commit()
    print("Aluno atualizado com sucesso!")

put_aluno()