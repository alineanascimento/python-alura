import os

restaurantes = [
    {"nome": "Restaurante A", "categoria": "Japonesa", "ativo": True},
    {"nome": "Restaurante B", "categoria": "Italiana", "ativo": False},
    {"nome": "Restaurante C", "categoria": "Regional", "ativo": False}
]

def exibir_nome_do_progrma():
    
    print("""
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝""")

def exibir_opcao():
   
    print("1. Cadastrar restaurante")
    print("2. Listar restaurantes")
    print("3. Alternar status do restaurante")
    print("4. Sair\n")

def finalizar_app():
    exibir_subtitulo("Finalizando o app...")
    
def voltar_ao_menu_principal():
    input("Pressione qualquer tecla para voltar ao menu principal...")
    main() # Volta ao menu principal
    
def opcao_invalida():
    
    print("Opção inválida!\n")
    voltar_ao_menu_principal()

def exibir_subtitulo(texto):
    os.system("cls")
    linha = "*" * len(texto)
    print(linha)
    print(texto)
    print(linha)
    print()
    
def cadastrar_restaurante():
    """Essa função é responsável por cadastrar novos restaurantes
    Inputs:
    - Nome do restaurante
    - Categoria do restaurante
    
    Outputs:
    - Adiciona um novo restaurante na lista de restaurantes"""
    exibir_subtitulo("Cadastro de novos restaurantes")
    nome = input("Insira o nome do restaurante que deseja cadastrar: ")
    categoria = input("Insira a categoria do restaurante: ")
    dados_restaurante = {"nome": nome, "categoria": categoria, "ativo": False}
    restaurantes.append(dados_restaurante)
    
    print(f"O restaurante {nome} cadastrado com sucesso!\n")
    voltar_ao_menu_principal()

def listar_restaurantes():
    exibir_subtitulo("Lista de restaurantes cadastrados")
    
    print(f"{'Nome'.ljust(22)} | {'Categoria'.ljust(20)} | Status")
    
    for restaurante in restaurantes:
        nome_restaurante = restaurante["nome"]
        categoria_restaurante = restaurante["categoria"]
        ativo = "ativado" if restaurante["ativo"] else "desativado"
           
        print(f"- {nome_restaurante.ljust(20)} | {categoria_restaurante.ljust(20)} | {ativo}")
            
        
    voltar_ao_menu_principal()
  
def alterar_status_restaurante():
    exibir_subtitulo("Alterar status do restaurante")
    nome = input("Insira o nome do restaurante que deseja alterar o status: ")
    restaurante_encontrado = False
    for restaurante in restaurantes:
        if restaurante["nome"].lower() == nome.lower():
            restaurante_encontrado = True
            restaurante["ativo"] = not restaurante["ativo"] # Alterna o status
            mensagem_status = f"O restaurante {nome} foi ativado com scesso" if restaurante["ativo"] else f"O restaurante {nome} foi desativado com sucesso"
            print(mensagem_status)
    if not restaurante_encontrado:
        print(f"O restaurante {nome} não foi encontrado")
    voltar_ao_menu_principal()   
    
def escolher_opcoes():
    try:
        opcao_escolhida = int(input("Escolha uma opção: "))
        # print(f"Você escolheu a opção {opcao_escolhida}")

        if opcao_escolhida == 1:
            cadastrar_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            alterar_status_restaurante()
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
    


