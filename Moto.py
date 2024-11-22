# Parte 3 Herança


from Veiculo import Veiculo

class Moto(Veiculo):
    def __init__(self, marca, modelo):
        super().__init__(marca, modelo)
    

    def acelerar(self):
        self._velocidade += 15
    
   
    def freiar(self):
        self._velocidade -= 10
        if self._velocidade < 0:
            self._velocidade = 0

 
    def mostrar_velocidade(self):
        return self._velocidade
