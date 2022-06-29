from dataclasses import dataclass, field
from typing import List

import estado
import bairro

@dataclass
class Cidade:
    nome: str
    estado: estado.Estado
    bairros: List[bairro.Bairro] = field(default_factory=list)
