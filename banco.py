from conta import Conta
from cliente import Cliente

class Banco:
    def __init__(self, numero, nome_banco):
        self._numero_banco = numero
        self._nome_banco = nome_banco
        self._agencias = []
        self._contas:Conta = []
        self._clientes:Cliente = []
        
    @property
    def numero_banco(self):
        return self._numero_banco
    
    @property
    def nome_banco(self):
        return self._nome_banco
    
    @property
    def agencias(self):
        return self._agencias
    
    @property
    def contas(self):
        return self._contas
    
    @property
    def clientes(self):
        return self._clientes
    
    @agencias.setter
    def agencias(self, agencia):
        self._agencias.append(agencia)


    def verificar_agencia(self,conta:Conta):
        if conta.agencia not in self._agencias:
            return False
        return True

    def verificar_cliente(self, cliente:Cliente):
        if cliente not in self._clientes:
            return False
        return True
    
    def verificar_conta(self, conta:Conta):
        if conta not in self._contas:
            return False
        return True

    def inserir_agencia(self, agencia):
        self._agencias.append(agencia)
    
    def inserir_cliente(self, cliente:Cliente):
        self._clientes.append(cliente)
    
    def inserir_conta(self, conta:Conta):
        self._agencias.append(conta.agencia)
        self._contas.append(conta)


    def realizarSaque(self, conta:Conta, cliente:Cliente, valor):

        if not self.verificar_agencia(conta) and not self.verificar_cliente(cliente) and not self.verificar_conta(conta):
            return "Não é possível realizar saque!!"
        
        return conta.sacar(valor)
        
    def realizarDeposito(self, conta:Conta, cliente:Cliente, valor):
        
        if not self.verificar_agencia(conta) and not self.verificar_cliente(cliente) and not self.verificar_conta(conta):
            return "Não é possível realizar o deposito!!"
        
        return conta.depositar(valor)

