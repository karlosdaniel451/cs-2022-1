from dataclasses import dataclass, field
from enum import Enum
from typing import List

import endereco

class TipoLogradouro(Enum):
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
    nome: str
    tipo_logradouro: TipoLogradouro
    enderecos: List[endereco.Endereco] = field(default_factory=list)
