from usuario import Usuario
from assinatura import Assinatura
import csv

def ler_usuarios_csv(arquivo):
    usuarios = []
    csv_arq = open(arquivo)
    leitor = csv.reader(csv_arq, delimiter=';')
    for linha in leitor:
        usuario = Usuario() 
        usuario.desserializar(linha)
        usuarios.append(usuario) 
    return usuarios

    
def ler_assinaturas_csv(arquivo):
    assinaturas = []
    csv_arq = open(arquivo)
    leitor = csv.reader(csv_arq, delimiter=';')
    for linha in leitor:
        assinatura = Assinatura() 
        assinatura.desserializar(linha)
        assinaturas.append(assinatura) 
    return assinaturas

usuarios = ler_usuarios_csv("Usuarios.csv")
assinaturas = ler_assinaturas_csv("Assinaturas.csv")

for user in usuarios:
    for assinatura in assinaturas:
        if user.get_cpf() == assinatura._id_usuario:
            user.adicionar_assinatura(assinatura)

def salvar_alteracoes(lista, arquivo):
    with open(arquivo, mode='w', newline='') as arqCSV:
        escritor = csv.writer(arqCSV, delimiter=';')
        for elemento in lista:
            linha = elemento.serializar() 
            escritor.writerow(linha)

def adicionar_assinatura(usuario_logado):
    tipo = input("Digite o tipo de assinatura(Simples ou Premium): ")

    assinatura = Assinatura(usuario_logado.get_cpf(), tipo, ' 29.99 ' if tipo == "Simples" else ' 49.99 ', "Ativa")
    assinaturas.append(assinatura)
    salvar_alteracoes(assinaturas, 'Assinaturas.csv')

    usuario_logado.adicionar_assinatura(assinatura)
    
def cancelar_assinatura(usuario_logado):
    if len(usuario_logado._assinaturas) == 0:
        print("Você não tem assinaturas ativas.")
        print()
        exibir_menu(usuario_logado)
    
    for i, assinatura in enumerate(usuario_logado._assinaturas):
        print("ID: {}".format(i))
        assinatura.exibir_detalhes()
    
    id_assinatura = int(input("Digite o número da assinatura para cancelar: "))

    assinatura = usuario_logado.cancelar_assinatura(id_assinatura)

    for i in assinaturas:
        if assinatura == i:
            i._status = "Inativa"
    salvar_alteracoes(assinaturas, 'Assinaturas.csv')


def exibir_menu(usuario_logado):
    opcao = 0
    while opcao != 3:
        print("Menu:")
        print("1. Adicionar assinatura")
        print("2. Cancelar assinatura")
        print("3. Sair")
        opcao = int(input("Digite o número da opção desejada: "))

        if opcao == 1:
            adicionar_assinatura(usuario_logado)
        elif opcao == 2:
            cancelar_assinatura(usuario_logado)  
        elif opcao == 3:
            print("Saindo...")
        else:
            print("Opção inválida!")


def login():
    nome_usuario = input("Digite o nome de usuário: ")
    senha = input("Digite a senha: ")
    usuario_logado = None

    usuario_autenticado = False
    for usuario in usuarios:
        if usuario.verificar_autenticacao(nome_usuario, senha):
            usuario_autenticado = True
            usuario_logado = usuario
            break

    if usuario_autenticado:
        print("Autenticação bem-sucedida!")
        exibir_menu(usuario_logado)
    else:
        print("Credenciais inválidas. Tente novamente.")
        menu_login()

def adicionar_usuario():
    nome = input("Digite o nome: ")
    sobrenome = input("Digite o sobrenome: ")
    data_nascimento = input("Digite a data de nascimento (dd/mm/YYYY): ")
    cpf = input("Digite o CPF: ")
    nome_usuario = input("Digite o nome de usuário: ")
    senha = input("Digite a senha: ")

    usuario = Usuario(nome, sobrenome, data_nascimento, cpf, nome_usuario, senha)
    usuarios.append(usuario)
    salvar_alteracoes(usuarios, 'Usuarios.csv')
    exibir_menu(usuario)

def menu_login():
    print("Menu de Login")
    print("1. Login")
    print("2. Cadastro")
    opcao = input("Digite o número da opção desejada: ")

    if opcao == "1":
        login()
    elif opcao == "2":
        adicionar_usuario()
    else:
        print("Opção inválida. Tente novamente.")
        menu_login()

menu_login()

