# Parte 5 Composição

class Motor:
    def __init__(self, potencia):
        self.__potencia = potencia
    
    def getPotencia(self):
        return self.__potencia
    
    def setPotencia(self, potencia):
        self.__potencia = potencia
