from veiculo import Veiculo

class Caminhao(Veiculo):
    def __init__(self, marca, modelo, ano, carga_maxima):
        super().__init__(marca, modelo, ano)
        self.carga_maxima = carga_maxima

    def carregar(self):
        print("Carregando o caminhão!")

    def descarregar(self):
        print("Descarregando o caminhão!")
