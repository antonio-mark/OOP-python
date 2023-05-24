from soldado import Soldado
from arqueiro import Arqueiro
from cavaleiro import Cavaleiro

unidadeSoldado = Soldado()
unidadeArqueiro = Arqueiro()
unidadeCavaleiro = Cavaleiro()

unidades = []

unidades.append(unidadeSoldado)
unidades.append(unidadeArqueiro)
unidades.append(unidadeCavaleiro)


for i in unidades:
    i.mover()
    i.atacar()