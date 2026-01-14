from conta import Conta


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

        if(valor < 0):
            return "Informe um valor maior que zero!"

        if (valor > self._saldo):
            return "Saldo insuficiente!"
        
        self.saldo -= valor
        return "Saque realizado com sucesso!"
    
    def depositar(self,valor):
        if (valor <= 0):
            return "Valor invalido!"
        self._saldo += valor
        return f"Deposito realizado com sucesso!\nSaldo atual: R$ {self._saldo:.2f}"
    