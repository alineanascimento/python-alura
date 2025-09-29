#lista
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
nomes = ["Aline", "Bruna", "Carlos", "Daniel", "Eduardo"]
anos = [1990, 1985, 2000, 1975, 1960]

#for
for numero in numeros:
    print(numero)
    
#3
numeros_impares = []
for numero in numeros:
    if numero % 2 != 0 and numero <=10:
        numeros_impares.append(numero)
print(numeros_impares)

#4
numeros_lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for numero in numeros_lista:
   lista_decrescente = sorted(numeros_lista, reverse=True)
print(lista_decrescente)

#5 
numero_usuario = int(input("Insira um número: "))
for i in range (1, 11):
    resultado =+ numero_usuario * i
    print(f"{numero_usuario} x {i} = {resultado}")
    
#6
lista_soma = [1, 2, 3, 4, 5, "a"]
soma = 0
try:
    soma = sum(lista_soma)
    print(soma)
    
except TypeError:
    print("A lista contém valores não numéricos.")
    


"""ver a atividade feita depois"""