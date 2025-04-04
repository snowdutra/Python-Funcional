import paciente as pa
import vacina as va

def menu():
    while True:
        print("1. Cadastro de Paciente")
        print("2. Cadastro de Vacina")
        print("3. Sair")
        escolha = input("Escolha uma opção: ")

        if escolha == '1': 
            menu_paciente()
        elif escolha == '2':
            menu_vacina()
        elif escolha == '3':
            print("Saindo...")
            break   
        else:
            print("Opção inválida. Tente novamente.")

def menu_paciente():
    while True:
        print("1. Criar Paciente")
        print("2. Listar Paciente")
        print("3. Atualizar Paciente")
        print("4. Deletar Paciente")
        print("5. Voltar")
        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            nome = input("Nome: ")
            sobrenome = input("Sobrenome: ")
            pa.criar_paciente(nome, sobrenome)
            print("Paciente criado com sucesso!")
        
        elif escolha == '2':
            pacientes = pa.listar_pacientes()
            for paciente in pacientes:
                print(paciente)
        
        elif escolha == '3':
            id = int(input("ID do Paciente: "))
            nome = input("Novo Nome: ")
            sobrenome = input("Novo Sobrenome: ")
            pa.atualizar_paciente(id, nome, sobrenome)
            print("Paciente atualizado com sucesso!")
        
        elif escolha == '4':
            id = int(input("ID do Paciente: "))
            pa.deletar_paciente(id)
            print("Paciente deletado com sucesso!")

        elif escolha == '5':
            break
        
        else:
            print("Opção inválida. Tente novamente.")

def menu_vacina():
    while True:
        print("1. Criar Vacina")
        print("2. Listar Vacina")
        print("3. Atualizar Vacina")
        print("4. Deletar Vacina")
        print("5. Voltar")
        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            paciente_id = int(input("ID do Paciente: "))
            nome_vacina = input("Nome da Vacina: ")
            data_dose = input("Data da Dose (AAAA-MM-DD): ")
            numero_dose = int(input("Número da Dose: "))
            tipo_vacina = input("Tipo de Vacina: ")
            va.criar_vacina(paciente_id, nome_vacina, data_dose, numero_dose, tipo_vacina)
            print("Vacina criada com sucesso!")
        
        elif escolha == '2':
            vacinas = va.listar_vacinas()
            for vacina in vacinas:
                print(vacina)
        
        elif escolha == '3':
            id = int(input("ID da Vacina: "))
            paciente_id = int(input("ID do Paciente: "))
            nome_vacina = input("Novo Nome da Vacina: ")
            data_dose = input("Nova Data da Dose (AAAA-MM-DD): ")
            numero_dose = int(input("Novo Número da Dose: "))
            tipo_vacina = input("Novo Tipo de Vacina: ")
            va.atualizar_vacina(id, paciente_id, nome_vacina, data_dose, numero_dose, tipo_vacina)
            print("Vacina atualizada com sucesso!")

        elif escolha == '4':
            id = int(input("ID da Vacina: "))
            va.deletar_vacina(id)
            print("Vacina deletada com sucesso!")

        elif escolha == '5':
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()

