from figuraGeometrica import FiguraGeometrica
import math

class Triangulo(FiguraGeometrica):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    
    def calcularArea(self):
        return (self.base * self.altura) / 2
    
    def calcularPerimetro(self):
        lado1 = self.base
        lado2 = self.altura
        hipotenusa = math.sqrt(lado1 ** 2 + lado2 ** 2)
        return lado1 + lado2 + hipotenusa