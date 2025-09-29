import os

restaurantes = ["Restaurante A", "Restaurante B", "Restaurante C"]

def exibir_nome_do_progrma():
    
    print("""
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░""")

    
def exibir_opcao():
   
    print("Finalizando o app...\n")
    print("1. Cadastrar restaurante")
    print("2. Listar restaurantes")
    print("3. Ativar restaurante")
    print("4. Sair\n")

def finalizar_app():
    os.system("cls")
    print("Finalizando o app...\n")

def opcao_invalida():
    
    print("Opção inválida!\n")
    input("Pressione qualquer tecla para voltar ao menu principal...")
    main()

def cadastrar_restaurante():
    os.system("cls") # Limpa a tela
    print("Cadastro de novos restaurantes\n")
    nome = input("Insira o nome do restaurante que deseja cadastrar: ")
    restaurantes.append(nome)
    print(f"O restaurante {nome} cadastrado com sucesso!\n")
    input("Pressione qualquer tecla para voltar ao menu principal...")
    main() # Volta ao menu principal

def listar_restaurantes():
    os.system("cls")
    print("Lista de restaurantes cadastrados:\n")
    for restaurante in restaurantes:
        print(f"- {restaurante}")
    print("\n")
    input("Pressione qualquer tecla para voltar ao menu principal...")
    main()
    

def escolher_opcoes():
    try:
        opcao_escolhida = int(input("Escolha uma opção: "))
        # print(f"Você escolheu a opção {opcao_escolhida}")

        if opcao_escolhida == 1:
            cadastrar_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            print("Ativar restaurante...")
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()
        

def main():
    os.system("cls")
    exibir_nome_do_progrma()
    exibir_opcao()
    escolher_opcoes()
    
if __name__ == "__main__":
    main()
    


