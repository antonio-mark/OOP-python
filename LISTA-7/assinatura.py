class Assinatura():
    def __init__(self, id_usuario=None, tipo=None, preco=None, status=None):
        self._id_usuario = id_usuario
        self._tipo = tipo
        self._preco = preco
        self._status = status

    def serializar(self):
        return ';'.join(self._id_usuario, self._tipo, self._preco, self._status) 
    
    def desserializar(self, dados):
        for i in self:
            self[i] = dados[i]

    def exibir_detalhes(self):
        print("ID do usuário: " + self._id_usuario)
        print("Tipo: " + self._tipo)
        print("Preço: " + self._preco)
        print("Status: " + self._status)