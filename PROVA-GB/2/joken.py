#enum
import random

class Joken():
    Pedra = 0
    Papel = 1
    Tesoura = 2

    def opcoes(self):
        lista = [self.Papel, self.Tesoura, self.Papel]

        return random.choice(lista) 
    
    def resultado(self, opcao_um, opcao_dois):
        if opcao_um == self.Pedra:
            if opcao_dois == self.Tesoura:
                return opcao_um
            elif opcao_dois == self.Papel:
                return opcao_dois
            else: 
                return None
        
        elif opcao_um == self.Tesoura:
            if opcao_dois == self.Papel:
                return opcao_um
            elif opcao_dois == self.Pedra:
                return opcao_dois
            else: 
                return None
            
        else:
            if opcao_dois == self.Pedra:
               return opcao_um
            elif opcao_dois == self.Tesoura:
               return opcao_dois
            else:
               return None