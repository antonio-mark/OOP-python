from corpoceleste import CorpoCeleste

class Estrela(CorpoCeleste):
    def __init__(self, nome, diametro, composicao, temperatura, tipo_espectral):
        super().__init__(str(nome), float(diametro), str(composicao))
        self.temperatura = float(temperatura)
        self.tipo_espectral = str(tipo_espectral)

    def exibirInformacoes(self):
        super().exibirInformacoes()
        print("A temperatura da estrela é: " + str(self.temperatura))
        print("O tipo espectral da estrela é: " + self.tipo_espectral)