from cifraCesar import CifraCesar
from cifraXor import CifraXor

texto = "HelloWorld"
chave_cesar = 3
chave_xor = 50

cifra_cesar = CifraCesar(chave_cesar)
cifra_xor = CifraXor(chave_xor)

texto_cifrado_cesar = cifra_cesar.cifrar(texto)
texto_decifrado_cesar = cifra_cesar.decifrar(texto_cifrado_cesar)

texto_cifrado_xor = cifra_xor.cifrar(texto)
texto_decifrado_xor = cifra_xor.decifrar(texto_cifrado_xor)

print("Cifra de César:")
print("Texto original:", texto)
print("Texto cifrado:", texto_cifrado_cesar)
print("Texto decifrado:", texto_decifrado_cesar)
print()

print("Cifra XOR:")
print("Texto original:", texto)
print("Texto cifrado:", texto_cifrado_xor)
print("Texto decifrado:", texto_decifrado_xor)