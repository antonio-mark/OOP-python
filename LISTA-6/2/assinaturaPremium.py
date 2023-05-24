from assinatura import Assinatura

class AssinaturaPremium(Assinatura):
    def __init__(self, tipo):
        super().__init__(tipo, preco = 49.99, detalhes = "representa uma assinatura avançada que oferece acesso a filmes e séries em qualidade HD e Ultra HD.")

    def calcular_preco(self):
        return self._preco

    def exibir_detalhes(self):
        return self._detalhes