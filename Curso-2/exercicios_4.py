#1
class Carro:
    carros = []
    
    def __init__(self, modelo, cor, ano):
        self.modelo = modelo
        self.cor = cor
        self.ano = ano
        Carro.carros.append(self)
        
    def __str__(self):
        return f" {self.modelo} | {self.cor} | {self.ano}"
    
carro1 = Carro("honda", "azul", "2025")
carro2 = Carro("toyota", "branco", "2024")


#2
class Restaurante:
    restaurantes = []
    def __init__(self, nome, categoria, local, avaliacao):
        self.nome = nome
        self.categoria = categoria
        self.ativo = True
        self.local = local
        self.avaliacao = avaliacao
        Restaurante.restaurantes.append(self)
        
    def listar_restaurantes():
        for restaurante in Restaurante.restaurantes:
            print(f"{restaurante.nome} | {restaurante.categoria} | {restaurante.local} | {restaurante.avaliacao}")
            
            
restaurante1 = Restaurante("Aline", "Fast Food", "Recife", "5")

Restaurante.listar_restaurantes()

