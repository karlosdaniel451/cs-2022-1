from src.endereco import Endereco
from src.i_endereco import IEndereco


class IEnderecoImpl(IEndereco):
    def consultar_por_cep(self, CEP: int) -> Endereco:
        return super().consultar_por_cep(CEP)
