class Musica:
    musicas = []
    
    def __init__(self, nome , artista, duracao):
        self.nome = nome
        self.artista = artista
        self.duracao = duracao
        Musica.musicas.append(self)
        
    def __str__(self):
        return f"{self.nome} | {self.artista} | {self.duracao} segundos"
    
    def listar_musicas():
        for musica in Musica.musicas:
            print(f"{musica.nome} | {musica.artista} | {musica.duracao} segundos")
        
        
musica1 = Musica("Imagine", "John Lennon", 183)
musica2 = Musica("Billie Jean", "Michael Jackson", 294)
musica3 = Musica("Like a Prayer", "Madonna", 342)


Musica.listar_musicas()