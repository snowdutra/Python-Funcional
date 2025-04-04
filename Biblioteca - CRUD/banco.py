from conexao import conectar

def criar_banco():
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Livros (
        id INT AUTO_INCREMENT PRIMARY KEY,
        titulo VARCHAR(255) NOT NULL,
        autor VARCHAR(255) NOT NULL,
        ano_publicacao INT,
        editora VARCHAR(255)
    )''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Usuarios (
        id INT AUTO_INCREMENT PRIMARY KEY,
        nome VARCHAR(255) NOT NULL,
        email VARCHAR(255) NOT NULL,
        telefone VARCHAR(50)
    )''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Emprestimos (
        id INT AUTO_INCREMENT PRIMARY KEY,
        livro_id INT,
        usuario_id INT,
        data_emprestimo DATE,
        data_devolucao DATE,
        FOREIGN KEY (livro_id) REFERENCES Livros(id),
        FOREIGN KEY (usuario_id) REFERENCES Usuarios(id)
    )''')

    conn.commit()
    cursor.close()
    conn.close()
    print("Banco de dados e tabelas criados com sucesso.")

if __name__ == "__main__":
    criar_banco()

    print("Banco de dados e tabelas criados com sucesso.")