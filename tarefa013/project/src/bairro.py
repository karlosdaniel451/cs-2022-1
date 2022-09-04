from dataclasses import dataclass

from src.cidade import Cidade


@dataclass
class Bairro:
    """Classe cujas instancias representam bairros.
    
    Attributes
    ----------
    nome : `str`\n
        Nome do bairro.\n
    cidade: `Cidade`\n
        Cidade do bairro.\n
    
    Examples
    --------
    >>> from src.pais import Pais
    >>> from src.estado import Estado
    >>> from src.cidade import Cidade
    >>> from src.bairro import Bairro
    >>> pais = Pais(nome='Brasil')
    >>> estado = Estado(sigla='GO', nome='Goias', pais=pais)
    >>> cidade = Cidade(nome='Goiânia', estado=estado)
    >>> bairro = Bairro(nome='Chácaras Califórnia', cidade=cidade)
    >>> print(f'{bairro.nome}')
    Chácaras Califórnia
    >>> print(f'{bairro.cidade.nome}')
    Goiânia
    >>> print(f'{bairro.cidade.estado.nome}')
    Goiás
    >>> print(f'{cidade.estado.pais.nome}')
    Brasil

    Authors
    -------
    Karlos Daniel Pires da Silva : github.com/karlosdaniel451
    Date: 2022-07-15
    """

    nome: str
    cidade: Cidade
