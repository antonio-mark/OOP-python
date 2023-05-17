from figuraGeometrica import FiguraGeometrica
import math

class Circulo(FiguraGeometrica):
    def __init__(self, raio):
        self.raio = raio
    
    def calcularArea(self):
        return math.pi * (self.raio ** 2)
    
    def calcularPerimetro(self):
        return 2 * math.pi * self.raio