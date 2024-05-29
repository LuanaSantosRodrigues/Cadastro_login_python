from sistema import SistemaCadastroLogin

def main():
    sistema = SistemaCadastroLogin('mongodb://localhost:27017/', 'sistema_cadastro_login')
    
    while True:
        print("\n1. Cadastrar")
        print("\n2. Login")
        print("\n3. Sair")
        choice = input("Escolha uma opção: ")

        if choice == "1":
            nome = input("Digite o nome: ")
            telefone = input("Digite o telefone: ")
            cpf = input("Digite o CPF: ")
            email = input("Digite o e-mail: ")
            nome_social = input("Digite o nome social: ")
            cep = input("Digite o CEP: ")
            numero_residencia = input("Digite o número da residência: ")
            senha = input("Digite uma senha de 6 dígitos: ")

            print(sistema.cadastrar_usuario(nome, telefone, cpf, email, nome_social, cep, numero_residencia, senha))
        
        elif choice == "2":
            email = input("Digite o e-mail: ")
            senha = input("Digite a senha de 6 dígitos: ")
            print(sistema.login_usuario(email, senha))
        
        elif choice == "3":
            break
        
        else:
            print("Opção inválida, tente novamente.")

if __name__ == "__main__":
    main()
