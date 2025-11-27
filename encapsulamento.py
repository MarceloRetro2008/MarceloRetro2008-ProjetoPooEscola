class conta:
    def __init__(self, saldo=0):
        self._saldo = saldo
    
    @property
    def saldo(self):
        return self._saldo
    
    @saldo.setter
    def saldo(self, valor):
        if valor >= 0:
            self._saldo = valor
        else:
            print("saldo invalido")
    
    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor

conta2 = conta(500)
print("saldo inicial:", conta2.saldo)

conta2.saldo = -300
print("saldo final:", conta2.saldo)