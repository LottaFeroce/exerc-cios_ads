import mysql.connector
conexao = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = ""
)

#verify
if conexao.is_connected():
    print("\nConexão efetuada com exito")

#conexao.cursor().execute()
cursor = conexao.cursor()
cursor.execute("CREATE DATABASE IF NOT EXISTS aula_connect")

conexao.database = "aula_connect"

'''cursor.execute("Show databases")
show databases
for banco in cursor.fetchall():
    print(banco)'''

cursor.execute(
        '''CREATE TABLE IF NOT EXISTS alunos(
        ID_aluno int primary key auto_increment,
        nome varchar(100) not null,
        idade int)'''
    )
#Insert
sql = "INSERT INTO alunos(nome,idade) VALUES (%s, %s)"
values = ("Hokma", 60)
cursor.execute(sql, values)
#commit para enviar ao banco
conexao.commit()

#sql_update = "UPDATE alunos set idade =%s where nome = %s" 
sql_update = "UPDATE `aula_connect`.`alunos` SET `nome` = 'cleb' WHERE (`ID_aluno` = '1');"
cursor.execute(sql_update)
conexao.commit()

cursor.execute("SELECT * FROM alunos")
results = cursor.fetchall()
for linha in results:
    print(linha)

'''sql_del = "delete from alunos where id=%s"
valores_del = (1,)
cursor.execute(sql_del, valores_del)
conexao.commit()
'''
sql_delete = "DELETE FROM aula_connect.alunos WHERE ID_aluno IN (%s, %s)"
cursor.execute(sql_delete, (2, 3))
conexao.commit()

#close
cursor.close()
conexao.close()