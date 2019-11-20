class ContaCorrente:
    def __init__(self,nome,saldo):
        self._a=nome
        self._b=saldo
    def set_saldo(self,saldo):
        if (saldo>0):
            self.__b=saldo
        else:
            pass
    def get_saldo(self):
        return self.__b
    def get_nome(self):
        return self.__a
n1=ContaCorrente('LUCAS',100)
n2=ContaCorrente('ANDRÉ',-100)
print(n1._b,n1._a)
print(n2._b,n2._a)

