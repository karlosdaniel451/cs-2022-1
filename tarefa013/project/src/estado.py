from dataclasses import dataclass

from src.pais import Pais


@dataclass
class Estado:
    """Classe cujas instancias representam estados.
    
    Attributes
    ----------
    sigla : `str`\n
        Sigla do estado.\n
    nome : `str`\n
        Nome do estado.\n
    pais : `Pais`.\n
        Pais do estado.\n
    
    Examples
    --------
    >>> from src.pais import Pais
    >>> from src.estado import Estado
    >>> pais = Pais(nome='Brasil')
    >>> estado = Estado(sigla='GO', nome='Goias', pais=pais)
    >>> print(f'{estado.sigla} - {estado.nome} - {estado.pais.nome}')
    GO - Goiás - Brasil

    Authors
    -------
    Karlos Daniel Pires da Silva : github.com/karlosdaniel451
    Date: 2022-07-15
    """

    sigla: str
    nome: str
    pais: Pais
