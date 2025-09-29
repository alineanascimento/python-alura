#1

numero = int(input("Insira um número: "))
if numero % 2 == 0:
    print("O número é par")
else:
    print("O número é ímpar")
    
#2
idade = int(input("Insira sua idade: "))
if   0 <= idade < 12:
    print("Criança")
elif 13 <= idade < 18:
    print("Adolescente")
else:
    print("Adulto")

#3
nome_usuario = input("Insira seu nome de usuário: ")
senha_usuario = int(input("Insira sua senha: "))
if nome_usuario == "Aline" and senha_usuario == "1234":
    print("Acesso permitido")

#4
coordenadas = int(input("Insira a coordenada x: ")), int(input("Insira a coordenada y: "))
if coordenadas[0] > 0 and coordenadas[1] > 0:
    print("Primeiro quadrante")
elif coordenadas[0] < 0 and coordenadas[1] > 0:
    print("Segundo quadrante")
elif coordenadas[0] < 0 and coordenadas[1] < 0:
    print("Terceiro quadrante")
elif coordenadas[0] > 0 and coordenadas[1] < 0:
    print("Quarto quadrante")
else:
    print("Origem")
    
