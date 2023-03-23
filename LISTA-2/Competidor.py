import random

class Competidor:
    def __init__(self, nome):
        self.nome = nome
        self.pos = 0

    def atualizar(self):
        valor_random = random.randint(1, 6)
        self.pos += valor_random 
        
        if self.getPos() % 5 == 0:
            self.pos -= 1
        
        if self.getPos() == 7 or self.getPos() == 17:
            self.pos += 2

        if self.getPos() == 13:
            self.pos = 0    
    
    def getPos(self):
        return self.pos
    
    def getNome(self):
        return self.nome
    

sophie = Competidor('sophie')
ayaka = Competidor('ayaka')
bea = Competidor('bea')
mark = Competidor('mark')
nevok = Competidor('nevok')

competidores = [sophie, ayaka, bea, mark, nevok]

fim = False

while fim is not True:
    for competidor in competidores:
        competidor.atualizar() 
        
        print('\n' + competidor.getNome() + ' está na posição ' + str(competidor.getPos()))

        if competidor.getPos() > 20:
            print('\nO(A) corredor(a) {} foi o vencedor(a)!'.format(competidor.nome))
            fim = True
            break