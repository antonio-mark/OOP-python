class CadastroCliente:
    def __init__(self, nome, sobrenome, data_nascimento, email, cpf, senha):
        self._nome = nome
        self._sobrenome = sobrenome
        self._data_nascimento = data_nascimento
        self._email = email
        self.__cpf = cpf
        self.__senha = senha
        self.__auth = False
    
    def login(self, email, senha):
        if email != self._email or senha != self.__senha:
            print('\nEmail ou senha inválidos!')
            self.setAuth(False)
        else:
            self.setAuth(True)

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
bloqueio = False

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
        if bloqueio is True:
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
        if bloqueio is True:
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

            if cliente.getAuth() is True:
                cliente.consultar()
                break
        
        if cliente.getAuth() is False: 
            bloqueio = True   

    elif escolha == '3':
        print('Sistema finalizado!')  
        
    else:
        print('\nOpção desconhecida!\n')
        input('\n\nPressione ENTER para continuar   ')
