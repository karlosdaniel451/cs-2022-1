from src.produto import Produto
from src.livro import Livro
from src.mouse import Mouse


def main():
    NOME_LOJA = '123 Eletrônicos'

    carrinho: list[Produto] = []

    carrinho.append(Livro(
        nome_loja=NOME_LOJA,
        preco=(35.00),
        autor='Ray Bradbury',
        descricao='livro digital'))

    carrinho.append(Livro(
        nome_loja=NOME_LOJA,
        preco=(45.00),
        autor='Martin Kleppmann',
        descricao='livro digital'))

    carrinho.append(Mouse(
        nome_loja=NOME_LOJA,
        preco=130.49,
        tipo='Gamer',
        descricao='Mouse Gamer Logitech G203 LIGHTSYNC RGB, Efeito de Ondas de'
                  ' Cores, 6 Botões Programáveis e Até 8.000 DPI - Preto'))
    
    # for produto in carrinho:
    #     print(produto.descricao)
    
    [print(produto.descricao) for produto in carrinho]


if __name__ == '__main__':
    main()
