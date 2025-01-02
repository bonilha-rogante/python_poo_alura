class Musica:
    musicas = []
    def __init__(self, nome, artista, duracao):
        self.nome = nome
        self.artista = artista
        self.duracao = duracao
        Musica.musicas.append(self)
        
    def __str__(self):
        return f'{self.nome} | {self.artista} | {self.duracao}'
    
    def listar_musicas():
        for musica in Musica.musicas:
            print(f'{musica.artista} | {musica.nome} | {musica.duracao}')
        
musica_1 = Musica('Blind', 'Korn', 257)
musica_2 = Musica('Rajda', 'Yago', 265)
musica_3 = Musica('Count Me out', 'Kendrick', 207)

# # musica.nome = 'blind'
# # musica.artista = 'Korn'
# # musica.duracao = 257
print(musica_1)
print(musica_2)
print(musica_3)
Musica.listar_musicas()