from retangulo import Retangulo
from triangulo import Triangulo
from circulo import Circulo

figuras = [
    Retangulo(4, 5),
    Triangulo(3, 4),
    Circulo(2)
]

for figura in figuras:
    if isinstance(figura, Retangulo):
        print("Retângulo:")
    elif isinstance(figura, Triangulo):
        print("Triângulo:")
    elif isinstance(figura, Circulo):
        print("Círculo:")
    
    print("Área:", figura.calcularArea())
    print("Perímetro:", figura.calcularPerimetro())
    print()