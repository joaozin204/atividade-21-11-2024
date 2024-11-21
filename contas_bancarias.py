#atividade 1
class ContaBancaria:
    def __init__(self, numeroConta, titular):

        self.__NumeroConta = numeroConta
        self.__Titular = titular

        self.__saldo = 0

    def getNumerodaConta(self):
        return self.__NumeroConta

    def getTitular(self):
        return self.__Titular


    def getSaldo(self):
        return self.__saldo


    def setNumeroConta(self,numeroConta):
        self.__NumeroConta = numeroConta
    
    def setTitular(self, titular):
        self.__Titular = titular

    def depositar(self, valor):
        self.__saldo += valor

    def sacar(self, valor):
        if valor > self.__saldo:
            print("vc nao tem esse valor para sacar !!")

        else:
            self.__saldo -= valor
