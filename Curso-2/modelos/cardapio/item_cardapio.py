from abc import ABC, abstractmethod
#classe mãe
class ItemCardapio(ABC):
    
    def __init__(self, nome, preco):
        self._nome = nome
        self._preco = preco
        
    @abstractmethod
    def aplicar_desconto(self):
        pass
        
        
    