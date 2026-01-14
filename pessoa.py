from abc import ABC, abstractmethod

class Pessoa(ABC):
    
    def __init__(self, nome, sobrenome, idade):
        self._nome = nome
        self._sobrenome = sobrenome
        self._idade = idade



    #NOME
    @property
    @abstractmethod
    def nome(self): ...

    @nome.setter
    @abstractmethod
    def nome(self, nome): ...


    #SOBRENOME
    @property
    @abstractmethod
    def sobrenome(self):...
        
    @sobrenome.setter
    @abstractmethod
    def sobrenome(self, sobrenome): ...
    

    #IDADE
    @property
    @abstractmethod
    def idade(self): ...
      
    @idade.setter
    @abstractmethod
    def idade(self, idade): ...

        