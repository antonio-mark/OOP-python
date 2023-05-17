from veiculo import Veiculo

class Moto(Veiculo):
    def __init__(self, marca, modelo, ano, cilindrada):
        super().__init__(marca, modelo, ano)
        self.cilindrada = cilindrada

    def empinar(self):
        print("Empinando a moto!")

    def buzinar(self):
        print("Buzinando a moto!")