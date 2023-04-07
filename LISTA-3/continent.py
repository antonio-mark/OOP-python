from country import Country

class Continent():
    def __init__(self, name):
        self._name = name
        self._contries = []

    def addCountryOnContinent(self, country):
        if isinstance(country, Country):
            self._contries.append(country)
        else:
            print('Deve ser informado um país!')

    def getTotalDimension(self):
        dimensions = map(lambda pais: pais.getDimension(), self._contries)
        return sum(dimensions)
    
    def getTotalPopulation(self):
        populations = map(lambda pais: pais.getPopulation(), self._contries)
        return sum(populations)
    
    def getPopulationDensity(self):
        return self.getTotalPopulation() / self.getTotalDimension()
    
    def getLargerPopulationCountryInContinent(self):
        return max(self._contries, key=lambda pais: pais.getPopulation())
    
    def getSmallerPopulationCountryInContinent(self):
        return min(self._contries, key=lambda pais: pais.getPopulation())
    
    def getLargerDimensionCountryInContinent(self):
        return max(self._contries, key=lambda pais: pais.getDimension())
    
    def getSmallerDimensionCountryInContinent(self):
        return min(self._contries, key=lambda pais: pais.getDimension())
    
    def getTerritorialRatio(self):
        return self.getLargerDimensionCountryInContinent().getDimension() / self.getSmallerDimensionCountryInContinent().getDimension()

