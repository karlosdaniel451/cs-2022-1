from dataclasses import dataclass
from enum import Enum


class TipoLogradouro(Enum):
    """Enum para representacao de tipos de logradouro.

    Values
    ------
    ALAMEDA = 0\n
    AVENIDA = 1\n
    MARGINAL = 2\n
    RUA = 3\n
    RODOVIA = 4\n
    VIA = 5\n
    VIELA = 6\n
    TRAVESSA = 7
    """

    ALAMEDA = 0
    AVENIDA = 1
    MARGINAL = 2
    RUA = 3
    RODOVIA = 4
    VIA = 5
    VIELA = 6
    TRAVESSA = 7


@dataclass
class Logradouro:
    """Classe cujas instancias representam logradouros.
    
    Attributes
    ----------
    nome: `str`\n
        Nome do logradouro.\n
    tipo_logradouro : `TipoLogradouro`\n
        Tipo do logradouro.\n
    
    Examples
    --------
    >>> from src.pais import Pais
    >>> from src.estado import Estado
    >>> from src.cidade import Cidade
    >>> from src.bairro import Bairro
    >>> from src.endereco import Endereco, TipoEndereco
    >>> from src.logradouro import Logradouro, TipoLogradouro
    >>> pais = Pais(nome='Brasil')
    >>> estado = Estado(sigla='GO', nome='Goias', pais=pais)
    >>> cidade = Cidade(nome='Goiânia', estado=estado)
    >>> bairro = Bairro(nome='Chácaras Califórnia', cidade=cidade)
    >>> logradouro = Logradouro(
    ...     nome='Alameda Palmeiras',
    ...     tipo_logradouro=TipoLogradouro.ALAMEDA
    ... )
    >>> endereco = Endereco(
    ...     numero=0,
    ...     CEP=74690900,
    ...     tipo_endereco=TipoEndereco.COMERCIAL,
    ...     bairro=bairro,
    ...     logradouro=logradouro,
    ...     complemento='Quadra d'
    ... )
    >>> print(logradouro.nome)
    Alameda Palmeiras
    >>> print(logradouro.tipo_logradouro.name)
    ALAMEDA
    >>> print(endereco.logradouro is logradouro)
    True

    Authors
    -------
    Karlos Daniel Pires da Silva : github.com/karlosdaniel451
    Date: 2022-07-15
    """

    nome: str
    tipo_logradouro: TipoLogradouro
