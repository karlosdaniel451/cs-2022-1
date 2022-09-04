from dataclasses import dataclass

from src.estado import Estado


@dataclass
class Cidade:
    """Classe cujas instancias representam cidades.
    
    Attributes
    ----------
    nome : `str`\n
        Nome da cidade.\n
    estado: `Estado`\n
        Estado da cidade.\n
    
    Examples
    --------
    >>> from src.pais import Pais
    >>> from src.estado import Estado
    >>> from src.cidade import Cidade
    >>> pais = Pais(nome='Brasil')
    >>> estado = Estado(sigla='GO', nome='Goias', pais=pais)
    >>> cidade = Cidade(nome='Goiânia', estado=estado)
    >>> print(f'{cidade.nome}')
    Goiânia
    >>> print(f'{cidade.estado.nome}')
    Goiás
    >>> print(f'{cidade.estado.pais.nome}')
    Brasil

    Authors
    -------
    Karlos Daniel Pires da Silva : github.com/karlosdaniel451
    Date: 2022-07-15
    """

    nome: str
    estado: Estado
