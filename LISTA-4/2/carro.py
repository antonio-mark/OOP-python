from veiculo import Veiculo

class Carro(Veiculo):
    def __init__(self, marca, modelo, ano, cor):
        super().__init__(marca, modelo, ano)
        self.cor = cor

    def ligar_radio(self):
        print("Ligando o rádio do carro!")

    def abrir_porta(self):
        print("Abrindo a porta do carro!")