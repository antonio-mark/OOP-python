class Usuario():
    def __init__(self, nome=None, sobrenome=None, data_nascimento=None, cpf=None, nome_usuario=None, senha=None):
        self._nome = nome
        self._sobrenome = sobrenome
        self._data_nascimento = data_nascimento
        self.__cpf = cpf
        self._nome_usuario = nome_usuario
        self.__senha = senha
        self._assinaturas = []

    def verificar_autenticacao(self, nome_usuario, senha):
        return self._nome_usuario == nome_usuario and self.__senha == senha

    def get_senha(self):
        return self.__senha
    
    def get_cpf(self):
        return self.__cpf
    
    def set_cpf(self, cpf):
        self.__cpf = cpf

    def set_senha(self, senha):
        self.__senha = senha

    def adicionar_assinatura(self, assinatura):
        self._assinaturas.append(assinatura)

    def cancelar_assinatura(self, id_assinatura):
        return self._assinaturas.pop(id_assinatura)

    def exibir_dados(self):
        print("Nome: " + self._nome)
        print("Sobrenome: " + self._nome) 
        print("Data de nascimento: " + self._nome) 
        print("CPF: " + self.get_cpf()) 
        print("Nome de usuário: " + self._nome)
        print("Senha " + self.get_senha())

    def serializar(self):
        return [self._nome, self._sobrenome, self._data_nascimento, self.get_cpf(), self._nome_usuario, self.get_senha()]
    
    def desserializar(self, dados):
        self._nome = dados[0]
        self._sobrenome = dados[1]
        self._data_nascimento = dados[2]
        self.set_cpf(dados[3])
        self._nome_usuario = dados[4]
        self.set_senha(dados[5])
