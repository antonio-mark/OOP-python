from corpoceleste import CorpoCeleste

class Satelite(CorpoCeleste):
    def __init__(self, nome, diametro, composicao, planeta_orbita, periodo_orbita):
        super().__init__(str(nome), float(diametro), str(composicao))
        self.planeta_orbita = str(planeta_orbita)
        self.periodo_orbita = float(periodo_orbita)

    def exibirInformacoes(self):
        super().exibirInformacoes()
        print("O planeta de órbita do satelite é: " + self.planeta_orbita)
        print("O período de órbita do satelite é: " + str(self.periodo_orbita))