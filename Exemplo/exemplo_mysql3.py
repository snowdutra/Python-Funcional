import mysql.connector


conn = mysql.connector.connect(host='localhost', 
                               database='Sakila', 
                               user='root',
                               password='root',
                               port = '700')

print("Contectado ao banco de dados MySQL")

cursor= conn.cursor()
contato_id = input("Digite o ID do contato: ")
email = input("Digite o email: ")
sql = "INSERT INTO emails (contato_id, email) VALUES (%s, %s)"
cursor.execute(sql, (contato_id, email))

conn.commit()
print("Registro inserido com sucesso.")

conn.close()

