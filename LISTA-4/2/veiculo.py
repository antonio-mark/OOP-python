class Veiculo():
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = int(ano)

    def acelerar(self):
        print("Acelerando o veículo!")
    
    def frear(self):
        print("Freando o veículo!")