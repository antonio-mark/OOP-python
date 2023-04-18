faunaBR = [
    # [Animal	Amazônia Mata_Atlântica	Cerrado	Caatinga Pampa	Pantanal]
    ['Capivara',	True,	True,	True,	True,	True,	True],
    ['Gralha azul',	False,	True,	False,	False,	True,	False],
    ['Tamanduá-bandeira',	True,	True,	True,	False,	True,	False],
    ['Onça pintada',	True,	True,	False,	True,	False,	True],
    ['Tatu-bola',	False,	False,	False,	True,	False,	False]]

floraBR = [
    # [Planta	Amazônia Mata_Atlântica	Cerrado	Caatinga Pampa	Pantanal]
    ['Ipê amarelo',	True,	True,	True,	True,	True,	True],
    ['Araucária',	False,	True,	False,	False,	True,	False],
    ['Mandacaru',	False,	False,	True,	True,	False,	False],
    ['Vitória-régia',	True,	False,	False,	False,	False,	True],
    ['Jatobá',	True,	True,	True,	False,	False,	True]]

class Bioma:
    def __init__(self, nome):
        self.__nome = nome
        self.__fauna = []
        self.__flora = []

    def adicionarAnimal(self, animal):
        self.__fauna.append(animal)

    def adicionarVegetal(self, vegetal):
        self.__flora.append(vegetal)

    def exibirFauna(self):
        for i in self.__fauna:
            print(i.getNome())

    def exibirFlora(self):
        for i in self.__flora:
            print(i.getNome())


class Animal:
    def __init__(self, nome):
        self.__nome = nome
        self.__nomeCientifico = ""
        self.__filo = ""
        self.__classe = ""
        self.__familia = ""
        self.__genero = ""
        self.__especie = ""
        self.__estadoConservacao = 0

    def getNome(self):
        return self.__nome
    
class Vegetal:
    def __init__(self, nome):
        self.__nome = nome
        self.__nomeCientifico = ""
        self.__filo = ""
        self.__classe = ""
        self.__familia = ""
        self.__genero = ""
        self.__especie = ""
        self.__estadoConservacao = 0

    def getNome(self):
        return self.__nome

amazonia = Bioma("Amazônia")
mataAtlantica = Bioma("Mata Atlântica")   
cerrado = Bioma("Cerrado")   
caatinga = Bioma("Caatinga")   
pampa = Bioma("Pampa")   
pantanal = Bioma("Pantanal")   

listaBiomas = [amazonia, mataAtlantica, cerrado, caatinga, pampa, pantanal]

for animais in faunaBR:
    animal = Animal(animais[0])
    animais.remove(animais[0])
    for index, biomas in enumerate(listaBiomas):
        if animais[index] == True:
            listaBiomas[index].adicionarAnimal(animal)

for vegetais in floraBR:
    vegetal = Vegetal(vegetais[0])
    vegetais.remove(vegetais[0])
    for index, biomas in enumerate(listaBiomas):
        if vegetais[index] == True:
            listaBiomas[index].adicionarVegetal(vegetal)

        



        

