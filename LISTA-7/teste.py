from usuario import Usuario
from assinatura import Assinatura
import csv

def ler_usuarios_csv(arquivo):
    usuarios = []
    arqCSV = open(arquivo)
    leitor = csv.reader(arqCSV, delimiter=';')
    for linha in leitor:
        print(linha)
        usuario = Usuario() 
        usuario.desserializar(linha)
        usuarios.append(usuario) 
        return usuarios
    

print(ler_usuarios_csv('Usuarios.csv')[1].get_cpf())
    
def ler_assinaturas_csv(arquivo):
    assinaturas = []
    arqCSV = open(arquivo)
    leitor = csv.reader(arqCSV, delimiter=';')
    for linha in leitor:
        assinatura = Assinatura() 
        assinatura.desserializar(linha)
        assinaturas.append(assinatura) 
        return assinaturas