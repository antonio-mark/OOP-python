from assinatura import Assinatura

class AssinaturaSimples(Assinatura):
    def __init__(self, tipo, preco=29.99, detalhes="representa uma assinatura básica que fornece acesso a filmes e séries em qualidade padrão."):
        super().__init__(tipo, preco, detalhes)

    def calcular_preco(self):
        return self._preco

    def exibir_detalhes(self):
        return self._detalhes