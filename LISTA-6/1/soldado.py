from unidadeMilitar import UnidadeMilitar

class Soldado(UnidadeMilitar):
    def mover(self):
        print("A unidade Soldado está correndo")

    def atacar(self):
        print("A unidade Soldado está atacando com espada")