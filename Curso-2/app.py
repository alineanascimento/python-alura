from modelos.restaurantes import Restaurante


restaurante_praca = Restaurante("Praça", "Goumert")
restaurante_praca.receber_avaliacao("Aline", 10)
restaurante_praca.receber_avaliacao("Lais", 8)
restaurante_praca.receber_avaliacao("Bruna", 7)

def main():
    Restaurante.listar_restaurantes()


if __name__ == "__main__":
    main()