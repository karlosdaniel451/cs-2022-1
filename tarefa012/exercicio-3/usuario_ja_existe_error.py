class UsuarioJaExisteError(Exception):
    """Excecao lancada quando for realizada uma tentativa de criacao de
    usuario cujo nome de usuario ja exista."""

    def __init__(self,
                message='Ja existe um usuario com este nome de usuario.'):
        self.message = message
