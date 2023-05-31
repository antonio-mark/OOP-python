from animal import Animal

class Carnivoro(Animal):
    def __init__(self, nome):
        super().__init__(nome)

    def caçar(self):
        print("O carnivoro está caçando")

    def exibirDescricao(self):
        super().exibirDescricao()
        print("Sou um animal carnívoro")