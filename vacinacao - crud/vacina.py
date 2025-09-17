from conexao import conectar

def criar_vacina(paciente_id, nome_vacina, data_dose, numero_dose, tipo_vacina):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Vacina (paciente_id, nome_vacina, data_dose, numero_dose, tipo_vacina) VALUES (%s, %s, %s, %s, %s)", 
                   (paciente_id, nome_vacina, data_dose, numero_dose, tipo_vacina))
    conn.commit()
    cursor.close()
    conn.close()

def listar_vacinas():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Vacina")
    vacinas = cursor.fetchall()
    cursor.close()
    conn.close()
    return vacinas

def atualizar_vacina(id, paciente_id, nome_vacina, data_dose, numero_dose, tipo_vacina):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("UPDATE Vacina SET paciente_id = %s, nome_vacina = %s, data_dose = %s, numero_dose = %s, tipo_vacina = %s WHERE id = %s", 
                   (paciente_id, nome_vacina, data_dose, numero_dose, tipo_vacina, id))
    conn.commit()
    cursor.close()
    conn.close()

def deletar_vacina(id):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Vacina WHERE id = %s", (id,))
    conn.commit()
    cursor.close()
    conn.close()

def buscar_vacina_id(id):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Vacina WHERE id = %s", (id,))
    vacina = cursor.fetchone()
    cursor.close()
    conn.close()
    return vacina

print("Funções de CRUD para Vacinas definidas com sucesso.")
