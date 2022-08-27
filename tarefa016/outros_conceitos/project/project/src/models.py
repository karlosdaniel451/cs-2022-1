from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship


from .database import Base

class Pais(Base):
    __tablename__ = 'paises'
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(100), unique=True, nullable=False, index=True)

    estados = relationship('Estado', back_populates='pais')


class Estado(Base):
    __tablename__ = 'estados'
    id = Column(Integer, primary_key=True, index=True)
    sigla = Column(String, unique=True, nullable=False, index=True)
    nome = Column(String(100), unique=True, nullable=False, index=True)
    pais_id = Column(Integer, ForeignKey('paises.id'))

    pais = relationship('Pais', back_populates='estados')

    cidades = relationship('Cidade', back_populates='estado')


class Cidade(Base):
    __tablename__ = 'cidades'
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(100), unique=False, nullable=False, index=True)
    estado_id = Column(Integer, ForeignKey('estados.id'))
    
    estado = relationship('Estado', back_populates='cidades')
