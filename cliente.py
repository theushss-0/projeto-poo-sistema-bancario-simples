from pessoa import Pessoa
from conta import Conta

#Classe para pessoa
class Cliente(Pessoa):
    def __init__(self, nome, sobrenome, idade):
        super().__init__(nome, sobrenome, idade)
        self._conta = None
    
    #CONTA
    @property
    def conta(self):
        return self._conta
    
    @conta.setter
    def conta(self,conta:Conta):
        self._conta = conta


    #NOME
    @property
    def nome(self): 
        return self._nome

    @nome.setter   
    def nome(self, nome):
        self._nome = nome


    #SOBRENOME
    @property
    def sobrenome(self):
        return self._sobrenome  
          
    @sobrenome.setter
    def sobrenome(self, sobrenome): 
        self._sobrenome = sobrenome
    

    #IDADE
    @property
    def idade(self):
        return  self._idade
      
    @idade.setter
    def idade(self, idade): 
        self._idade = idade

    