# não ordenado, mutável, chave:valor


telefones = {"joao": 131313131, "aline": 99219848}


print(telefones)

print(telefones["aline"]) # vc passa a chave


#adicionar no dicionario
telefones["helena"] = 977266738 # coloca a chave e adiciona

print(telefones)

filmes_dict = {}

filmes = ["star wars", "harry potter"]

datas = ["01/02", "09/10"]

filmes_dict[filmes[0]]= datas[0] #populando o dicionario
filmes_dict[filmes[1]]= datas[1] #populando o dicionario

print(filmes_dict)

tupla = (1, 2, 3)
#técnicas de iteração
for i in filmes: # vai imprimir tudo da lista
    print(i)

for i in tupla: # vai imprimir tudo da tupla
    print(i)

for k, i in filmes_dict.items():
    print(k, i)
