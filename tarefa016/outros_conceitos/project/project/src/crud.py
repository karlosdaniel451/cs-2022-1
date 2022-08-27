from sqlalchemy.orm import Session

from . import models, schemas


def get_pais(db: Session, pais_id: int) -> models.Pais:
    return db.query(models.Pais).filter(models.Pais.id == pais_id).first()


def get_pais_by_nome(db: Session, nome: str) -> models.Pais:
    return db.query(models.Pais).filter(models.Pais.nome == nome).first()


def get_paises(db: Session, skip: int = 0, limit: int = 100) -> list[models.Pais]:
    return db.query(models.Pais).offset(skip).limit(limit).all()


def create_pais(db: Session, pais: schemas.PaisCreate) -> list[models.Pais]:
    db_pais = models.Pais(nome=pais.nome)

    db.add(db_pais)
    db.commit()
    db.refresh(db_pais)

    return db_pais


def get_estado(db: Session, estado_id: int) -> models.Estado:
    return db.query(
        models.Estado).filter(
        models.Estado.id == estado_id).first()

def is_estado_sigla_and_nome_new_for_pais(db: Session, nome: str, sigla: str, pais_id: int) -> bool:
    return get_estado_of_pais_by_nome(db, nome, pais_id) \
        or get_estado_of_pais_by_sigla(db, sigla, pais_id)

def get_estado_of_pais_by_nome(db: Session, nome: str, pais_id: int) -> list[models.Estado]:
    return \
        db.query(
            models.Estado
        ).filter(
            models.Estado.nome == nome and models.Estado.pais_id == pais_id
        ).first()

def get_estado_of_pais_by_sigla(db: Session, sigla: int, pais_id: int) -> list[models.Estado]:
    return \
        db.query(
            models.Estado
        ).filter(
            models.Estado.sigla == sigla and models.Estado.pais_id == pais_id
        ).first()

def get_estados(db: Session, skip: int = 0, limit: int = 100) -> list[models.Estado]:
    return db.query(models.Estado).offset(skip).limit(limit).all()


def create_estado(db: Session, estado: schemas.EstadoCreate, pais_id: int) -> models.Estado:
    db_estado = models.Estado(**estado.dict(), pais_id=pais_id)

    db.add(db_estado)
    db.commit()
    db.refresh(db_estado)

    return db_estado


def get_cidade(db: Session, cidade_id: int) -> models.Estado:
    return db.query(
        models.Cidade
    ).filter(
        models.Cidade.id == cidade_id
    ).first()


def is_cidade_nome_new_for_estado(db: Session, cidade_nome: int, estado_id: int) -> bool:
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
