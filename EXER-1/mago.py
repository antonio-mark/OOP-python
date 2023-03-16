# 1 e 2 
class Mago:
    def __init__(self, nome, idade, escola, tipo, magia):
        self.nome = nome 
        self.idade = idade   
        self.escola = escola
        self.tipo = tipo
        self.magia = magia 
        
    def andar(self):
        print('Estou andando')
    
    def falar(self):
        print('Ola amigue! Meu nome é', self.nome)
        
    def invocarMagia(self):
        print('Invocando magia!')

    def falarMagia(self):
        print('Minha magia atual é', self.magia)

    def trocarMagia(self, magia):
        self.magia = magia
        print("Magia trocada!")
    
    
hp = Mago('Harry Potter', 17, 'Hogwarts', 'Humano', 'Accio')
mdg = Mago('Mestre dos magos', 500, 'Caverna do dragão', 'Humano', 'Desaparecimento')
ahri = Mago('Ahri', 25, 'LOL', 'Raposa', 'Charme')

hp.falarMagia()
hp.trocarMagia('Imperio')
hp.falarMagia()

mdg.falar()

ahri.falarMagia()