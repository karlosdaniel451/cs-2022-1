from dataclasses import dataclass
from enum import Enum

import bairro

class TipoEndereco(Enum):
    COMERCIAL = 0
    RESIDENCIAL = 1


@dataclass
class Endereco:
    numero: int
    complemento: str
    CEP: int
    tipo_endereco: TipoEndereco
    bairro: bairro.Bairro
