from dataclasses import dataclass, field
from typing import List

import estado

@dataclass
class Pais:
    nome: str
    estados: List[estado.Estado] = field(default_factory=list)
