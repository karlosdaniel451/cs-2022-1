from sqlalchemy.orm import Session

from . import models, schemas


def get_pais(db: Session, pais_id: int):
    return db.query(models.Pais).filter(models.Pais.id == pais_id).first()


def get_pais_by_nome(db: Session, nome: str):
    return db.query(models.Pais).filter(models.Pais.nome == nome).first()


def get_paises(db: Session, skip: int = 0, limit: int = 100) -> list:
    return db.query(models.Pais).offset(skip).limit(limit).all()


def create_pais(db: Session, pais: schemas.PaisCreate):
    db_pais = models.Pais(nome=pais.nome)

    db.add(db_pais)
    db.commit()
    db.refresh(db_pais)

    return db_pais


def get_estado(db: Session, estado_id: int):
    return db.query(
        models.Estado).filter(
        models.Estado.id == estado_id).first()

def get_estado_of_pais_by_nome(db: Session, estado_nome: int, pais_id: int):
    return \
        db.query(
            models.Estado
        ).filter(
            models.Estado.nome == estado_nome and models.Estado.pais_id == pais_id
        ).first()

def get_estado_of_pais_by_sigla(db: Session, estado_sigla: int, pais_id: int):
    return \
        db.query(
            models.Estado
        ).filter(
            models.Estado.sigla == estado_sigla and models.Estado.pais_id == pais_id
        ).first()

def get_estados(db: Session, skip: int = 0, limit: int = 100) -> list:
    return db.query(models.Estado).offset(skip).limit(limit).all()


def create_estado(db: Session, estado: schemas.EstadoCreate, pais_id: int):
    db_estado = models.Estado(**estado.dict(), pais_id=pais_id)

    db.add(db_estado)
    db.commit()
    db.refresh(db_estado)

    return db_estado


def get_cidade(db: Session, cidade_id: int):
    return db.query(
        models.Cidade
    ).filter(
        models.Cidade.id == cidade_id
    ).first()


def get_cidade_of_estado_by_nome(db: Session, cidade_nome: int, estado_id: int):
    return \
        db.query(
            models.Cidade
        ).filter(
            models.Cidade.nome == cidade_nome and models.Cidade.estado_id == estado_id
        ).first()


def get_cidades(db: Session, skip: int = 0, limit: int = 100) -> list:
    return db.query(models.Cidade).offset(skip).limit(limit).all()


def create_cidade(db: Session, cidade: schemas.CidadeCreate, estado_id: int):
    db_cidade = models.Cidade(**cidade.dict(), estado_id=estado_id)

    db.add(db_cidade)
    db.commit()
    db.refresh(db_cidade)

    return db_cidade
