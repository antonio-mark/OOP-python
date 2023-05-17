from criptografia import Criptografia

class CifraCesar(Criptografia):
    def __init__(self, deslocamento):
        self.deslocamento = deslocamento

    def cifrar(self, texto):
        texto_cifrado = ""
        for char in texto:
            if char.isalpha():
                ascii_offset = ord('a') if char.islower() else ord('A')
                cifrado = chr((ord(char) - ascii_offset + self.deslocamento) % 26 + ascii_offset)
                texto_cifrado += cifrado
            else:
                texto_cifrado += char
        return texto_cifrado

    def decifrar(self, texto_cifrado):
        texto_decifrado = ""
        for char in texto_cifrado:
            if char.isalpha():
                ascii_offset = ord('a') if char.islower() else ord('A')
                decifrado = chr((ord(char) - ascii_offset - self.deslocamento) % 26 + ascii_offset)
                texto_decifrado += decifrado
            else:
                texto_decifrado += char
        return texto_decifrado 