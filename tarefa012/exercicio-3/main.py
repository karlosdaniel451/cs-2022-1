import json

from login import Login
from login_invalido_error import LoginInvalidoError
from usuario_ja_existe_error import UsuarioJaExisteError

def conta_ja_esta_criada(usuario: str,
                        dados_de_login: list[dict[str, str]]) -> bool:

    for dado_de_login in dados_de_login:
        if usuario == dado_de_login['usuario']:
            return True
    
    return False


def criar_conta(dados_de_login: list[dict[str, str]]):
    usuario = input('Usuario: ')
    senha = input('Senha: ')

    if conta_ja_esta_criada(usuario, dados_de_login):
        raise UsuarioJaExisteError()
    
    dados_de_login.append({'usuario': usuario, 'senha': senha})


def fazer_login(dados_de_login: list[dict[str, str]]):
    usuario = input('Usuario: ')
    senha = input('Senha: ')

    login = Login(usuario, senha, dados_de_login)

    try:
        login.fazer_login(usuario, senha)
    except LoginInvalidoError as error:
        raise error
    # else:
    #     pass


def ler_dados_de_login(filename: str) -> list[dict[str, str]]:
    try:
        with open(filename, encoding='utf-8', mode='r') as f:
            dados_de_login = json.load(f)
            return dados_de_login
    except FileNotFoundError:
        escrever_dados_de_login(filename, [])
        return []


def escrever_dados_de_login(filename: str, dados_de_login: list[dict[str, str]]):
    with open(filename, encoding='utf-8', mode='w') as f:
        json.dump(dados_de_login, f)


def main():
    FILENAME = 'dados_de_login.json'
    dados_de_login: list[dict[str, str]] = ler_dados_de_login(FILENAME)

    while True:
        opcao = input('Digite:\n'
                      '0 - Para sair.\n'
                      '1 - Para criar uma conta.\n'
                      '2 - Para fazer login.\n\n')
        match opcao:
            case '0':
                exit()
            case '1':
                try:
                    criar_conta(dados_de_login)
                    escrever_dados_de_login(FILENAME, dados_de_login)
                except UsuarioJaExisteError as error:
                    print(f'\nErro: {error.message}\n')
                else:
                    print('\nConta criada com sucesso!\n')
            case '2':
                try:
                    fazer_login(dados_de_login)
                except LoginInvalidoError as error:
                    print(f'\nErro: {error.message}\n')
                else:
                    print('\nLogin realiado com sucesso!\n')
            case _:
                print('Error: Opcao invalida. Por favor, tente novamente.')


if __name__ == '__main__':
    main()
