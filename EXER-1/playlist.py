# 4
from musica import Musica
import random 

musicas = Musica.mostrarBaseDeDados()

class Playlist():
    def __init__(self):
        self.lista_musicas = []
 
    def montarPlaylist(self):
        parar_de_adicionar = False
        while not parar_de_adicionar:
            id_musica = int(input('Digite o id da musica: '))
            ja_existe = False
            for musica in self.lista_musicas:
                if musica.id == id_musica:
                    print('Musica já esta na playlist')
                    ja_existe = True
                    break
            if not ja_existe and id_musica < len(musicas):
                self.lista_musicas.append(musicas[id_musica])
            opcao = ''
            while opcao != 'S' and opcao != 'N':
                opcao = input('Deseja adicionar mais musicas? (S/N)').upper()
                if opcao == 'N': 
                    parar_de_adicionar = True

    def visualizarPlaylist(self):
        for musica in self.lista_musicas:
            Musica.mostrarParametros(musica)

    def embaralharPlaylist(self):
        random.shuffle(self.lista_musicas)

    def exibirDuracaoPlaylist(self):
        duracao = 0
        for musica in self.lista_musicas:
           duracao += float(musica.duracao.replace(":", "."))
    
        [min, seg] = str(duracao).split('.')
        print("A playlist tem {} minutos e {} segundos".format(min, seg))

    def consultarMusica(self):
        nome_musica = input('Digite o título da musica: ')
        for musica in self.lista_musicas:
            print(musica.id) if nome_musica in musica.nome_musica else print('Não tem essa música na playlist')
                



playlist = Playlist()

playlist.montarPlaylist()
# playlist.visualizarPlaylist()
# playlist.embaralharPlaylist()
# playlist.visualizarPlaylist()
# playlist.exibirDuracaoPlaylist()
# playlist.consultarMusica()