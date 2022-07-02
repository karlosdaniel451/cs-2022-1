from dataclasses import dataclass, field
from typing import List

import pais
import cidade

@dataclass
class Estado:
    sigla: str
    nome: str
    pais: pais.Pais
    cidades: List[cidade.Cidade] = field(default_factory=list)
