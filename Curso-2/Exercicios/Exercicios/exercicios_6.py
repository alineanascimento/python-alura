class Livro:

    def __init__(self, titulo, autor, ano):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
        self.disponivel = True

    def __str__(self):
        return f"{self.titulo} | {self.autor} | {self.ano}"
    
    def emprestar(self):
        self.disponivel = False

    @staticmethod
    def verificar_disponibilidade(ano):
        livros_disponiveis = [livro for livro in Livro.livros if livro.ano == ano and livro.disponivel]
        return livros_disponiveis


livro1 = Livro("Aprendendo python", "Aline", "2000")
livro2 = Livro("\nAprendendo oo", "Aline", "2001")
print(livro1, livro2)

livro3 = Livro("Python Cookbook", "Samuel Developer", 2019)
print(f"Antes de emprestar: Livro disponível? {livro3.disponivel}")
livro3.emprestar()
print(f"Depois de emprestar: Livro disponível? {livro3.disponivel}")

Livro.livros = [livro1, livro2, livro3]  # Adicionando os livros à lista de livros
