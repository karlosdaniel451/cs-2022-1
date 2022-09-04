class LoginInvalidoError(Exception):
    """Excecao lancada quando for realizada uma tentativa de login invalida."""

    def __init__(self, message='Login ou usuario invalido.'):
        self.message = message
