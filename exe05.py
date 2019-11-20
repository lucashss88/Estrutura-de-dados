class ContaCorrente:
    def __init__(self,saldo,numero):
        self._saldo= saldo
        self._numero= numero
    def debitar(self,valor):
        self._saldo -= valor
    def creditar(self,valor):
        self._saldo += valor
    def transferencia(self,valor,conta):
        self.debitar(valor)
        conta.creditar(valor)
conta1=ContaCorrente(100,'123')
conta2=ContaCorrente(50,'456')
conta1.transferencia(20,conta2)
conta2.transferencia(50,conta1)
print(conta1._saldo,conta2._saldo)