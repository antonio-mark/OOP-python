class Data:
    def __init__(self, dia, mes, ano):
        self.dia = dia
        self.mes = mes
        self.ano = ano
    
    def __init__(self, dia=2, mes=12, ano=1996):
        self.dia = dia
        self.mes = mes
        self.ano = ano
        
    def imprimirData(self):
        print(f"{self.dia}/{self.mes}/{self.ano}")
        
    def imprimirDataPorExtenso(self, cidade):
        meses = ["janeiro", "fevereiro", "março", "abril", "maio", "junho", "julho",
                 "agosto", "setembro", "outubro", "novembro", "dezembro"]
        mes_extenso = meses[self.mes - 1]
        print(f"{cidade}, {self.dia} de {mes_extenso} de {self.ano}")

d = Data()
d.imprimirData()
d.imprimirDataPorExtenso('Milão')

data = Data(1, 11, 2012)
data.imprimirData()
data.imprimirDataPorExtenso('Roma')