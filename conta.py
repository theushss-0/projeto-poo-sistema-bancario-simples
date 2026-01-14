from abc import ABC, abstractmethod

class Conta(ABC):
    
    def __init__(self, agencia, numero_conta, saldo):
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

    @abstractmethod
    def depositar(self,valor):...

    