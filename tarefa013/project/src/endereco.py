from dataclasses import dataclass
from enum import Enum

from src.bairro import Bairro
from src.logradouro import Logradouro


class TipoEndereco(Enum):
    """Enum para representacao de tipos de endereco.

    Values
    ------
    COMERCIAL = 0\n
    RESIDENTIAL = 1
    """

    COMERCIAL = 0
    RESIDENCIAL = 1


@dataclass
class Endereco:
    """Classe cujas instancias representam enderecos.
    
    Attributes
    ----------
    numero : `int`\n
        Numero do endereco.\n
    CEP : `int`\n
        CEP do endereco.\n
    tipo_endereco : `TipoEndereco`\n
        Tipo do endereco.\n
    bairro : `Bairro`\n
        Bairro do endereco.\n
    logradouro : `Logradouro`\n
        Logradouro do endereco.\n
    complemento : `str` | `None` = `None`\n
        Complemento do endereco.\n  
    
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
    >>> print(endereco.numero)
    0
    >>> print(endereco.CEP)
    74690900
    >>> print(endereco.tipo_endereco.name)
    COMERCIAL
    >>> print(endereco.bairro.nome)
    Chácaras Califórnia
    >>> print(endereco.logradouro.nome)
    Alameda Palmeira
    >>> print(endereco.complemento)
    Quadra d

    Authors
    -------
    Karlos Daniel Pires da Silva : github.com/karlosdaniel451
    Date: 2022-07-15
    """

    numero: int
    CEP: int
    tipo_endereco: TipoEndereco
    bairro: Bairro
    logradouro: Logradouro
    complemento: str | None = None
