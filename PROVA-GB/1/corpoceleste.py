class CorpoCeleste():
    def __init__(self, nome, diametro, composicao):
        self.nome = str(nome)
        self.diametro = float(diametro)
        self.composicao = str(composicao)

    def exibirInformacoes(self):
        print("O nome do corpo celeste é: " + self.nome)
        print("O diâmetro do corpo celeste é: " + str(self.diametro))
        print("A composição do corpo celeste é: " + self.composicao)
