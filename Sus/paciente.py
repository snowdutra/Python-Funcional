from conexao import conectar

def criar_paciente(nome, sobrenome):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO Paciente (nome, sobrenome) VALUES (%s, %s)",
        (nome, sobrenome)
    )
    conn.commit()
    cursor.close()
    conn.close()

def listar_pacientes():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Paciente")
    pacientes = cursor.fetchall()
    cursor.close()
    conn.close()
    return pacientes

def atualizar_paciente(id, nome, sobrenome):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE Paciente SET nome = %s, sobrenome = %s WHERE id = %s",
        (nome, sobrenome, id)
    )
    conn.commit()
    cursor.close()
    conn.close()

def deletar_paciente(id):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Paciente WHERE id = %s", (id,))
    conn.commit()
    cursor.close()
    conn.close()

def buscar_paciente_id(id):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Paciente WHERE id = %s", (id,))
    paciente = cursor.fetchone()
    cursor.close()
    conn.close()
    return paciente

print("Funções de CRUD para Pacientes definidas com sucesso.")

