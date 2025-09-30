class Restaurante:
    restaurantes = []
    
    def __init__(self, nome, categoria):
        self._nome = nome.title() #comecar com a letra maiscula usa-se title
        self._categoria = categoria.upper() # tudo com letra maiscula
        self._ativo = False # significa que o atributo é privado
        Restaurante.restaurantes.append(self)
    # ao selecionar um nome e apertar f2 vc muda o nome
    def __str__(self):
        return f"{self._nome} | {self.categoria}"
    
    @classmethod
    def listar_restaurantes(cls):
        print(f"{"Nome do Restaurante".ljust(25)} | {"Categoria".ljust(25)} | {"Status"}")
        for restaurante in cls.restaurantes:
            print(f"{restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(25)} | {restaurante._ativo}")
    
    # _ significa que o atributo não pode ser mexido, só pela propriedade
    @property # modificar como aquilo vai ser lido
    def ativo(self):
        return "❌" if self._ativo else "✔️"
    
    #metodo de objeto
    def alternar_estado(self):
        self._ativo = not self._ativo
    
    
restaurante_praca = Restaurante("praça", "Gourmet")
restaurante_praca._nome = "Praça 2.0"
restaurante_praca.alternar_estado()
restaurante_pizza = Restaurante("Pizza Place", "Fast Food")

Restaurante.listar_restaurantes()