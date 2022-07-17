from abc import ABC, abstractmethod

from src.endereco import Endereco


class IEndereco(ABC):

    @abstractmethod
    def consultar_por_cep(self, CEP: int) -> Endereco:
        """Busca um endereco de acordo com o seu CEP.

        Parameters
        ----------
        CEP : `int`\n
            CEP do endereco a ser buscado.
        
        Returns
        -------
        endereco : `Endereco`\n
            Instancia de `Endereco` que representa o endereco buscado,
            de modo que `endereco.CEP` == `CEP`.

        Authors
        -------
        Karlos Daniel Pires da Silva : github.com/karlosdaniel451
        Date: 2022-07-15
        """
        pass
