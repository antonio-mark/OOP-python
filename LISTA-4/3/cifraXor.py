from criptografia import Criptografia

class CifraXor(Criptografia):
    def __init__(self, chave):
        self.chave = chave

    def cifrar(self, texto):
        texto_cifrado = ""
        for char in texto:
            cifrado = chr(ord(char) ^ self.chave)
            texto_cifrado += cifrado
        return texto_cifrado

    def decifrar(self, texto_cifrado):
        return self.cifrar(texto_cifrado)