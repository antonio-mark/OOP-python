from animal import Animal

class Herbivoro(Animal):
    def __init__(self, nome):
        Animal.__init__(self, nome)

    def pastar(self):
        print("O herbívoro está pastando")

    def exibirDescricao(self):
        super().exibirDescricao()
        print("Sou um animal herbívoro")