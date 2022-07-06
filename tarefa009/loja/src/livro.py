from src.produto import Produto


class Livro(Produto):
    def __init__(self, nome_loja: str, preco: float, autor: str, descricao: str):
        super().__init__(nome_loja, preco)
        self.autor = autor
        self._descricao = descricao

    @property
    def descricao(self) -> str:
        return f'{self._descricao} - autor = {self.autor}'
