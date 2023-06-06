from corpoceleste import CorpoCeleste

class Planeta(CorpoCeleste):
    def __init__(self, nome, diametro, composicao, num_luas, tipo_atmosfera):
        super().__init__(str(nome), float(diametro), str(composicao))
        self.num_luas = int(num_luas)
        self.tipo_atmosfera = str(tipo_atmosfera)

    def exibirInformacoes(self):
        super().exibirInformacoes()
        print("O número de luas do planeta é: " + str(self.num_luas))
        print("O tipo de atmosfera do planeta é: " + self.tipo_atmosfera)