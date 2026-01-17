from abc import ABC, abstractmethod

class Conta(ABC):
    
    def __init__(self, agencia, numero_conta, saldo:float):
       self._agencia = agencia
       self._numero_conta = numero_conta
       self._saldo = saldo

    @property
    @abstractmethod
    def agencia(self):...

    @agencia.setter
    @abstractmethod
    def agencia(self, agencia): ...

    @property
    @abstractmethod
    def numero_conta(self):...

    @numero_conta.setter
    @abstractmethod
    def numero_conta(self, numero_conta): ...

    @property
    @abstractmethod
    def saldo(self):...

    @saldo.setter
    @abstractmethod
    def saldo(self, saldo): ...

    @abstractmethod
    def sacar(self,valor):...

    def depositar(self,valor:float):

        if(valor <= 0):
            return f"Valor invalido!"
        
        self._saldo += valor
        return f"Deposito realizado com sucesso!\nSaldo atual: R$ {self._saldo:.2f}"




    