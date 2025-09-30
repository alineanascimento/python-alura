from modelos.avaliacao import Avaliacao

class Restaurante:
    restaurantes = []
    
    def __init__(self, nome, categoria):
        self._nome = nome.title() #comecar com a letra maiscula usa-se title
        self._categoria = categoria.upper() # tudo com letra maiscula
        self._ativo = False # significa que o atributo é privado
        self._avaliacao = []
        Restaurante.restaurantes.append(self)
        
    # ao selecionar um nome e apertar f2 vc muda o nome
    def __str__(self):
        return f"{self._nome} | {self._categoria}"
    
    @classmethod
    def listar_restaurantes(cls):
        print(f"{"Nome do Restaurante".ljust(25)} | {"Categoria".ljust(25)} | {"Avaliação".ljust(25)} | {"Status"}")
        for restaurante in cls.restaurantes:
            print(f"{restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(25)} | {str(restaurante.media_avaliacao).ljust(25)} | {restaurante.ativo}")
    
    # _ significa que o atributo não pode ser mexido, só pela propriedade
    @property # modificar como aquilo vai ser lido
    def ativo(self):
        return "❌" if self._ativo else "✔️"
    
    #metodo de objeto
    def alternar_estado(self):
        self._ativo = not self._ativo
    
    
    def receber_avaliacao(self, cliente, nota):
        if 0 < nota <= 5:
            avaliacao = Avaliacao(cliente, nota)
            self._avaliacao.append(avaliacao)
        
        
    @property
    def media_avaliacao(self):
        if not self._avaliacao:
            return "-"
        soma_das_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)
        quantidade_de_notas = len(self._avaliacao)
        media = round(soma_das_notas / quantidade_de_notas, 1)
        return media
    
