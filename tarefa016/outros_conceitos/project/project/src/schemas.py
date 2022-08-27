from pydantic import BaseModel


class CidadeBase(BaseModel):
    nome: str


class CidadeCreate(CidadeBase):
    pass


class Cidade(CidadeBase):
    id: int
    estado_id : int

    class Config:
        orm_mode = True


class EstadoBase(BaseModel):
    sigla: str
    nome: str


class EstadoCreate(EstadoBase):
    pass


class Estado(EstadoBase):
    id: int
    pais_id: int
    cidades: list[Cidade] = []

    class Config:
        orm_mode = True


class PaisBase(BaseModel):
    nome: str


class PaisCreate(PaisBase):
    pass


class Pais(PaisBase):
    id: int
    estados: list[Estado] = []

    class Config:
        orm_mode = True
