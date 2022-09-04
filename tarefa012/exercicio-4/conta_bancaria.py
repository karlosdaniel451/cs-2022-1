from exceptions.saldo_insuficiente_error import SaldoInsuficienteError

class ContaBancaria:
    def __init__(self, saldo: float=0):
        self.saldo = saldo

    def depositar(self, valor: float):
        self.saldo += valor

    def sacar(self, valor: float):
        if self.saldo < valor:
            raise SaldoInsuficienteError()

        self.saldo -= valor
