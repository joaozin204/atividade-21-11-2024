from ContaBancaria import ContaBancaria

print('Testando a classe bancária: \n')

 
conta = ContaBancaria(1, 'laun')


print('Dados da conta bancária:')
print(f'Número da conta: {conta.getNumerodaConta()}, Titular: {conta.getTitular()}, Saldo: R${conta.getSaldo():.2f}\n')


print('Depósito de R$100')
conta.depositar(100)
print(f'Saldo: R${conta.getSaldo():.2f}\n')

print('Você está retirando R$50 da conta:')
conta.sacar(50)
print(f'Saldo: R${conta.getSaldo():.2f}\n')


print('Tentando sacar R$200 e recebendo o aviso que não tem esse valor na conta:')
conta.sacar(200)
print(f'Saldo: R${conta.getSaldo():.2f}\n')


print('Alterando os dados da conta e o nome do titular:')
conta.setNumeroConta(10)
conta.setTitular('O brabo da ZN')
print('Dados alterados com sucesso.')
print(f'Número da Conta: {conta.getNumerodaConta()}, Titular: {conta.getTitular()}, Saldo: R${conta.getSaldo():.2f}\n')

