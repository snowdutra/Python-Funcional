from conexao import conectar


def criar_banco():
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Paciente (
        id INT AUTO_INCREMENT PRIMARY KEY,
        nome VARCHAR(255) NOT NULL,
        sobrenome VARCHAR(255) NOT NULL
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Vacina (
        id INT AUTO_INCREMENT PRIMARY KEY,
        paciente_id INT,
        nome_vacina VARCHAR(255) NOT NULL,
        data_dose DATE,
        numero_dose INT,
        tipo_vacina VARCHAR(255),
        FOREIGN KEY (paciente_id) REFERENCES Paciente(id)
    )
    ''')

    conn.commit()
    cursor.close()
    conn.close()


if __name__ == "__main__":
    criar_banco()

    print("Banco de dados e tabelas criados com sucesso.")
