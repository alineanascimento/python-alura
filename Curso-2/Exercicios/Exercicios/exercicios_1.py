#1
class Restaurante:
    nome = ""
    categoria = ""
    ativo = False
    
    
restaurante_praca = Restaurante()
restaurante_praca.nome = "Restaurante da Praça"
restaurante_praca.categoria = "Italiana"
#2
print(restaurante_praca.nome)
#3
if restaurante_praca.ativo:
    print("O restaurante está ativo.")
else:
    print("O restaurante está inativo.")
    
#4
categoria = restaurante_praca.categoria
print(f"A categoria do restaurante é: {categoria}")
#5
restaurante_praca.nome = "Bistrô"
print(restaurante_praca.nome)
#6
restaurante_pizza = Restaurante()
restaurante_pizza.nome = "Pizza Place"
restaurante_pizza.categoria = "Fast Food"
#7
if restaurante_pizza.categoria == "Fast Food":
    print("O restaurante é de Fast Food.")
else:
    print("O restaurante não é de Fast Food.")
#8
restaurante_pizza.ativo = True
if restaurante_pizza.ativo:
    print("O restaurante está ativo.")
else:
    print("O restaurante está inativo.")
#9
print(f"Nome: {restaurante_praca.nome}, Categoria: {restaurante_praca.categoria}, Ativo: {restaurante_praca.ativo}")