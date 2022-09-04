from dataclasses import dataclass


@dataclass
class Pais:
    """Classe cujas instancias representam paises.
    
    Attributes
    ----------
    nome : `str`\n
        Nome do pais.\n
    
    Examples
    --------
    >>> pais = Pais(nome='Brasil')
    >>> print(f'{pais.nome}')
    Brasil

    Authors
    -------
    Karlos Daniel Pires da Silva : github.com/karlosdaniel451
    Date: 2022-07-15
    """

    nome: str
