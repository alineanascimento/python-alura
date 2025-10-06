# escrever um arquivo com a funcao open()

with open("dados.txt", "w") as f:  # criar um arquivo com o nome dados
    f.write("Olá mundo")


with open("dados.txt", "r") as f: # ler o conteudo escrito
    conteudo = f.read()


print(conteudo)

with open ("dados.txt", "a") as f:
    f.write("\nultima linha")

#tipos de arquivos
""" .txt -> simples, para salvar o log de registros, consome pouco espaco
.csv -> dados
.json -> dicionarios, requisicoes, facil conversao
"""

#csv
import csv
with open("dados.csv", "w") as f:
    escritor = csv.writer(f)
    escritor.writerow(["nome", "idade"])
    escritor.writerow(["Ana", "32"])

with open ("dadox.csv", newline = "") as f:
    leitor = csv.reader(f)
    for linha in leitor:
        print(linha)


#json
import json 
dados = {"nome": "ana", "idade": 20, "enderecos":["a", "b"]}
with open ("dados.json", "w") as f:
    json.dump(dados, f)


with open("dados.json", "r") as f:
    dados_lidos = json.load(f)
    print(dados_lidos)
"""
limitacoes ddo uso de arquivos
-falta de estrutura relacional
-dificuldade de busca
-concorrência 
-falta de seguranca e integridade
-escalabilidade

"""

