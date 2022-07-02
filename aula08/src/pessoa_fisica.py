from dataclasses import dataclass
import datetime

import endereco

@dataclass
class PessoaFisica:
    nome: str
    sexo: str
    data_nascimento: datetime.date
    endereco: endereco.Endereco
