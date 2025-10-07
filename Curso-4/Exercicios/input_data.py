nome = input("Digite seu nome:")
idade = input("Digite sua idade:")

'''with open ("input_data.txt","w") as f:    #troca sempre o conteudo
    f.write(f"Nome: {nome}\n")
    f.write(f"Idade: {idade}\n")'''

with open ("input_data.txt","a") as f: #adiciona o conteudo
    f.write(f"Nome: {nome}\n")
    f.write(f"Idade: {idade}\n")