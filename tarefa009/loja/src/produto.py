class Produto:

    def __init__(self, nome_loja: str, preco: float):
        self.nome_loja = nome_loja
        self.preco = preco

    @property
    def descricao(self) -> str:
        return 'Produto de Informática'
