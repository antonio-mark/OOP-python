# 4
class Musica:
    def __init__(self, id, nome_musica, artista_banda, genero, ano, duracao):
        self.id = id 
        self.nome_musica = nome_musica   
        self.artista_banda = artista_banda
        self.genero = genero
        self.ano = ano
        self.duracao = duracao

    def mostrarBaseDeDados():   
        musica1 = Musica(0, 'Fa fe fi fo Funk', 'Anira', 'Funk', 2019, '3:05')
        musica2 = Musica(1, 'Sofrência de programar', 'Ada & Turing', 'Sertanejo', 1998, '2:58')
        musica3 = Musica(2, 'Rock’n Rolo', 'The Buns', 'Rock', 1984, '4:01')
        musica4 = Musica(3, 'Grifinoria Girls', 'Katy Potter', 'Pop', 2017, '2:25')
        return [musica1, musica2, musica3, musica4]
    
    def mostrarParametros(self):
        print()
        print(self.id)
        print(self.nome_musica)
        print(self.artista_banda)
        print(self.genero)
        print(self.ano)
        print(self.duracao)
        print("\n")




