# Parte 4 Polimorfismo
from Carro import Carro
from Moto import Moto
from Motor import Motor

print('Testando as classes Carro e Moto herdadas de Veiculo e a composicao com a classe Motor:\n')


def teste_veiculo(veiculo):
    
    veiculo.acelerar()
    veiculo.acelerar()
    
    print(f'Velocidade atual: {veiculo.mostrar_velocidade()} Km/h')

    veiculo.freiar()
 
    print(f'Velocidade atual: {veiculo.mostrar_velocidade()} Km/h\n')




carro = Carro('NISSAN', 'sykeline', Motor(6.0))

print(f'Dados do Carro: {carro.getMarca()} - {carro.getModelo()} - {carro.getMotor()}')
teste_veiculo(carro)

moto = Moto('Honda', 'Xre 300')
print(f'Dados da Moto: {moto.getMarca()} - {moto.getModelo()}')
teste_veiculo(moto)
