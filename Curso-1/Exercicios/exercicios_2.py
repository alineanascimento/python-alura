#1
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
nomes = ["Aline", "Bruna", "Carlos", "Daniel", "Eduardo"]
anos = [1990, 1985, 2000, 1975, 1960]

#2
for numero in numeros:
    print(numero)
    
#3
soma_impares = 0
for i in range(1, 11, 2):
    soma_impares += i
print(soma_impares)

#4
numeros_lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for numero in numeros_lista:
   lista_decrescente = sorted(numeros_lista, reverse=True)
print(lista_decrescente)
# ou resposta da lisa:
for i in range(10, 0, -1):
    print(i)

#5 
numero_tabuada = int(input("Digite um número para a tabuada: "))
for i in range(1, 11):
    resultado = numero_tabuada * i
    print(f"{numero_tabuada} x {i} = {resultado}")



#6
lista_soma = [1, 2, 3, 4, 5, "a"]
soma = 0
try:
    for numero in lista_soma:
        soma += numero
        print(f"Soma dos elementos: {soma}")
    
except Exception as e:
    print("A lista contém valores não numéricos.")
    

#7
lista_valores = []
soma_valores = 0

try:
    for valor in lista_valores:
        soma_valores += valor

    media = soma_valores / len(lista_valores)
    print(f"Média dos valores: {media}")
except ZeroDivisionError:
    print("A lista está vazia, não é possível calcular a média.")
except Exception as e:
    print(f"Ocorreu um erro: {e}")
