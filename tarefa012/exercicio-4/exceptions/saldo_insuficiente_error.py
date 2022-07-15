class SaldoInsuficienteError(Exception):
    # """Excecao lancada quando for realizada uma tentativa de login invalida."""

    def __init__(self, message='Saldo insuficiente.'):
        self.message = message
