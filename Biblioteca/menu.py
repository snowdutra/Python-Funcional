from livro import criar_livro, listar_livros, atualizar_livro, deletar_livro, buscar_livro_id
from usuario import criar_usuario, listar_usuarios, atualizar_usuario, deletar_usuario, buscar_usuario_id
from emprestimo import criar_emprestimo, listar_emprestimos, atualizar_emprestimo, deletar_emprestimo, buscar_emprestimo_id

def menu():
    while True:
        print("\nGerenciamento de Biblioteca")
        print("1. Gerenciar Livros")
        print("2. Gerenciar Usuários")
        print("3. Gerenciar Empréstimos")
        print("4. Sair")
        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            menu_livros()
        elif escolha == '2':
            menu_usuarios()
        elif escolha == '3':
            menu_emprestimos()
        elif escolha == '4':
            print("Saindo...")
            break
        else:
            print("Opção inválida! Tente novamente.")

def menu_livros():
    while True:
        print("\nGerenciamento de Livros")
        print("1. Criar Livro")
        print("2. Listar Livros")
        print("3. Atualizar Livro")
        print("4. Deletar Livro")
        print("5. Voltar")
        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            titulo = input("Título: ")
            autor = input("Autor: ")
            ano = int(input("Ano de Publicação: "))
            editora = input("Editora: ")
            criar_livro(titulo, autor, ano, editora)
            print("Livro criado com sucesso!")
        
        elif escolha == '2':
            livros = listar_livros()
            for livro in livros:
                print(livro)
        
        elif escolha == '3':
            id = int(input("ID do Livro: "))
            titulo = input("Novo Título: ")
            autor = input("Novo Autor: ")
            ano = int(input("Novo Ano de Publicação: "))
            editora = input("Nova Editora: ")
            atualizar_livro(id, titulo, autor, ano, editora)
            print("Livro atualizado com sucesso!")
        
        elif escolha == '4':
            id = int(input("ID do Livro: "))
            deletar_livro(id)
            print("Livro deletado com sucesso!")
        
        elif escolha == '5':
            break
        else:
            print("Opção inválida! Tente novamente.")

def menu_usuarios():
    while True:
        print("\nGerenciamento de Usuários")
        print("1. Criar Usuário")
        print("2. Listar Usuários")
        print("3. Atualizar Usuário")
        print("4. Deletar Usuário")
        print("5. Voltar")
        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            nome = input("Nome: ")
            email = input("Email: ")
            telefone = input("Telefone: ")
            criar_usuario(nome, email, telefone)
            print("Usuário criado com sucesso!")
        
        elif escolha == '2':
            usuarios = listar_usuarios()
            for usuario in usuarios:
                print(usuario)
        
        elif escolha == '3':
            id = int(input("ID do Usuário: "))
            nome = input("Novo Nome: ")
            email = input("Novo Email: ")
            telefone = input("Novo Telefone: ")
            atualizar_usuario(id, nome, email, telefone)
            print("Usuário atualizado com sucesso!")
        
        elif escolha == '4':
            id = int(input("ID do Usuário: "))
            deletar_usuario(id)
            print("Usuário deletado com sucesso!")
        
        elif escolha == '5':
            break
        else:
            print("Opção inválida! Tente novamente.")

def menu_emprestimos():
    while True:
        print("\nGerenciamento de Empréstimos")
        print("1. Criar Empréstimo")
        print("2. Listar Empréstimos")
        print("3. Atualizar Empréstimo")
        print("4. Deletar Empréstimo")
        print("5. Voltar")
        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            livro_id = int(input("ID do Livro: "))
            usuario_id = int(input("ID do Usuário: "))
            data_emprestimo = input("Data de Empréstimo (AAAA-MM-DD): ")
            criar_emprestimo(livro_id, usuario_id, data_emprestimo)
            print("Empréstimo criado com sucesso!")
        
        elif escolha == '2':
            emprestimos = listar_emprestimos()
            for emprestimo in emprestimos:
                print(emprestimo)
        
        elif escolha == '3':
            id = int(input("ID do Empréstimo: "))
            data_devolucao = input("Data de Devolução (AAAA-MM-DD): ")
            atualizar_emprestimo(id, data_devolucao)
            print("Empréstimo atualizado com sucesso!")
        
        elif escolha == '4':
            id = int(input("ID do Empréstimo: "))
            deletar_emprestimo(id)
            print("Empréstimo deletado com sucesso!")
        
        elif escolha == '5':
            break
        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    menu()
