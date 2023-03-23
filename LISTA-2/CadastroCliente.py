class Auth():
    REPROVADO = 0
    APROVADO = 1
    BLOCK = 2

class CadastroCliente:
    def __init__(self, nome, sobrenome, data_nascimento, email, cpf, senha):
        self._nome = nome
        self._sobrenome = sobrenome
        self._data_nascimento = data_nascimento
        self._email = email
        self.__cpf = cpf
        self.__senha = senha
        self.__auth = Auth.REPROVADO
        self._count = 0
    
    def login(self, email, senha):       
        if email != self._email or senha != self.__senha:
            print('\nEmail ou senha inválidos!')
            self.setAuth(Auth.REPROVADO)
            self._count += 1        
            if self._count == 3:
                self.setAuth(Auth.BLOCK)       
        else:
            self.setAuth(Auth.APROVADO)

    def setAuth(self, auth):
        self.__auth = auth

    def getAuth(self):
        return self.__auth

    def consultar(self):
        print()
        print('nome: ' + self._nome)
        print('sobrenome: ' + self._sobrenome)
        print('data de nascimento: ' + self._data_nascimento)
        print('email: ' + self._email)
        print('cpf: ' + self.__cpf)
        print()

escolha = None
cliente = None

def menu():
    print('\n..:: Escolha sua opção ::..\n')
    print('1 - Cadastrar')
    print('2 - Consultar')
    print('3 - Sair\n')
    item = input('Escolha uma opção: ')
    return item      

while escolha != '3':
    escolha = menu()
    
    if escolha == '1':
        if cliente is not None and cliente.getAuth() is Auth.BLOCK:
            print('BLOQUEIO DE SEGURANÇA')
            continue
        
        print('\nOlá, insira seus dados abaixo\n')       
        nome = input('Digite seu nome: ')
        sobrenome = input('Digite seu sobrenome: ')
        data_nascimento = input('Digite sua data de nascimento: ')
        email = input('Digite seu email: ')
        cpf = input('Digite seu cpf: ')     
        senha = input('Digite sua senha: ')
        
        cliente = CadastroCliente(nome, sobrenome, data_nascimento, email, cpf, senha)
        
    elif escolha == '2':
        if cliente is not None and cliente.getAuth() is Auth.BLOCK:
            print('BLOQUEIO DE SEGURANÇA')
            continue
        
        if cliente is None:
            print('Realize seu cadastro primeiro!')
            continue 
        
        print('\nInforme seu email e senha para consulta\n')
        
        for i in range(3):
            email = input('Digite seu email: ')
            senha = input('Digite sua senha: ')
            cliente.login(email, senha)

            if cliente.getAuth() is Auth.APROVADO:
                cliente.consultar()
                break  

    elif escolha == '3':
        print('Sistema finalizado!')  
        
    else:
        print('\nOpção desconhecida!\n')
        input('\n\nPressione ENTER para continuar   ')
