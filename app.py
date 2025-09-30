import os

restaurantes = [
    {"nome": "Restaurante A", "categoria": "Japonesa", "ativo": True},
    {"nome": "Restaurante B", "categoria": "Italiana", "ativo": False},
    {"nome": "Restaurante C", "categoria": "Regional", "ativo": False}
]

def exibir_nome_do_progrma():
    """Essa função exibe o nome do programa
    Inputs: Nenhum
    Outputs: Nome do programa exibido no console"""
    print("""
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝""")

def exibir_opcao():
    """Essa função exibe as opções do menu principal
    Inputs: Nenhum
    Outputs: Opções exibidas no console"""
    print("1. Cadastrar restaurante")
    print("2. Listar restaurantes")
    print("3. Alternar status do restaurante")
    print("4. Sair\n")

def finalizar_app():
    """Essa função finaliza o app
    Inputs: Nenhum
    Outputs: Mensagem de finalização exibida no console"""
    exibir_subtitulo("Finalizando o app...")
    
def voltar_ao_menu_principal():
    """Essa função volta ao menu principal
    Inputs: Nenhum
    Outputs: Menu principal exibido no console"""
    input("Pressione qualquer tecla para voltar ao menu principal...")
    main() # Volta ao menu principal
    
def opcao_invalida():
    """Essa função exibe uma mensagem de opção inválida
    Inputs: Nenhum
    Outputs: Mensagem de opção inválida exibida no console"""
    print("Opção inválida!\n")
    voltar_ao_menu_principal()

def exibir_subtitulo(texto):
    """Essa função exibe um subtítulo formatado
    Inputs:
    - texto: string com o texto do subtítulo
    Outputs:
    - Subtítulo exibido no console"""
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
    """Essa função lista os restaurantes cadastrados
    Inputs: Nenhum
    Outputs: Lista de restaurantes exibida no console"""
    exibir_subtitulo("Lista de restaurantes cadastrados")
    
    print(f"{'Nome'.ljust(22)} | {'Categoria'.ljust(20)} | Status")
    
    for restaurante in restaurantes:
        nome_restaurante = restaurante["nome"]
        categoria_restaurante = restaurante["categoria"]
        ativo = "ativado" if restaurante["ativo"] else "desativado"
           
        print(f"- {nome_restaurante.ljust(20)} | {categoria_restaurante.ljust(20)} | {ativo}")
            
        
    voltar_ao_menu_principal()
  
def alterar_status_restaurante():
    """Essa função altera o status de um restaurante (ativo/inativo)
    Inputs:
    - Nome do restaurante
    Outputs:
    - Mensagem de sucesso ou erro exibida no console"""
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
    """Essa função escolhe a opção do menu principal
    Inputs: Nenhum
    Outputs: Chama a função correspondente à opção escolhida"""
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
    """Função principal do programa
    Inputs: Nenhum
    Outputs: Exibe o menu principal e chama a função para escolher opções"""
    os.system("cls")
    exibir_nome_do_progrma()
    exibir_opcao()
    escolher_opcoes()
    
if __name__ == "__main__":
    main()
    


