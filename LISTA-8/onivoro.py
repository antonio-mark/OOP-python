from random import randint
from carnivoro import Carnivoro
from herbivoro import Herbivoro

class Onivoro(Carnivoro, Herbivoro):
    def __init__(self, nome):
        Carnivoro.__init__(self, nome)
        Herbivoro.__init__(self, nome)

    def comer(self):
        super().caçar() if randint(0, 1) == 0 else super().pastar()
        # Carnivoro.caçar(self)                  Herbivoro.pastar(self)

    def exibirDescricao(self):
        super().exibirDescricao() 
        print("Sou um animal onívoro")