# CLASSE DE EXEMPLO DO CHAT GPT - DESCONSIDERAR

import random

class Animal:
    def __init__(self, nome):
        self.nome = nome
    
    def exibirDescricao(self):
        print("Sou um animal chamado", self.nome)

class Carnivoro(Animal):
    def caçar(self):
        print("Estou caçando como um animal carnívoro")
    
    def exibirDescricao(self):
        super().exibirDescricao()
        print("Sou um animal carnívoro")

class Herbivoro(Animal):
    def pastar(self):
        print("Estou pastando como um animal herbívoro")
    
    def exibirDescricao(self):
        super().exibirDescricao()
        print("Sou um animal herbívoro")

class Onivoro(Carnivoro, Herbivoro):
    def comer(self):
        escolha = random.randint(0, 1)
        if escolha == 0:
            self.caçar()
        else:
            self.pastar()
    
    def exibirDescricao(self):
        super().exibirDescricao()
        print("Sou um animal onívoro")

# Exemplo de uso das classes

tigre = Carnivoro("Tigre")
tigre.exibirDescricao()
tigre.caçar()

coelho = Herbivoro("Coelho")
coelho.exibirDescricao()
coelho.pastar()

urso = Onivoro("Urso")
urso.exibirDescricao()
urso.comer()
