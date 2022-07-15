from login_invalido_error import LoginInvalidoError


class Login:
    def __init__(
        self,
        usuario: str,
        senha: str,
        dados_de_login: list[dict[str, str]]
    ):
        self.usuario = usuario
        self.senha = senha
        self.dados_de_login = dados_de_login

    def fazer_login(self, usuario: str, senha: str) -> bool:
        for dado_de_login in self.dados_de_login:
            usuario = dado_de_login['usuario']
            senha = dado_de_login['senha']

            if usuario == self.usuario and senha == self.senha:
                return True

        raise LoginInvalidoError()
