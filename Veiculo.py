# Parte 2 Abstração

from abc import ABC, abstractmethod


class Veiculo(ABC):
    def __init__(self, marca, modelo):

        self.__marca = marca
        self.__modelo = modelo
    
        self._velocidade = 0
    
    def getMarca(self):
        return self.__marca

    def getModelo(self):
        return self.__modelo
    

    @abstractmethod
    def mostrar_velocidade(self):
        pass

   
    @abstractmethod
    def acelerar(self):
        pass

   
    @abstractmethod
    def freiar(self):
        pass
