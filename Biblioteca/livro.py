from conexao import conectar


def criar_livro(titulo, autor, ano_publicacao, editora):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Livros (titulo, autor, ano_publicacao, editora) VALUES (%s, %s, %s, %s)", (titulo, autor, ano_publicacao, editora))
    conn.commit()
    cursor.close()
    conn.close()

def listar_livros():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Livros")
    livros = cursor.fetchall()
    cursor.close()
    conn.close()
    return livros

def atualizar_livro(id, titulo, autor, ano_publicacao, editora):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("UPDATE Livros SET titulo = %s, autor = %s, ano_publicacao = %s, editora = %s WHERE id = %s", (titulo, autor, ano_publicacao, editora, id))
    conn.commit()
    cursor.close()
    conn.close()

def deletar_livro(id):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Livros WHERE id = %s", (id,))
    conn.commit()
    cursor.close()
    conn.close()

def buscar_livro_id(id):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Livros WHERE id = %s", (id,))
    livro = cursor.fetchone()
    cursor.close()
    conn.close()
    return livro    

print("Funções de CRUD para Livros definidas com sucesso.")