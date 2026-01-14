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


class ContaCorrente(Conta):

    LIMITE = 200.0

    def __init__(self, agencia, numero_conta, saldo):
        super().__init__(agencia, numero_conta, saldo)
        self._limite_extra = 0

    @property
    def agencia(self):
        return self._agencia

    @agencia.setter
    def agencia(self, agencia): 
        self._agencia = agencia

    @property
    def numero_conta(self):
        return self._numero_conta

    @numero_conta.setter
    def numero_conta(self, numero_conta): 
        self._numero_conta = numero_conta

    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, saldo): 
        self._saldo = saldo

    @property
    def limite_extra(self):
        return self.limite_extra

    @limite_extra.setter
    def limite_extra(self, limite): 
        self.limite_extra = limite
    
    # # # # # # # # # # 
    # METODO DE SACAR #
    # # # # # # # # # # 
    
    def sacar(self,valor: float):

        limite_extra_disponivel = ContaCorrente.LIMITE - self._limite_extra
        saldo_total = 0 if self._saldo <= 0 else self._saldo

        if limite_extra_disponivel > 0:
            saldo_total += limite_extra_disponivel

        if self._limite_extra == ContaCorrente.LIMITE:
            return f"Saldo é insuficiente!\nSeu saldo atual é R${self._saldo:.2f}\nRealize um Deposito!!"
        else:
            if(valor > saldo_total):
                return f"Saldo é insuficiente!\nSeu saldo atual é R${self._saldo:.2f}\nRealize um Deposito!!"
            elif(valor < saldo_total):
                if valor > self._saldo:
                    self._limite_extra = valor-self._saldo
                    self._saldo -= valor
                    return f"Saldo realizado com sucesso!!\nSaldo atual: R${self._saldo}"
                self._saldo -= valor
                return f"Saldo realizado com sucesso!!\nSaldo atual: R${self._saldo}"
        

    # # # # # # # # # # # #
    # METODO DE DEPOSITAR #
    # # # # # # # # # # # # 
    
    def depositar(self,valor:float):

        if self._limite_extra > 0:
            if valor > self._limite_extra:
                self._limite_extra = 0.0
                self._saldo += valor
                return f"Deposito realizado com sucesso!\nSeu saldo atual é R${self._saldo:.2f}"
            elif(valor < self._limite_extra):
                self._limite_extra -= valor
                self._saldo += valor
                return f"Deposito realizado com sucesso!\nSeu saldo atual é R${self._saldo:.2f}"
            else:
                self._limite_extra = valor
                self._saldo += valor
                return f"Deposito realizado com sucesso!\nSeu saldo atual é R${self._saldo:.2f}"
            
        self._saldo += valor
        return f"Deposito realizado com sucesso!\nSeu saldo atual é R${self._saldo:.2f}"



class ContaPoupanca(Conta):
    
    @property
    def agencia(self):
        return self._agencia

    @agencia.setter
    def agencia(self, agencia): 
        self._agencia = agencia

    @property
    def numero_conta(self):
        return self._numero_conta

    @numero_conta.setter
    def numero_conta(self, numero_conta): 
        self._numero_conta = numero_conta

    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, saldo): 
        self._saldo = saldo

    
    def sacar(self,valor):
        if ((self.saldo-valor) == 0):
            return "Saldo insuficiente!"
        
        self.saldo -= valor

    def depositar(self,valor):
        ...
    