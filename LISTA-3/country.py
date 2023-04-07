class Country:
    def __init__(self, codeISO, name, dimension):
        self.__codeISO = codeISO
        self.__name = name
        self.__dimension = dimension
        self._borders = []

    def setCodeISO(self, code):
        self.__codeISO = code
    
    def setName(self, name):
        self.__name = name

    def setPopulation(self, population):
        self.__population = population

    def setDimension(self, dimension):
        self.__dimension = dimension

    def getCodeISO(self):
        return self.__codeISO 
    
    def getName(self):
        return self.__name 
    
    def getPopulation(self):
        return self.__population 
     
    def getDimension(self):
        return self.__dimension
    
    def addCountryOnBorder(self, country):
        self._borders.append(country)
    
    def verifyCountry(self, country):
        return self.__codeISO == country.getCodeISO()
    
    def verifyNeighbor(self, country):
        return country in self._borders
    
    def getPopulationDensity(self):
        return self.getPopulation() / self.getDimension()
    
    def commonNeighbors(self, country):
        return list(set(self._borders) & set(country._borders))

