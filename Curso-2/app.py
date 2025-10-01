from modelos.restaurantes import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato


restaurante_praca = Restaurante("Praça", "Goumert")
bebida_suco = Bebida("Suco de Melancia", 5.0, "grande")
prato_paozinho = Prato("Paozinho", 2.00, "O melhor pão da cidade")
restaurante_praca.adicionar_no_cardapio(bebida_suco)
restaurante_praca.adicionar_no_cardapio(prato_paozinho)


def main():
    pass


if __name__ == "__main__":
    print(bebida_suco)
    print(prato_paozinho)