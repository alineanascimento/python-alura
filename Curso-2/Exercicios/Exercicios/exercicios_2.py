class Musica:
    nome = ""
    artista = ""
    duracao = 0
musica1 = Musica()  
musica1.nome = "Imagine"
musica1.artista = "John Lennon"
musica1.duracao = 183
print(musica1.nome)
print(musica1.artista)
print(musica1.duracao) 


class Restaurante:
    restaurantes = []
    
    def __init__(self, nome, categoria):
        self.nome = nome
        self.categoria = categoria
        self.ativo = False
        
    def __str__(self):
        return f"{self.nome} | {self.categoria}"
    
restaurante_praca = Restaurante("Praça", "Gourmet")
restaurante_pizza = Restaurante("Pizza Place", "Fast Food")

restaurantes = [restaurante_praca, restaurante_pizza]

print(restaurante_praca)
print(restaurante_pizza)