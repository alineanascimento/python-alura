#1
pessoa = {"nome": "Aline", "idade": 30, "cidade": "Recife"}

#2
pessoa["idade"] = 31
pessoa["profissão"] = "Engenheira"
del pessoa["cidade"]

print(pessoa)

#2
numeros_quadrados = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
print(numeros_quadrados)

# ou resposta do curso:
numeros_quadrados = {x: x**2 for x in range(1, 6)}
print(numeros_quadrados)

#4
pessoa = {'nome': 'Amanda', 'idade': 19, 'cidade': 'São Luís'}
if 'nome'in pessoa:
    print("A chave 'nome' existe no dicionário.")
else:
    print("A chave 'nome' não existe no dicionário.")

#5
frase = "Python se tornou uma das linguagens de programação mais populares do mundo nos últimos anos."
contagem_palavras = {}  # Criando o dicionário
palavras = frase.split() # A função .split() separa o texto pelos espaços e cria uma lista
for palavra in palavras:
    contagem_palavras[palavra] = contagem_palavras.get(palavra, 0) + 1
"""O método .get() busca a palavra no dicionário.

Se não existir ainda, ele retorna 0 (em vez de dar erro).

Então:

Se a palavra já apareceu, soma mais 1.

Se é a primeira vez, começa com 0 e soma 1 → fica 1."""



print(contagem_palavras)