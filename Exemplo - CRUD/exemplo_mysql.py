import mysql.connector


conn = mysql.connector.connect(host='localhost', 
                               database='Sakila', 
                               user='root',
                               password='root',
                               port = '700')

print("Contectado ao banco de dados MySQL")

tabela_contatos = """
CREATE TABLE contatos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    telefone VARCHAR(20) NOT NULL
)
"""

tabela_emails= """
CREATE TABLE emails (
    id INT AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(100) NOT NULL,
    contato_id INT
)
"""

cursor= conn.cursor()
cursor.execute(tabela_contatos)
print("Tabela contatos criada com sucesso.")
cursor.execute(tabela_emails)
print("Tabela emails criada com sucesso.")

conn.close()
print("Conexão fechada.")