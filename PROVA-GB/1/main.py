from corpoceleste import CorpoCeleste
from estrela import Estrela
from planeta import Planeta
from satelite import Satelite

estrela = Estrela("Estrela do zodiaco", 155.55, "zodiaco", 45, "zodiac")
planeta = Planeta("Terra", 500, "Agua", 1, "Oxigenio")
satelite = Satelite("Satelite junior", 1.2, "Zodiaco", "Venus", 100.99)

corposCelestes = []

corposCelestes.append(estrela)
corposCelestes.append(planeta)
corposCelestes.append(satelite)

for i in corposCelestes:
    i.exibirInformacoes()
    print()