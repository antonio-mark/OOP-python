class Calculadora:
    def somar(self, num1, num2):
        return num1 + num2
    
    def subtrair(self, num1, num2):
        return num1 - num2
        
    def multiplicar(self, num1, num2):
        return num1 * num2
    
    def dividir(self, num1, num2):
        if num2 == 0:
            print('ATENÇÃO, NÃO EXISTE DIVISÃO POR ZERO')
            return -1
        else: 
            return num1 / num2
        
