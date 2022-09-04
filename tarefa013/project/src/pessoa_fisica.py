import datetime
from dataclasses import dataclass

# import endereco
from src.endereco import Endereco


@dataclass
class PessoaFisica:
    """Classe cujas instancias representam pessoas fisicas.

    Attributes
    ----------
    nome : `str`\n
        Nome da pessoa fisica.\n
    sexo : `str`\n
        Genero sexual da pessoa fisica\n
    data_nascimento : `datetime.date`\n
        Data de nascimento da pessoa fisica.\n
    endereco : `Endereco`\n
        Endereco da pessoa fisica.
    
    Examples
    --------
    >>> from faker import Faker
    >>> from src.pais import Pais
    >>> from src.estado import Estado
    >>> from src.cidade import Cidade
    >>> from src.bairro import Bairro
    >>> from src.endereco import Endereco, TipoEndereco
    >>> from src.logradouro import Logradouro, TipoLogradouro
    >>> from src.pessoa_fisica import PessoaFisica
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
    >>> fake = Faker('pt_BR')
    >>> fake_profile = fake.profile()
    >>> pessoa_fisica = PessoaFisica(
    ...     nome=fake_profile['name'],
    ...     sexo=fake_profile['sex'],
    ...     data_nascimento=fake_profile['birthdate'],
    ...     endereco=endereco
    ... )
    >>> pessoa_fisica.nome
    'Amanda Sales'
    >>> pessoa_fisica.sexo
    'F'
    >>> pessoa_fisica.data_nascimento
    datetime.date(1974, 3, 3)
    >>> pessoa_fisica.endereco.logradouro.nome
    'Alameda Palmeiras'

    Authors
    -------
    Karlos Daniel Pires da Silva : github.com/karlosdaniel451
    Date: 2022-07-15
    """

    nome: str
    sexo: str
    data_nascimento: datetime.date
    endereco: Endereco
