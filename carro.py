# Parte 3 Herança

from Veiculo import Veiculo
from Motor import Motor

class Carro(Veiculo):

    def __init__(self, marca, modelo, motor: Motor):
        super().__init__(marca, modelo)
    
        self.__motor = motor

    def acelerar(self):
        self._velocidade += 10
    

    def freiar(self):
        self._velocidade -= 10
        if self._velocidade < 0:
            self._velocidade = 0

    #
    def mostrar_velocidade(self):
        return self._velocidade

    
    def getMotor(self):
        return self.__motor.getPotencia()
    
    def setMotor(self, motor):
        self.__motor = motor

