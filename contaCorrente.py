from conta import Conta

class ContaCorrente(Conta):


    def __init__(self, agencia, numero_conta, saldo, limite_extra = 200.0):
        super().__init__(agencia, numero_conta, saldo)
        self._limite_extra = limite_extra

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

    @property
    def saldo_total(self):
        return self._saldo + self._limite_extra

    def sacar(self,valor: float):

        if(valor <= 0):
            return "Informe um valor maior que 0!"
        
        if(valor > self.saldo_total):
            return "Saldo é insuficiente!"
        
        self._saldo -= valor
        return f"Saque realizado com sucesso!\nSaldo Atual: R$ {self._saldo:.2f}"
     

    

