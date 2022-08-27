from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


USER = 'postgres'
PASSWORD = '123456789'
HOSTNAME = 'localhost'
PORT_NUMBER = 5432
DATABASE = 'enderecos'

SQLALCHEMY_DATABASE_URL = f'postgresql://{USER}:{PASSWORD}@{HOSTNAME}:{PORT_NUMBER}/{DATABASE}'

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

