from dataclasses import dataclass, field
from typing import List

import cidade
import endereco

@dataclass
class Bairro:
    nome: str
    cidade: cidade.Cidade
    enderecos: List[endereco.Endereco] = field(default_factory=list)
