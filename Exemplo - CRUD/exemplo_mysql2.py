import mysql.connector


conn = mysql.connector.connect(host='localhost', 
                               database='Sakila', 
                               user='root',
                               password='root',
                               port = '700')

print("Contectado ao banco de dados MySQL")

cursor= conn.cursor()
sql = "INSERT INTO contatos (nome, telefone) VALUES (%s, %s)"
cursor.execute(sql, ('João', '1234-5678'))
cursor.execute(sql, ('Maria', '9999-8888'))
cursor.execute(sql, ('Pedro', '7777-6666'))

conn.commit()
print("Registros inseridos com sucesso.")

sql = 'update contatos set telefone = %s where id = %s'
cursor.execute(sql, ('9999-9999', 2))
conn.commit()
print("Registro atualizado com sucesso.")

sql = 'delete from contatos where id = %s'
cursor.execute(sql, (3,))
conn.commit()
print("Registro deletado com sucesso.")


sql = 'select * from contatos'
cursor.execute(sql)

for linha in cursor.fetchall():
    print(linha)

conn.close()
