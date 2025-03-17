from conexao import conectar

def criar_emprestimo(livro_id, usuario_id, data_emprestimo, data_devolucao=None):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Emprestimos (livro_id, usuario_id, data_emprestimo, data_devolucao) VALUES (%s, %s, %s, %s)", (livro_id, usuario_id, data_emprestimo, data_devolucao))
    conn.commit()
    cursor.close()
    conn.close()

def listar_emprestimos():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Emprestimos")
    emprestimos = cursor.fetchall()
    cursor.close()
    conn.close()
    return emprestimos

def atualizar_emprestimo(id, data_devolucao):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("UPDATE Emprestimos SET data_devolucao = %s WHERE id = %s", (data_devolucao, id))
    conn.commit()
    cursor.close()
    conn.close()

def deletar_emprestimo(id):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Emprestimos WHERE id = %s", (id,))
    conn.commit()
    cursor.close()
    conn.close()

def buscar_emprestimo_id(id):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Emprestimos WHERE id = %s", (id,))
    emprestimo = cursor.fetchone()
    cursor.close()
    conn.close()
    return emprestimo

print("Funções de CRUD para Empréstimos definidas com sucesso.")