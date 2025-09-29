import os
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

def escolher_opcoes():
    opcao_escolhida = int(input("Escolha uma opção: "))
    # print(f"Você escolheu a opção {opcao_escolhida}")

    if opcao_escolhida == 1:
        print("Cadastrar restaurante...")
    elif opcao_escolhida == 2:
        print("Listar restaurantes...")
    elif opcao_escolhida == 3:
        print("Ativar restaurante...")
    else:
        finalizar_app()
# print(f"Você escolheu a opção {opcao_escolhida}")

# exercicio
"""
#1 
print("Python na Escola de Programação da Alura")
nome = "Aline"
idade = 20
mentira = "É mentira"
#2
print(f"Meu nome é {nome} e tenho {idade} anos. {mentira}.")
#3
print("A\nL\nU\nR\nA")
#4
pi = 3.14159
print(f"O valor arredondado de pi é: {pi:.2f}")"""


def main():
    exibir_nome_do_progrma()
    exibir_opcao()
    escolher_opcoes()
    
if __name__ == "__main__":
    main()