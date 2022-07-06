from src.produto import Produto


class Mouse(Produto):
    def __init__(self, nome_loja: str, preco: float, tipo: str, descricao: str):
        super().__init__(nome_loja, preco)
        self.tipo = tipo
        self._descricao = descricao

    @property
    def descricao(self) -> str:
        return f'{self._descricao} - tipo = {self.tipo}'
