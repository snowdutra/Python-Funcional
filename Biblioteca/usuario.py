from conexao import conectar

def criar_usuario(nome, email, telefone):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Usuarios (nome, email, telefone) VALUES (%s, %s, %s)", (nome, email, telefone))
    conn.commit()
    cursor.close()
    conn.close()

def listar_usuarios():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT u.id, u.nome, u.email, u.telefone, GROUP_CONCAT(l.titulo SEPARATOR ', ') AS livros
        FROM Usuarios u
        LEFT JOIN Emprestimos e ON u.id = e.usuario_id
        LEFT JOIN Livros l ON e.livro_id = l.id
        GROUP BY u.id
    """)
    usuarios = cursor.fetchall()
    cursor.close()
    conn.close()
    return usuarios

def atualizar_usuario(id, nome, email, telefone):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("UPDATE Usuarios SET nome = %s, email = %s, telefone = %s WHERE id = %s", (nome, email, telefone, id))
    conn.commit()
    cursor.close()
    conn.close()

def deletar_usuario(id):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Usuarios WHERE id = %s", (id,))
    conn.commit()
    cursor.close()
    conn.close()

def buscar_usuario_id(id):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Usuarios WHERE id = %s", (id,))
    usuario = cursor.fetchone()
    cursor.close()
    conn.close()
    return usuario

print("Funções de CRUD para Usuários definidas com sucesso.")
