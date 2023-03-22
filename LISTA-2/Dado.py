import random

class Dado:
    def __init__(self, numeroFaces):
        self.numeroFaces = numeroFaces
    
    def Rolar(self):
        lista = []
        
        for i in range(1, self.numeroFaces + 1):
            lista.append(i)

        return random.choice(lista)
    
def main():
    dado_virtual_6 = Dado(6)
    dado_virtual_8 = Dado(8)
    dado_virtual_12 = Dado(12)

    print(dado_virtual_6.Rolar())
    print(dado_virtual_6.Rolar())
    print(dado_virtual_6.Rolar())
    

    print(dado_virtual_8.Rolar())
    print(dado_virtual_8.Rolar())
    print(dado_virtual_8.Rolar())

    print(dado_virtual_12.Rolar())
    print(dado_virtual_12.Rolar())
    print(dado_virtual_12.Rolar())

main()
    

        

