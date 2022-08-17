import uvicorn
from fastapi import Depends, FastAPI, HTTPException, status
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(engine)

app = FastAPI()


# Dependência a ser injetada.
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get('/')
def read_root():
    return {'hello': 'world'}


@app.post('/paises/', response_model=schemas.Pais,
          status_code=status.HTTP_201_CREATED)
def create_pais(pais: schemas.PaisCreate, db: Session = Depends(get_db)):
    db_pais = crud.get_pais_by_nome(db, nome=pais.nome)
    if db_pais:
        raise HTTPException(
            status.HTTP_400_BAD_REQUEST,
            detail='Nome de país já cadastrado'
        )

    return crud.create_pais(db, pais=pais)


@app.get("/paises/", response_model=list[schemas.Pais])
def read_paises(
        skip: int = 0,
        limit: int = 100,
        db: Session = Depends(get_db)):
    paises = crud.get_paises(db, skip=skip, limit=limit)
    return paises


@app.get('/paises/{pais_id}', response_model=schemas.Pais)
def read_pais(pais_id: int, db: Session = Depends(get_db)):
    db_pais = crud.get_pais(db, pais_id=pais_id)

    if db_pais is None:
        raise HTTPException(status.HTTP_404_NOT_FOUND,
                            detail='País não encontrado')

    return db_pais


@app.post('/estados/{pais_id}/', response_model=schemas.Estado)
def create_estado_for_pais(
    pais_id: int, estado: schemas.EstadoCreate, db: Session = Depends(get_db)
):
    # Check that pais actually exists.
    if crud.get_pais(db, pais_id=pais_id) is None:
        raise HTTPException(
            status.HTTP_404_NOT_FOUND,
            detail=f'Não existe país com o id {pais_id}'
        )

    # Check that the estado.nome and estado.sigla is new for the estado.
    if crud.get_estado_of_pais_by_nome(
            db,
            pais_id=pais_id,
            estado_nome=estado.nome) or crud.get_estado_of_pais_by_sigla(
            db,
            pais_id=pais_id,
            estado_sigla=estado.sigla):
        raise HTTPException(
            status.HTTP_409_CONFLICT,
            detail=f'O pais de id {pais_id} já possui um estado chamado'
                   f' {estado.nome} ou com sigla {estado.sigla}.'
        )

    return crud.create_estado(db, estado=estado, pais_id=pais_id)


@app.get("/estados/", response_model=list[schemas.Estado])
def read_estados(
        skip: int = 0,
        limit: int = 100,
        db: Session = Depends(get_db)):
    estados = crud.get_estados(db, skip=skip, limit=limit)
    return estados


@app.get('/estados/{estado_id}', response_model=schemas.Estado)
def read_estado(estado_id: int, db: Session = Depends(get_db)):
    db_estado = crud.get_estado(db, estado_id=estado_id)
    if db_estado is None:
        raise HTTPException(
            status.HTTP_404_NOT_FOUND,
            detail='Estado não encontrado'
        )

    return db_estado


@app.post('/cidades/{estado_id}/', response_model=schemas.Cidade)
def create_cidade_for_estado(
    estado_id: int, cidade: schemas.CidadeCreate, db: Session = Depends(get_db)

):
    # Check that estado actually exists.
    if crud.get_estado(db, estado_id=estado_id) is None:
        raise HTTPException(
            status.HTTP_404_NOT_FOUND,
            detail=f'Não existe estado com o id {estado_id}'
        )

    # Check that the city's name is new for the estado.
    if crud.get_cidade_of_estado_by_nome(
            db, estado_id=estado_id, cidade_nome=cidade.nome):
        raise HTTPException(
            status.HTTP_409_CONFLICT,
            detail=f'O estado de id {estado_id} já possui uma cidade chamada'
                   f' {cidade.nome}.'
        )

    return crud.create_cidade(db, cidade=cidade, estado_id=estado_id)


@app.get("/cidades/", response_model=list[schemas.Cidade])
def read_cidades(
        skip: int = 0,
        limit: int = 100,
        db: Session = Depends(get_db)):
    cidades = crud.get_cidades(db, skip=skip, limit=limit)
    return cidades


@app.get('/cidades/{cidade_id}', response_model=schemas.Cidade)
def read_cidade(cidade_id: int, db: Session = Depends(get_db)):
    db_cidade = crud.get_cidade(db, cidade_id=cidade_id)
    if db_cidade is None:
        raise HTTPException(
            status.HTTP_404_NOT_FOUND,
            detail='Cidade não encontrada'
        )

    return db_cidade


def start():
    '''Launched with `poetry run start` at root level'''
    uvicorn.run('project.src.main:app', host='0.0.0.0', port=8000, reload=True)


def capitalize(func):
    def uppercase():
        result = func()
        return result.upper()
    return uppercase


@capitalize
def say_hello():
    return "hello"


print(say_hello())  # 'HELLO'
