# crie uma classe chamada Calculadora, com os métodos somar, subtrair, multiplicar e dividir dois
# números. Cada um destes métodos recebe por parâmetro dois números reais e retorna o
# resultado da operação com os dois números. Se houver divisão por zero, imprimir um aviso na
# execução do método e retornar -1

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
        
